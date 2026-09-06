+++
id = "functional-analysis/holomorphic-functional-calculus-banach-algebra"
title = "Holomorphic functional calculus in a Banach algebra"
kind = "definition"
summary = "A contour-integral calculus that evaluates functions holomorphic near the spectrum at a Banach-algebra element."
aliases = ["analytic functional calculus", "Riesz–Dunford calculus", "holomorphic functional calculus"]
domains = ["functional-analysis"]
section_mode = "progressive"
prerequisites = ["functional-analysis/banach-algebra", "functional-analysis/banach-algebra-spectrum", "functional-analysis/banach-algebra-resolvent"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(A\) be a complex unital [[functional-analysis/banach-algebra|Banach algebra]], let \(a\in A\), and let \(f\) be holomorphic on an open neighborhood
of the [[functional-analysis/banach-algebra-spectrum|spectrum]]
\(\sigma_A(a)\). Choose a positively oriented contour \(\Gamma\) in the
[[functional-analysis/banach-algebra-resolvent|resolvent set]] that winds once
around \(\sigma_A(a)\) and zero times around points outside the chosen
neighborhood. The **holomorphic functional calculus** defines
\[
f(a)=\frac{1}{2\pi i}\int_\Gamma
f(z)(z1_A-a)^{-1}\,dz.
\]
The Banach-valued contour integral is independent of every admissible choice of
\(\Gamma\), so \(f(a)\) depends only on \(a\) and the germ of \(f\) near its
spectrum.

## Algebraic and spectral properties

For a fixed neighborhood of \(\sigma_A(a)\), the assignment \(f\mapsto f(a)\)
is a continuous unital [[algebra-modules/algebra-homomorphism|algebra homomorphism]]. It agrees with polynomial
evaluation and with rational evaluation when the poles avoid the spectrum. It
also satisfies the [[operator-algebras/spectral-mapping-theorem|spectral mapping theorem]]
\[
\sigma_A(f(a))=f(\sigma_A(a)).
\]
If \(g\) is holomorphic near \(f(\sigma_A(a))\), then
\((g\mathbin{\circ}f)(a)=g(f(a))\). These properties follow from the resolvent
identity and the Cauchy integral formula.

## Spectral projections and comparison

Suppose \(\sigma_A(a)\) is the disjoint union of two compact subsets separated
by open neighborhoods. A locally constant holomorphic function that is one
near the first subset and zero near the second produces an idempotent
\(p=f(a)\), called a Riesz spectral projection. Thus the calculus can isolate
spectral components even when \(a\) is not normal.

When \(A\) is a \(C^*\)-algebra and \(a\) is normal, this construction agrees
with the [[operator-algebras/continuous-functional-calculus|continuous functional calculus]] on functions that are holomorphic near the spectrum.

## Conventions and scope

**Warning.** The calculus requires complex scalars and holomorphy on a
neighborhood of the entire spectrum; pointwise values only on the spectrum do
not determine an admissible function in general. Reversing the convention from
\((z1_A-a)^{-1}\) to \((a-z1_A)^{-1}\) changes the contour sign. For a
nonunital algebra, one first passes to its unitization and checks whether the
result lies in the original algebra when that distinction matters.

## References

1. Gerard J. Murphy, *C*-Algebras and Operator Theory, Academic Press, 1990. [DOI record](https://doi.org/10.1016/C2009-0-22289-6). Relevant: §1.3 on the holomorphic functional calculus and spectral mapping.
2. F. F. Bonsall and J. Duncan, Complete Normed Algebras, Springer, 1973. [Publisher record](https://link.springer.com/book/9783540373865). Relevant: Chapter III on spectra and analytic functional calculus in Banach algebras.
