+++
id = "differential-geometry/elliptic-differential-operator"
title = "Elliptic differential operator"
kind = "definition"
summary = "A differential operator whose principal symbol is invertible at every nonzero cotangent vector."
aliases = ["elliptic operator", "ellipticity"]
domains = ["differential-geometry"]
prerequisites = ["fiber-bundles/vector-bundle", "differential-geometry/differential-operator-vector-bundles", "differential-geometry/principal-symbol", "convex-analysis/image-and-kernel-linear-isomorphism"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(D:\Gamma^\infty(E)\to\Gamma^\infty(F)\) be a differential operator of order \(m\geq0\) between smooth [[fiber-bundles/vector-bundle|vector bundles]] over \(M\). The operator \(D\) is **elliptic** if, for every \(x\in M\) and every nonzero \(\xi\in T_x^*M\), its [[differential-geometry/principal-symbol|principal symbol]]
\[
\sigma_m(D)(x,\xi):E_x\longrightarrow F_x
\]
is a [[convex-analysis/image-and-kernel-linear-isomorphism|linear isomorphism]]. Ellipticity is therefore a condition on the highest-order part alone. It implies that \(E\) and \(F\) have equal rank on each [[topology/connected-component|connected component]], but it does not by itself impose self-adjointness or compactness of the base manifold.

## Analytic consequences

Elliptic regularity says that distributional solutions gain smoothness wherever the right-hand side is smooth. On a [[topology/closed-manifold|closed manifold]], the Sobolev extension
\[
D:H^{s+m}(E)\longrightarrow H^s(F)
\]
is [[functional-analysis/fredholm-operator|Fredholm]] for every real \(s\); hence its kernel and cokernel are finite-dimensional.

## Examples and non-examples

The scalar Laplace–Beltrami operator has symbol \(|\xi|^2\) and is elliptic. [[noncommutative-geometry/dirac-type-operator|Dirac-type operators]] have Clifford-linear symbol and are first-order elliptic operators. By contrast, \(\partial/\partial x_1\) on \(\mathbb R^n\) with \(n>1\) has symbol \(\xi_1\), which vanishes for many nonzero covectors, so it is not elliptic.

## Conventions and scope

**Warning.** Boundary-value problems require an additional elliptic boundary condition; ellipticity of the interior operator alone does not make such a problem Fredholm. On a noncompact manifold, ellipticity alone likewise need not give a Fredholm operator or discrete spectrum.

## References

1. R. O. Wells Jr., *Differential Analysis on Complex Manifolds*, 3rd ed., Springer, 2008. [Publisher record](https://doi.org/10.1007/978-0-387-73892-5). Relevant: chapter IV, elliptic operator theory.
2. H. B. Lawson Jr. and M.-L. Michelsohn, *Spin Geometry*, Princeton University Press, 1989. [Publisher record](https://doi.org/10.1515/9781400883912). Relevant: chapter III, ellipticity and analytic properties.
