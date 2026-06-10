# Experience transformation gaps from paper set

##### [**Undermind**](https://undermind.ai)

---


## Table of Contents

- [Challenges](#challenges)
  - [Warm-start dependence remains structural](#warm-start-dependence-remains-structural)
  - [Verification remains the decisive weak link](#verification-remains-the-decisive-weak-link)
  - [Credit assignment remains unresolved across levels of granularity](#credit-assignment-remains-unresolved-across-levels-of-granularity)
  - [Failure reuse is promising, but still fragile](#failure-reuse-is-promising-but-still-fragile)
  - [Self-improvement loops still go stale or self-confirm](#self-improvement-loops-still-go-stale-or-self-confirm)
  - [Experience carriers still lose crucial state](#experience-carriers-still-lose-crucial-state)
  - [Evaluation still hides the hardest parts of the problem](#evaluation-still-hides-the-hardest-parts-of-the-problem)
- [Future directions](#future-directions)
  - [Failure-native pipelines are the clearest underdeveloped direction](#failure-native-pipelines-are-the-clearest-underdeveloped-direction)
  - [Evaluators need to co-evolve and become more grounded](#evaluators-need-to-co-evolve-and-become-more-grounded)
  - [Credit assignment should become adaptive rather than doctrinal](#credit-assignment-should-become-adaptive-rather-than-doctrinal)
  - [Internalization methods need to avoid both prompt crutches and over-cleaning](#internalization-methods-need-to-avoid-both-prompt-crutches-and-over-cleaning)
  - [Richer multimodal carriers need direct comparison, not isolated proposals](#richer-multimodal-carriers-need-direct-comparison-not-isolated-proposals)
  - [Transfer-first evaluation should replace near-distribution reporting](#transfer-first-evaluation-should-replace-near-distribution-reporting)
- [References](#references)

## Challenges

| Challenge | Why it is still undercovered | Representative support |
|:---|:---|:---|
| Bootstrapping still depends on strong seeds, strong teachers, or both | Most pipelines need a competent base policy, successful traces, or a stronger evaluator before self-improvement becomes productive | \[Son24\], \[Xia25h\], \[He25g\], \[Li26n\], \[Yua25c\], \[Bai24\] |
| Verification is still the main bottleneck in turning experience into supervision | LLM judges, reward models, and replay verifiers remain noisy enough that transformed data cannot be treated as clean ground truth | \[Xia25e\], \[Sun24b\], \[Xu24\], \[He24e\], \[Din26\], \[Das25\], \[Zho24e\] |
| Credit assignment is unresolved across trajectory, turn, and step scales | Dense signals help, but naive step signals are unstable, while coarse signals miss the real point of failure | \[Son24\], \[Xio24\], \[Wan25x\], \[Wan26aj\], \[Pan26\], \[Wan26u\], \[Xu26j\] |
| Failure is useful, but current reuse schemes are still brittle and narrow | The best recent methods salvage only certain failure types and often need heavy filtering, relabeling, or purification to avoid poisoning learning | \[Din26\], \[Yua25c\], \[Xu26j\], \[He25g\], \[Son24\], \[Ge26\] |
| Self-improvement loops still drift, stale, or overfit to their own transformed experience | Policy, critic, and skill distributions move during training, and many loops become unstable or locally self-confirming | \[Li26l\], \[Li26n\], \[Wan26aj\], \[Wan26al\], \[Ye26f\], \[Qi24\], \[Bai24\] |
| Carrier and representation choices still erase crucial state | Many methods compress experience into text, hints, skills, or purified traces that lose visual, temporal, or causal detail needed later | \[Sin25b\], \[Xu25q\], \[Sar24b\], \[Wu25b\], \[Zho24e\], \[Das25\] |
| Evaluation still flatters progress by simplifying the hard parts | Many papers narrow websites, tasks, action spaces, or reward definitions in ways that make transformed experience look cleaner than it is | \[He24e\], \[Xu24\], \[Fai26\], \[Qi24\], \[Bai24\], \[Sar24b\], \[Das25\] |

### Warm-start dependence remains structural

The literature still does not show a reliable way to start from mostly bad interaction data and climb upward without a strong seed. \[Son24\] is unusually direct: Table 5 shows that ETO without behavioral cloning drops to 12.5 average reward, below the untuned base model at 17.9, so failure-based contrastive learning does not bootstrap itself. \[Xia25h\] states in Section 5.2 that PLD assumes a non-zero base success rate for warm-start exploration. \[He25g\] makes the same dependency operational. Section 10 notes that if the teacher does not produce successful computer-use trajectories, the synthesis pipeline has nothing usable to distill. \[Yua25c\] identifies the same problem in reflective self-training. Section 3.2 says the early model discovers only a limited number of optimal trajectories, so the whole revision loop is bottlenecked by cold-start scarcity. \[Bai24\] also begins from AutoUI-Base checkpoints rather than raw exploration.

The stronger claim is that even papers marketed as self-evolving remain teacher bootstrapped. \[Li26n\] uses GPT-4o as the general-purpose reward model during the “early stages” in Section 4.1. \[Sun24b\] relies on GPT-4o both for reverse task synthesis and for the trajectory reward model in Section 4.1. \[Xu24\] filters tutorials with GPT-4o-mini and then validates replay with a VLM evaluator whose accuracy is only 84 percent in Appendix D. **Inference.** The field has many flywheels, but very few genuine ignition mechanisms. Most current systems begin after competence already exists, either in the policy, the teacher, or the verifier \[Son24, Xia25h, He25g, Li26n, Yua25c\].

### Verification remains the decisive weak link

Across this paper set, experience is rarely reused directly. It is filtered, relabeled, judged, or purified first, and that verification layer is still noisy. \[Xia25e\] builds a custom benchmark because no standard GUI reward benchmark exists, then shows in Table 7 that unified history-aware reward modeling helps. Yet Section 5 still admits that the reward model may produce suboptimal signals and cannot guarantee fully correct expanded trajectories. \[Sun24b\] uses a GPT-4o-based trajectory reward model to filter synthesized trajectories, but Section 5.3 shows performance saturating around 1,500 trajectories, which suggests that more generated data does not solve judgment noise by itself. \[Xu24\] reports only 84 percent agreement for its evaluator in Appendix D, while Appendix H shows failures caused by tutorial expiration and website change. \[He24e\] leans on GPT-4o as both auto-evaluator and improvement signal, and Section 4.3 admits cross-website gains are unstable.

The same bottleneck appears in hindsight and robotics settings. \[Din26\] adds a multi-stage validation loop because naive relabeling is harmful. Table 2 shows that removing the confidence filter increases noise from 2.3 percent to 14.8 percent, and random relabeling loses 6.0 points versus full AgentHER. \[Das25\] can only transform manipulation experience because the simulator provides an automatic verification operator in Section III-B. When that strong verifier disappears, the method’s premise weakens sharply. \[Zho24e\] reaches a related conclusion from language feedback: Appendix G shows weaker judges identify spurious actions as productive, and Table 3 shows that direct action imitation can underperform simple behavioral cloning. **Inference.** The field’s real limiting reagent is not raw experience volume. It is verifier reliability at the level where the transformation happens \[Xia25e, Xu24, Din26, Das25, Zho24e\].

### Credit assignment remains unresolved across levels of granularity

Several papers show that outcome-only supervision is too coarse, but they disagree on what finer signal should replace it. \[Son24\] finds in Table 4 that step-level contrastive data is dramatically worse than trajectory-level data, with average reward dropping from 67.4 to 8.3. \[Xio24\] moves in the opposite direction and argues that iterative step-level refinement is helpful, but Table 4 also shows performance peaking at iteration 4 and then dropping at iteration 5, while Section 5.3 admits Monte Carlo step scoring is noisy. \[Wan25x\] identifies deviations with Monte Carlo step rewards, yet Section 7 lists the heavy cost of reward construction and the inability to handle multiple deviated actions as core limitations. \[Xu26j\] shows why crude token or trajectory credit is problematic: Section 3 argues that GRPO reinforces erroneous reasoning inside successful solutions, while Appendix B reports that using erroneous tool calls as negative DPO pairs can trigger late-stage collapse.

The deeper problem is that different papers need different supervision units. \[Wan26aj\] maps verbal self-guidance into small scalar rewards at each step, but Figure 5 shows that full-strength internal reward too early harms performance, and Appendix B reports query looping in WebShop rising from 17.5 percent to 67.8 percent. \[Pan26\] argues that whether a critic helps depends on explained variance, not on a fixed PPO versus GRPO commitment. Figure 5 shows critic usefulness can even regress mid-training in FrozenLake. \[Wan26u\] mixes outcome and process signals, but Table 2 reveals a trade-off between optimizing the policy and optimizing the reward model’s own process accuracy. **Inference.** The open question is no longer whether denser feedback helps. It is when a denser signal is causally aligned with eventual success and when it is only a more convenient proxy \[Son24, Xio24, Wan25x, Pan26, Wan26aj, Wan26u, Xu26j\].

### Failure reuse is promising, but still fragile

Some of the most interesting progress in this set comes from learning from failure rather than discarding it, but the gains are narrow and highly mediated. \[Din26\] shows that hindsight relabeling works best for incomplete trajectories and yields much smaller gains for tool errors, only 2.1 points in Figure 5 because crashes leave little salvageable signal. \[Yua25c\] finds that self-corrected trajectories can outperform GPT-4o “optimal” trajectories for training the base agent, but the whole loop depends on the model already being able to identify the first error in Section 3.1. \[Xu26j\] goes further by purifying failed trajectories with SAAR, yet Section 4.3 says 30 percent raw trajectories must be kept for the 7B model to preserve robustness. Full purification makes the learner brittle. \[He25g\] also shows that even successful trajectories contain many wrong steps. Table 2 finds that fewer than half the steps in successful traces are correct, so success labels cannot be reused naively.

The hidden difficulty is that each paper salvages a different slice of failure. \[Ge26\] argues in Table 4 that rehearsal on successful rollouts is not enough and that counterfactual correction is what lifts Pass@128. \[Son24\] uses failure as trajectory-level negative evidence but cannot localize the bad action without destabilizing training. \[Wan25x\] calibrates at the first deviation only, then lists multi-deviation calibration as future work in Section 7. **Inference.** The field still lacks a general representation of failure that preserves at least four things together: where the trajectory went wrong, why it went wrong, what repair was attempted, and whether the repair generalized beyond that episode \[Din26, Yua25c, Xu26j, He25g, Ge26, Wan25x\].

### Self-improvement loops still go stale or self-confirm

The newest papers increasingly agree that transformed experience becomes stale as soon as the policy changes. \[Li26l\] is the clearest statement of the problem. Figure 3 shows fail-pattern drift over training, and Table 2 shows that removing critic evolution hurts much more than removing saturation-aware shaping. \[Li26n\] also presents a closed-loop reward reflux system, but Table 5 shows that combining domain-specific and general-purpose reward models actually hurts moderate-difficulty tasks relative to the domain-specific model alone. \[Wan26al\] finds that letting the teacher own rollout generation causes catastrophic off-policy collapse, and Table 2 shows frozen teachers plateau far below evolving ones. \[Ye26f\] reaches a parallel result from another angle: Figure 6 shows off-policy context distillation causes catastrophic forgetting of general capabilities, while on-policy consolidation avoids that failure.

The same pattern appears in environment-facing agents. \[Qi24\] uses replay buffers, KL control, and confidence filtering because the policy otherwise drifts toward recent tasks and forgets older behavior. Appendix C shows a real cross-site trade-off, with Map performance declining while other sites improve. \[Bai24\] demonstrates policy staleness directly in Figure 4, where frozen device-control policies degrade over days as the environment changes. \[He24e\] shows a subtler version of the same issue: Section 4.4 says iterative optimization makes trajectories shorter, but this also increases hallucinated early stopping. **Inference.** Current loops are better described as moving-target supervision systems than as simple self-improvement pipelines. They still need principled mechanisms for evaluator refresh, replay selection, and anti-collapse control \[Li26l, Li26n, Wan26al, Ye26f, Qi24, Bai24, He24e\].

### Experience carriers still lose crucial state

A recurring limitation is that transformed experience often becomes easier to train on by becoming less faithful to the original interaction. \[Sin25b\] improves VLM feedback by adding trajectory sketches, but Section VI still says the method is bounded by the underlying VLM and would likely need intermediate views or subgoal annotations for long-horizon tasks. \[Xu25q\] uses selective state representation, keeping only the current image and converting history into text in Section 3.3, which is an implicit compression gamble in visually grounded planning. \[Sar24b\] reports a strong embodied abstraction story, but Table 1 shows success dropping from 35.1 percent with ground-truth perception to 10.5 percent with estimated perception, so the distilled program of thought cannot repair missing perception. Table S1 also shows that full text trajectory memory can beat the more visibly multimodal variant on VisualWebArena. \[Wu25b\] narrows reflection data mostly to visual and action-grounded errors and says in Appendix B that deeper planning failures are not yet covered.

Other papers expose the same problem from different carriers. \[Zho24e\] names the verbalization module as a core limitation, because the whole feedback loop depends on turning environmental state into faithful text. \[Das25\] trains manipulation policies from privileged simulator state, then shows in Figure 4 that success drops sharply when deployment uses visual observations instead of ground-truth state. **Inference.** Much of the current literature transforms experience by stripping away exactly the spatial, perceptual, and temporal detail that later failures depend on. This is efficient for training, but it constrains how much of the original experience can actually be reused \[Sin25b, Xu25q, Sar24b, Wu25b, Zho24e, Das25\].

### Evaluation still hides the hardest parts of the problem

Many gains in this set depend on evaluation choices that make the transformation problem cleaner than real deployment. \[He24e\] excludes richer interaction types such as drag and hover and still relies heavily on accessibility trees, despite presenting a multimodal web agent. \[Xu24\] narrows ScreenSpot evaluation to web-only cases aligned with its dataset and reports a replay success rate of only 39.9 percent in Appendix C, which means most harvested tutorials never become usable trajectories. \[Fai26\] caps exploration at 1,000 synthesized tasks per website and excludes Wikipedia and Maps from WebArena evaluation. \[Qi24\] evaluates on WebArena-Lite for cost reasons and uses manually reviewed GPT-4o filtered tasks. \[Bai24\] excludes portions of Android-in-the-Wild for security and account reasons despite the “in-the-wild” framing. \[Sar24b\] omits the verification stage entirely on Ego4D because the task is passive, so the full loop is not tested there. \[Das25\] depends on simulator-side ground truth and structured manipulation tasks.

These are not minor implementation details. They shape what kinds of transformed experience appear to work. Binary final rewards, filtered task pools, fixed APIs, and privileged state all make experience reuse look more reliable than it is under interface drift or ambiguous partial progress. **Inference.** The literature still has stronger evidence for whether a method can exploit a curated scaffold than for whether it can robustly transform messy open-world experience into reusable knowledge \[He24e, Xu24, Fai26, Qi24, Bai24, Sar24b, Das25\].

## Future directions

| Direction | What concrete progress would look like | Core support |
|:---|:---|:---|
| Failure-native transformation pipelines | Store partial progress, failure type, repair attempt, and verified recovery rather than success-only traces | \[Din26\], \[Yua25c\], \[Xu26j\], \[Ge26\], \[Wan25x\] |
| Co-evolving and grounded evaluators | Refresh judges and reward models online while tying more of their signals to environment-checkable changes | \[Li26l\], \[Li26n\], \[Xia25e\], \[Wan26u\], \[Zho24e\] |
| Adaptive multi-scale credit assignment | Learn when to use trajectory, turn, step, or token supervision instead of fixing one granularity for all tasks | \[Pan26\], \[Wan26aj\], \[Son24\], \[Xio24\], \[Wan25x\], \[Xu26j\] |
| Internalization without prompt overfitting or purification collapse | Distill hints, skills, and reflection into policy weights while preserving robustness and exploration diversity | \[Ala25\], \[Wan26al\], \[Ye26f\], \[Ge26\], \[Wu25b\] |
| Richer multimodal carriers and cross-carrier comparisons | Compare the same underlying experience after conversion into different representations and test which details survive | \[Sin25b\], \[Sar24b\], \[Xu25q\], \[Wu25b\], \[Das25\] |
| Transfer-first evaluation and online systems reporting | Measure gains on unseen sites, changed interfaces, stale tasks, and changing environments, with full rollout economics | \[He24e\], \[Xu24\], \[Qi24\], \[Bai24\], \[Fai26\], \[Xia25h\] |

### Failure-native pipelines are the clearest underdeveloped direction

This paper set already shows that partial failures can be more valuable than filtered success, but only when they are transformed with structure. \[Din26\] demonstrates the core idea with hindsight relabeling, but Figure 5 also shows the transformability of failures is highly uneven across failure types. \[Yua25c\] shows that revision trajectories derived from the model’s own errors can beat expert trajectories for training, which means repair traces are not just auxiliary metadata. They can be better supervision than pristine demonstrations. \[Xu26j\] adds a second lesson: cleaned trajectories cannot fully replace raw ones, because some noise must stay in the curriculum to preserve self-repair ability. \[Ge26\] then shows that counterfactual correction, not rehearsal alone, is what changes the capability ceiling. \[Wan25x\] suggests that the timing of correction matters too, but currently corrects only at the first deviation.

Concrete progress would look like a single training object that preserves four linked fields for each imperfect episode: the best verified prefix, the diagnosed failure span, the repair attempt, and the post-repair outcome. A convincing paper would compare success-only replay, hindsight relabeling, repair-annotated replay, and mixed raw-plus-purified replay under the same rollout budget. It should measure recovery from seeded failure families, not only end-task success. That would test whether the agent is learning reusable repair skills rather than merely benefiting from cleaner labels.

### Evaluators need to co-evolve and become more grounded

The strongest recent papers already point toward moving judges and reward models online. \[Li26l\] shows directly that stale critics underperform as failure patterns drift. \[Li26n\] uses disagreement between domain-specific and general-purpose reward models as a reflux signal, but Table 5 also shows that more judge diversity is not automatically better. \[Xia25e\] collapses step and outcome reward into one unified reward model, which is useful, yet Section 5 still warns that reward noise can corrupt trajectory expansion. \[Wan26u\] treats environment, reward model, and policy as jointly evolving objects, and its main contribution is precisely that the reward model should not remain fixed while the task pool changes. \[Zho24e\] offers a complementary lesson from older language-feedback work: feedback is most useful when it is informative and cheap, but it is brittle when verbalization and judge quality drift.

Concrete progress would mean evaluator systems that are both adaptive and auditable. The most promising path is not unrestricted LLM judgment. It is hybrid feedback in which some signals are tied to verifiable state changes, action effects, or partial completion, while other signals remain textual and diagnostic. Verification should report judge false positives and false negatives over training time, not only final policy wins. Right now the field has many better judges, but too little evidence about whether those judges stay calibrated after the policy moves.

### Credit assignment should become adaptive rather than doctrinal

Different papers in this set each discover that one supervision granularity is not enough. \[Pan26\] formalizes the critic question as a dynamic gating problem rather than a static algorithm choice. \[Wan26aj\] shows that step-level self-guidance is useful only under a trust schedule, because the same internal reward can help later and harm earlier. \[Son24\] shows that naive step-level contrastive supervision can be much worse than trajectory-level learning. \[Xio24\] and \[Wan25x\] show that finer-grained process signals help only when their construction is sufficiently reliable. \[Xu26j\] demonstrates that token- and action-level punishment can create reasoning-action misalignment if the correction target is too local.

The undercovered direction is a learner that decides when the supervision unit should be the whole rollout, a segment, a single step, or a token block. Verification for such a system should include counterexamples where denser signals hurt. A method would be much more convincing if it could explain why it used trajectory-level supervision on one failure class and step-level repair on another. That would move the field beyond the current pattern of proposing one favored granularity per paper.

### Internalization methods need to avoid both prompt crutches and over-cleaning

A second frontier is how to turn externalized experience into policy weights without simply teaching the model to depend on added context or overly sanitized traces. \[Ala25\] shows that hint internalization can beat ever-growing prompts, but its appendix also reveals human-written hints and balancing choices still matter, and some ablations show trade-offs across tasks rather than uniform gains. \[Wan26al\] makes the prompt-overfitting problem especially clear: skill-augmented GRPO reaches high training accuracy but collapses badly on validation, while using skills to guide the teacher rather than the student generalizes much better. \[Ye26f\] shows that raw trajectories are worse than extracted knowledge for consolidation and that off-policy context distillation causes catastrophic forgetting. \[Ge26\] shows that internalizing reflective experience can expand the capability ceiling, but Table 6 also shows auxiliary RL or early-experience targets can shrink Pass@128 while improving Pass@1. \[Wu25b\] adds a cautionary signal from GUI reflection, where regular GUI pretraining erodes reflection-related abilities before reflection tuning restores them.

Concrete progress would mean internalization systems that report two things at once: whether the model can act without the external artifact at inference, and whether it retains robustness when new errors appear. A strong benchmark would test the same learner with hints, skills, rubrics, or reflections available only during training, then remove them at test time and measure both greedy performance and recovery from unfamiliar errors.

### Richer multimodal carriers need direct comparison, not isolated proposals

Several papers suggest that the choice of carrier may matter more than the amount of experience. \[Sin25b\] shows that adding trajectory sketches resolves a real blind spot in final-state VLM judging. \[Sar24b\] shows that distilled programs of thought can beat raw noisy demonstrations, but also that text trajectory memory can outperform some multimodal variants and that estimated perception remains a hard ceiling. \[Xu25q\] quietly exposes the same issue when it compresses history into text while keeping only the current frame. \[Wu25b\] confines reflection mostly to local grounding errors, which suggests the current carrier does not yet encode higher-level planning failures well. \[Das25\] shows how a policy trained on state-rich simulator experience weakens sharply when that carrier changes to noisy visual observations.

A high-value next paper would take one fixed interaction corpus and convert it into at least three carriers such as full multimodal trace, summarized textual lesson, and structured repair artifact. The same base policy should then be trained under matched budgets. That experiment would answer a question the current literature mostly leaves implicit: which information survives conversion, and which apparent gains are really just carrier-model compatibility effects.

### Transfer-first evaluation should replace near-distribution reporting

This paper set repeatedly shows that transformed experience often works best near its source distribution. \[He24e\] reports unstable cross-website improvement. \[Xu24\] is vulnerable to tutorial expiration and changing websites. \[Qi24\] improves average performance while losing ground on some sites. \[Bai24\] demonstrates that frozen policies decay as device environments change over time. \[Fai26\] improves within website families but still evaluates in a budgeted, bounded synthesis regime. \[Xia25h\] shows real generalization gains in cluttered unseen settings, yet Section 6 still calls for work on continual on-robot learning and safer exploration.

Concrete progress would look like routine reporting across at least four axes: unseen instances, changed interfaces over time, unseen sites or apps, and shifts in observation carrier. Papers should also report the economics of those gains: rollout time, judge cost, success-to-usable-data ratio, and crash or invalid-action rates. The systems burden is part of the research problem in this area, not an appendix detail. A method that improves success only on a filtered benchmark slice but requires extremely expensive verification may still be less important than a slightly weaker method that scales to broader, noisier experience collection.

---

## References

\[Son24\] Y. Song, D. Yin, X. Yue, J. Huang, S. Li, and B. Y. Lin, “Trial and Error: Exploration-Based Trajectory Optimization for LLM Agents,” *Annual Meeting of the Association for Computational Linguistics*, pp. 7584–7600, Mar. 2024, doi: [10.48550/arXiv.2403.02502](https://doi.org/10.48550/arXiv.2403.02502).

\[Xia25h\] W. Xiao *et al.*, “Self-Improving Vision-Language-Action Models with Data Generation via Residual RL,” *ArXiv*, vol. abs/2511.00091, Oct. 2025, doi: [10.48550/arXiv.2511.00091](https://doi.org/10.48550/arXiv.2511.00091).

\[He25g\] Y. He, P. Chawla, Y. Souri, S. Som, and X. Song, “Scalable Data Synthesis for Computer Use Agents with Step-Level Filtering,” *ArXiv*, vol. abs/2512.10962, Nov. 2025, doi: [10.48550/arXiv.2512.10962](https://doi.org/10.48550/arXiv.2512.10962).

\[Li26n\] Z. Li *et al.*, “MagicGUI-RMS: A Multi-Agent Reward Model System for Self-Evolving GUI Agents via Automated Feedback Reflux,” *ArXiv*, vol. abs/2601.13060, Jan. 2026, doi: [10.48550/arXiv.2601.13060](https://doi.org/10.48550/arXiv.2601.13060).

\[Yua25c\] S. Yuan, Z. Chen, Z. Xi, J. Ye, Z. Du, and J. Chen, “Agent-R: Training Language Model Agents to Reflect via Iterative Self-Training,” *ArXiv*, vol. abs/2501.11425, Jan. 2025, doi: [10.48550/arXiv.2501.11425](https://doi.org/10.48550/arXiv.2501.11425).

\[Bai24\] H. Bai *et al.*, “DigiRL: Training In-The-Wild Device-Control Agents with Autonomous Reinforcement Learning,” *ArXiv*, vol. abs/2406.11896, Jun. 2024, doi: [10.48550/arXiv.2406.11896](https://doi.org/10.48550/arXiv.2406.11896).

\[Xia25e\] H. Xiao *et al.*, “UI-Genie: A Self-Improving Approach for Iteratively Boosting MLLM-based Mobile GUI Agents,” *ArXiv*, vol. abs/2505.21496, May 2025, doi: [10.48550/arXiv.2505.21496](https://doi.org/10.48550/arXiv.2505.21496).

\[Sun24b\] Q. Sun *et al.*, “OS-Genesis: Automating GUI Agent Trajectory Construction via Reverse Task Synthesis,” *ArXiv*, vol. abs/2412.19723, Dec. 2024, doi: [10.48550/arXiv.2412.19723](https://doi.org/10.48550/arXiv.2412.19723).

\[Xu24\] Y. Xu *et al.*, “AgentTrek: Agent Trajectory Synthesis via Guiding Replay with Web Tutorials,” *ArXiv*, vol. abs/2412.09605, Dec. 2024, doi: [10.48550/arXiv.2412.09605](https://doi.org/10.48550/arXiv.2412.09605).

\[He24e\] H. He *et al.*, “OpenWebVoyager: Building Multimodal Web Agents via Iterative Real-World Exploration, Feedback and Optimization,” *Annual Meeting of the Association for Computational Linguistics*, pp. 27545–27564, Oct. 2024, doi: [10.48550/arXiv.2410.19609](https://doi.org/10.48550/arXiv.2410.19609).

\[Din26\] L. Ding, “AgentHER: Hindsight Experience Replay for LLM Agent Trajectory Relabeling,” Mar. 22, 2026.

\[Das25\] R. J. Das *et al.*, “BLAZER: Bootstrapping LLM-based Manipulation Agents with Zero-Shot Data Generation,” *ArXiv*, vol. abs/2510.08572, Oct. 2025, doi: [10.48550/arXiv.2510.08572](https://doi.org/10.48550/arXiv.2510.08572).

\[Zho24e\] V. Zhong, D. Misra, X. Yuan, and M.-A. Côté, “Policy Improvement using Language Feedback Models,” *ArXiv*, vol. abs/2402.07876, Feb. 2024, doi: [10.48550/arXiv.2402.07876](https://doi.org/10.48550/arXiv.2402.07876).

\[Xio24\] W. Xiong *et al.*, “Watch Every Step! LLM Agent Learning via Iterative Step-level Process Refinement,” *ArXiv*, vol. abs/2406.11176, Jun. 2024, doi: [10.48550/arXiv.2406.11176](https://doi.org/10.48550/arXiv.2406.11176).

\[Wan25x\] H. Wang, J. Wang, C. T. Leong, and W. Li, “STeCa: Step-level Trajectory Calibration for LLM Agent Learning,” *Annual Meeting of the Association for Computational Linguistics*, pp. 11597–11614, Feb. 2025, doi: [10.48550/arXiv.2502.14276](https://doi.org/10.48550/arXiv.2502.14276).

\[Wan26aj\] X. Wang *et al.*, “Co-Evolution of Policy and Internal Reward for Language Agents,” Apr. 03, 2026.

\[Pan26\] C. Pan *et al.*, “EVPO: Explained Variance Policy Optimization for Adaptive Critic Utilization in LLM Post-Training,” Apr. 21, 2026.

\[Wan26u\] Y. Wang, T. Xie, K. Shen, M. Wang, and L. Yang, “RLAnything: Forge Environment, Policy, and Reward Model in Completely Dynamic RL System,” *ArXiv*, vol. abs/2602.02488, Feb. 2026, doi: [10.48550/arXiv.2602.02488](https://doi.org/10.48550/arXiv.2602.02488).

\[Xu26j\] T. Xu, Y.-T. Chen, and M. Li, “CLEANER: Self-Purified Trajectories Boost Agentic Reinforcement Learning,” *ArXiv*, vol. abs/2601.15141, Jan. 2026, doi: [10.48550/arXiv.2601.15141](https://doi.org/10.48550/arXiv.2601.15141).

\[Ge26\] R. Ge *et al.*, “Internalizing Agency from Reflective Experience,” Mar. 17, 2026.

\[Li26l\] Z. Li *et al.*, “No More Stale Feedback: Co-Evolving Critics for Open-World Agent Learning,” *ArXiv*, vol. abs/2601.06794, Jan. 2026, doi: [10.48550/arXiv.2601.06794](https://doi.org/10.48550/arXiv.2601.06794).

\[Wan26al\] H. Wang *et al.*, “Skill-SD: Skill-Conditioned Self-Distillation for Multi-turn LLM Agents,” Apr. 12, 2026.

\[Ye26f\] T. Ye, L. Dong, Q. Dong, X. Wu, S. Huang, and F. Wei, “Online Experiential Learning for Language Models,” Mar. 17, 2026.

\[Qi24\] Z. Qi *et al.*, “WebRL: Training LLM Web Agents via Self-Evolving Online Curriculum Reinforcement Learning,” *ArXiv*, vol. abs/2411.02337, Nov. 2024, doi: [10.48550/arXiv.2411.02337](https://doi.org/10.48550/arXiv.2411.02337).

\[Sin25b\] A. Singh *et al.*, “VARP: Reinforcement Learning from Vision-Language Model Feedback with Agent Regularized Preferences,” *ArXiv*, vol. abs/2503.13817, Mar. 2025, doi: [10.48550/arXiv.2503.13817](https://doi.org/10.48550/arXiv.2503.13817).

\[Xu25q\] H. Xu, Z. Yu, Y. Tang, P. Hu, Y. Tang, and H. Dong, “MCTS-EP: Empowering Embodied Planning with Online Preference Optimization,” *ArXiv*, vol. abs/2509.17116, Sep. 2025, doi: [10.48550/arXiv.2509.17116](https://doi.org/10.48550/arXiv.2509.17116).

\[Sar24b\] G. Sarch, L. Jang, M. J. Tarr, W. W. Cohen, K. Marino, and K. Fragkiadaki, “VLM Agents Generate Their Own Memories: Distilling Experience into Embodied Programs of Thought,” *Advances in Neural Information Processing Systems 37*, Jun. 2024, doi: [10.52202/079017-2418](https://doi.org/10.52202/079017-2418).

\[Wu25b\] P. Wu, S. Ma, B. Wang, J. Yu, L. Lu, and Z. Liu, “GUI-Reflection: Empowering Multimodal GUI Models with Self-Reflection Behavior,” *ArXiv*, vol. abs/2506.08012, Jun. 2025, doi: [10.48550/arXiv.2506.08012](https://doi.org/10.48550/arXiv.2506.08012).

\[Fai26\] F. Faisal, Q. Wu, B. Peng, and J. Gao, “AutoSurfer -- Teaching Web Agents through Comprehensive Surfing, Learning, and Modeling,” Apr. 29, 2026.

\[Ala25\] M. Alakuijala *et al.*, “Memento No More: Coaching AI Agents to Master Multiple Tasks via Hints Internalization,” *ArXiv*, vol. abs/2502.01562, Feb. 2025, doi: [10.48550/arXiv.2502.01562](https://doi.org/10.48550/arXiv.2502.01562).
