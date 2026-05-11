---
name: exp-transform-annotate
description: 将 Title/URL/Abstract 三段式 markdown 论文清单批量标注为本 Survey 的 Experience-Transformation 结构化字段（Pathway / Source & Target Experience / Modality / Method / Mechanism），与 Carrier 体系（N-Tok / S-Tok / Lat / π-Par / V-Par）和 7 条 Pathway（P1–P7）对齐。当用户给出新一批论文摘要要求标注、批量打标签、归 Pathway、按 Carrier 分类、生成 Taxonomy 工作底稿、做经验转化路径分析时务必使用此 skill。常见触发词：annotate papers、批量打标签、Pathway 归属、experience transformation 标注、carrier 体系归类、taxonomy 底稿、按 P1–P7 分类、abstract 标注。
---

# Experience-Transformation 论文摘要标注

将一批论文摘要按本 Survey 主轴（Carrier × Transformation Pathway）解析为结构化标注块。仅对 Abstract 可直接推断的内容下判定，**严禁臆测或扩写**。

---

## 强制前置：每次会话刷新框架

执行任何标注前，**必须**重新读取以下两份源文件，确保术语与判定规则与最新版本对齐：

1. `Project_Infos.md` —— 核心立意、Carrier 分类（§2.2）、Transformation 双条件（§2.3：Grounding + Embodiment）、Scope 纳入与排除（§3）、7 条已知 Pathway（§4）、复合路径处理原则（§4 末段）。
2. `Notions.md` —— Carrier 记号（`N-Tok` / `S-Tok` / `Lat` / `π-Par` / `V-Par`）、Modality / Source / Method 标签、Pathway 编号 P1–P7 对照表、领域缩写。

不要凭印象操作。框架可能在不同时点有微调；source-of-truth 永远是这两份文件。

**术语纪律**：分析中一律使用新 Carrier 术语（Narrative / Schematic / Latent / Policy / Evaluator）。旧术语（Textual、Structured、Multimodal Raw 等）仅在引用论文原文时可出现。

---

## Python 环境

调用项目 conda 环境：

```
/Users/lingshuai/opt/anaconda3/envs/cc/bin/python
```

---

## 工作流

### 步骤 1：解析输入

```bash
/Users/lingshuai/opt/anaconda3/envs/cc/bin/python \
  .claude/skills/exp-transform-annotate/scripts/parse_papers.py <input.md>
```

脚本读取 Title/URL/Abstract 三段式 markdown（见 `csv-to-markdown` 输出格式），按 `------` 切块，输出 JSON 到 stdout：

```json
{
  "count": N,
  "papers": [{"index": 1, "title": "...", "url": "...", "abstract": "..."}, ...],
  "errors": [{"block": <int>, "reason": "..."}]
}
```

如 `errors` 非空，先把它们记下来，最终在输出文件末尾汇报；继续处理 `papers`，不阻断流程。

### 步骤 2：逐篇标注

对每条 `papers[i]`，按下文「Pathway 判定流程」与「字段输出模板」生成一个标注块。各块之间用一个空行分隔。**仅基于 Abstract**，不臆测、不补全、不外推；摘要未明示的字段一律填 "不清楚"。

### 步骤 3：写出文件

- 用户指定了输出路径 → 写到该路径。
- 用户未指定 → 默认写到项目根目录的 `<input_basename>_annotated.md`。例如 `papers.md` → `/Users/lingshuai/Projects/AgentProjects/CSUR_ExpTransfer/papers_annotated.md`。

### 步骤 4：附录（新标签 + 失败清单）

在输出文件末尾追加（仅当对应内容非空时输出对应段）：

```
## New Tags Introduced
- ⟨RL: XXX⟩ —— 一句话定义；首次出现：「<论文标题>」
- ...

## Annotation Failures
- 「<论文标题>」（block #N）—— 失败原因
- ...

## Parser Errors
- block #N —— <parser 报告的原因>
```

---

## 字段输出模板

每篇论文按以下顺序输出，标签符号与 `Notions.md` 一致：

```
[Title]: <论文完整标题>
- [Pathway]: <X → Y> 或 <X → Y → Z>，若命中 P1–P7 末尾标 (Pn)
- [Source Experience]: <源端经验的具体形式>
- [Target Experience]: <目标端经验的具体形式>
- [Source Modality]: <[txt] / [vis+txt] / [GUI] / [embodied] / [cross-modal] 或新模态>
- [Target Modality]: <同上>
- [Experience Source]: <{self} / {human} / {teacher} 之一或组合>
- [Utilization]: <转化后经验在论文中如何被复用；摘要未明示则写 "不清楚">
- [Method]: <⟨LLM-extract⟩ / ⟨SFT⟩ / ⟨RL: GRPO/PPO/DPO/ReST⟩ / ⟨MCTS⟩ / ⟨hybrid⟩ 或新方法；多方法见下文约定>
- [Mechanism]: <转化机制详细描述：源经验"通过什么具体过程"变成目标经验>
```

