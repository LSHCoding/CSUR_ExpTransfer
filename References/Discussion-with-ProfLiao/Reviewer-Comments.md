# Reviewer #052b77e

1. How relevant do you think the topic is in the broad context of AI research? *
Answer: Highly Relevant: the topic is of great interest for the whole AI community

2. Does the topic need this kind of survey? *
Answer: Useful: this survey adds some new perspectives, without necessarily filling any gaps in the understanding of the topic

3. Do the submitted CV(s) provide clear publication evidence that at least one author is an expert in the surveyed area? *
Answer: Clearly knowledgeable

4. Does the survey provide a well-organized taxonomy or framework for understanding the field? *
Answer: Moderate: some categorization or structure is provided, but it is either incomplete or lacks coherence

5. Detailed review of survey presentation *
Please enter a detailed review describing the strengths and weaknesses of the submitted survey taking into account the guidelines and expected scope expressed in the CFP: https://2026.ijcai.org/ijcai-ecai-2026-call-for-papers-survey/
- If you are an Informed Outsider, please write your review according to how accessible the material has been for you to learn more about the topic.
- If you are Knowledgeable about the topic, please write your review according to how it has changed your view of the topic or has provided more insight and understanding.
- If you are an Expert in this topic, please write your review according to how well you think it reflects the state of the art and future directions.

