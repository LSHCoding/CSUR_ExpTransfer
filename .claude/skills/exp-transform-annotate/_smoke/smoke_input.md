Title: Reflexion: Verbal Reinforcement Learning

URL: https://example.org/reflexion

Abstract: We propose Reflexion, a framework that enables a large-language-model agent to verbally reflect on task feedback signals after each rollout. The agent stores these reflections as natural-language critiques in an episodic memory buffer, and on subsequent attempts conditions its policy on the buffer to avoid prior mistakes. Across HotpotQA, AlfWorld, and HumanEval, Reflexion converges within five trials and improves success rate by 22% over a non-reflective baseline. The agent's language model weights are not updated; all gains arise from textual self-feedback recycled into the prompt context.

------

Title: WorkflowBoost: Distilling Code-Schema Skills into Agent Policies

URL: https://example.org/workflowboost

Abstract: We present WorkflowBoost, a two-stage training pipeline for tool-using LLM agents. In the first stage, we collect raw interaction trajectories on a suite of tool-use tasks and prompt a critic model to summarize each successful trajectory as a typed Python workflow with input/output specifications. The resulting library of executable workflows is then used as additional supervision signal: in the second stage, we fine-tune the agent's base model with supervised learning on (instruction, workflow, trajectory) triples, encouraging the policy to either invoke an existing workflow or follow its API contract. WorkflowBoost outperforms ReAct and Reflexion on three benchmark suites, with the largest gains observed on long-horizon multi-tool tasks.

------

Title: Pretraining Vision Foundation Models with Masked Autoencoding

URL: https://example.org/mae-vision

Abstract: We revisit masked autoencoders as scalable self-supervised learners for image representation. Random patches of the input image are masked, and a lightweight decoder reconstructs the missing pixels from the remaining ones. After pretraining on ImageNet-1K without labels, our representations transfer favorably to downstream classification, detection, and segmentation tasks, surpassing supervised counterparts at high model capacities. The approach is simple, efficient, and architecture-agnostic.

------

Title: RAFT-Agent: Reward-Ranked Fine-Tuning for Tool Calling

URL: https://example.org/raft-agent

Abstract: We adapt Reward rAnked FineTuning (RAFT) to the tool-calling setting. Given a base agent and a scalar reward function over completed tool-using trajectories, we sample K candidate trajectories per prompt, retain only those whose reward exceeds the per-prompt median, and then apply standard supervised fine-tuning on this filtered subset. Iterating this sample-rank-finetune loop for three rounds, the policy progressively concentrates its mass on high-reward trajectories without ever computing policy gradients on rejected samples. RAFT-Agent matches PPO on ToolBench at less than 30% of the GPU cost.

------
