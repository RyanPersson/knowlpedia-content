+++
id = "differential-geometry/polarized-hodge-structure"
title = "Polarized Hodge structure"
kind = "definition"
summary = "A pure Hodge structure equipped with a parity-compatible bilinear form satisfying Hodge orthogonality and positivity."
aliases = ["Hodge polarization", "polarization of a Hodge structure"]
domains = ["differential-geometry"]
prerequisites = ["differential-geometry/pure-hodge-structure", "linear-algebra/bilinear-form"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

A **polarization** of a real [[differential-geometry/pure-hodge-structure|pure Hodge structure]] \(V\) of weight \(n\) is a nondegenerate real [[linear-algebra/bilinear-form|bilinear form]] \(Q\) such that
\[
Q(v,w)=(-1)^nQ(w,v),
\qquad
Q(V^{p,q},V^{r,s})=0\ \text{unless }(r,s)=(q,p),
\]
and, for every nonzero \(v\in V^{p,q}\),
\[
i^{\,p-q}Q(v,\overline v)>0.
\]
A **polarized Hodge structure** is the pair \((V,Q)\). For a rational or integral Hodge structure, \(Q\) is required to be defined over the corresponding coefficient ring, with nondegeneracy interpreted after extending scalars.
Thus \(Q\) is symmetric in even weight and alternating in odd weight.

## Weil-operator formulation

The Weil operator \(C\) acts on \(V^{p,q}\) by \(i^{p-q}\). The positivity condition says that
\[
h(v,w)=Q(Cv,\overline w)
\]
is a positive-definite Hermitian form. The orthogonality and positivity conditions are the abstract form of the [[differential-geometry/hodge-riemann-bilinear-relations|Hodge–Riemann bilinear relations]].

## Cohomological construction

For a compact [[differential-geometry/kahler-manifold|Kähler manifold]] with a rational [[differential-geometry/kahler-class|Kähler class]], each [[differential-geometry/primitive-cohomology|primitive cohomology]] group becomes polarized after the signed intersection pairing is normalized by the factor \((-1)^{n(n-1)/2}\) appropriate to its weight. Lefschetz decomposition then expresses the full cohomology as a sum of polarized primitive pieces.

## Conventions and near-misses

Some authors place a weight-dependent sign in \(Q\), in the Weil operator, or in the positivity inequality. These conventions describe equivalent structures only when all three formulas are adjusted together. A nondegenerate form satisfying the parity rule is not automatically a polarization: it must also satisfy Hodge orthogonality and positivity.

## References

1. Claire Voisin, *Hodge Theory and Complex Algebraic Geometry I*, Cambridge Studies in Advanced Mathematics 76, Cambridge University Press, 2002. [Chapter record](https://doi.org/10.1017/CBO9780511615344.008). Relevant: §7.1.2, polarizations, and the primitive cohomology examples.
2. Daniel Huybrechts, *Complex Geometry: An Introduction*, Springer, 2005. [Publisher record](https://doi.org/10.1007/b137952). Relevant: Chapter 3, Hodge–Riemann bilinear relations and polarized cohomology.
