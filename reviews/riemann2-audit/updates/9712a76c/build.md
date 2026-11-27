# Build and link verification

The production compiler at `12cc7330` loaded a registry of 5,777 knowls and generated all 812 Riemann2 HTML pages and their fragments in a fresh output directory. Validation exited with status 1 and eight missing-target errors on six older draft pages. The preceding audit had ten errors. All 778 ordinary links in the 150 added or edited pages resolve to an existing ID. [Compiler entry point](https://github.com/RyanPersson/knowlpedia/blob/12cc7330341b6b4fb72c78b91a659e67e82a4b18/packages/compiler/knowl_compile.py#L2877) · [Previous build](../b4aa180e/build-and-tools.md)

Two speculative unfolding-B links from the previous run were replaced by Lean placeholders. Each placeholder has an exact knowl owner, so the ordinary-link errors have cleared and the final resolution pass can make these clickable. [Filling data reference](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/filling-data.knowl.md#L56) · [Its owner](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-core/filling-data-of-admissible-data.knowl.md#L10) · [Admissibility reference](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/filling-admissible.knowl.md#L35) · [Its new reference’s owner](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-a/scaled-siegel-constant-bound.knowl.md#L10)

## Remaining missing targets

| Referring knowl | Ordinary link target |
| --- | --- |
| [square-moduli, line 30](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/determinant-chain/square-moduli.knowl.md#L30) | `proofs/grh/determinant-chain/modulus-relation-of-the-chain` |
| [triangle-of-arrows, line 42](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/determinant-chain/triangle-of-arrows.knowl.md#L42) | `proofs/grh/determinant-chain/triangle-of-theta-lifts` |
| [hyperplane-sums-annihilate, line 48](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/onelift-values/hyperplane-sums-annihilate.knowl.md#L48) | `proofs/grh/onelift-values/false-lifts-from-a-line` |
| [sum-over-shells, line 48](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-frames-b/sum-over-shells.knowl.md#L48) | `proofs/grh/spanning-frames-b/finite-shells` |
| [sum-over-shells, line 48](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-frames-b/sum-over-shells.knowl.md#L48) | `proofs/grh/spanning-frames-b/real-shells` |
| [archimedean-head-weight, line 35](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-mainterm/archimedean-head-weight.knowl.md#L35) | `proofs/grh/spanning-mainterm/global-weight` |
| [damped-power, line 22](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-mainterm/damped-power.knowl.md#L22) | `proofs/grh/spanning-mainterm/sieve-over-all-places` |
| [damped-power, line 27](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-mainterm/damped-power.knowl.md#L27) | `proofs/grh/spanning-mainterm/sum-over-frequencies-bound` |

## Math and source metadata

The 150 added or edited pages contain 7,633 math occurrences and 3,976 distinct expression/display-mode pairs. KaTeX 0.16.47 parsed every one. The full 812-page scan parsed 43,823 occurrences and 19,809 distinct pairs, and the generated HTML contains no `katex-error` marker. The explicit wiki placeholder inside a field display is valid TeX text and still appears literally in the rendered formula. [Before-and-after bracket scan](brackets.md)

The changed pages contain 282 Lean placeholders and 70 concept placeholders in prose outside math. Every listed source file exists. The full GRH registry has 4,119 distinct Lean names in page headers and each has a single page owner. All current concept-table destinations are existing IDs or the exact `NEW` marker. Whether each choice is the right mathematical concept is checked in the concept review. [Source ownership](provenance.md) · [Concept review](concepts.md)

To reproduce the build, run `packages/compiler/knowl_compile.py` from the pinned Knowlpedia checkout against `knowlpedia-content` with `--profile production`, a fresh `--out` directory and one `--only` argument per canonical ID under `content/proofs/grh`. For the expression count use the compiler’s math pattern on titles, summaries and bodies, masking inline and fenced code. [Math pattern](https://github.com/RyanPersson/knowlpedia/blob/12cc7330341b6b4fb72c78b91a659e67e82a4b18/packages/compiler/knowl_patterns.py#L17)
