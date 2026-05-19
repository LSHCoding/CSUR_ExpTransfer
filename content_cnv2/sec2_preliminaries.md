# §2 Preliminaries: Experience, Carriers, and Transformations

Before discussing agent experience transformation, we formalize three foundational concepts: Agent, Agent Experience, and Experience Transformation.

## §2.1 Agent

We define an agent as a system that performs sequential decision-making in an environment according to task context. At each decision step $t$, the agent perceives the current context $c_t$, produces an action $a_t$, optionally receives an objective consequence $o_t$ from the environment, and optionally receives an evaluative signal $f_t$.

The agent's action $a_t$ spans heterogeneous forms including natural language reasoning chains, code generation, tool invocations, and environment manipulations—it is not confined to a single action space. The agent operates through the following loop:

$$
c_t \xrightarrow{\pi} a_t \xrightarrow{\mathcal{E}} (o_t) \xrightarrow{} (f_t) \xrightarrow{} c_{t+1},
$$

where $\pi$ is the agent's policy, $\mathcal{E}$ is the environment, and $(\cdot)$ denotes optional elements. Each round $(c_t, a_t, o_t, f_t)$ constitutes one atomic experience record. Under this definition, the environment can be reasoning verification, tool execution, or the physical world—the defining feature is sequential decision-making within it, not its physical properties.

## §2.2 Agent Experience

### §2.2.1 Minimal Semantic Unit

The minimal semantic unit of agent experience is a modality-agnostic quadruple:

$$e = (c, a, o, f),$$

where $c$ (Context) and $a$ (Action) are required, and $o$ (Observation) and $f$ (Feedback) are optional. This definition simultaneously carries decision-process semantics and satisfies the heterogeneous action space condition.

A full task execution produces a temporally ordered sequence of experience units, denoted as a trajectory $\tau = (e_1, e_2, \dots, e_T)$, where $T$ is the trajectory length. A collection of trajectories is denoted as $\mathcal{D} = \{\tau^{(i)}\}_{i=1}^N$.

### §2.2.2 Experience Carriers

While the minimal unit $e$ describes the *semantic content* of experience—"what happened"—Experience Carriers describe the *form* in which experience exists within the model architecture, serving as the foundational coordinate system for analyzing transformation pathways.

Carrier classification follows the axis of "locus in the model architecture," rather than conventional dimensions (modality, technique, component). This choice rests on three considerations. First, architectural locus maps directly to the core trade-offs that concern agent systems—interpretability, inference cost, editability—making the taxonomy itself analytically productive. Second, locus is orthogonal to modality: experience in any modality can exist at the Tokenized, Latent, or Parametric level, allowing multimodal work to integrate naturally without requiring special channels. Third, locus captures the fundamental differences in carrier form, maximizing the discriminative power of pathway classification.

Carriers are divided into three top-level categories:

**Tokenized Carriers ($\mathcal{C}^T$).** Experience carriers that explicitly enter the model's forward pass as discrete token sequences. They encompass text tokens, visual patch tokens, action tokens, and serialized structural tokens—not limited to natural language text. They occupy the context window and require full processing at inference time. By degree of formalization, they are further divided:

- **Narrative Tokenized ($\mathcal{C}^T_N$, N-Tok):** Weakly formalized carriers organized by natural language or perceptual sequence, reused through language or multimodal understanding. Typical forms: raw trajectories, reflections, summaries, screenshots, video sequences.
- **Schematic Tokenized ($\mathcal{C}^T_S$, S-Tok):** Strongly formalized carriers organized by syntactic or topological structure, reused through parsing, execution, or graph traversal. Typical forms: code libraries, workflows, knowledge graphs, decision trees.

Raw interaction trajectories are the zero-abstraction special case of Narrative Tokenized—they are unrefined Narrative carriers rather than a separate category outside the carrier system. Transformations typically take raw as the starting point.

**Latent Carriers ($\mathcal{C}^L$, Lat).** Experience carriers existing as continuous vectors or hidden states, directly participating in attention or hidden-state computation. They are neither discrete tokens (do not occupy the context window) nor solidified in weights (do not alter model parameters), serving as a bridge layer between Tokenized and Parametric. Typical forms: KV cache, prefix cache, learnable soft prompts, continuous memory tokens. Latent carriers can be distinguished by implementation regime into session-scoped (no training, e.g., KV cache) and cross-session reusable (requires training, e.g., soft prompts), though we do not treat these as formal subclasses.

**Parametric Carriers ($\mathcal{C}^P$).** Experience solidified in neural network weight distributions, fully implicit. They incur no context window cost at inference and produce output through direct forward propagation; modification requires retraining, yielding the lowest editability. By functional role, they are further divided:

- **Policy Parameters ($\mathcal{C}^P_\pi$, $\pi$-Par):** Actor weights that generate actions $a$, encompassing LLM agents, VLA, GUI agent weights, and LoRA adapters.
- **Evaluator Parameters ($\mathcal{C}^P_\phi$, V-Par):** Judge weights that assess $(c, a, o, f)$, encompassing reward models, process reward models (PRMs), verifiers, critics, and VLM judges.

