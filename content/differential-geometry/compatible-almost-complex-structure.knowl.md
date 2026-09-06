+++
id = "differential-geometry/compatible-almost-complex-structure"
title = "Compatible almost-complex structure"
kind = "definition"
summary = "An almost-complex structure that preserves a symplectic form and makes its associated bilinear form positive definite."
aliases = ["symplectic-compatible almost-complex structure", "omega-compatible almost-complex structure"]
domains = ["differential-geometry"]
prerequisites = ["differential-geometry/symplectic-manifold", "differential-geometry/almost-complex-structure"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \((M,\omega)\) be a [[differential-geometry/symplectic-manifold|symplectic manifold]]. A [[differential-geometry/almost-complex-structure|almost-complex structure]] \(J\) on \(M\) is **compatible with \(\omega\)** if
\[
\omega(Jv,Jw)=\omega(v,w)
\]
for all tangent vectors \(v,w\) based at the same point, and
\[
g_J(v,w)=\omega(v,Jw)
\]
is positive definite. The first condition makes \(g_J\) symmetric, so \(g_J\) is a Riemannian metric. Compatibility is a pointwise condition varying smoothly with the base point; it is stronger than merely requiring \(\omega(v,Jv)>0\), which defines a tamed almost-complex structure.

## Equivalent linear-algebra formulation

At each \(p\in M\), compatibility says that \(J_p\) is a complex structure on the [[differential-geometry/symplectic-vector-space|symplectic vector space]] \((T_pM,\omega_p)\), that \(J_p\) is symplectic, and that \(\omega_p(\,\cdot\,,J_p\,\cdot\,)\) is an [[linear-algebra/inner-product|inner product]]. Equivalently, the three tensors satisfy
\[
\omega(v,w)=g_J(Jv,w),\qquad g_J(Jv,Jw)=g_J(v,w).
\]

## Existence and deformation

Every symplectic [[fiber-bundles/vector-bundle|vector bundle]] admits compatible complex structures. Consequently every symplectic manifold has compatible almost-complex structures, and the space of all such structures is nonempty and contractible. This flexibility is central to constructions whose final invariant should not depend on the auxiliary choice of \(J\).

## Relation to complex and Kähler geometry

Compatibility does not imply that \(J\) comes from holomorphic coordinates. When \(J\) is additionally [[differential-geometry/integrable-almost-complex-structure|integrable]], the triple \((M,\omega,J)\), with metric \(g_J\), is a [[differential-geometry/kahler-manifold|Kähler manifold]]. Thus compatibility supplies the metric bridge between symplectic and complex geometry, while integrability is a separate differential condition.

## References

1. D. McDuff and D. Salamon, *J-Holomorphic Curves and Symplectic Topology*, 2nd ed., American Mathematical Society, 2012. [AMS DOI record](https://doi.org/10.1090/coll/052). Relevant: §2.5.
2. A. Cannas da Silva, *Lectures on Symplectic Geometry*, Springer, 2001. [Springer DOI record](https://doi.org/10.1007/978-3-540-45330-7). Relevant: compatible complex structures on symplectic vector spaces and bundles.
