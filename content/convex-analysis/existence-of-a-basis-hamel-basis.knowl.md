+++
id = "convex-analysis/existence-of-a-basis-hamel-basis"
title = "Existence of a basis"
kind = "knowl"
summary = "Assuming the axiom of choice, every vector space admits a Hamel basis."
aliases = ["existence-of-a-basis-hamel-basis", "Existence of a basis"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/existence-of-a-basis-hamel-basis.md"
+++

**Theorem (existence of a Hamel basis).** Assuming the axiom of choice, every
vector space \(X\) has a
[[convex-analysis/basis-hamel-basis-and-dimension|Hamel basis]].

## Derivation

The empty set is linearly independent, so
[[convex-analysis/extension-of-a-linearly-independent-set-to-a-basis|the
extension theorem]], proved using Zorn's lemma, extends it to a basis of \(X\).
For \(X=\{0\}\), this basis is the empty set.

## Examples

- \(\mathbb{R}^n\) has the standard basis.
- Infinite-dimensional examples (like all sequences) have a Hamel basis, but it typically cannot be written down explicitly.
