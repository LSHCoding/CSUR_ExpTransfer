
- AgentTrek: Agent Trajectory Synthesis via Guiding Replay with Web Tutorials
- Stage 1 对应 P2：tutorial-like texts 被过滤并转成 structured task specifications；Stage 2 对应 P5：VLM agent 执行这些 specs 生成 GUI trajectories，VLM evaluator 验证正确性后作为 agent training data。


- Scaling Synthetic Task Generation for Agents via Exploration
- AutoPlay 先让 MLLM explorer 系统探索环境状态和功能，再由 task generator 利用探索轨迹与 guideline prompts 合成 feasible/verifiable tasks；executor/verifier 生成 demos 和 rewards，用于 UI-agent training/RL。
