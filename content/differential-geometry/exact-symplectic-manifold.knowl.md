+++
id = "differential-geometry/exact-symplectic-manifold"
title = "Exact symplectic manifold"
kind = "definition"
summary = "A symplectic manifold whose symplectic form is the exterior derivative of a global one-form."
aliases = ["exact symplectic form"]
domains = ["differential-geometry"]
section_mode = "progressive"
prerequisites = ["differential-geometry/symplectic-manifold", "fiber-bundles/exact-differential-form"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

An **exact symplectic manifold** is a [[differential-geometry/symplectic-manifold|symplectic manifold]] \((M,\omega)\) for which there exists a global one-form \(\lambda\in\Omega^1(M)\) satisfying
\[
\omega=d\lambda.
\]
Equivalently, the symplectic form is an [[fiber-bundles/exact-differential-form|exact differential form]]. The one-form \(\lambda\) is called a primitive or Liouville form for \(\omega\), but it is additional, noncanonical data: the assertion that \((M,\omega)\) is exact requires only that at least one such primitive exist.

## Choice of primitive

If \(\lambda\) and \(\lambda'\) are primitives of the same symplectic form, then \(\lambda'-\lambda\) is closed. They differ by an exact one-form only when their de Rham cohomology classes agree. Many constructions in Liouville and Weinstein geometry therefore concern a specified pair \((\omega,\lambda)\), not just the property that \(\omega\) is exact.

## Canonical example

On a [[fiber-bundles/cotangent-bundle|cotangent bundle]] \(T^*Q\), the tautological one-form \(\theta\) gives a canonical exact symplectic form, written \(d\theta\) or \(-d\theta\) according to convention. Cotangent bundles model the local behavior of many exact symplectic and contact-geometric constructions.

## Global restriction

A positive-dimensional compact symplectic manifold without boundary cannot be exact. Indeed, if \(\omega=d\lambda\) on a \(2n\)-manifold with \(n\geq1\), then
\[
\omega^n=d(\lambda\wedge\omega^{n-1}),
\]
so [[differential-geometry/stokes-theorem|Stokes' theorem]] would force \(\int_M\omega^n=0\), contradicting that \(\omega^n\) is a volume form. Compact exact symplectic manifolds are consequently studied with boundary and additional behavior of the primitive near that boundary.

## References

1. K. Cieliebak and Y. Eliashberg, *From Stein to Weinstein and Back*, American Mathematical Society, 2012. [AMS DOI record](https://doi.org/10.1090/coll/059). Relevant: §2 and the conventions for Liouville forms.
2. D. McDuff and D. Salamon, *Introduction to Symplectic Topology*, 3rd ed., Oxford University Press, 2017. [Oxford DOI record](https://doi.org/10.1093/oso/9780198794899.001.0001). Relevant: exact symplectic forms and cotangent bundles.
