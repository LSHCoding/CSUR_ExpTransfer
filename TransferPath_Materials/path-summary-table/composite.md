## (A) Completed table

| Work | Composition Pattern | Constituent Pathways | Carrier Pipeline | Integration Mechanism | Training Method | Domain |
|------|---------------------|----------------------|------------------|-----------------------|-----------------|--------|
| [Xia25e] | Evaluator–Policy Co-Evolution | P4↔P6 | π-Par → V-Par → π-Par | alternating-2party | SFT | mobile |
| [Li26n] | Evaluator–Policy Co-Evolution | P4↔P6 | π-Par → V-Par → π-Par | 3party | mixed | GUI |
| [Li26l] | Evaluator–Policy Co-Evolution | P4↔P6 | π-Par → V-Par → π-Par | alternating-2party | GRPO/PPO | out-of-vocab: cross-domain |
| [Wan26u] | Evaluator–Policy Co-Evolution | P4↔P6 | π-Par → V-Par → π-Par | 3party | GRPO/PPO | out-of-vocab: cross-domain |
| [Zha25y] | Evaluator–Policy Co-Evolution | P4↔P6 | π-Par → V-Par → π-Par | alternating-2party | GRPO/PPO | text/reasoning |
| [Sin25b] | Evaluator–Policy Co-Evolution | P4↔P6 | π-Par → V-Par → π-Par | alternating-2party | out-of-vocab: SAC-style RL | embodied |
| [Pan26] | out-of-scope | out-of-scope | out-of-scope | out-of-scope | out-of-scope | out-of-scope |
| [Wan26aj] | Evaluator–Policy Co-Evolution | P4↔P6 | π-Par → V-Par → π-Par | shared-params | GRPO/PPO | tool-use |
| [Sun24b] | Generative Experience Curation | P7→P1→P5 | π-Par → N-Tok → N-Tok → π-Par | exploration-synthesis | SFT | GUI |
| [He24e] | Generative Experience Curation | P7→P2→P5 | π-Par → N-Tok → π-Par | quality-filtering | SFT | web |
| [Xu24] | Generative Experience Curation | P1→P7→P5 | N-Tok → S-Tok → N-Tok → π-Par | exploration-synthesis | SFT | web |
| [Wan24ad] | Generative Experience Curation | P7→P1→P5 | π-Par → N-Tok → N-Tok → π-Par | exploration-synthesis | SFT | embodied |
| [Xu25q] | Generative Experience Curation | P7→P2→P5 | π-Par → S-Tok → π-Par | search-preference | DPO/step-DPO | embodied |
| [Xia25h] | Generative Experience Curation | P7→P5 | π-Par → N-Tok → π-Par | exploration-synthesis | SFT | embodied |
| [He25g] | Generative Experience Curation | P7→P2→P5 | π-Par → S-Tok → π-Par | quality-filtering | SFT | GUI |
| [Son24] | Generative Experience Curation | P7→P2→P5 | π-Par → S-Tok → π-Par | search-preference | DPO/step-DPO | tool-use |
| [Fai26] | Generative Experience Curation | P7→P1→P5 | π-Par → N-Tok → N-Tok → π-Par | exploration-synthesis | SFT | web |
| [Qi24] | Evaluator–Policy Co-Evolution | P4↔P6 | π-Par → V-Par → π-Par | 3party | GRPO/PPO | web |
| [Put24] | Generative Experience Curation | P7→P2→P5 | π-Par → S-Tok → π-Par | search-preference | DPO/step-DPO | web |
| [Bai24] | Generative Experience Curation | P7→P3→P6 | π-Par → V-Par → π-Par | quality-filtering | out-of-vocab: advantage-weighted RL | mobile |
| [Das25] | Generative Experience Curation | P7→P2→P5 | π-Par → N-Tok → π-Par | quality-filtering | SFT | embodied |
| [Ge26] | Refinement-Mediated Internalization | P7→P1→P5 | π-Par → N-Tok → π-Par | privileged-distillation | distillation | text/reasoning |
| [Xio24] | Refinement-Mediated Internalization | P2→P5 | V-Par → S-Tok → π-Par | posterior-reasoning | mixed | tool-use |
| [Yua25c] | Refinement-Mediated Internalization | P7→P1→P5 | π-Par → N-Tok → π-Par | failure-rewriting | SFT | tool-use |
| [Wan26al] | Refinement-Mediated Internalization | P7→P1→P5 | π-Par → S-Tok → π-Par | privileged-distillation | mixed | tool-use |
| [Ye26f] | Refinement-Mediated Internalization | P7→P1→P5 | π-Par → N-Tok → π-Par | privileged-distillation | distillation | text/reasoning |
| [Wan25x] | Refinement-Mediated Internalization | P7→P1→P5 | π-Par → N-Tok → π-Par | failure-rewriting | GRPO/PPO | embodied |
| [Wu25b] | Refinement-Mediated Internalization | P1→P5 | N-Tok → π-Par | failure-rewriting? | mixed | GUI |
| [Yan24m] | Refinement-Mediated Internalization | P1→P5 | N-Tok → N-Tok → π-Par | posterior-reasoning | mixed | tool-use |
| [Xu26j] | Refinement-Mediated Internalization | P7→P1→P5 | π-Par → N-Tok → π-Par | failure-rewriting | GRPO/PPO | tool-use |
| [Din26] | Refinement-Mediated Internalization | P7→P1→P5 | π-Par → N-Tok → π-Par | failure-rewriting | mixed | tool-use |
| [Ala25] | Refinement-Mediated Internalization | P1→P5 | N-Tok → N-Tok → π-Par | privileged-distillation | distillation | tool-use |
| [Zho24e] | out-of-scope | out-of-scope | out-of-scope | out-of-scope | out-of-scope | out-of-scope |
| [Zha26] | Evaluator–Policy Co-Evolution | P4↔P6 | π-Par → V-Par → π-Par | shared-params | mixed | tool-use |
| [Sar24b] | out-of-scope | out-of-scope | out-of-scope | out-of-scope | out-of-scope | out-of-scope |

