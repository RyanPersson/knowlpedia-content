+++
id = "fiber-bundles/yang-mills-energy-identity"
title = "Yang–Mills energy identity"
kind = "theorem"
summary = "The four-dimensional decomposition of Yang–Mills energy into a topological curvature integral and a nonnegative self-dual or anti-self-dual term."
aliases = ["topological Yang–Mills energy bound", "instanton energy bound", "Bogomolny decomposition"]
domains = ["fiber-bundles", "differential-geometry"]
section_mode = "progressive"
prerequisites = ["fiber-bundles/principal-g-bundle", "linear-algebra/inner-product", "lie-groups/lie-algebra", "fiber-bundles/curvature-2-form-of-a-principal-connection", "shared-foundations/lower-bound", "fiber-bundles/construction-adjoint-lie-algebra-bundle-ad", "fiber-bundles/vector-bundle-valued-differential-form", "fiber-bundles/yangmills-functional", "fiber-bundles/l2-inner-product-on-bundle-valued-forms", "differential-geometry/hodge-star-operator", "differential-geometry/integration-of-differential-forms", "fiber-bundles/wedge-product-of-differential-forms", "fiber-bundles/invariant-polynomial-on-a-lie-algebra"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(P\to X\) be a [[fiber-bundles/principal-g-bundle|principal bundle]] with compact structure group over a closed oriented Riemannian four-manifold, and choose an Ad-invariant [[linear-algebra/inner-product|inner product]] on its [[lie-groups/lie-algebra|Lie algebra]]. For any connection \(A\), write \(F_A=F_A^++F_A^-\) for the Hodge decomposition of its [[fiber-bundles/curvature-2-form-of-a-principal-connection|curvature]] and set \(\operatorname{YM}(A)=\tfrac12\|F_A\|_{L^2}^2\). Then
\[
\operatorname{YM}(A)
=\frac12\int_X\langle F_A\wedge F_A\rangle+\|F_A^-\|_{L^2}^2
=-\frac12\int_X\langle F_A\wedge F_A\rangle+\|F_A^+\|_{L^2}^2.
\]
The curvature integral depends only on the bundle and the chosen invariant polynomial, without requiring integral normalization; an integral normalization is needed only to identify it with an integer characteristic number. These identities hold for every smooth connection and immediately imply a sharp [[shared-foundations/lower-bound|lower bound]].


Here \(F_A\) denotes the base-valued curvature: if \(\Omega_A\) is the principal curvature on \(P\), then \(F_A(x)(v,w)=[p,\Omega_A(\widetilde v,\widetilde w)]\in\operatorname{ad}(P)_x\), with \(p\in P_x\) and any lifts of \(v,w\). Horizontality and equivariance make this independent of the choices. The Hodge star acts on the differential-form factor.
## Derivation

The [[differential-geometry/hodge-star-operator|Hodge star]] is an orthogonal involution on two-forms in dimension four. Consequently,
\[
\|F_A\|_{L^2}^2=\|F_A^+\|_{L^2}^2+\|F_A^-\|_{L^2}^2,
\qquad
\int_X\langle F_A\wedge F_A\rangle
=\|F_A^+\|_{L^2}^2-\|F_A^-\|_{L^2}^2.
\]
Adding and subtracting these two equalities gives the identity. [[fiber-bundles/chern-weil-homomorphism|Chern–Weil theory]] makes the second integral independent of \(A\), so the identity compares connections in one topological bundle class.

## Equality cases

The two remainder terms are nonnegative. Hence
\[
\operatorname{YM}(A)\geq
\frac12\left|\int_X\langle F_A\wedge F_A\rangle\right|.
\]
Equality holds exactly when \(F_A^-=0\) or \(F_A^+=0\), with the choice determined by the sign of the topological term. Thus [[fiber-bundles/self-dual-and-anti-self-dual-connection|self-dual and anti-self-dual connections]] are absolute energy minimizers within their topological class.

For an \(SU(r)\)-bundle with inner product \(\langle\xi,\eta\rangle=-\operatorname{tr}(\xi\eta)\), the [[fiber-bundles/instanton-number|instanton number]] satisfies
\[
k=\frac{1}{8\pi^2}\int_X\operatorname{tr}(F_A\wedge F_A),
\]
so the convention \(\operatorname{YM}(A)=\tfrac12\|F_A\|^2\) gives \(\operatorname{YM}(A)\geq4\pi^2|k|\).

## Conventions and scope

**Warning.** Many authors define Yang–Mills energy without the factor \(1/2\), producing the more familiar bound \(8\pi^2|k|\). Signs also change with orientation and with Hermitian versus skew-Hermitian curvature conventions. The invariant content is the norm decomposition and its equality condition, not a coefficient detached from these choices.

## References

1. Simon K. Donaldson and Peter B. Kronheimer, *The Geometry of Four-Manifolds*, Oxford University Press, 1990. [DOI record](https://doi.org/10.1093/oso/9780198535539.001.0001). Relevant: §2.1, curvature decomposition and the topological energy bound.
2. Daniel S. Freed and Karen K. Uhlenbeck, *Instantons and Four-Manifolds*, 2nd ed., Springer, 1991. [DOI record](https://doi.org/10.1007/978-1-4613-9703-8). Relevant: Chapter 2, Chern–Weil normalization and Yang–Mills energy.
