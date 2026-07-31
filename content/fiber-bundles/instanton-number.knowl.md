+++
id = "fiber-bundles/instanton-number"
title = "Instanton number"
kind = "definition"
summary = "For an SU(r)-connection on a closed oriented four-manifold, the instanton number is the integral second Chern number represented by curvature."
aliases = ["topological charge", "second Chern number of an instanton"]
domains = ["fiber-bundles", "differential-geometry"]
section_mode = "progressive"
+++

Let \(E\to M\) be a rank-\(r\) Hermitian [[fiber-bundles/vector-bundle|vector bundle]] with structure group \(SU(r)\) over a closed oriented four-manifold, and let \(A\) be a [[fiber-bundles/hermitian-connection|unitary connection]] with curvature \(F_A\). Its **instanton number** is
\[
k(E)= -\frac{1}{8\pi^2}\int_M\operatorname{tr}(F_A\wedge F_A)
=\langle c_2(E),[M]\rangle\in\mathbb Z,
\]
using the defining representation and the stated sign convention. It is the [[fiber-bundles/chern-number|second Chern number]] of \(E\), so it is independent of \(A\). When \(A\) is a [[fiber-bundles/instanton|Yang–Mills instanton]], this integer labels its topological sector but is not additional connection data.

## Chern–Weil independence

The four-form
\[
-\frac{1}{8\pi^2}\operatorname{tr}(F_A\wedge F_A)
\]
represents \(c_2(E)\) because \(c_1(E)=0\) for an \(SU(r)\)-bundle. Replacing \(A\) by another connection changes this form by an exact [[fiber-bundles/transgression-form|transgression form]], whose integral over closed \(M\) vanishes. Thus the number depends on the bundle and orientation, not on the chosen representative connection.

For a general compact structure group, an “instanton number” requires choosing an invariant quadratic form normalized to represent an integral [[fiber-bundles/characteristic-class|characteristic class]]. The resulting charge need not use the displayed trace normalization.

## Energy and self-duality

In four dimensions, decompose \(F_A=F_A^++F_A^-\) using the Hodge star. The Chern–Weil integral is proportional to
\[
\|F_A^-\|_{L^2}^2-\|F_A^+\|_{L^2}^2
\]
with the present orientation and trace conventions. The Yang–Mills energy is the corresponding sum. Hence self-dual or [[fiber-bundles/self-dual-and-anti-self-dual-connection|anti-self-dual connections]] saturate a topological [[shared-foundations/lower-bound|lower bound]] proportional to \(|k(E)|\) [Donaldson–Kronheimer, §2.1].

Reversing the orientation interchanges self-duality and anti-self-duality and changes the sign of the integral, while leaving its [[real-analysis/absolute-value|absolute value]] unchanged.

## Related characteristic numbers

For a principal \(SU(2)\)-bundle \(P\), the adjoint real rank-three bundle satisfies
\[
p_1(\operatorname{ad}P)=-4c_2(E)
\]
under standard conventions. Thus “Pontryagin charge” may encode the same sector but with a sign or factor of four. It is not included as an alias because the normalization is not identical to the instanton number displayed here.

**Warning.** Authors vary the sign in the definition of \(k\), the choice of Hermitian versus skew-Hermitian curvature, and the normalization of the [[fiber-bundles/yangmills-functional|Yang–Mills functional]]. Any numerical energy identity must be read together with those conventions.

## References

1. Simon K. Donaldson and Peter B. Kronheimer, *The Geometry of Four-Manifolds*, Oxford University Press, 1990. [DOI record](https://doi.org/10.1093/oso/9780198535539.001.0001). Relevant: §2.1, characteristic number, curvature decomposition, and the instanton energy bound.
2. Daniel S. Freed and Karen K. Uhlenbeck, *Instantons and Four-Manifolds*, 2nd ed., Springer, 1991. [DOI record](https://doi.org/10.1007/978-1-4613-9703-8). Relevant: chapter 2, Chern–Weil normalization and topological charge.
