# Anti-AI-Voice Rules for Academic English Writing (ACM CSUR)

> Purpose: suppress the generic "LLM voice" in English survey prose. These rules are constraints on the *output*, not on the reasoning. Violating one of them occasionally is fine; violating several of them per paragraph is what produces AI-flavored text.

---

## 1. Sentence rhythm

**R1. Vary sentence length.** Do not write three or more consecutive sentences with similar length. Mix short sentences (5–15 words) into passages of long sentences. Sentence-length variance is one of the strongest human-vs-LLM signals.

**R2. Avoid chained parallelism.** Constructions like *"not X, but Y"*, *"not only X, but also Y"*, *"from X to Y"*, *"X is less about Y than about Z"* are legitimate individually but become an AI tic when stacked. **At most one such construction per paragraph.**

**R3. Prefer "X is Y" over "X is not A, it is B."** The negate-then-assert pattern should only be used when readers are genuinely likely to hold belief A. Otherwise assert directly.

**R4. Break the rule of three.** Do not pad two-item lists into three-item lists by adding a near-synonym. If there are two points, write two. If the third item is just a rephrasing of the first two, delete it.

**R5. Use em dashes sparingly.** At most one em dash per paragraph, and only for genuine interruption. Replace most em dashes with commas, periods, or parentheses.

**R6. No semicolon chains.** A sentence with three or more semicolons should be split into multiple sentences.

---

## 2. Word choice

**R7. Ban LLM-signature vocabulary.** Avoid these words unless the exact word is genuinely needed:

> *delve, tapestry, nuanced, underscore, pivotal, paramount, leverage (as verb), seamless, seamlessly, navigate (figurative), realm, intricate, multifaceted, robust (unless technical), crucial, vital, essential, profound, profoundly, meticulous, meticulously, rich (figurative), vibrant, landscape (figurative).*

If tempted to use one, pick a plainer synonym or cut the adjective entirely.

**R8. Demote hedging intensifiers.** Words like *key, core, fundamental, crucial, essential, central, deep, deeper* add emphasis but not information. Delete them on the first pass; restore only if the sentence genuinely weakens without them.

**R9. Replace vague "carrier" verbs with concrete ones.** Generic verbs such as *embody, capture, reflect, encompass, constitute, represent, manifest, exhibit* often stand in for precise verbs like *store, encode, compress, execute, index, replace, override*. Prefer the precise verb.

**R10. Avoid nominalization.** Prefer *"we analyze X"* over *"we conduct an analysis of X"*; prefer *"X changes Y"* over *"X leads to a change in Y"*. Verbs carry more information than the noun forms of the same verbs.

**R11. No grandiose framing nouns without substance.** Words like *paradigm, lens, perspective, framework, dimension, axis* are legitimate but become filler when overused. Aim for at most one per paragraph unless the term is genuinely operative.

---

## 3. Argumentative posture

**R12. No empty balance.** Do not automatically append *"however, this approach has limitations"* or *"that said, challenges remain"* after every claim. Add a caveat only when you can name the specific limitation in the same sentence.

**R13. No meta-commentary on the reader's attention.** Delete phrases such as *"it is worth noting that"*, *"interestingly"*, *"importantly"*, *"notably"*, *"remarkably"*, *"it should be emphasized that"*. If the point is important, the content shows it; if it is not, the phrase is padding.

**R14. Do not restate the paragraph in its last sentence.** Closing sentences should add a new inference, a consequence, or a transition — not summarize what was just said. Cut *"In summary"*, *"Taken together"*, *"Thus we see that"* unless a real synthesis follows.

**R15. No false-problem setups.** Avoid *"A central question is whether…"*, *"One might ask…"*, *"This raises the question of…"* as decorative openers. Either the question is actually being answered next, or it should be cut.

**R16. Cite with specificity.** *"Prior work has explored X"* followed by six citations is lazy. Either name the 1–2 works that matter and describe what they did, or group works by the specific *variant of X* they studied.

---

## 4. Paragraph structure

**R17. Not every paragraph needs intro-body-conclusion.** Allow paragraphs that just make one point and stop. Survey sections become tedious when every paragraph is a miniature essay.

**R18. Do not template section openings.** Avoid starting every subsection with *"In this section, we…"* or *"Having discussed X, we now turn to Y"*. Some sections should open by stating a claim directly.

**R19. Limit bullet lists.** Use bullets for genuinely parallel short items (names, numbers, short phrases). If each bullet is a full sentence with its own clauses, write a paragraph instead. Long narrative content in bullet form is an AI tell.

**R20. Topic sentences should carry specific content.** *"There are several challenges in this pathway"* is empty; *"Two failure modes dominate this pathway: reward hacking and distributional collapse"* is informative. Make the first sentence of each paragraph a claim, not a category label.

---

## 5. Survey-specific

**R21. No "gap-filling" clichés.** Avoid *"Despite significant progress, … remains underexplored"*, *"To bridge this gap, we…"*, *"A comprehensive understanding is still lacking"*. State what is actually missing and why it matters.

**R22. Trade-off tables must contain information, not adjectives.** Cells reading *"high"*, *"low"*, *"moderate"*, *"flexible"*, *"complex"* are worthless. Each cell should contain either (a) a concrete quantity or order of magnitude, (b) a mechanism phrase (e.g., *"bounded by context window"*), or (c) an explicit *"not reported in the literature"*.

**R23. Do not announce contributions in body text.** Phrases like *"We propose…"*, *"Our framework offers…"*, *"This survey makes three contributions"* belong in the Introduction and Conclusion only. Body sections should let the analysis speak.

**R24. Do not copy internal scaffolding into prose.** Design-doc labels such as *"Core question:"*, *"Essence:"*, *"Claim template:"* are useful for planning but must not appear in the manuscript. Unpack them into natural exposition.

**R25. Comparative claims need a reference point.** *"X achieves better generalization"* means nothing without *"better than Y under conditions Z"*. If the reference point is unavailable in the literature, say so explicitly rather than using a vague comparative.

---

## 6. Quick self-check

Before submitting a draft paragraph, check:

- Did I use any word from the R7 ban list? Replace or delete.
- Did I use more than one parallel construction (R2) or em dash (R5)?
- Can I delete every *"key / core / crucial / fundamental"* (R8) without the sentence collapsing? If yes, delete them.
- Does my closing sentence add something new (R14)?
- If I read this paragraph aloud, does the rhythm sound uniform (R1)?

If three or more of these checks fail, the paragraph still reads as AI-generated.

---

## 7. Calibration note

The goal is **low concentration**, not zero occurrence. Academic English requires some abstract nouns, some parallel structure, some hedging. A paragraph that uses *"however"* once is fine; a paragraph that uses it three times, alongside two em dashes and a *"crucially"*, is not. Apply these rules as density constraints, not absolute prohibitions.