## (B) Evidence & Notes

### [Xia25e]

- read: full-text
- Composition Pattern — Fig. 3; §3.3: agent and RM improve across self-improvement rounds.
- Constituent Pathways — §3.3: reward-guided exploration yields data; later rounds retrain agent/RM.
- Carrier Pipeline — Fig. 3: policy rollouts feed reward model, then updated policy.
- Integration Mechanism — §3.3: alternating agent update and RM update.
- Training Method — §4.1; App. A.2.1: agent fine-tuned on expanded trajectory data.
- Domain — §1; §4.2.1: mobile GUI task setting.

### [Li26n]

- read: full-text
- Composition Pattern — Fig. 1; §3.3: DS-RM, GP-RM, and UI agent form closed loop.
- Constituent Pathways — Fig. 1; §3.3: reward reflux updates evaluator stack and agent.
- Carrier Pipeline — Fig. 1: agent rollouts judged by DS-RM/GP-RM then reused.
- Integration Mechanism — Fig. 1; §3.3: three parties, not just policy plus one critic.
- Training Method — §4.1; §4.2.3: SFT, RL-style fine-tuning, and reflux retraining coexist.
- Domain — Abstract; §1: GUI agents across desktop/mobile interfaces.

### [Li26l]

- read: full-text
- Composition Pattern — Fig. 1(b); §3: critic and actor co-evolve to avoid stale feedback.
- Constituent Pathways — §3.3: synchronized updates couple critic refinement and policy RL.
- Carrier Pipeline — Fig. 1(b): policy rollouts feed critic; critic reward reshapes policy.
- Integration Mechanism — §3.3: two-party synchronized loop, no third trained module.
- Training Method — §3.3: synchronized GRPO-style optimization.
- Domain — Table 1; §4: WebShop, ALFWorld, SciWorld, DeepSearch span domains.
- Notes — Domain marked `out-of-vocab: cross-domain`.

### [Wan26u]

- read: full-text
- Composition Pattern — Fig. 2; §2: policy, reward model, and environment all adapt.
- Constituent Pathways — Alg. 1: same rollouts update reward and policy under dynamic tasks.
- Carrier Pipeline — Fig. 2: policy trajectories scored by reward model then reused.
- Integration Mechanism — §3.1.4; Fig. 2: explicit three-way coupling with environment evolution.
- Training Method — §2.1; Alg. 1: RL updates with integrated process/outcome rewards.
- Domain — §3.1.1; Fig. 1: OSWorld, AlfWorld, LiveBench are cross-domain.
- Notes — Domain marked `out-of-vocab: cross-domain`.

### [Zha25y]

