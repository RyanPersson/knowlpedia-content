+++
id = "differential-geometry/dolbeault-operators"
title = "Dolbeault operators"
kind = "definition"
summary = "The two bidegree components of the exterior derivative on a complex manifold."
aliases = ["Dolbeault differentials", "partial and d-bar operators", "∂ and ∂̄"]
domains = ["differential-geometry"]
section_mode = "progressive"
+++

Let \(X\) be a [[differential-geometry/complex-manifold|complex manifold]]. For a [[differential-geometry/differential-form-of-type-pq|form of type \((p,q)\)]], the [[fiber-bundles/exterior-derivative|exterior derivative]] has only two type components. The **Dolbeault operators** are their projections:
\[
\partial:\Omega^{p,q}(X)\to\Omega^{p+1,q}(X),
\qquad
\bar\partial:\Omega^{p,q}(X)\to\Omega^{p,q+1}(X),
\qquad d=\partial+\bar\partial.
\]
They are complex-linear first-order differential operators. Since \(d^2=0\) and the three resulting bidegrees are distinct, they satisfy \(\partial^2=0\), \(\bar\partial^2=0\), and \(\partial\bar\partial+\bar\partial\partial=0\). Thus each operator is intrinsic to the complex structure and independent of the chosen holomorphic coordinates.

## Local formulas

In holomorphic coordinates \(z^1,\ldots,z^n\), for a smooth function \(f\),
\[
\partial f=\sum_j\frac{\partial f}{\partial z^j}\,dz^j,
\qquad
\bar\partial f=\sum_j\frac{\partial f}{\partial\bar z^j}\,d\bar z^j.
\]
The operators extend to forms by the graded Leibniz rule. A smooth complex-valued function is holomorphic exactly when \(\bar\partial f=0\).

## Dolbeault complexes

For fixed \(p\), the identity \(\bar\partial^2=0\) makes
\[
\Omega^{p,0}(X)\xrightarrow{\bar\partial}\Omega^{p,1}(X)
\xrightarrow{\bar\partial}\Omega^{p,2}(X)\longrightarrow\cdots
\]
a [[algebra-homological/cochain-complex|cochain complex]]. Its cohomology is [[differential-geometry/dolbeault-cohomology|Dolbeault cohomology]]. The analogous \(\partial\)-complex fixes \(q\), and complex conjugation interchanges the two operators.

## Integrability and scope

On an almost-complex manifold, \(d\) may have additional components of bidegrees \((2,-1)\) and \((-1,2)\). Their disappearance is equivalent to [[differential-geometry/integrable-almost-complex-structure|integrability]], so the two-term formula above uses the complex-manifold hypothesis [Wells, Chapter I, §3](https://doi.org/10.1007/978-0-387-73892-5).

## References

1. R. O. Wells Jr., *Differential Analysis on Complex Manifolds*, 3rd ed., Springer, 2008. [DOI record](https://doi.org/10.1007/978-0-387-73892-5). Relevant: Chapter I, §3, the operators \(\partial\) and \(\bar\partial\).
2. C. Voisin, *Hodge Theory and Complex Algebraic Geometry I*, Cambridge University Press, 2002. [DOI record](https://doi.org/10.1017/CBO9780511615344). Relevant: §2.1, bidegrees and Dolbeault complexes.