字段约定：

| 字段                         | 说明                                                                                              |
| -------------------------- | ----------------------------------------------------------------------------------------------- |
| Pathway                    | X, Y, Z ∈ {Narrative, Schematic, Latent, Policy, Evaluator}。命中 7 条已知路径标 (P1)–(P7)；新路径不标 P 编号。 |
| Source / Target Experience | 用论文摘要中出现的具体名词（raw trajectories、reflection、skill library、KV cache、reward model 等）。              |
| Source / Target Modality   | 沿 `Notions.md §2.1` 标签集合；不足时按"开放词典"规则新增。                                                       |
| Experience Source          | 沿 `Notions.md §2.2` 标签集合；多来源用并列书写（如 `{self}, {human}`）。                                        |
| Utilization                | 例如：作为 prompt prefix、作为 RAG 索引、作为 SFT 训练数据、作为 RM 在 RLHF 里给 policy 打分。摘要不明示则填 "不清楚"。             |
| Method                     | 沿 `Notions.md §2.3` 标签集合；不足时按"开放词典"规则新增。多方法组合见下文「多方法标注约定」。                                   |
| Mechanism                  | 必须说明源 → 目标的具体转化过程；含训练时说明监督信号与优化目标；多步组合时分段拆解、并标出构成它的已知 P 编号。                                  |

Mechanism 字段的额外要求：

- 若 Method 含 `⟨LLM-extract⟩`，必须描述提取过程的关键要素（迭代逻辑 / 过滤准则 / 反思条件等）。
- 若 Method 含训练，须说明监督信号来源、损失或优化目标。
- 若为多步组合（X → Y → Z），须分步骤拆解每一段转化，并显式标出每段对应的已知 P 编号（如「Stage 1 对应 P2，Stage 2 对应 P5」）；[Pathway] 头部不重复这些 P 编号。
- 若引入了任何新标签，在末尾按"开放词典"规则追加 `> New tag: ...` 说明行（见下文）。

### 多方法标注约定

一篇论文涉及多种方法时按以下规则填 [Method]：

- **单方法** → `⟨X⟩`。
- **两个方法清晰分布在不同 pipeline 阶段（前后承接）** → 用逗号列出：`⟨X⟩, ⟨Y⟩`。Mechanism 中按阶段拆解时分别绑定到具体阶段。
- **三种以上方法、或方法相互交织难以单独剥离**（如 MCTS-guided sampling + reward modeling + DPO 同时介入）→ 使用 `⟨hybrid⟩`，并在 Mechanism 中显式列出参与的具体方法（"hybrid 由 ⟨MCTS⟩ + ⟨RL: DPO⟩ + ⟨LLM-extract⟩ 组成"）。

---

## Pathway 判定流程

按以下顺序逐题作答。**论文的自我表述（"self-play"、"bootstrapping"、"iterative self-training"）不决定路径，底层机制决定**。

**1. Scope 检查**（参见 Project_Infos.md §3）

满足 §3.1 两条纳入标准吗（决策过程语义 + 异构动作空间）？

- 否 → `[Pathway]: Out of Scope`，[Mechanism] 一句话说明排除理由（属于 §3.2 的哪一类），其余字段省略。
- 是 → 继续。

**2. 识别源端载体**

摘要中"被消化的输入"位于哪一层次？

- 自然语言日志、reflection、screenshot 序列、interaction logs → **Narrative** (N-Tok)
- code、workflow、SOP、API spec、graph、structured library → **Schematic** (S-Tok)
- KV cache、soft prompt、continuous memory token、prefix cache → **Latent** (Lat)
- LLM agent 权重、VLA 权重、LoRA → **Policy** (π-Par)
- RM、PRM、verifier、judge 权重 → **Evaluator** (V-Par)

**载体归类的两条易错点**（按 Project_Infos.md §2.2.3）：
- "workflow / SOP / routine / procedural template / pipeline" **无论以 code 或 NL 模板形式存在均属 Schematic**（程序化产物按拓扑结构归类，不看表面文字密度）。看到论文称其产物为 workflow / SOP / routine 就默认 Schematic，除非摘要明确说它只是 hint / guideline / skill description。
- "rule / guideline / hint / skill description / strategy / insight" 即便读起来像分点步骤说明，仍属 **Narrative**（弱形式化、无显式拓扑或语法约束）。

**3. 识别目标端载体**

同样的层次表，判定"产出的新东西"。

**4. 判定单步 vs 复合**

