+++
id = "lie-groups/baker-campbell-hausdorff-formula"
title = "Baker–Campbell–Hausdorff formula"
kind = "theorem"
summary = "A Lie series for the product exp(X)exp(Y) expressed as exp(BCH(X,Y))."
aliases = ["baker-campbell-hausdorff-formula", "Baker–Campbell–Hausdorff formula"]
domains = ["lie-groups"]
prerequisites = ["fiber-bundles/lie-group", "lie-groups/exponential-map-lie-group", "fiber-bundles/lie-bracket", "lie-groups/nilpotent-lie-algebra"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
legacy_source_path = "lie-groups/baker-campbell-hausdorff-formula.md"
section_mode = "progressive"
+++

Let \(G\) be a [[fiber-bundles/lie-group|Lie group]] with Lie algebra \(\mathfrak{g}\) and [[lie-groups/exponential-map-lie-group|exponential map]] \(\exp:\mathfrak{g}\to G\). For \(X,Y\in\mathfrak{g}\) sufficiently small, there is a unique \(Z\in\mathfrak{g}\) near \(0\) such that \(\exp(X)\exp(Y)=\exp(Z)\); write \(Z=\mathrm{BCH}(X,Y)\).

**Theorem (BCH).** In a neighborhood of \(0\in\mathfrak{g}\),
\[
\mathrm{BCH}(X,Y)
= X+Y+\frac12[X,Y]+\frac1{12}[X,[X,Y]]-\frac1{12}[Y,[X,Y]]+\cdots,
\]

where the omitted terms are (universal) Lie polynomials in iterated [[fiber-bundles/lie-bracket|brackets]] of total degree \(\ge 4\).

Moreover, if \(\mathfrak{g}\) is [[lie-groups/nilpotent-lie-algebra|nilpotent]], then all sufficiently deep iterated brackets vanish and the BCH series truncates to a finite sum.

## Formal Lie series

The same expression exists without an analytic Lie group. Over
\(\mathbb Q\), let \(\widehat L(X,Y)\) be the completion by bracket degree of
the free Lie algebra on \(X,Y\). In the completed
[[lie-groups/universal-enveloping-algebra|universal enveloping algebra]],
\[
\operatorname{BCH}(X,Y)
=
\log\!\bigl(\exp(X)\exp(Y)\bigr)
\in\widehat L(X,Y).
\]
This identity defines a universal formal Lie series. Its homogeneous component
of any fixed degree is a finite rational linear combination of iterated
brackets, so it can be evaluated degree by degree in formal coordinates on
every finite-dimensional Lie algebra over a characteristic-zero field.

More generally, the series evaluates in a complete filtered Lie algebra when
brackets raise filtration and \(X,Y\) lie in the positive filtration. In that
setting “convergence” means convergence in the filtration, not convergence of
real or complex numbers.

Associativity of multiplication of exponentials implies the formal identity
\[
\operatorname{BCH}(\operatorname{BCH}(X,Y),Z)
=
\operatorname{BCH}(X,\operatorname{BCH}(Y,Z)).
\]
Together with identity \(0\) and inverse \(-X\), this makes BCH a
[[formal-groups/formal-group-law|formal group law]] and supplies the
integration functor in the
[[formal-groups/lie-algebra-formal-group-equivalence|characteristic-zero
formal Lie correspondence]].

## Analytic interpretation

**Context.** BCH is the mechanism by which \(\mathfrak{g}\) determines the local group law: via the [[lie-groups/logarithm-map|logarithm map]] (local inverse to \(\exp\)), it turns multiplication in \(G\) into an explicit Lie series on \(\mathfrak{g}\). This is central to the [[lie-groups/lie-correspondence|Lie correspondence]] and to computations in exponential coordinates, especially for nilpotent and solvable groups.

The formal identity and the analytic assertion have different hypotheses.
Formal evaluation only uses degree completion and rational coefficients.
Analytic evaluation requires a topology and sufficiently small inputs (unless
nilpotence makes the series finite).

## References

1. Nicolas Bourbaki, *Lie Groups and Lie Algebras: Chapters 1–3*, Springer, 1989. [Publisher record](https://link.springer.com/book/9783540642428). Relevant: Chapter 2, exponential, logarithmic, and Hausdorff series.
2. Jean-Pierre Serre, *Lie Algebras and Lie Groups*, second edition, Springer, 1992. [Publisher record](https://link.springer.com/book/10.1007/978-3-540-70634-2). Relevant: Part I, formal Lie theory.
