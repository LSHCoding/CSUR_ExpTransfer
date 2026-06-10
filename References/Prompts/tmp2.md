
**Table 5.1.** Overview of Evaluator Internalization methods.

列定义：**Supervision Granularity** 记录监督信号绑定的粒度；**Output Form** 记录评估器输出是标量判定还是自然语言；**Evaluator Output** 记录评估器产物的具体形态；**Label Source** 记录训练监督标签的来源；**Training Method** 记录评估器参数的更新方式；**Domain** 记录实验场景；**Downstream Use**（可选）记录评估器输出在下游被消费的方式。各列取值集合：Supervision Granularity ∈ {`outcome`, `process`}；Output Form ∈ {`discriminative`, `generative`}；Evaluator Output ∈ {`binary label`, `graded score`, `preference`, `progress/advantage`, `step critique`, `failure diagnosis`, `corrective suggestion`, `structured verdict`}；Label Source ∈ {`human`, `environment-outcome`, `MC-rollout`, `ground-truth match`, `teacher-model`, `rule-based`, `self-generated`}；Training Method ∈ {`SFT`, `BCE`, `ranking-BT/PL`, `RL-GRPO/PPO`, `regression`, `TD/GAE`}；Domain ∈ {`text/reasoning`, `web`, `GUI`, `mobile`, `embodied`, `code`}；Downstream Use* ∈ {`RL reward`, `BoN/rerank`, `refinement`, `abort-gate`}。

| Work | Supervision Granularity | Output Form | Evaluator Output | Label Source | Training Method | Domain |
|------|-------------------------|-------------|------------------|--------------|-----------------|--------|
|      |                         |             |                  |              |                 |        |

