+++
id = "lie-groups/exponential-one-parameter-subgroup-lemma"
title = "Exponentials and one-parameter subgroups"
kind = "knowl"
summary = "The curve t ↦ exp(tX) is the unique one-parameter subgroup with initial velocity X."
aliases = ["exponential-one-parameter-subgroup-lemma", "Exponentials and one-parameter subgroups"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/exponential-one-parameter-subgroup-lemma.md"
prerequisites = ["fiber-bundles/lie-group", "lie-groups/lie-algebra-of-a-lie-group", "lie-groups/exponential-map-lie-group", "lie-groups/one-parameter-subgroup"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(G\) be a [[fiber-bundles/lie-group|Lie group]] with [[lie-groups/lie-algebra-of-a-lie-group|Lie algebra]] \(\mathfrak g=T_eG\).

**Lemma (Exponential–one-parameter subgroup).**
For each \(X\in\mathfrak g\), there is a unique smooth [[lie-groups/one-parameter-subgroup|one-parameter subgroup]]
\[
\gamma_X:\mathbb R\to G
\]
with \(\gamma_X'(0)=X\). Conversely, every one-parameter subgroup \(\gamma\) is uniquely determined by \(X=\gamma'(0)\).
Moreover, after the [[lie-groups/exponential-map-lie-group|exponential map]] is defined by this correspondence,
\[
\gamma_X(t)=\exp(tX).
\]

## Remarks

**Context.**
This lemma packages the correspondence between elements of \(\mathfrak g\) and flows of left-invariant vector fields: the curve \(\gamma_X\) is the integral curve through \(e\) of the left-invariant field determined by \(X\) (compare [[lie-groups/one-parameter-subgroups-integral-curves|one-parameter subgroups as integral curves]]). Locally, it is compatible with the fact that \(\exp\) is a [[lie-groups/exponential-local-diffeomorphism|local diffeomorphism near 0]].
