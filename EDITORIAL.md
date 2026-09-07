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

Keep the defining axioms in the core. Do not replace an axiomatic construction with a shorter characterization that assumes an already constructed object, while moving its axioms into a later disclosure. For example, a basis for a topology opens with covering and intersection-refinement axioms; the generated-topology characterization follows afterward. Minimal means removing unnecessary material, not hiding necessary structure.

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
conventions, and records mathematical evidence plus a SHA-256 hash of the reviewed
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

For elementary claims, specific direct reasoning is valid evidence; leave the
source list empty when no external source was used. Do not attach a syllabus,
publisher page, or unrelated chapter to imply a theorem was checked. Unresolved
claims keep the review targeted. Record partial results early and count only
accepted full reviews whose source hashes still match.

Prerequisites must form a DAG even before their lists receive an editorial
review. A definition may mention a later theorem without depending on it.
Do not remove a theorem's hypotheses or an object's defining ingredients just
to break a cycle. Resolve circular exposition at its definition boundary and
retain useful ordinary links. A component already defined within the complete
data of an object need not become a prerequisite merely because a companion
knowl extracts that component.


## Flagged issues

Store concerns about an individual knowl in optional `[[issues]]` tables at
**the end of its TOML front matter**, before the closing `+++`. Keep all
existing top-level metadata above these tables: TOML keys following an
`[[issues]]` header belong to that issue. No `issues` field is needed on
knowls without reports. These records belong to the content repository and
are versioned with the knowl. They are editorial metadata, not reader-facing
content; the compiler does not publish them in HTML or the registry.

Each issue has these fields:

| Field | Convention |
| --- | --- |
| `id` | Stable UUID string; never renumber or reuse for another concern. |
| `status` | `open`, `resolved`, or `dismissed`. Start with `open`. |
| `summary` | Short description of the concern, not an unverified assertion of error. |
| `reported_at` | UTC timestamp string in ISO 8601 format, retained unchanged. |
| `updated_at` | UTC timestamp string, updated when the record changes. |
| `report` | Reviewer's original concern; preserve it on subsequent updates. |
| `selected_text` | Optional exact excerpt supplied with the report. |
| `assessment` | Model's findings, evidence, uncertainty, and proposed next step. Initially empty if investigation is pending. |
| `resolution` | Required when resolved or dismissed: explain the fix and checks, or evidence for dismissal. |

The containing knowl's `id` associates the issue with its subject; do not
repeat the knowl ID inside the issue. Escape strings correctly for TOML and
parse the whole front matter after every edit. Never put access keys,
authentication data, or conversation transcripts in these records.

**Flag issue** records the concern before investigation, then updates the
assessment. It does not authorize corrections to the mathematical body.
Leave uncertain concerns open, even when a possible fix is apparent.
**Request change** may apply a correction and resolve the matching issue
after focused checks. Dismissal means evidence shows no correction is needed;
record that reasoning. Retain closed records rather than deleting history.
For a clearly duplicate concern, reuse the issue and append new information
to its assessment without replacing the original report; reopen if new
evidence calls the previous resolution into question.

Flagging an issue does not increment dependency-review counts or constitute
a completed refactor review. The refactor ledger continues to record reviews;
`[[issues]]` records actionable concerns and their disposition. These records
are saved by the feedback model using repository edits, not by a separate
issue database. If the model fails before saving, the conversation alone is
not a saved issue; its final reply must identify the saved issue and file, or
explicitly report that it could not save the flag.