- 源 → 目标是单次直接转化 → `X → Y`。
- 源 → 中间 → 目标是论文的整体方法、贡献点在路径间衔接机制 → `X → Y → Z`，分步骤在 Mechanism 中拆解。
- 同一论文中两条相对独立、无衔接关系的转化（"偶现"）→ 按主线路径标注，在 Mechanism 中提及次要转化；不要错按复合路径处理。

**易漏识别的 composite 模板**（参 Project_Infos.md §4 + `Docs/Taxonomy_Reorganized.md §8` 的 canonical 目录）—— 看到这些信号时优先按 composite 处理，不要被单一终态拉去标单路径。已收录文献中按频率从高到低排查：

| 信号                                                                                | 对应 composite                                                                | 频率 | 论文贡献点                                            |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------- | -- | ------------------------------------------------ |
| 当前 policy 自己 rollout → 数据回灌再训练 policy（self-evolving / self-improvement / iterative self-training 作为整体 paradigm） | **Policy → Narrative → Policy**（§8.1）—— P7 自生成 + 可选 P1 中间 refinement + P5 内化 | 极高 | 闭环衔接机制：用什么替代 reward、如何过滤 / 反思 / curriculum / backtracking |
| 先 reflection / rule / skill / principle 中间抽象，再以该 refined Narrative 做 SFT/RL       | **Narrative (raw) → Narrative (refined) → Policy**（§8.3）—— P1 + P5           | 高  | refined Narrative 如何作为低噪监督；中间 refine 步噪声需低于 raw  |
| 先把 token 经验压成 latent 用于 attention / 检索 / 继续训练                                     | **Narrative → Latent**（§8.4）—— P3 后可接 V-Par refiner 等                       | 中  | latent 桥接层的设计与训练目标；当前文献全为 cross-session 实现，需训练   |
| 先训练 RM / PRM / critic，再用其信号训 policy（同一篇里两步都做）                                    | **Narrative → Evaluator → Policy**（§8.2）—— P4 + P6                          | 中  | Evaluator 作为可训练的噪声过滤器                            |
| 先把 trajectory 形式化为 code / workflow / graph，再以该结构为对象训 policy / 优化 workflow         | **Narrative → Schematic → Policy / Workflow**（§8.5）—— P2 + P5（亦可终于 S-Tok）   | 低  | Schematic 结构如何成为显式优化对象                           |
| 先 internalize 进权重，再由已更新 policy 外化 skill 库（拓扑与 §8.3 相反）                            | **Narrative → Policy → Narrative (skill)**（§8.6，萌芽）—— P5 + P7               | 萌芽 | 学会再总结——某些 skill 只有在 policy 能"做出来"后才能被正确描述         |
| policy 自生成数据用于训练 Evaluator（而非训练自己）                                                | **Policy → Narrative → Evaluator**（§8.7，萌芽）—— P7 + P4                       | 萌芽 | 外化数据如何缩小 judge 训练上的人工标注 gap                      |

### 边界判别

**P7（纯外化）vs §8.1（self-reinforce 闭环）**：若 policy 外化的 trajectory 又被吞回自己做训练（`π → N → π`），归 §8.1 而非 P7。P7 仅指外化后**不再直接用回自身训练**的纯外化（典型用途：合成数据集发布、跨模型蒸馏数据、benchmark 构造）。

**§6（V-Par → π-Par）几乎不独立出现**：已收录文献中所有 V-Par → π-Par 的 alignment 步骤都嵌在 §8.2 composite 中（同一篇工作既训 RM / PRM / critic 又做 RLHF / DPO 对齐）；单独"冻结某个 RM 做 alignment"的工作池内为空。判定时若摘要描述了"训练 RM" + "用 RM 信号训 policy"两步，归 §8.2 而非 P6 单步。

**Multi-target 论文（一篇同时产出多类 Carrier 目标，§8.8）**：若多目标共享同源经验且彼此并列、不构成链式衔接（典型如 SEAgent 同时产出 V-Par world state model、refined N-Tok、π-Par 三类目标；G-Memory 同时产出 S-Tok graph 与 N-Tok insights），按主轴路径标注 [Pathway] 头部，[Mechanism] 中显式列出其余 transformation 分支并各标对应 P 编号。

**Pattern 重叠地带**：一篇论文可同时落入两个 §8 pattern（如 LEAFE / RetroAct 既属 §8.1 闭环，也带 §8.3 中间 reflection）。此时 [Pathway] 头部按主轴标注，在 [Mechanism] 中点出兼属的另一 pattern。

**5. 命中已知 Pathway 编号**

