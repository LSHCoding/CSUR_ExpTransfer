\subsection{Single-LLM System}
\label{sec:Single-LLM System}

\par Single-LLM System relies on a single model to perform judgment tasks, with its effectiveness largely determined by the LLM's capabilities and the strategies used to process input data. This approach can generally be divided into three fundamental components: \textbf{Prompt Engineering} (\S\ref{sec:Prompt Engineering}), \textbf{Tuning} (\S\ref{sec:Tuning}), and \textbf{Post-processing} (\S\ref{sec:Post-processing}) of model outputs.

\subsubsection{Prompt-based}
\label{sec:Prompt Engineering}
\par Prompt engineering~\cite{sahoo2024systematic} involves crafting clear and structured input prompts tailored to elicit accurate and contextually appropriate responses from LLM judges. This approach is crucial for ensuring that LLMs grasp the complexities of specific tasks and provide relevant, consistent, and goal-aligned judgments. 
In many cases, well-designed prompts significantly reduce the need for extensive model training.


\textbf{In-Context Learning.} In-Context Learning (ICL) is a distinctive capability of LLMs that allows them to dynamically adapt to evaluation tasks using carefully curated examples or explanations within the prompt~\cite{dong2022survey}. Several recent methods have demonstrated the power of ICL in LLM-as-judges, showcasing how it enhances the flexibility and performance of LLMs in diverse settings. For example, GPTScore~\cite{fu2023gptscore} leverages the few-shot learning capability of generative pre-trained models to evaluate generated text. By using relevant examples to customize prompts, it provides a flexible, training-free approach to assess multiple aspects of text quality.
Similarly, LLM-EVAL~\cite{lin2023llm} incorporates carefully crafted examples into prompts, proposing a unified, multi-dimensional automatic evaluation method for open-domain dialogue.
Another notable example is TALEC~\cite{zhang2024talec}, a model-based evaluation method that leverages in-context learning to enable users to set custom evaluation criteria for LLMs in specific domains. Through careful prompt engineering, users can iteratively adjust the examples to refine the evaluation process as needed.
In addition, Jain et al.~\cite{jain2023multi} proposed the In-Context Learning-based Evaluator (ICE) for multi-dimensional text evaluation. ICE leverages LLMs and a small number of in-context examples to evaluate generated text summaries, achieving competitive results.

While ICL can enable effective evaluation, it is not without challenges. One major issue is that the model's responses may be influenced by the selection of prompt examples, potentially leading to bias~\cite{zhao2021calibrate,zhou2023batch,han2022prototypical,fei2023mitigating}.
To address this issue, Hasanbeig et al. proposed ALLURE~\cite{hasanbeig2023allure}, a comprehensive protocol designed to mitigate bias in ICL for LLMs during text evaluation. ALLURE~\cite{hasanbeig2023allure} improves evaluator accuracy by iteratively incorporating discrepancies between its assessments and annotated data into the learning context. Moreover, after uncovering the existence of symbol bias within LLM evaluators when using ICL, Song et al.~\cite{song2024can} proposed two effective mitigation strategy prompt templates, Many-Shot with Reference (MSwR) and Many-Shot without Reference (MSoR), to bolster the reliability and precision of LLM-based assessments.






\textbf{Step-by-step.}
Step-by-step involves breaking down complex evaluation tasks into fine-grained components, leveraging the reasoning capabilities of LLMs to simplify the evaluation process. The most straightforward example of which is perhaps Chain-of-Thought (CoT)~\cite{wei2022chain,kotonya2023little}. Building on that, frameworks like G-EVAL~\cite{liu2023g} have been proposed to assess the quality of NLG outputs. G-EVAL~\cite{liu2023g} combines CoT with a form-filling paradigm, allowing the LLM to assess outputs in a structured manner.
Similarly, ICE-Score~\cite{zhuo2023ice} introduces a step-by-step framework for evaluating code, in which the LLM is instructed with task definitions, evaluation criteria, and detailed evaluation steps. By breaking the task down into clear steps, ICE-Score~\cite{zhuo2023ice} improves the quality and consistency of code evaluation. Also, ProtocoLLM~\cite{yi2024protocollm} employs a similar step-by-step approach to evaluate the specialized capabilities of LLMs in generating scientific protocols. 
Portia~\cite{li2023split} achieves better evaluation results in a lightweight yet effective manner. It divides the answer into multiple parts, aligns similar content between candidate answers, and then merges them back into a single prompt for evaluation by the LLM.


