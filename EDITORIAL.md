# Knowlpedia editorial model

Knowls should support two reading speeds: a reader who needs the definition now, and a reader who wants to explore why it matters.

## Concept ownership

An ordinary knowl owns one independently reusable definition, theorem,
construction, example, or convention. Progressive sections may explain that
subject, state variants, introduce indispensable auxiliary notation, and
compare neighboring concepts; they must not serve as hidden homes for other
concepts that readers may need to link directly.

In particular, do not send labels for distinct terms to an umbrella knowl that
defines each term in a different section. Give each term a canonical knowl and
link the relationship between them. Genuine surveys, source transcripts,
historical bridges, and navigation collections should declare an appropriate
container kind such as `document`, `page`, `section`, or `index` rather than
masquerading as a single definition.

Conjunctions are not violations by themselves. A theorem relating two
conditions, a comparison page, inverse constructions, or the data and
universal property of one construction may be a coherent single subject. Use
semantic judgment rather than splitting titles mechanically.

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

For editorial review, distinguish three scopes. A full review reads the
complete knowl and its direct prerequisite definitions, checks the adopted
conventions, and records source evidence plus a SHA-256 hash of the reviewed
source. A targeted review covers only named claims or sections and does not
close the full-review queue. A dependencies review checks the complete
prerequisite list and its provenance; metadata-only changes are not content
corrections. Record these reviews in reviews/refactor-ledger.json and
regenerate progress with scripts/review_progress.py.

Use primary papers for distinctive technical claims and authoritative
monographs or standard texts for established definitions. Record the exact
section, theorem, page, or equivalent locator that was actually checked.
Never describe a rendered build or an automated validation pass as proof of
mathematical truth.
