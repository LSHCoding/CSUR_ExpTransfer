# Notation — Unified Symbol Glossary

---

## 1. Core Carrier Notation（核心载体记号）


| 符号      | 全称                  | 定义                                                                     |
| ------- | ------------------- | ---------------------------------------------------------------------- |
| `N-Tok` | Narrative Tokenized | 弱形式化离散 token 载体，依自然语言/感知顺序组织，通过 language / multimodal understanding 复用 |
| `S-Tok` | Schematic Tokenized | 强形式化离散 token 载体，依语法/拓扑结构组织，通过 parsing / execution / graph traversal 复用 |
| `Lat`   | Latent              | 连续向量 / hidden state 载体，直接参与 attention 或 hidden-state 计算                |
| `π-Par` | Policy Parameter    | 固化在模型权重中的决策能力（actor），生成 action                                         |
| `V-Par` | Evaluator Parameter | 固化在模型权重中的评估能力（RM / PRM / verifier / critic / judge）                    |


> `Tokenized → Latent → Parametric`：沿此方向 reuse 从 token-level → latent-state-level → parameter-level，interpretability ↓, inference efficiency ↑, editability ↓。

---

## 2. Orthogonal Attribute Tags（正交属性标签）

### 2.1 Modality


| 标签              | 含义                                |
| --------------- | --------------------------------- |
| `[txt]`         | 纯文本                               |
| `[vis+txt]`     | 视觉+文本交织                           |
| `[GUI]`         | GUI 操作（screen coordinate, widget） |
| `[embodied]`    | 具身（robot sensor, motor command）   |
| `[cross-modal]` | 跨模态（输入输出模态不同）                     |


### 2.2 Experience Source


| 标签          | 含义               |
| ----------- | ---------------- |
| `{self}`    | Agent 自身交互生成     |
| `{human}`   | 人类专家示范           |
| `{teacher}` | Teacher model 合成 |


### 2.3 Method


| 标签              | 含义                                 |
| --------------- | ---------------------------------- |
| `⟨LLM-extract⟩` | LLM 推理提取，无参数更新                     |
| `⟨SFT⟩`         | 监督微调                               |
| `⟨RL: GRPO⟩`    | Group Relative Policy Optimization |
| `⟨RL: PPO⟩`     | Proximal Policy Optimization       |
| `⟨RL: DPO⟩`     | Direct Preference Optimization     |
| `⟨RL: ReST⟩`    | Reinforced Self-Training           |
| `⟨hybrid⟩`      | 多种方法混合                             |
| `⟨MCTS⟩`        | Monte Carlo Tree Search            |


---

## 3. Pathway Notation（路径记号）


| 记号   | 全称                                           | 定义                                                                          |
| ---- | -------------------------------------------- | --------------------------------------------------------------------------- |
| `P1` | Narrative → Narrative                        | Intra-Tokenized abstraction：raw → reflection / rule / insight / skill 等     |
| `P2` | Narrative → Schematic                        | Intra-Tokenized formalization：自然语言 → code / workflow / graph / API          |
| `P3` | Tokenized → Latent                           | Latent compression：discrete tokens → continuous vectors                     |
| `P4` | Tokenized → Parametric (Evaluator)           | Evaluator internalization：trajectories → RM / PRM / verifier                |
| `P5` | Tokenized → Parametric (Policy)              | Policy internalization：trajectories → policy weights via SFT / RL           |
| `P6` | Parametric (Evaluator) → Parametric (Policy) | Preference alignment：RM 信号 → policy weights via RLHF / DPO                  |
| `P7` | Parametric → Tokenized                       | Knowledge externalization：weights → synthetic trajectories / demonstrations |


**箭头语法**：`X → Y` 表示单步转化，`X → Y → Z` 表示多步组合（composite pipeline）。X, Y, Z ∈ {Narrative, Schematic, Latent, Policy, Evaluator}。

---

## 4. Domain Abbreviations（领域缩写）

正文高频使用但未在文件头部显式声明的领域通用缩写。


| 缩写     | 全称                                         | 备注                                 |
| ------ | ------------------------------------------ | ---------------------------------- |
| `RM`   | Reward Model                               | Evaluator 的典型实例                    |
| `PRM`  | Process Reward Model                       | 对推理链中间步骤评分的 RM                     |
| `ORM`  | Outcome Reward Model                       | 仅对最终输出评分的 RM                       |
| `RLHF` | Reinforcement Learning from Human Feedback | P6 的核心机制                           |
| `MCTS` | Monte Carlo Tree Search                    | 亦作为 Method 标签 ⟨MCTS⟩ 使用            |
| `VLA`  | Vision-Language-Action Model               | 具身领域的 policy 模型                    |
| `VLM`  | Vision-Language Model                      | 多模态基础模型                            |
| `CoT`  | Chain of Thought                           | 逐步推理                               |
| `ICL`  | In-Context Learning                        | 无参数更新的上下文学习                        |
| `KG`   | Knowledge Graph                            | Schematic 的常见产品形式                  |
| `LoRA` | Low-Rank Adaptation                        | parameter-efficient fine-tuning 方法 |
| `RAG`  | Retrieval-Augmented Generation             | 检索增强生成                             |


