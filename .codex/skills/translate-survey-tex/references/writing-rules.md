# Survey Academic English Rules

Use these rules when translating Chinese Markdown survey prose into English LaTeX for an ACM CSUR-style manuscript.

## Concision

- Delete redundant phrasing when meaning is unchanged: use "because" rather than "due to the fact that", "as" rather than "in the form of", and "often" rather than "in many cases".
- Prefer verbs over nominalizations: write "analyze", "install", and "consider" rather than "conduct an analysis", "effect an installation", or "give consideration".
- Keep the grammatical subject visible. Prefer "This method eliminates the problem" over "The use of this method eliminates the problem".
- Split long sentences when they obscure the claim, relation, or evidence.

## Clarity

- Prefer active voice when it identifies the actor and improves clarity. Passive voice is acceptable when the actor is unknown, irrelevant, or conventional for methods-style description.
- Follow given-new order: put familiar context early and new, technical, or complex information late in the sentence.
- Keep parallel items grammatically parallel.
- Place modifiers next to the terms they modify.

## Consistency

- Keep terminology, capitalization, hyphenation, acronyms, symbols, and citation style consistent with the target TeX context.
- Define an acronym on first use in the fragment only if the surrounding target context has not already defined it.
- Do not alternate translations for the same concept unless the Chinese source distinguishes them.

## Common Chinglish Fixes

- Add an explicit subject when Chinese omits one.
- Avoid double connectors: use either "although" or "but", and either "because" or "so".
- Avoid repeated emphasis structures such as "It is ... that ..." unless contrast is necessary.
- Remove redundant twins such as "various and different", "final and ultimate", and "basic and fundamental".
- Replace vague intensifiers such as "very", "quite", "really", "obviously", and "clearly" with precise wording or delete them.

## Tense And Person

- Use present tense for field status, definitions, taxonomy claims, and this survey's organization.
- Use past tense for specific completed prior work when naming what authors did.
- Use present perfect for trends or accumulated findings across recent work.
- Use past tense, with passive voice when useful, for experiments or implementation details.
- Use formal academic tone. "We" is acceptable for survey actions such as "we classify"; avoid "I" and "you".

## Citations

- Keep citation keys and citation claims faithful to the source. Do not invent citations.
- Support core survey claims with specific representative citations when the source already provides them or the target context clearly contains them.
- Avoid citation dumps. Prefer the representative works that support the exact claim.
- Do not make second-hand citation claims unless the source explicitly does so.
