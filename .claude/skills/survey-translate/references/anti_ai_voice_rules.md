# Anti-AI-Voice Rules for Academic English Writing

> Apply as density constraints, not absolute prohibitions. Goal: low concentration of AI-voice patterns.

## 1. Sentence Rhythm

**R1. Vary sentence length.** No three or more consecutive sentences with similar length. Mix short (5–15 words) into long passages.

**R2. Avoid chained parallelism.** Constructions like "not X, but Y", "not only X, but also Y", "from X to Y", "X is less about Y than about Z" — at most one such construction per paragraph.

**R3. Prefer "X is Y" over "X is not A, it is B."** Use negate-then-assert only when readers are genuinely likely to hold belief A.

**R4. Break the rule of three.** Don't pad two-item lists into three with near-synonyms. If there are two points, write two.

**R5. Use em dashes sparingly.** At most one em dash per paragraph, only for genuine interruption. Replace most with commas, periods, or parentheses.

**R6. No semicolon chains.** A sentence with three or more semicolons must be split.

## 2. Word Choice

**R7. Ban LLM-signature vocabulary.** Avoid: delve, tapestry, nuanced, underscore, pivotal, paramount, leverage (as verb), seamless/seamlessly, navigate (figurative), realm, intricate, multifaceted, robust (unless technical), crucial, vital, essential, profound/profoundly, meticulous/meticulously, rich (figurative), vibrant, landscape (figurative). Pick a plainer synonym or cut the adjective.

**R8. Demote hedging intensifiers.** Words like key, core, fundamental, crucial, essential, central, deep, deeper add emphasis but not information. Delete on first pass; restore only if the sentence genuinely weakens.

**R9. Replace vague "carrier" verbs with concrete ones.** embody, capture, reflect, encompass, constitute, represent, manifest, exhibit → prefer precise verbs like store, encode, compress, execute, index, replace, override.

**R10. Avoid nominalization.** "we analyze X" not "we conduct an analysis of X"; "X changes Y" not "X leads to a change in Y".

**R11. No grandiose framing nouns without substance.** paradigm, lens, perspective, framework, dimension, axis — at most one per paragraph unless genuinely operative.

## 3. Argumentative Posture

**R12. No empty balance.** Don't automatically append "however, this approach has limitations" or "that said, challenges remain" after every claim. Add a caveat only with a specific limitation in the same sentence.

**R13. No meta-commentary on the reader's attention.** Delete: "it is worth noting that", "interestingly", "importantly", "notably", "remarkably", "it should be emphasized that". If the point is important, the content shows it.

**R14. Do not restate the paragraph in its last sentence.** Closing sentences should add a new inference, consequence, or transition — not summarize what was just said. Cut "In summary", "Taken together", "Thus we see that" unless real synthesis follows.

**R15. No false-problem setups.** Avoid "A central question is whether…", "One might ask…", "This raises the question of…" as decorative openers.

**R16. Cite with specificity.** "Prior work has explored X" + six citations is lazy. Name 1–2 works that matter and describe what they did, or group by the specific variant they studied.

## 4. Paragraph Structure

**R17. Not every paragraph needs intro-body-conclusion.** Allow paragraphs that make one point and stop.

**R18. Do not template section openings.** Avoid starting every subsection with "In this section, we…" or "Having discussed X, we now turn to Y". Some sections should open with a claim directly.

**R19. Limit bullet lists.** Use bullets only for genuinely parallel short items. If each bullet is a full sentence with clauses, write a paragraph.

**R20. Topic sentences should carry specific content.** "There are several challenges in this pathway" is empty; "Two failure modes dominate this pathway: reward hacking and distributional collapse" is informative.

## 5. Survey-Specific

**R21. No "gap-filling" clichés.** Avoid "Despite significant progress, … remains underexplored", "To bridge this gap, we…", "A comprehensive understanding is still lacking". State what is actually missing and why.

**R22. Trade-off tables must contain information, not adjectives.** Cells with "high", "low", "moderate", "flexible", "complex" are worthless. Use concrete quantities, mechanism phrases, or "not reported".

**R23. Do not announce contributions in body text.** "We propose…", "Our framework offers…", "This survey makes three contributions" belong in Introduction and Conclusion only.

**R24. Do not copy internal scaffolding into prose.** Design-doc labels like "Core question:", "Essence:", "Claim template:" must not appear in the manuscript.

**R25. Comparative claims need a reference point.** "X achieves better generalization" means nothing without "better than Y under conditions Z". If the reference point is unavailable, say so explicitly.

## Quick Self-Check

Before finalizing a paragraph, verify:
- Any word from the R7 ban list? Replace or delete.
- More than one parallel construction (R2) or em dash (R5)?
- Can I delete every "key / core / crucial / fundamental" (R8) without the sentence collapsing? If yes, delete them.
- Does the closing sentence add something new (R14)?
- If read aloud, does the rhythm sound uniform (R1)?

If three or more checks fail, the paragraph still reads as AI-generated.
