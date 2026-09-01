+++
id = "differential-geometry/isotropic-subspace"
title = "Isotropic subspace"
kind = "definition"
summary = "A linear subspace on which the ambient symplectic form vanishes identically."
aliases = ["totally isotropic subspace", "isotropic linear subspace"]
domains = ["differential-geometry", "linear-algebra"]
prerequisites = ["differential-geometry/symplectic-vector-space", "convex-analysis/linear-subspace", "differential-geometry/symplectic-orthogonal-complement"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \((V,\omega)\) be a finite-dimensional [[differential-geometry/symplectic-vector-space|symplectic vector space]], and let \(W\subseteq V\) be a [[convex-analysis/linear-subspace|linear subspace]]. The subspace \(W\) is **isotropic** if
\[
\omega|_{W\times W}=0.
\]
Equivalently, every vector in \(W\) is symplectically orthogonal to every other vector in \(W\), or
\[
W\subseteq W^\omega,
\]
where \(W^\omega\) is the [[differential-geometry/symplectic-orthogonal-complement|symplectic orthogonal complement]]. Isotropy is a condition on the whole subspace, not merely the automatic identities \(\omega(w,w)=0\) for individual vectors.

## Dimension bound

If \(\dim V=2n\), then
\[
\dim W+\dim W^\omega=2n.
\]
The inclusion \(W\subseteq W^\omega\) therefore implies \(\dim W\leq n\). An isotropic subspace of the maximal possible dimension \(n\) satisfies \(W=W^\omega\) and is called Lagrangian.

## Examples and contrasts

Every one-dimensional subspace is isotropic because an alternating form vanishes on pairs of proportional vectors. In a [[differential-geometry/symplectic-basis|symplectic basis]], \(\operatorname{span}(e_1,\ldots,e_k)\) is isotropic for \(k\leq n\). By contrast, \(\operatorname{span}(e_1,f_1)\) is a [[differential-geometry/symplectic-subspace|symplectic subspace]], not an isotropic one.

## Quotients and geometry

The restriction of \(\omega\) to \(W^\omega\) has kernel \(W\) when \(W\) is isotropic. Hence it descends to a nondegenerate alternating form on \(W^\omega/W\). Pointwise isotropic [[differential-geometry/tangent-space|tangent spaces]] similarly define [[differential-geometry/isotropic-submanifold|isotropic submanifolds]]; the present knowl concerns the underlying linear notion.

## References

1. Dusa McDuff and Dietmar Salamon, *Introduction to Symplectic Topology*, 3rd ed., Oxford University Press, 2017. [DOI record](https://doi.org/10.1093/oso/9780198794899.001.0001). Relevant: Chapter 2, isotropic, coisotropic, and Lagrangian subspaces.
2. Maurice A. de Gosson, *Symplectic Geometry and Quantum Mechanics*, Birkhäuser, 2006. [DOI record](https://doi.org/10.1007/3-7643-7575-2). Relevant: Chapter 1, symplectic spaces and Lagrangian planes.