- read: full-text
- Composition Pattern — Fig. 1; §3.2: generator and verifier reinforced together.
- Constituent Pathways — Alg. 1; §3.2: verifier rewards feed generator; generator supplies verifier data.
- Carrier Pipeline — §3.2: reasoning traces scored by verifier then internalized.
- Integration Mechanism — Eq. 7; Alg. 1: alternating generator/verifier RL.
- Training Method — Alg. 1; §3.2: interleaved RL for both models.
- Domain — §4: math and language reasoning benchmarks.

### [Sin25b]

- read: full-text
- Composition Pattern — Alg. 1; §IV.A: reward model and policy alternate updates.
- Constituent Pathways — Fig. 1; §IV.A.4: policy rollouts become VLM-labeled reward targets.
- Carrier Pipeline — Fig. 1: policy trajectories train reward model; reward model trains policy.
- Integration Mechanism — §IV.C; Eq. 5: alternating reward/policy improvement loop.
- Training Method — §IV.A.4: SAC inner-loop policy optimization.
- Domain — §V.A: MetaWorld and DMControl robotics.
- Notes — Training marked `out-of-vocab: SAC-style RL`.

### [Pan26]

- read: full-text
- Composition Pattern — §3.3: adaptive critic gating inside RL optimizer, not composite transformation.
- Constituent Pathways — §3.2–§3.3: no substantive serial carrier transform beyond baseline RL.
- Carrier Pipeline — Fig. 1: critic/no-critic switch stays inside training loop.
- Integration Mechanism — §3.3: hard EV gating is optimizer control, not table mechanism.
- Training Method — Alg. 1: PPO/GRPO switcher, but paper is excluded on scope grounds.
- Domain — §4.1: mixed tasks, but scope failure occurs earlier.
- Notes — Marked `out-of-scope`: optimizer-selection paper, not a substantive composite transformation method.

### [Wan26aj]

- read: full-text
- Composition Pattern — §3.5; Fig. 2: policy and internal reward co-evolve end-to-end.
- Constituent Pathways — §3.2–§3.5: same model emits guidance and learns from rewardized guidance.
- Carrier Pipeline — Fig. 2: policy outputs self-guidance that becomes internal reward.
- Integration Mechanism — §3.2; §3.5: same parameters produce guidance and action.
- Training Method — §3.4: single GRPO objective.
- Domain — §4.1: interactive agents across ALFWorld, ScienceWorld, WebShop.
- Notes — Domain collapsed to `tool-use`.

### [Sun24b]

- read: full-text
- Composition Pattern — Fig. 2–3; §3.2: exploration precedes reverse task synthesis.
- Constituent Pathways — §3.2: interactions become tasks, then new trajectories, then SFT data.
- Carrier Pipeline — Fig. 2–3: policy traces become text tasks, then training trajectories.
- Integration Mechanism — §3.2: reverse synthesis from exploration is the core bridge.
- Training Method — §4.2: SFT on collected trajectories.
- Domain — §4.1; Tables 1–2: GUI/mobile-web control.

### [He24e]

- read: full-text
- Composition Pattern — Fig. 2; §4: exploration, judging, and optimization form curation loop.
- Constituent Pathways — §4.2–§4.3: exploratory trajectories filtered by GPT-4o judgments before retraining.
- Carrier Pipeline — Fig. 2: policy rollouts become accepted trajectory data for SFT.
- Integration Mechanism — §4.3: retained only well-performing judged trajectories.
- Training Method — Fig. 2; §4: imitation/self-improvement fine-tuning.
- Domain — §3.1: real-world web navigation.

### [Xu24]

- read: full-text
- Composition Pattern — Fig. 2; §2: tutorials are replayed into executable web trajectories.
- Constituent Pathways — §2.1–§2.2.2: raw tutorial text → task spec → replayed trajectory.
- Carrier Pipeline — Fig. 2; Fig. 5: tutorial tokens become structured guidance then training traces.
- Integration Mechanism — §2.2: guided replay is the defining bridge.
- Training Method — §2.3.3; §3.2: SFT on synthesized data.
- Domain — §3.1: web automation across 127 websites.

### [Wan24ad]

- read: full-text
- Composition Pattern — Fig. 1a; §3.2: generator and navigator drive self-refining data flywheel.
- Constituent Pathways — Fig. 2: trajectories are re-captioned into instructions, then reused.
- Carrier Pipeline — Fig. 1a–2: navigator rollouts become instructions, then improved training data.
- Integration Mechanism — §3.2: instruction synthesis from exploration is central.
- Training Method — §3.2; §4.1: LoRA/SFT on refined data.
- Domain — §1: vision-and-language navigation.

### [Xu25q]

