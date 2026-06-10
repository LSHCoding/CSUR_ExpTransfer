#!/usr/bin/env bash
set -euo pipefail

REMOTE="origin"
ACTION="${1:-}"
MESSAGE="${2:-${m:-}}"

usage() {
  cat <<'EOF'
用法：
  bash scripts/git-sync.sh start
  bash scripts/git-sync.sh finish "提交信息"
  bash scripts/git-sync.sh status
EOF
}

error() {
  echo "错误：$*" >&2
}

ensure_repository() {
  if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
    error "当前目录不在 Git 仓库中。"
    exit 1
  fi
}

git_path_exists() {
  local path

  path="$(git rev-parse --git-path "$1")"
  [[ -e "$path" ]]
}

ensure_no_git_operation() {
  local operation=""

  if git_path_exists "rebase-merge" || git_path_exists "rebase-apply"; then
    operation="rebase"
  elif git_path_exists "MERGE_HEAD"; then
    operation="merge"
  elif git_path_exists "CHERRY_PICK_HEAD"; then
    operation="cherry-pick"
  elif git_path_exists "REVERT_HEAD"; then
    operation="revert"
  elif git_path_exists "BISECT_LOG"; then
    operation="bisect"
  elif git_path_exists "sequencer"; then
    operation="sequencer"
  fi

  if [[ -n "$operation" ]]; then
    error "检测到尚未完成的 Git ${operation} 操作。"
    error "请先完成或终止该操作，再运行此命令。"
    exit 1
  fi
}

current_branch() {
  local branch

  branch="$(git branch --show-current)"
  if [[ -z "$branch" ]]; then
    error "当前处于 detached HEAD 状态，不支持自动同步。"
    exit 1
  fi

  printf '%s\n' "$branch"
}

ensure_head_exists() {
  if ! git rev-parse --verify HEAD >/dev/null 2>&1; then
    error "当前分支还没有初始提交。"
    exit 1
  fi
}

ensure_remote() {
  if ! git remote get-url "$REMOTE" >/dev/null 2>&1; then
    error "未配置远端仓库 '${REMOTE}'。"
    exit 1
  fi
}

remote_ref() {
  local branch="$1"
  printf 'refs/remotes/%s/%s\n' "$REMOTE" "$branch"
}

remote_branch_exists() {
  local branch="$1"
  git show-ref --verify --quiet "$(remote_ref "$branch")"
}

fetch_remote() {
  echo "正在获取 GitHub 更新……"
  git fetch --prune "$REMOTE"
}

working_tree_status() {
  git status --short
}

working_tree_is_clean() {
  [[ -z "$(working_tree_status)" ]]
}

ahead_behind() {
  local branch="$1"
  git rev-list --left-right --count "HEAD...${REMOTE}/${branch}"
}

show_relation() {
  local ahead="$1"
  local behind="$2"

  if (( ahead == 0 && behind == 0 )); then
    echo "同步状态：本地与远端完全同步"
  elif (( ahead > 0 && behind == 0 )); then
    echo "同步状态：本地领先 ${ahead} 个提交"
  elif (( ahead == 0 && behind > 0 )); then
    echo "同步状态：本地落后 ${behind} 个提交"
  else
    echo "同步状态：本地与远端已分叉（领先 ${ahead}，落后 ${behind}）"
  fi
}

verify_synced() {
  local branch="$1"
  local ahead
  local behind

  read -r ahead behind < <(ahead_behind "$branch")
  if (( ahead != 0 || behind != 0 )); then
    error "同步验证失败（本地领先 ${ahead}，落后 ${behind}）。"
    exit 1
  fi
}

push_branch() {
  local branch="$1"

  echo "正在推送分支 ${branch} 到 ${REMOTE}……"
  if ! git push "$REMOTE" "$branch"; then
    error "推送失败，远端可能在 fetch 后发生了变化。"
    error "请检查仓库状态后重新运行 make finish。"
    exit 1
  fi
}

