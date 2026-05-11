---
name: translate-survey-tex
description: Translate Chinese Markdown survey draft fragments into faithful, polished English LaTeX fragments for ACM CSUR-style manuscripts, and insert them into a user-specified .tex file when requested. Use when the user provides a Chinese Markdown source file plus a target TeX file, asks for Survey academic English writing or polishing, needs Markdown emphasis removed from TeX output, or asks for anti-AI-voice revision while preserving the original Chinese meaning.
---

# Translate Survey TeX

## Contract

Produce the English LaTeX fragment corresponding to the user-specified Chinese Markdown content. Preserve the source meaning, claim order, scope, hedging, citations, and technical distinctions. Do not add papers, examples, taxonomy changes, arguments, caveats, or restructuring that the Chinese source does not support.

When working in this repository, read `CLAUDE.md` before reading or editing project files. Only read the source Markdown file, the target TeX file, this skill's references, and any explicitly referenced local instructions.

## References

- Read `references/writing-rules.md` before drafting the English version.
- Read `references/anti-ai-voice-rules.md` after drafting, then revise the text once to reduce generic LLM phrasing.

## Workflow

1. Confirm the source Markdown path and target `.tex` path from the user request. If the insertion point is ambiguous, inspect only the relevant target file context; ask a concise question if editing would require guessing where the fragment belongs.
2. Read the Chinese Markdown source exactly as the source of truth. Treat headings, bullets, emphasis, citations, inline math, and terminology as content signals, not permission to reorder the argument.
3. Draft a faithful English academic version. Keep paragraph boundaries and information order close to the Chinese source unless a sentence must be split for grammatical English.
4. Convert to a LaTeX fragment only:
   - Do not include a preamble, `\begin{document}`, bibliography, or unrelated section scaffolding.
   - Preserve existing LaTeX commands, math, labels, citation keys, and cross-references.
   - Escape literal TeX special characters only when they are text, not commands.
   - Remove Markdown emphasis markers such as `**bold**`, `*italic*`, and `_italic_`. Do not convert them to `\textbf{}` or `\emph{}` unless the user explicitly asks for styled TeX.
5. Polish for ACM CSUR survey prose using the writing reference: concise verbs, clear subjects, consistent terminology, precise tense, and citation-specific claims.
6. Run the anti-AI-voice pass using the anti-AI reference. Remove formulaic transitions, padded triads, generic intensifiers, decorative balance, and vague carrier verbs while keeping the same meaning.
7. If the user asked to write into the target TeX file, edit only that file and only the requested region. Otherwise, return only the TeX fragment.

## Quality Gate

Before finalizing, check:

- The English text says no more and no less than the Chinese source.
- No Markdown emphasis syntax remains in the TeX fragment.
- No unsupported literature claim, citation, or taxonomy term was introduced.
- Terms are consistent within the fragment and with the target TeX context that was actually read.
- The prose avoids the banned or high-risk AI-voice patterns in `references/anti-ai-voice-rules.md`.
