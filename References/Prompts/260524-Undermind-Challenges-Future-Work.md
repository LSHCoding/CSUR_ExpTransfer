# Task

I am writing a survey paper for submission to ACM Computing Surveys (CSUR) on **Experience Transformation in LLM-based Agents**—how interaction experience in LLM-based agents is transformed and reused across different carrier forms.

I will provide you with a list of papers. Please **read each paper in full** (do not rely solely on the abstract, introduction, or conclusion—key information is often embedded in the method, experiments, ablation studies, limitations, and appendix sections), and then extract:

1. The **challenges** currently present in this research direction
2. The **future directions** this research area may develop toward

# Extraction Requirements

- The number of challenges and future directions is not fixed—include as many as the literature genuinely supports.
- A challenge or future direction does not need to be supported by all papers. Some may be grounded in only a few papers, or even a single paper—this is acceptable, but please explicitly indicate which papers support each point.
- Every challenge and future direction must be backed by **concrete evidence from the papers**—cite specific papers, specific sections, or specific experimental observations. **Do not fabricate information. Do not make vague, ungrounded claims.** If an observation is your own inference rather than something stated in the papers, mark it explicitly as "inference."

# Dig for Hidden Content

Authors typically frame their work to highlight contributions and downplay weaknesses. The most valuable material for a survey Discussion often lies in what authors **do not want you to focus on**. Actively surface this hidden content, including but not limited to:

- **Ablation mismatches**: components the paper's narrative emphasizes as central, but which ablation studies reveal contribute little; or conversely, components described as auxiliary that turn out to be load-bearing.
- **Hedging language**: phrases like "may," "in our setting," "we leave to future work," "limited to," "preliminary"—these often mark places where authors quietly concede a limitation without flagging it as such.
- **Rejected design alternatives**: choices the authors briefly mention having tried and abandoned, with reasons that imply a deeper difficulty than stated.
- **Buried negative results**: experiments in the appendix or supplementary material that complicate or contradict the main narrative.
- **Scope retreats**: claims in the abstract or introduction that quietly narrow as the paper progresses (e.g., a method introduced as general but evaluated only on a specific subset).
- **Implicit assumptions**: prerequisites the method silently depends on but never defends—often visible only by noticing what is conspicuously absent from the discussion.
- **Evaluation conveniences**: benchmark choices, baseline selections, or metric definitions that subtly favor the proposed method.

When you surface such hidden content, cite the specific location in the paper (section, table, appendix), and briefly explain why this matters for the field's overall picture.

# Depth of Each Challenge and Future Direction

Each challenge and future direction must be elaborated in substantive detail—not a single sentence, not a one-line bullet. For each item, develop the following:

- **What the challenge / direction is**, stated precisely (avoid generic phrasing like "scalability remains an issue").
- **Concrete evidence from the papers** that establishes the challenge or motivates the direction—specific experimental findings, specific failure modes, specific design tensions. Quote or paraphrase the relevant observations with citations.
- **Why it matters and where current work falls short** (for challenges) or **what concrete progress would look like and how it could be verified** (for future directions).
- **Disagreements or alternative positions** across papers, if any—do not flatten genuine divergence into false consensus.

Aim for each item to be a substantive paragraph (or several) of analytical content, not a header followed by a sentence.

# Output Requirements

- Output in English.
- No introduction or conclusion needed. Go directly into the analysis of challenges and future directions.
- Do not summarize each paper one by one.

---


# Paper List

| 引用标识       | 标题                                                                                                             |
| ---------- | -------------------------------------------------------------------------------------------------------------- |
| [Xia25e]  | UI-Genie: A Self-Improving Approach for Iteratively Boosting MLLM-based Mobile GUI Agents                      |
| [Li26n]   | MagicGUI-RMS: A Multi-Agent Reward Model System for Self-Evolving GUI Agents via Automated Feedback Reflux     |
| [Li26l]   | No More Stale Feedback: Co-Evolving Critics for Open-World Agent Learning                                      |
| [Wan26u]  | RLAnything: Forge Environment, Policy, and Reward Model in Completely Dynamic RL System                        |
| [Zha25y]  | RL Tango: Reinforcing Generator and Verifier Together for Language Reasoning                                   |
| [Sin25b]  | VARP: Reinforcement Learning from Vision-Language Model Feedback with Agent Regularized Preferences            |
| [Pan26]   | EVPO: Explained Variance Policy Optimization for Adaptive Critic Utilization in LLM Post-Training              |
| [Wan26aj] | Co-Evolution of Policy and Internal Reward for Language Agents                                                 |
| [Sun24b]  | OS-Genesis: Automating GUI Agent Trajectory Construction via Reverse Task Synthesis                            |
| [He24e]   | OpenWebVoyager: Building Multimodal Web Agents via Iterative Real-World Exploration, Feedback and Optimization |
| [Xu24]    | AgentTrek: Agent Trajectory Synthesis via Guiding Replay with Web Tutorials                                    |
| [Wan24ad] | Bootstrapping Language-Guided Navigation Learning with Self-Refining Data Flywheel                             |
| [Xu25q]   | MCTS-EP: Empowering Embodied Planning with Online Preference Optimization                                      |
| [Xia25h]  | Self-Improving Vision-Language-Action Models with Data Generation via Residual RL                              |
| [He25g]   | Scalable Data Synthesis for Computer Use Agents with Step-Level Filtering                                      |
| [Son24]   | Trial and Error: Exploration-Based Trajectory Optimization for LLM Agents                                      |
| [Fai26]   | AutoSurfer -- Teaching Web Agents through Comprehensive Surfing, Learning, and Modeling                        |
| [Qi24]    | WebRL: Training LLM Web Agents via Self-Evolving Online Curriculum Reinforcement Learning                      |
| [Put24]   | Agent Q: Advanced Reasoning and Learning for Autonomous AI Agents                                              |
| [Bai24]   | DigiRL: Training In-The-Wild Device-Control Agents with Autonomous Reinforcement Learning                      |
| [Das25]   | BLAZER: Bootstrapping LLM-based Manipulation Agents with Zero-Shot Data Generation                             |
| [Ge26]    | Internalizing Agency from Reflective Experience                                                                |
| [Xio24]   | Watch Every Step! LLM Agent Learning via Iterative Step-level Process Refinement                               |
| [Yua25c]  | Agent-R: Training Language Model Agents to Reflect via Iterative Self-Training                                 |
| [Wan26al] | Skill-SD: Skill-Conditioned Self-Distillation for Multi-turn LLM Agents                                        |
| [Ye26f]   | Online Experiential Learning for Language Models                                                               |
| [Wan25x]  | STeCa: Step-level Trajectory Calibration for LLM Agent Learning                                                |
| [Wu25b]   | GUI-Reflection: Empowering Multimodal GUI Models with Self-Reflection Behavior                                 |
| [Yan24m]  | ReAct Meets ActRe: When Language Agents Enjoy Training Data Autonomy                                           |
| [Xu26j]   | CLEANER: Self-Purified Trajectories Boost Agentic Reinforcement Learning                                       |
| [Din26]   | AgentHER: Hindsight Experience Replay for LLM Agent Trajectory Relabeling                                      |
| [Ala25]   | Memento No More: Coaching AI Agents to Master Multiple Tasks via Hints Internalization                         |
| [Zho24e]  | Policy Improvement using Language Feedback Models                                                              |
| [Zha26]   | RetroAgent: From Solving to Evolving via Retrospective Dual Intrinsic Feedback                                 |
| [Sar24b]  | VLM Agents Generate Their Own Memories: Distilling Experience into Embodied Programs of Thought                |