- read: full-text
- Composition Pattern — Fig. 1; Alg. 1: MCTS collects preference data before optimization.
- Constituent Pathways — §3.4: searched trajectories become preference pairs for policy update.
- Carrier Pipeline — Fig. 1: policy rollouts condensed into preference-structured supervision.
- Integration Mechanism — §3.4: online preference optimization from tree search.
- Training Method — Alg. 1; §3.4: SFT warm-up plus DPO.
- Domain — §5.1: embodied planning is headline setting.
- Notes — WebShop also appears, but embodied is primary framing.

### [Xia25h]

- read: full-text
- Composition Pattern — Fig. 3: residual probing collects improved data for later distillation.
- Constituent Pathways — §3: specialist rollouts are curated then distilled into generalist.
- Carrier Pipeline — Fig. 3: policy-generated trajectories return as SFT data.
- Integration Mechanism — §3.2: probe/learn stage exists to synthesize better data.
- Training Method — §3: final stage is standard SFT.
- Domain — §4: robot manipulation / VLA.

### [He25g]

- read: full-text
- Composition Pattern — Fig. 1; §2: noisy teacher data are graded then filtered.
- Constituent Pathways — §3.1–§3.2: teacher rollouts get step grades before policy training.
- Carrier Pipeline — Fig. 1: policy traces become graded steps, then student weights.
- Integration Mechanism — §3.2: keep only correct steps.
- Training Method — §4.1: multimodal SFT.
- Domain — §1; Table 1: computer-use GUI setting.

### [Son24]

- read: full-text
- Composition Pattern — Fig. 1–2: exploration produces failure/success pairs for optimization.
- Constituent Pathways — §3.2: sampled trajectories become contrastive preference supervision.
- Carrier Pipeline — Fig. 1: policy rollouts converted into structured preference pairs.
- Integration Mechanism — §3.2: trajectory preferences, not plain filtering.
- Training Method — §3.2: iterative DPO after SFT warm-start.
- Domain — §4.1: mixed agent tasks; collapsed to `tool-use`.

### [Fai26]

- read: full-text
- Composition Pattern — Fig. 1; §2.2.2: exploration directly grounds later task synthesis.
- Constituent Pathways — §2.2–§2.4: site exploration yields synthesized/refined tuples for training.
- Carrier Pipeline — Fig. 1: surfed traces become tasks/tuples then SFT corpus.
- Integration Mechanism — §2.2.2: exploration-guided synthesis is primary.
- Training Method — §2.4: refined tuples converted to SFT data.
- Domain — §1: website automation.

### [Qi24]

- read: full-text
- Composition Pattern — Abstract; Fig. 2: curriculum, ORM, and policy evolve together.
- Constituent Pathways — Alg. 1: failures spawn new tasks; ORM scores rollouts; policy updated.
- Carrier Pipeline — Fig. 2: policy rollouts feed ORM, which guides RL.
- Integration Mechanism — §2.1–§2.2: three parties, including self-evolving curriculum.
- Training Method — §2.2; Alg. 1: PPO-style online RL.
- Domain — §3.1: web agents.

### [Put24]

- read: full-text
- Composition Pattern — Fig. 4; §5.2: MCTS plus critic curate preference data.
- Constituent Pathways — Alg. 1: searched trajectories scored into preference pairs for DPO.
- Carrier Pipeline — §5.2: policy traces become structured preference supervision.
- Integration Mechanism — §5.1.1: search-ranked preferences are the bridge.
- Training Method — §5.2: off-policy step-level DPO.
- Domain — §4; §6: web shopping / booking.

### [Bai24]

- read: full-text
- Composition Pattern — Fig. 5; §4.2–§4.3: collected experience is filtered at step and instruction levels.
- Constituent Pathways — §4.2–§4.4: same rollouts train value filters that shape actor updates.
- Carrier Pipeline — Fig. 5: policy experience transformed into value-weighted supervision then actor.
- Integration Mechanism — §4.3: prioritize/filter experience rather than rewrite it.
- Training Method — §4: advantage-weighted offline-to-online RL.
- Domain — §1; Fig. 1: Android device control.
- Notes — Training marked `out-of-vocab: advantage-weighted RL`.

### [Das25]

- read: full-text
- Composition Pattern — Fig. 2; §III-B: generated solutions are simulator-verified before training.
- Constituent Pathways — Eq. 4–5: generated demonstrations filtered by verifier then SFT.
- Carrier Pipeline — Fig. 2: generated plans enter verified database then student model.
- Integration Mechanism — §III-B: filter wrong solutions using simulator verification.
- Training Method — Eq. 5; §IV-A: SFT.
- Domain — §I; §IV.C: robotic manipulation.