This division is directly relevant to pathway organization—Evaluator parameters can serve as both the product of a transformation (Tokenized → Evaluator) and the intermediate state enabling a further transformation (Evaluator → Policy via RLHF).

The three carrier categories form a continuum:

> **Tokenized → Latent → Parametric**
>
> Along this direction: interpretability ↓, inference efficiency ↑, editability ↓; storage location shifts from external database / prompt → GPU memory → model checkpoint.

### §2.2.3 Orthogonal Attributes

The following three dimensions serve as attribute tags on each carrier instance, not as classification dimensions—they are used as weaving dimensions in pathway analysis:

| Attribute | Values | Usage Context |
|---|---|---|
| **Modality** | textual [txt], visual+text [vis+txt], GUI, embodied, cross-modal | Discussing implementation differences across modalities within each pathway |
| **Abstraction Level** | raw / refined | Distinguishing raw trajectories from refined derivatives, primarily within the Tokenized layer |
| **Experience Source** | {self} (agent self-generated), {human} (human demonstration), {teacher} (teacher model synthesized) | Discussing the impact of experience source on pathway selection |

### §2.2.4 Boundary Clarifications

**Positioning of raw experience.** Raw trajectories are the zero-abstraction instance of Narrative Tokenized, not a category outside the carrier system. Transformations typically start from raw and aim to increase abstraction level (Narrative refined), change formalization degree (Narrative → Schematic), or change architectural locus (Tokenized → Latent / Parametric).

**Embedding attribution by usage.** When embeddings serve as a retrieval index for external memory (retrieved content then enters the context), they are attributed to the Tokenized content they index rather than to Latent. When embeddings serve as learnable memory representations (directly participate in model attention without decoding back to tokens), they are attributed to Latent.

## §2.3 Experience Transformation

Experience Transformation refers to the migration of experience between different carriers. A mapping

$$\mathcal{T}: \mathcal{C}_{\text{src}} \rightarrow \mathcal{C}_{\text{tgt}}$$

constitutes an experience transformation if and only if it satisfies two conditions, where $\mathcal{C}_{\text{src}}, \mathcal{C}_{\text{tgt}} \in \{\mathcal{C}^T_N, \mathcal{C}^T_S, \mathcal{C}^L, \mathcal{C}^P_\pi, \mathcal{C}^P_\phi\}$:

**Condition 1 — Experience Grounding.** The source content must be traceable to one or more experience records $e = (c, a, o, f)$ or their derivatives.

**Condition 2 — Experience Embodiment.** The target carrier must encode the semantic content of the source experience, rather than merely undergoing a semantically irrelevant format conversion.

Condition 1 excludes generic processing that operates on the same data type but lacks traceability to concrete agent decision processes (e.g., pretraining on generic corpora). Condition 2 excludes pure format transcription (e.g., converting a JSON trajectory to markdown) and storage or transmission operations that do not carry experience semantics. Together, these conditions ensure that our analytical focus remains on substantive experience transformation rather than arbitrary steps in a data pipeline.

## §2.4 Seven Foundational Transformation Pathways

Within the above framework, we identify 7 foundational transformation pathways, organized by source carrier type into four subsequent sections:

| Pathway | Definition | Section |
|---|---|---|
| P1: $\mathcal{C}^T_N \rightarrow \mathcal{C}^T_N$ | Narrative → Narrative: same-level semantic abstraction (raw → reflections / rules / insights) | §3 |
| P2: $\mathcal{C}^T_N \rightarrow \mathcal{C}^T_S$ | Narrative → Schematic: same-level formalization (logs → code / workflows / graphs) | §3 |
| P3: $\mathcal{C}^T \rightarrow \mathcal{C}^L$ | Tokenized → Latent: cross-level compression (trajectories → KV cache / soft prompts / memory tokens) | §4 |
| P4: $\mathcal{C}^T \rightarrow \mathcal{C}^P_\phi$ | Tokenized → Evaluator: evaluator internalization (trajectories → RM / PRM / verifier) | §5 |
| P5: $\mathcal{C}^T \rightarrow \mathcal{C}^P_\pi$ | Tokenized → Policy: policy internalization (trajectories → policy weights via SFT / RL) | §5 |
| P6: $\mathcal{C}^P_\phi \rightarrow \mathcal{C}^P_\pi$ | Evaluator → Policy: preference alignment (RM signal → policy weights via RLHF / DPO) | §6 |
| P7: $\mathcal{C}^P \rightarrow \mathcal{C}^T$ | Parametric → Tokenized: knowledge externalization (weights → synthetic trajectories / demonstrations) | §6 |

**Handling of composite pathways.** When a single paper chains multiple pathways as an integrated method (e.g., $\mathcal{C}^T_N \rightarrow \mathcal{C}^T_S \rightarrow \mathcal{C}^P_\pi$ or $\mathcal{C}^T \rightarrow \mathcal{C}^L \rightarrow \mathcal{C}^P_\pi$), its contribution lies in the integration mechanism between pathways rather than in any single pathway itself. Such works are discussed as first-class objects in the independent §7 Composite Pipelines. Papers that incidentally perform two independent transformations are cited in the respective single-pathway sections.