| 编号  | 路径                                           | 速记                              |
| --- | -------------------------------------------- | ------------------------------- |
| P1  | Narrative → Narrative                        | raw → reflection / rule / skill |
| P2  | Narrative → Schematic                        | logs → code / workflow / graph  |
| P3  | Tokenized → Latent                           | tokens → KV cache / soft prompt |
| P4  | Tokenized → Parametric (Evaluator)           | trajectories → RM / PRM         |
| P5  | Tokenized → Parametric (Policy)              | trajectories → policy via SFT/RL |
| P6  | Parametric (Evaluator) → Parametric (Policy) | RM 信号 → policy via RLHF/DPO     |
| P7  | Parametric → Tokenized                       | weights → synthetic trajectories |

命中 → 末尾标 (Pn)；未命中 → 不标编号，并在 [Mechanism] 中显式说明为何是新路径（哪条已知 Pathway 都覆盖不了）。

---

## 标签纪律：开放词典而非封闭枚举

`Notions.md` 列出的 Modality / Source / Method 标签是**当前已观察到的常见取值，不是封闭集合**。允许新增，但守五条纪律：

1. **优先复用** —— 能用现有标签覆盖的一律复用；只有损失关键信息或造成误标时才考虑新增。
2. **维度不变** —— 新标签只能落入 Modality / Source / Method / Pathway 任一已有维度，**不允许新增维度**（新维度是 Survey 框架级决策，不在标注阶段处理）。
3. **格式一致** —— Modality 用 `[...]`、Source 用 `{...}`、Method 用 `⟨...⟩`，命名简短、英文化、与既有风格对齐（如新方法用 `⟨RL: XXX⟩` 形式）。
4. **同义不复造** —— 已有 `⟨SFT⟩` 就不再造 `⟨fine-tune⟩` 等同义新标签。
5. **显式标记** —— 首次出现时在该论文 [Mechanism] 末尾追加：
   ```
   > New tag: <标签名> — <一句话定义；说明为何既有标签不足以覆盖>
   ```
   并在最终输出末尾的「## New Tags Introduced」段汇总。

---

## Out-of-Scope 处理

落入 `Project_Infos.md §3.2` 的论文一律标 `[Pathway]: Out of Scope`，[Mechanism] 一句话说明排除理由，其余字段省略。常见排除场景：

- 静态语料预训练（无决策过程语义）
- 单步分类 / 标注 SFT（非异构动作空间）
- 纯模型蒸馏 Parametric → Parametric（经验语义链断裂）
- 纯图像分类 / 视觉基础模型训练（无序贯决策语义）
- 非 LLM-based 系统（传统 RL 等）

---

## 错误处理

- **Parser 阶段**：JSON 中 `errors` 列表非空 → 不阻断，继续处理 `papers`，最后在输出文件末尾「## Parser Errors」段汇报。
- **标注阶段**：单篇 abstract 信息不足或判定不出（例如摘要只是一句宣传语、完全无法识别源端 / 目标端载体）→ 保留 `[Title]: ...` 头，`[Pathway]: Annotation Failed`，[Mechanism] 简述失败原因（"abstract 仅一句话，无法识别源经验形式"等），继续处理下一篇。最后在输出文件末尾「## Annotation Failures」段汇总。

不要为了凑齐字段而编造内容。失败比臆测更可接受。

---

## 完整示例

**输入**（节选）：

> we propose Training-Free Group Relative Policy Optimization (Training-Free GRPO), a cost-effective solution that enhances LLM agent performance without any parameter updates. Our method leverages the group relative semantic advantage instead of numerical ones within each group of rollouts, iteratively distilling high-quality experiential knowledge during multi-epoch learning on a minimal ground-truth data. Such knowledge serves as the learned token prior, which is seamlessly integrated during LLM API calls to guide model behavior.

**输出**：

```
[Title]: Training-Free Group Relative Policy Optimization
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Raw interaction rollouts / raw trajectories
- [Target Experience]: Experiential Knowledge / Rules（自然语言经验库）
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 作为 learned token prior 在 LLM API 调用时无缝集成，用于 guide model behavior
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 不更新 LLM 参数，而是通过多轮 rollout、组内语义相对比较（group relative semantic advantage）和自我反思，把成功 / 失败经验蒸馏成自然语言经验库；经验库再作为 prompt / token prior 注入模型，从而在上下文空间模拟 GRPO 在参数空间中的策略优化效果。
```

---

## 输出文件结构

```
{annotation_block_1}

{annotation_block_2}

{annotation_block_3}
...

## New Tags Introduced
- ⟨...⟩ —— ...

## Annotation Failures
- 「...」（block #N）—— ...

## Parser Errors
- block #N —— ...
```

后三段仅在对应内容非空时输出。

---

## 沟通规范

按 CLAUDE.md 的 Chinese Anti-AI Patterns 输出对话内容。保持 CSUR 资深审稿人立场——若发现摘要描述与 Pathway 判定存在张力（例如论文自称 "self-play" 但底层机制不构成 transformation），直接指出并按底层机制标注，不顺论文自我表述。