### [Ge26]

- read: full-text
- Composition Pattern — Fig. 2; §3.2: reflective corrections are distilled into policy.
- Constituent Pathways — §3.1–§3.2: rollback/reflection produce corrected trajectories for distillation.
- Carrier Pipeline — Fig. 2: policy experience becomes natural-language corrective experience, then weights.
- Integration Mechanism — §3.2: teacher has privileged experience context; student does not.
- Training Method — §3.2; §4: experience distillation via SFT-style objective.
- Domain — §4.1: mainly reasoning/puzzle/code benchmarks.
- Notes — Domain collapsed to `text/reasoning`.

### [Xio24]

- read: full-text
- Composition Pattern — Fig. 2; §3.3: step-reward comparisons become training supervision.
- Constituent Pathways — §3.2–§3.3: evaluator-derived contrastive step pairs feed optimization.
- Carrier Pipeline — §3.3: step reward model yields structured preference pairs for policy.
- Integration Mechanism — §3.2: posterior step scoring selects better continuation.
- Training Method — Eq. 10: step-DPO + outcome-DPO + SFT.
- Domain — §4.1: WebShop, InterCodeSQL, ALFWorld; collapsed to `tool-use`.

### [Yua25c]

- read: full-text
- Composition Pattern — Fig. 2; §3: failed paths are spliced into revision trajectories.
- Constituent Pathways — §3.1–§3.2: first-error localization and splice create new training traces.
- Carrier Pipeline — Fig. 2: policy failures become revised textual trajectories, then policy weights.
- Integration Mechanism — §3.1: direct failure rewriting around first error.
- Training Method — Fig. 2; §3.2: iterative supervised fine-tuning.
- Domain — §4.1: WebShop, ScienceWorld, TextCraft; collapsed to `tool-use`.

### [Wan26al]

- read: full-text
- Composition Pattern — Fig. 1; §3.2: rollout summaries become privileged teacher skills.
- Constituent Pathways — §3.2–§3.4: student rollouts summarized into skills, then distilled back.
- Carrier Pipeline — Fig. 1: policy trajectories become skill summaries then student weights.
- Integration Mechanism — §3.2; Eq. 6–7: skills only condition teacher during training.
- Training Method — Eq. 14: GRPO plus self-distillation loss.
- Domain — §4.1: AppWorld and Sokoban; collapsed to `tool-use`.

### [Ye26f]

- read: full-text
- Composition Pattern — Fig. 3; §3.2: extracted knowledge is distilled into parameters.
- Constituent Pathways — §3.1–§3.2: trajectories yield knowledge context, then on-policy distillation.
- Carrier Pipeline — Fig. 3: policy experience becomes textual experiential knowledge then weights.
- Integration Mechanism — §1; Eq. 2: teacher sees knowledge context; student does not.
- Training Method — §3.2; Eq. 2: context distillation.
- Domain — §4.1: FrozenLake and Sokoban text games.

### [Wan25x]

- read: full-text
- Composition Pattern — Fig. 2; §3.2: deviated actions are reflected into calibrated trajectories.
- Constituent Pathways — §3.2–§3.3: exploration traces are rewritten, then reused for policy training.
- Carrier Pipeline — Fig. 2: policy trajectories become calibrated textual trajectories then weights.
- Integration Mechanism — §3.2: explicit reflection-based trajectory correction after deviation.
- Training Method — Eq. 10: reward-weighted policy-gradient reinforced training.
- Domain — §4.1; App. G.1: VirtualHome, ALFWorld, ScienceWorld; collapsed to `embodied`.

### [Wu25b]

- read: full-text
- Composition Pattern — Fig. 2; §2.4–§2.5: synthetic reflection data are internalized into model.
- Constituent Pathways — §2.4: successful trajectories converted into reflection/error-correction supervision.
- Carrier Pipeline — Fig. 2: rewritten reflection data directly trains GUI model.
- Integration Mechanism — §2.4; Fig. 4: offline rewriting plus online mined corrections; closest to failure rewriting.
- Training Method — Abstract; Fig. 2: pretraining + offline SFT + online tuning.
- Domain — §2.1; Table 3: GUI/mobile automation.
- Notes — Mechanism marked `failure-rewriting?` because §2.5 also has posterior correction mining.

