.DEFAULT_GOAL := help

.PHONY: help start finish status

help:
	@printf '%s\n' \
		'Git 协作同步命令：' \
		'  make start                 开始工作前获取并安全更新远端代码' \
		'  make finish m="提交信息"   提交全部修改、同步远端并推送' \
		'  make status                查看工作区和本地/远端同步状态'

start:
	@bash scripts/git-sync.sh start

finish:
	@bash scripts/git-sync.sh finish "$(m)"

status:
	@bash scripts/git-sync.sh status
