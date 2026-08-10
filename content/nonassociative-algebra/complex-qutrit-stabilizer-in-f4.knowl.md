+++
id = "nonassociative-algebra/complex-qutrit-stabilizer-in-f4"
title = "Complex-qutrit stabilizer in F4"
kind = "theorem"
summary = "The identity component of the F_4 stabilizer of an H_3(C) subalgebra is (SU(3) times SU(3))/Z_3."
aliases = ["H3(C) stabilizer in F4", "complex qutrit isotropy in F4", "SU(3) SU(3) subgroup of F4"]
domains = ["nonassociative-algebra", "lie-groups"]
section_mode = "progressive"
+++

Let \(J=H_3(\mathbb O)\), let \(F_4=\operatorname{Aut}(J)\), and let
\(B\subset J\) be a Jordan subalgebra isomorphic to \(H_3(\mathbb C)\). The
identity component of its setwise stabilizer is
\[
\operatorname{Stab}_{F_4}(B)^0
\cong\frac{\mathrm{SU}(3)\times\mathrm{SU}(3)}{\mu_3},
\]
where \(\mu_3=\{(\zeta I,\zeta I):\zeta^3=1\}\) is the diagonal central
subgroup. This is a connected closed subgroup of compact \(F_4\).

## The two factors

Using \(\mathbb O\cong\mathbb C\oplus\mathbb C^3\), one obtains a real
vector-space decomposition
\[
H_3(\mathbb O)\cong H_3(\mathbb C)\oplus M_3(\mathbb C).
\]
Representatives \((g,h)\in\mathrm{SU}(3)\times\mathrm{SU}(3)\) act by
\[
(X,M)\longmapsto(gXg^\dagger,hMg^\dagger).
\]
The first factor acts by unitary conjugation on the complex qutrit algebra;
the second fixes that algebra pointwise and acts on its orthogonal complement.
The diagonal \(\mu_3\) is precisely the kernel.

## Why the identity component matters

The full stabilizer \(\operatorname{Stab}_{F_4}(B)\) is disconnected. Besides
its unitary component, it has elements whose restriction to \(B\) is induced
by an antiunitary transformation. Consequently one must not replace
\(\operatorname{Stab}_{F_4}(B)^0\) by the full stabilizer in intersection
theorems without changing the resulting group.

## References

1. John C. Baez and Paul Schwahn, “The Standard Model Gauge Group from the Exceptional Jordan Algebra,” 2026, §3. [arXiv:2606.15235](https://arxiv.org/abs/2606.15235).
2. Ichirô Yokota, *Exceptional Lie Groups*, 2009, §2.12, Remark 2. [arXiv:0902.0431](https://arxiv.org/abs/0902.0431).
3. Ilka Agricola, Thomas Friedrich, and Jos Höll, “Sp(3) structures on 14-dimensional manifolds,” *Journal of Geometry and Physics* 69 (2013), 12–30, Appendix A. [Article](https://doi.org/10.1016/j.geomphys.2013.03.002).