### [Yan24m]

- read: full-text
- Composition Pattern — Fig. 1; §2.1: ActRe supplies posterior reasons for sampled actions.
- Constituent Pathways — §2.1–§2.2: posterior-rationalized trajectories become self-training data.
- Carrier Pipeline — Fig. 1: sampled actions become ReAct-style trajectories, then weights.
- Integration Mechanism — §2.1: posterior rationales are the key intermediate.
- Training Method — Eq. 1–2: SFT bootstrap plus policy-gradient contrastive self-training.
- Domain — §3: ALFWorld and WebShop; collapsed to `tool-use`.

### [Xu26j]

- read: full-text
- Composition Pattern — Fig. 1; §4: noisy trajectories are purified by rollback/replacement.
- Constituent Pathways — §4: failed segments are corrected before RL updates.
- Carrier Pipeline — Fig. 1; SAAR: policy trajectories become purified trajectories then reused.
- Integration Mechanism — §4: self-purification is explicit failure rewriting.
- Training Method — §5: improves agentic RL; GRPO-style family is terminal optimizer.
- Domain — §5.1: math/science/code with tools; collapsed to `tool-use`.

### [Din26]

- read: full-text
- Composition Pattern — Fig. 2; §3.6: failed trajectories relabeled into usable hindsight data.
- Constituent Pathways — §3.3–§3.6: failure classification, relabeling, packaging, then training.
- Carrier Pipeline — Fig. 2: failed policy traces become rewritten goal-conditioned training data.
- Integration Mechanism — §3.4–§3.5: hindsight relabeling rewrites failure into valid supervision.
- Training Method — Abstract; §3.6; Table 2: outputs SFT, DPO, and ShareGPT formats.
- Domain — Abstract: WebArena and ToolBench; collapsed to `tool-use`.

### [Ala25]

- read: full-text
- Composition Pattern — Fig. 3; §3: hint-conditioned teacher outputs are distilled into student.
- Constituent Pathways — §3: task hints create coached trajectories, then student internalizes them.
- Carrier Pipeline — Fig. 3: hints and coached outputs become agent weights.
- Integration Mechanism — §3: hints are privileged training context, absent at inference.
- Training Method — §3; Fig. 3: iterative context distillation.
- Domain — §5.1: ToolQA and OfficeBench; collapsed to `tool-use`.

### [Zho24e]

- read: full-text
- Composition Pattern — §3–§4: LFM is a single evaluator-to-policy transfer step.
- Constituent Pathways — Fig. 1: feedback model directly selects desirable behavior for imitation.
- Carrier Pipeline — Fig. 1: no substantive composite chain beyond evaluator-guided imitation.
- Integration Mechanism — §3: not co-evolution, not refinement chain, not curation chain.
- Training Method — §4: imitation from LFM-selected behaviors.
- Domain — §5.1: grounded instruction following.
- Notes — Marked `out-of-scope`: single-step evaluator→policy transfer, not a composite transformation pattern for Table 7.1.

### [Zha26]

- read: full-text
- Composition Pattern — Fig. 1–2; §3.1: policy and self-reflection capability jointly evolve.
- Constituent Pathways — §3.4: intrinsic-feedback evaluator and policy are jointly optimized.
- Carrier Pipeline — Fig. 2: same model produces reflective feedback that trains action policy.
- Integration Mechanism — Eq. 4; §4.11: shared parameters across reflection and acting.
- Training Method — §3.4: GRPO for decision policy plus REINFORCE for reflection.
- Domain — §4.1: ALFWorld, WebShop, Sokoban, Minesweeper; collapsed to `tool-use`.

### [Sar24b]

- read: full-text
- Composition Pattern — §3; Fig. 1: token-to-token memory abstraction for retrieval.
- Constituent Pathways — §3: no terminal policy/evaluator internalization.
- Carrier Pipeline — Fig. 1: distilled “programs of thought” stay as external memory.
- Integration Mechanism — §3: inference-time retrieval, not Table 7.1 composition.
- Training Method — §4: memory retrieval ablations, not policy internalization.
- Domain — §4.1: TEACh, VisualWebArena, Ego4D.
- Notes — Marked `out-of-scope`: composite token-memory distillation, not policy/evaluator composite internalization.

Possible next steps:

1. I can turn this into a project file with cleaner wording for CSUR.
2. I can also produce a stricter second-pass audit on the uncertain rows (`Wu25b`, mixed-domain papers, and any `out-of-vocab` cells).