In addition, please give your opinion about the structure and flow of the paper, how it presents the major concepts and insights in the area, as well as any factual or conceptual error or any other aspect that could prevent this submission from being a short yet illuminating survey on the topic for the AI community.
Answer: This survey introduces Experience Transformation as a unifying lens for understanding how LLM-based agents convert accumulated interaction trajectories into different reusable carriers—Textual, Structured, Evaluator, and Parametric representations. It formalizes agent experience as a minimal semantic record and systematizes six transformation pathways. Across these paradigms, the paper analyzes trade-offs in reusability, verifiability, efficiency, and adaptability, and outlines forward-looking challenges such as active experience management, recursive alignment, multimodal transformation, and modular parametric memory.
Strong points
S1. The paper proposes a coherent transformation-centric abstraction under a single representation-to-representation framework.
S2. The taxonomy covers both intra-carrier and cross-carrier transformations with categorization of representative systems.
S3. The survey analyzes trade-offs (interpretability, efficiency, verifiability, adaptability.
Weak points
W1. While “Experience Transformation” is presented as a unifying lens, much of the taxonomy reorganizes already well-established threads in the literature—memory summarization, reward modeling, RLHF, self-training, and tool-use learning—without substantially new theoretical synthesis beyond renaming the representation transitions. The distinction from prior surveys (e.g., agent architectures, memory surveys, PRM surveys) is asserted but not rigorously differentiated in terms of methodological contribution; the framework largely overlays an alternative grouping over existing categorizations.
W2. The survey cites a very large number of recent (2024–2026) works, many of which are arXiv preprints; while timely, this heavy emphasis on very recent and not-yet-mature work raises concerns about stability and long-term generalizability of the taxonomy. The comparative critical analysis across paradigms is relatively shallow; most works are categorized but not deeply contrasted in terms of empirical robustness, scalability, or reproducibility.
W3. The proposed future directions (Active Experience Management, Recursive Alignment, Multimodal Transformation, Modular Parametric Memory) are largely conceptual. The meta-learning framing of experience management is compelling, yet the paper does not specify how the meta-policy would be evaluated, what reward signals would supervise transformation actions, or how to avoid circular optimization loops. In addition, there is no unified evaluation protocol to compare transformation strategies end-to-end (e.g., compression ratio vs. downstream performance vs. cost vs. editability), leaving the trade-off analysis largely qualitative.

6. Please provide an overall recommendation to the Survey Track Chairs regarding this submission. *
Answer: Weak Reject: It may be a good survey, but not good enough. That said, I wouldn't be too unhappy if the paper was accepted.

7. Overall Recommendation Justification. *
Please assess the quality of the submission by focusing on:
- novelty: does the survey introduce a fresh synthesis, novel taxonomy, or unique perspective that distinguishes it from existing surveys?
- coverage: does the survey comprehensively cover the key literature in the field, or are there notable omissions or biases?
- clarity: is the survey well-organized, clearly written, and accessible to both experts and non-specialists in the AI community?
- significance: what is the likely impact of this survey on AI researchers and practitioners, and will it serve as a key reference for future work in this area?
- expertise of the authors (listed in author CV): do the authors have deep expertise and insight in the surveyed area?
Answer: The paper is comprehensive and timely. However, much of the analysis reorganizes existing strands of agent research without delivering substantially new analytical insights or formal tools. The future directions are ambitious but under-specified. The reviewer lean toward a weak reject in its current form.


# Reviewer #052f098

1. How relevant do you think the topic is in the broad context of AI research? *
Answer: Highly Relevant: the topic is of great interest for the whole AI community

2. Does the topic need this kind of survey? *
Answer: Useful: this survey adds some new perspectives, without necessarily filling any gaps in the understanding of the topic

3. Do the submitted CV(s) provide clear publication evidence that at least one author is an expert in the surveyed area? *
Answer: Recognized expert in the field

4. Does the survey provide a well-organized taxonomy or framework for understanding the field? *
Answer: Good: the taxonomy/framework is well-organized and helps structure the field meaningfully

5. Detailed review of survey presentation *
Please enter a detailed review describing the strengths and weaknesses of the submitted survey taking into account the guidelines and expected scope expressed in the CFP: https://2026.ijcai.org/ijcai-ecai-2026-call-for-papers-survey/
- If you are an Informed Outsider, please write your review according to how accessible the material has been for you to learn more about the topic.
- If you are Knowledgeable about the topic, please write your review according to how it has changed your view of the topic or has provided more insight and understanding.
- If you are an Expert in this topic, please write your review according to how well you think it reflects the state of the art and future directions.

In addition, please give your opinion about the structure and flow of the paper, how it presents the major concepts and insights in the area, as well as any factual or conceptual error or any other aspect that could prevent this submission from being a short yet illuminating survey on the topic for the AI community.
Answer: Main content:
This survey frames experience transformation as a unifying lens for how LLM-based agents learn and adapt. It defines experience as a minimal semantic record e = (c, a, o, f), groups reusable experience into four carrier types (textual, structured, evaluator, parametric), and walks through six cross-carrier transformation pathways. Each pathway gets its own subsection with method subcategories and a closing Discussion. Four future directions round out the paper. The central claim, that the core challenge is not accumulating experience but transforming it, is stated early but not convincingly argued.

Main strengths:
1. The organizing angle is fresh. Instead of the usual module-by-module layout (memory, planning, tools), the paper threads the literature through representation-to-representation transformation routes, which helps readers see connections across subfields like memory management, reward modeling, and policy tuning.
2. The taxonomy holds together well. The four-carrier split and six pathways are logically consistent, and Figure 2 gives a clean map for locating related work.
3. The references are unusually up to date, covering 2025-2026 work (Mem0, GRPO, DeepSeek-R1, etc.). This kind of currency is rare in surveys.

Main weaknesses:
w1. The motivation is asserted rather than argued. The paper claims in lines 65-68 that the core challenge in agent evolution is not merely experience accumulation but experience transformation, yet the only supporting evidence is a brief mention of RAG bottlenecks such as context window limits and retrieval latency. Two prior questions go unanswered: (a) why is experience the right abstraction for organizing the field, as opposed to more established concepts like trajectories, memory, or feedback? (b) why is carrier-to-carrier transformation the key bottleneck, rather than, say, better retrieval, prompt design, or architectural choices?

w2. The agent definition is missing in a meaningful sense, and the discussion scope is never properly framed. A survey built around agent experience should open with a clear definition of what counts as an agent and use that definition to scope the discussion, specifying which systems are in and which are out. Section 2.1 instead offers a single formula (a_t ~ pi_theta(. | c_t)) and moves on. It does not spell out what distinguishes an LLM agent from a general LLM application, nor does it clarify under what system boundary the notion of experience applies. As a result, the applicability of the six transformation pathways remains ambiguous throughout.

w3. The per-section Discussions stay too local and never connect back to the bigger picture. What role does experience transformation actually play in making agents better? The same trade-offs keep showing up across pathways, so does that tell us something fundamental? How should these observations guide the community going forward? A survey should offer synthesis that individual papers cannot. These Discussions do not do that. After reading them, I know what each method's trade-offs are, but I still do not know why experience transformation matters for the field or what it teaches us.

w4. The literature coverage reads like a catalog. Section 3 walks through each pathway listing methods one after another (A does X, B extends this to Y), but there is little comparative analysis, no summary tables, no applicability matrices, no head-to-head assessment. Worse, the paper explicitly excludes utilization in Section 2.4, cutting off retrieval policies, context orchestration, and operational maintenance from the discussion. For someone trying to actually build an agent system, the survey tells you what transformation options exist but not when to pick one, how to combine them, or what pitfalls to expect in practice.

w5. The multimodal future direction comes out of nowhere. The entire main body (Sections 2-3) stays within the textual modality, and then Section 4.3 suddenly introduces multimodal experience transformation as a future direction, opening by admitting the framework systematizes transformation mechanisms primarily within the textual modality. There is no mention of visual or embodied experience in any of the Discussions, so the transition feels abrupt.

w6. The writing shows strong signs of AI-generated text. The structure, phrasing, and Discussion format are highly templated across all sections.

6. Please provide an overall recommendation to the Survey Track Chairs regarding this submission. *
Answer: Reject: A basic summary of the topic, not of the outstanding quality expected for this track.

7. Overall Recommendation Justification. *
Please assess the quality of the submission by focusing on:
- novelty: does the survey introduce a fresh synthesis, novel taxonomy, or unique perspective that distinguishes it from existing surveys?
- coverage: does the survey comprehensively cover the key literature in the field, or are there notable omissions or biases?
- clarity: is the survey well-organized, clearly written, and accessible to both experts and non-specialists in the AI community?
- significance: what is the likely impact of this survey on AI researchers and practitioners, and will it serve as a key reference for future work in this area?
- expertise of the authors (listed in author CV): do the authors have deep expertise and insight in the surveyed area?
Answer: Novelty: Below moderate. The transformation-centric framing is a reasonable idea, but the paper never makes the case for why this framing is necessary (W1), and does not generate insights that go beyond listing methods (W3). The framework ends up feeling more like an organizational convenience than a genuine conceptual contribution.

Coverage: Not sufficient. By restricting the scope to textual modality and explicitly leaving out utilization (W4), the survey misses important practical territory, including end-to-end system design, evaluation practices, and multimodal settings (W5). The depth across pathways is also uneven. Section 3.4 (Textual to Parametric) is far more developed than Sections 3.5 or 3.6.

Clarity: The taxonomy itself is clear and easy to follow. However, the heavily templated writing and formulaic phrasing (W6) work against credibility, especially in a paper that is meant to reflect expert judgment.

Depth: This is the biggest concern. The Discussion paragraphs never leave the local scope of each pathway (W3) and do not address why experience or experience transformation matters for agent development. There is no decision guidance for practitioners (W4), and the agent definition is too loose to anchor the discussion (W2).

Author expertise: The CVs suggest the authors have relevant research background.

Taken together, the paper builds a clean taxonomic skeleton but falls short on three fronts: the skeleton's necessity is not justified (W1), it does not generate field-level insight (W3), and important adjacent topics are systematically excluded (W4, W5). The templated writing (W6) compounds the problem by making the paper feel more like a formatted index than an authored survey. In its current form, the paper does not meet the acceptance bar for the IJCAI Survey Track. I would encourage the authors to substantially revise and resubmit.

# Reviewer #0530cde

1. How relevant do you think the topic is in the broad context of AI research? *
Answer: Highly Relevant: the topic is of great interest for the whole AI community

2. Does the topic need this kind of survey? *
Answer: Useful: this survey adds some new perspectives, without necessarily filling any gaps in the understanding of the topic

3. Do the submitted CV(s) provide clear publication evidence that at least one author is an expert in the surveyed area? *
Answer: Clearly knowledgeable

4. Does the survey provide a well-organized taxonomy or framework for understanding the field? *
Answer: Good: the taxonomy/framework is well-organized and helps structure the field meaningfully

5. Detailed review of survey presentation *
Please enter a detailed review describing the strengths and weaknesses of the submitted survey taking into account the guidelines and expected scope expressed in the CFP: https://2026.ijcai.org/ijcai-ecai-2026-call-for-papers-survey/
- If you are an Informed Outsider, please write your review according to how accessible the material has been for you to learn more about the topic.
- If you are Knowledgeable about the topic, please write your review according to how it has changed your view of the topic or has provided more insight and understanding.
- If you are an Expert in this topic, please write your review according to how well you think it reflects the state of the art and future directions.

In addition, please give your opinion about the structure and flow of the paper, how it presents the major concepts and insights in the area, as well as any factual or conceptual error or any other aspect that could prevent this submission from being a short yet illuminating survey on the topic for the AI community.
Answer: Strengths:
- Interesting topic addressed, not already covered too much yet by other existing surveys
- The proposed taxonomy is technically sound and can help the newcomers in categorizing the different types of possible approaches
- The paper is generally well organized and well written

Weaknesses:
- The introduced taxonomy is sufficiently novel for experience transformation in LLM agents but not outstandingly novel for similar context+experience fusion algorithms used in other agent-oriented contexts
- Given the many systems covered by the survey, the technical description of the surveyed solutions (Section 3) is quite superficial
- There is insufficient discussion in the paper on how to select which category of approach depending on the characteristics of the application domain and/or the constraints of the deployment environment

6. Please provide an overall recommendation to the Survey Track Chairs regarding this submission. *
Answer: Weak Accept: It is a really good survey, even though it has some limitations. That said, I wouldn't be too unhappy if the paper got rejected.

7. Overall Recommendation Justification. *
Please assess the quality of the submission by focusing on:
- novelty: does the survey introduce a fresh synthesis, novel taxonomy, or unique perspective that distinguishes it from existing surveys?
- coverage: does the survey comprehensively cover the key literature in the field, or are there notable omissions or biases?
- clarity: is the survey well-organized, clearly written, and accessible to both experts and non-specialists in the AI community?
- significance: what is the likely impact of this survey on AI researchers and practitioners, and will it serve as a key reference for future work in this area?
- expertise of the authors (listed in author CV): do the authors have deep expertise and insight in the surveyed area?
Answer: Please see the previous parts of this review form.


# Area Chair #008f87f

1. Meta review *
The meta review should provide an overview of the submission and reviewers comments.
Please assess the quality of the submission by focusing on:
- novelty: does the survey introduce a fresh synthesis, novel taxonomy, or unique perspective that distinguishes it from existing surveys?
- coverage: does the survey comprehensively cover the key literature in the field, or are there notable omissions or biases?
- clarity: is the survey well-organized, clearly written, and accessible to both experts and non-specialists in the AI community?
- significance: what is the likely impact of this survey on AI researchers and practitioners, and will it serve as a key reference for future work in this area?
- expertise of the author (listed in author CV): do the authors have deep expertise and insight in the surveyed area?
Answer: The authors survey LLM-based agents through an experience transformation perspective, organizing how interaction histories are converted into reusable representations such as, text, structured data, evaluators, and parameters.

The reviewers agree the topic is highly relevant and timely, and that the paper proposes a coherent and generally well-structured taxonomy around experience transformation. However, opinions diverge on its contribution.

-novelty: While the transformation-centric framing is seen as somewhat fresh, most reviewers find it largely reorganizes existing strands without sufficient conceptual justification or deeper analysis.
-coverage: The survey is broad and up-to-date, but uneven and somewhat superficial, with limited comparative analysis and omissions (e.g., utilization aspects, multimodal settings).
-clarity: The taxonomy and structure are generally clear, though concerns are raised about templated writing and lack of high-level discussion.
-significance: The paper may serve as a useful entry point, but is unlikely to become a key reference without stronger insights, evaluation frameworks, and practitioner guidance.
-author expertise: The authors are consistently viewed as knowledgeable with relevant expertise.

In summary, the paper is a solid but not yet compelling survey; its main weakness lies in insufficient justification of its central perspective and limited depth of analysis, leading to mixed recommendations (leaning towards reject).