+++
id = "differential-geometry/symplectic-orthogonal-complement"
title = "Symplectic orthogonal complement"
kind = "definition"
summary = "The subspace of vectors symplectically orthogonal to every vector in a specified subspace."
aliases = ["symplectic orthogonal", "skew-orthogonal complement", "symplectic complement"]
domains = ["differential-geometry", "linear-algebra"]
section_mode = "progressive"
+++

Let \((V,\omega)\) be a [[differential-geometry/symplectic-vector-space|symplectic vector space]] and let \(W\subseteq V\) be a [[convex-analysis/linear-subspace|linear subspace]]. The **symplectic orthogonal complement** of \(W\) is
\[
W^\omega=\{v\in V:\omega(v,w)=0\text{ for every }w\in W\}.
\]
It is a linear subspace determined by both \(W\) and the symplectic form. Because \(\omega\) is nondegenerate and \(V\) is finite-dimensional,
\[
\dim W+\dim W^\omega=\dim V
\qquad\text{and}\qquad
(W^\omega)^\omega=W.
\]
Unlike the [[linear-algebra/orthogonal-complement|orthogonal complement]] for an [[linear-algebra/inner-product|inner product]], \(W\) and \(W^\omega\) need not meet trivially and need not form a direct sum.

## Algebraic properties

The operation reverses inclusions: if \(A\subseteq B\), then \(B^\omega\subseteq A^\omega\). It also exchanges sums and intersections:
\[
(A+B)^\omega=A^\omega\cap B^\omega,
\qquad
(A\cap B)^\omega=A^\omega+B^\omega.
\]
The second equality uses finite dimensionality; the first follows directly from the defining vanishing conditions.

## Classification of subspaces

The relative position of \(W\) and \(W^\omega\) determines the standard classes of symplectic linear subspaces. The subspace is isotropic when \(W\subseteq W^\omega\), coisotropic when \(W^\omega\subseteq W\), and Lagrangian when \(W=W^\omega\). The restriction \(\omega|_W\) is nondegenerate exactly when \(W\cap W^\omega=\{0\}\).

## Examples

In \(\mathbb R^{2n}\) with coordinates \((q_1,\ldots,q_n,p_1,\ldots,p_n)\) and standard symplectic form, the span of the \(q_i\) is its own symplectic orthogonal and is therefore Lagrangian. The symplectic orthogonal of \(V\) is \(\{0\}\), and that of \(\{0\}\) is \(V\).

## Conventions and scope

The notation \(W^\omega\) records the dependence on the form and is preferable when several [[linear-algebra/bilinear-form|bilinear forms]] are present. Some authors write \(W^\perp\), \(W^{\perp_\omega}\), or “skew orthogonal.” In infinite-dimensional spaces, dimension formulas and the double-complement identity can fail without topological closure or additional nondegeneracy hypotheses. See [Cannas da Silva, §1.1].

## References

1. Ana Cannas da Silva, *Lectures on Symplectic Geometry*, Lecture Notes in Mathematics 1764, Springer, 2001. [DOI record](https://doi.org/10.1007/978-3-540-45330-7). Relevant: §1.1, symplectic vector spaces and orthogonal complements.
2. Dusa McDuff and Dietmar Salamon, *Introduction to Symplectic Topology*, 3rd ed., Oxford University Press, 2017. [DOI record](https://doi.org/10.1093/oso/9780198794899.001.0001). Relevant: linear symplectic geometry and subspaces.