start_work() {
  local branch="$1"
  local ahead
  local behind

  echo "当前分支：${branch}"

  if ! working_tree_is_clean; then
    error "开始同步前，工作区必须保持干净："
    echo
    working_tree_status
    echo
    error "请先提交、暂存或删除这些修改。"
    exit 1
  fi

  fetch_remote

  if ! remote_branch_exists "$branch"; then
    error "远端分支 '${REMOTE}/${branch}' 不存在。"
    error "这可能是新建的本地分支，请运行 make finish 发布它。"
    exit 1
  fi

  read -r ahead behind < <(ahead_behind "$branch")

  if (( ahead == 0 && behind == 0 )); then
    echo "本地与远端已同步，可以开始工作。"
  elif (( ahead == 0 && behind > 0 )); then
    echo "远端领先 ${behind} 个提交，正在 fast-forward 更新……"
    git merge --ff-only "${REMOTE}/${branch}"
    verify_synced "$branch"
    echo "同步完成，可以开始工作。"
  elif (( ahead > 0 && behind == 0 )); then
    error "本地领先远端 ${ahead} 个提交。"
    error "请先运行 make finish 推送这些提交。"
    exit 1
  else
    error "本地与远端已分叉（领先 ${ahead}，落后 ${behind}）。"
    error "请人工处理分支历史后再开始工作。"
    exit 1
  fi
}

commit_changes() {
  local message="$1"
  local answer=""

  if working_tree_is_clean; then
    echo "没有待提交的文件修改。"
    return 0
  fi

  echo "以下修改将被提交："
  echo
  working_tree_status
  echo

  if [[ -z "$message" ]]; then
    error "缺少提交信息。"
    error "用法：make finish m=\"描述本次修改\""
    exit 1
  fi

  read -r -p "是否提交以上全部修改？[y/N] " answer || true
  if [[ ! "$answer" =~ ^[Yy]$ ]]; then
    echo "已取消提交，未执行 git add 或 git commit。"
    exit 1
  fi

  git add -A
  git commit -m "$message"
}

finish_work() {
  local branch="$1"
  local ahead
  local behind

  echo "当前分支：${branch}"
  commit_changes "$MESSAGE"
  fetch_remote

  if ! remote_branch_exists "$branch"; then
    echo "远端分支不存在，正在首次发布……"
    git push -u "$REMOTE" "$branch"
    verify_synced "$branch"
    echo "收工同步完成，本地与远端已完全同步。"
    return 0
  fi

  read -r ahead behind < <(ahead_behind "$branch")

  if (( ahead == 0 && behind == 0 )); then
    echo "本地与远端已完全同步，无需推送。"
  elif (( ahead > 0 && behind == 0 )); then
    push_branch "$branch"
  elif (( ahead == 0 && behind > 0 )); then
    echo "远端领先 ${behind} 个提交，正在 fast-forward 更新……"
    git merge --ff-only "${REMOTE}/${branch}"
  else
    echo "本地与远端均有新提交，正在 rebase 到 ${REMOTE}/${branch}……"
    if ! git rebase "${REMOTE}/${branch}"; then
      echo
      error "同步时发生冲突，当前处于 rebase 状态。"
      cat >&2 <<'EOF'

解决冲突后执行：
  git add <已解决的文件>
  git rebase --continue
  git push

放弃本次 rebase：
  git rebase --abort
EOF
      exit 1
    fi
    push_branch "$branch"
  fi

  verify_synced "$branch"
  echo "收工同步完成，本地与远端已完全同步。"
}

show_status() {
  local branch="$1"
  local ahead
  local behind
  local dirty=0

  echo "当前分支：${branch}"
  fetch_remote
  echo

  if working_tree_is_clean; then
    echo "工作区：干净"
  else
    dirty=1
    echo "待提交文件："
    working_tree_status
  fi

  echo
  if ! remote_branch_exists "$branch"; then
    echo "远端分支：${REMOTE}/${branch} 不存在"
    echo "建议操作：make finish"
    echo
    echo "最近的本地提交："
    git log -3 --oneline --decorate HEAD
    return 0
  fi

  echo "远端分支：${REMOTE}/${branch}"
  read -r ahead behind < <(ahead_behind "$branch")
  show_relation "$ahead" "$behind"

  if (( dirty == 1 || ahead > 0 || behind > 0 )); then
    echo "建议操作：make finish"
  else
    echo "建议操作：无需处理"
  fi

  echo
  echo "最近的本地提交："
  git log -3 --oneline --decorate HEAD
  echo
  echo "最近的远端提交："
  git log -3 --oneline --decorate "${REMOTE}/${branch}"
}

ensure_repository
ensure_no_git_operation
BRANCH="$(current_branch)"
ensure_head_exists
ensure_remote

case "$ACTION" in
  start)
    start_work "$BRANCH"
    ;;
  finish)
    finish_work "$BRANCH"
    ;;
  status)
    show_status "$BRANCH"
    ;;
  *)
    usage
    exit 1
    ;;
esac
