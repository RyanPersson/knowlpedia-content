+++
id = "differential-geometry/linear-coisotropic-reduction"
title = "Linear coisotropic reduction"
kind = "construction"
summary = "The symplectic quotient of a coisotropic subspace by its characteristic subspace."
aliases = ["symplectic reduction of a vector space", "coisotropic quotient"]
domains = ["differential-geometry", "linear-algebra"]
prerequisites = ["differential-geometry/symplectic-vector-space", "differential-geometry/coisotropic-subspace", "convex-analysis/quotient-vector-space-codimension", "differential-geometry/symplectic-orthogonal-complement"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \((V,\omega)\) be a [[differential-geometry/symplectic-vector-space|symplectic vector space]] and \(W\subseteq V\) a [[differential-geometry/coisotropic-subspace|coisotropic subspace]]. Its **linear coisotropic reduction** is the [[convex-analysis/quotient-vector-space-codimension|quotient vector space]]
\[
W_{\mathrm{red}}=W/W^\omega
\]
equipped with
\[
\omega_{\mathrm{red}}([u],[v])=\omega(u,v),
\]
where \(W^\omega\) is the [[differential-geometry/symplectic-orthogonal-complement|symplectic orthogonal complement]] of \(W\). This formula is independent of representatives because every element of \(W^\omega\) pairs trivially with \(W\). Its kernel is zero, so \(\omega_{\mathrm{red}}\) is nondegenerate. Hence \((W_{\mathrm{red}},\omega_{\mathrm{red}})\) is again a symplectic vector space.
No complement to \(W^\omega\) is chosen, so the construction is canonical from \(W\subseteq V\) and \(\omega\).

## Why the quotient is symplectic

The restriction \(\omega|_W\) is generally degenerate, and its kernel is exactly \(W\cap W^\omega\). Coisotropy gives \(W^\omega\subseteq W\), so this kernel is \(W^\omega\). Passing to \(W/W^\omega\) removes precisely the null directions and no others. Alternation and bilinearity descend immediately, while the kernel calculation proves nondegeneracy.

If \(\dim V=2n\) and \(\operatorname{codim}W=k\), then \(\dim W^\omega=k\) and
\[
\dim W_{\mathrm{red}}=2n-2k.
\]
The reduced dimension is therefore even, as required.

## Examples and boundary cases

For \(W=V\), one has \(W^\omega=\{0\}\), so the reduction is \(V\) itself. If \(W\) is [[differential-geometry/lagrangian-subspace|Lagrangian]], then \(W=W^\omega\), and its reduction is the zero symplectic vector space.

In standard \(\mathbb R^{2n}\) with coordinates \((q_i,p_i)\), let \(W\) be defined by \(p_1=\cdots=p_k=0\). Then \(W^\omega\) is spanned by \(\partial/\partial q_1,\ldots,\partial/\partial q_k\), and the quotient retains the coordinate pairs \((q_{k+1},p_{k+1}),\ldots,(q_n,p_n)\).

## Relation to manifold reduction

For a [[differential-geometry/coisotropic-submanifold|coisotropic submanifold]], the corresponding null spaces form the characteristic distribution. When that distribution integrates to a sufficiently regular foliation with a smooth leaf space, the quotient inherits a symplectic form by the same descent argument. The linear construction is the tangent-space model, but it avoids the global regularity and Hausdorffness issues of a manifold quotient.

## References

1. Ana Cannas da Silva, *Lectures on Symplectic Geometry*, Lecture Notes in Mathematics 1764, Springer, 2001. [DOI record](https://doi.org/10.1007/978-3-540-45330-7). Relevant: Chapter 1 and Homework 1 for symplectic orthogonals; Chapters 23–24 for manifold reduction.
2. Victor Guillemin and Shlomo Sternberg, *Symplectic Techniques in Physics*, Cambridge University Press, 1984. [DOI record](https://doi.org/10.1017/CBO9780511624112). Relevant: Chapter 1, linear symplectic reduction.
