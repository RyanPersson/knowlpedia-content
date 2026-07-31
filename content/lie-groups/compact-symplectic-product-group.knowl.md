+++
id = "lie-groups/compact-symplectic-product-group"
title = "The group Sp(n)Sp(1)"
kind = "definition"
summary = "The central quotient of the product of two compact symplectic groups acting on quaternionic Euclidean space."
aliases = ["Sp(n) dot Sp(1)", "Sp(n)·Sp(1)"]
domains = ["lie-groups", "differential-geometry"]
section_mode = "progressive"
+++

For \(n\geq1\), let the [[lie-groups/compact-symplectic-group|compact symplectic group]] \(\operatorname{Sp}(n)\) act on \(\mathbb H^n\) from the left and let its unit-quaternion subgroup \(\operatorname{Sp}(1)\) act from the right. The homomorphism
\[
\operatorname{Sp}(n)\times\operatorname{Sp}(1)\longrightarrow\operatorname{SO}(4n),
\qquad
(A,q)\longmapsto\bigl(v\mapsto Avq^{-1}\bigr)
\]
has kernel \(\{(I,1),(-I,-1)\}\). Its image is the **group \(\operatorname{Sp}(n)\operatorname{Sp}(1)\)**. Hence
\[
\operatorname{Sp}(n)\operatorname{Sp}(1)
\cong
\bigl(\operatorname{Sp}(n)\times\operatorname{Sp}(1)\bigr)/\{\pm(I,1)\}.
\]
It is a compact connected [[lie-groups/lie-subgroup|Lie subgroup]] of \(\operatorname{SO}(4n)\), not the direct product denoted by simply placing the two factors side by side.

## Action on quaternionic structures

The left \(\operatorname{Sp}(n)\)-factor commutes with right quaternionic multiplication. The right \(\operatorname{Sp}(1)\)-factor conjugates the three-dimensional space \(\operatorname{Im}\mathbb H\) of imaginary units, inducing the standard rotation action through \(\operatorname{Sp}(1)/\{\pm1\}\cong\operatorname{SO}(3)\). Thus the quotient preserves the rank-three family of complex structures while generally rotating its local basis \(I,J,K\). This is why the group, rather than \(\operatorname{Sp}(n)\) alone, is natural in quaternionic Kähler geometry [Besse, §14.G].

## Low-rank case and dimensions

Its [[lie-groups/lie-algebra|Lie algebra]] is \(\mathfrak{sp}(n)\oplus\mathfrak{sp}(1)\), because quotienting by a finite central subgroup does not change the Lie algebra. Therefore
\[
\dim\operatorname{Sp}(n)\operatorname{Sp}(1)=n(2n+1)+3.
\]
For \(n=1\), the action identifies \(\operatorname{Sp}(1)\operatorname{Sp}(1)\) with \(\operatorname{SO}(4)\). In quaternionic Kähler geometry the holonomy condition is normally stated for \(n\geq2\); real dimension four is treated separately.

## Relation to geometric structures

A Riemannian \(4n\)-manifold whose frame bundle reduces to this subgroup has an almost quaternionic Hermitian structure. If its Levi–Civita [[fiber-bundles/holonomy-group|holonomy group]] lies in \(\operatorname{Sp}(n)\operatorname{Sp}(1)\), it is quaternionic Kähler under the standard higher-dimensional convention. By contrast, holonomy contained in the smaller subgroup \(\operatorname{Sp}(n)\) is the hyperkähler condition. The two conditions should not be conflated [Salamon, pp. 143–145].

## Conventions and scope

Authors variously print the middle operation as adjacency, a centered dot, or an explicit quotient. None of these denotes a direct product in this context. The expression \(\{\pm(I,1)\}\) abbreviates the two diagonal central elements \((I,1)\) and \((-I,-1)\), not four independently chosen signs.

## References

1. Arthur L. Besse, *Einstein Manifolds*, Springer, 1987. [DOI record](https://doi.org/10.1007/978-3-540-74311-8). Relevant: §14.G on quaternionic Kähler manifolds and their holonomy group.
2. Simon Salamon, “Quaternionic Kähler Manifolds,” *Inventiones Mathematicae* 67 (1982), 143–171. [DOI record](https://doi.org/10.1007/BF01393378). Relevant: pp. 143–145 on the groups \(\operatorname{Sp}(n)\operatorname{Sp}(1)\) and \(\operatorname{GL}(n,\mathbb H)\operatorname{Sp}(1)\).
