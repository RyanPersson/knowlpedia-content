# Knowlpedia editorial model

Knowls should support two reading speeds: a reader who needs the definition now, and a reader who wants to explore why it matters.

## Canonical core

Place the smallest sufficient statement before the first level-two heading. The core should:

- name the definiendum or theorem immediately;
- state all hypotheses needed for correctness;
- link genuine prerequisites;
- stand on its own when opened inline.

Do not begin with history, a long analogy, or a list of examples. A short orienting sentence is useful when the formal statement alone is hard to parse.

## Optional sections

Use descriptive `##` headings for material that helps some readers but should not obscure the core. Common choices include:

- `## Intuition` or `## Guiding picture`
- `## How to read the definition`
- `## Examples`
- `## Equivalent characterizations`
- `## Properties`
- `## Interpretation`
- `## Remarks`
- `## History` or `## Literature`

The compiler turns these headings into full-page disclosures and inline section chips. A standalone `**Examples:**` block is also recognized for compatibility with migrated content.

Knowls of kind `document`, `index`, `page`, or `section` remain continuous by default. Any knowl may set `section_mode = "progressive"` or `section_mode = "continuous"` in its front matter when its reading form calls for an explicit override.

## Mathematical communication

- Explain the role of displayed maps and equations in prose; do not make readers infer why a formula is present.
- Separate an analogy from the definition and state where the analogy stops being literal.
- Put setting-sensitive cautions in Remarks as a clearly labeled warning.
- Prefer one representative example that exposes the mechanism over a long unstructured list.
- Link a term when expanding it would answer a plausible reader question at that point.
- Avoid link saturation: ordinary words and notation defined locally do not need knowls.

## References and citations

Put bibliographic sources and clickable external links only in a final
`## References` section. Do not place source attributions in the core or other
sections, either as hyperlinks or as plain text such as `[Author, Chapter 3]`.
Body prose should state the mathematics directly and may use internal knowl
links where a definition or theorem is a genuine dependency.