Some studies break down evaluations into two steps: ``explanation-rating.'' This approach suggests that providing an explanation enhances the reliability of the rating. Chiang et al.~\cite{chiang2023closer} offer empirical guidelines to improve the quality of LLM evaluations, demonstrating that combining rating with explanation (rate-explain) or explanation with rating (explain-rate) leads to higher correlations with human ratings.
Another effective strategy is to decompose complex evaluation standards into specific, discrete criteria, allowing the LLM to assess each aspect independently. FineSurE~\cite{song2024finesure} is an advanced example of this method, offering a framework for the fine-grained evaluation of text summarization quality. It breaks down the evaluation into multiple dimensions, such as faithfulness, completeness, and conciseness. Through detailed analysis, including fact-checking and key fact alignment, FineSurE~\cite{song2024finesure} outperforms traditional methods in terms of evaluation accuracy.




\textbf{Definition Augmentation.}
The Enhanced Definition approach involves refining prompts to inject improved evaluation criteria, establish assessment principles, or incorporate external knowledge into the LLM judge's decision-making process.
Some studies focus on enriching and clarifying the prompts to ensure that the evaluation criteria are both comprehensive and well-defined.



For example, Liu et al. propose AUTOCALIBRATE~\cite{liu2023calibrating}, a multi-stage, gradient-free approach. This method involves the drafting, revision, and application of calibrated criteria, and it automatically calibrates and aligns an LLM-based evaluator to match human preferences for NLG quality assessment.
Furthermore, SALC~\cite{gupta2024unveiling} enables LLMs to autonomously generate context-aware evaluation criteria for self-assessment, overcoming the limitations of static, human-defined metrics. 
On the other hand, the LLM-as-a-Personalized-Judge approach~\cite{dong2024can} introduces a novel perspective by incorporating diverse evaluative roles and principles. This allows LLMs to adapt to complex, varied evaluation scenarios, resulting in more nuanced and context-sensitive assessments.

Another key aspect of Definition Augmentation is the retrieval of external knowledge, which helps reduce hallucinations and provides more factual support. For instance, BiasAlert~\cite{fan2024biasalert}, a tool designed to detect social bias in LLM-generated open-text outputs. It integrates external human knowledge with the LLM judge's inherent reasoning capabilities to reliably identify and mitigate bias, outperforming GPT4-as-A-Judge across various scenarios.
Moreover, Chen et al.~\cite{chen2024llms} found that within retrieval-augmented generation (RAG) frameworks, LLM judges do not exhibit a significant self-preference effect during evaluation.


\textbf{Multi-turn Optimization.}
Multi-turn optimization involves iterative interactions between the evaluator and the evaluated entity, refining evaluation results through diverse forms of feedback, thus fostering deeper analysis and a progressive improvement in evaluation quality~\cite{zhou2024fairer}.
Unlike traditional methods that rely on predefined criteria, Xu et al. proposed ACTIVE-CRITIC~\cite{xu2024large}, enabling LLMs to infer evaluation criteria from data and dynamically optimize prompts through multiple rounds of interaction. Moreover, 
Some studies~\cite{zhao2024auto,luo2024videoautoarena,bai2024benchmarking,yu2024kieval} leverage LLMs as question designers to engage in dynamic interactions with the evaluated entities, adjusting the questions and task design in real time. This allows for flexible modification of the evaluation content based on the performance of the evaluated entity, thereby enabling more comprehensive assessments.