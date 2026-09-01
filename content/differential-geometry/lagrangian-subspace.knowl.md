+++
id = "differential-geometry/lagrangian-subspace"
title = "Lagrangian subspace"
kind = "definition"
summary = "A subspace equal to its symplectic orthogonal, equivalently a maximal isotropic subspace."
aliases = ["maximal isotropic subspace", "Lagrangian linear subspace"]
domains = ["differential-geometry", "linear-algebra"]
prerequisites = ["differential-geometry/symplectic-vector-space", "convex-analysis/linear-subspace", "differential-geometry/symplectic-orthogonal-complement", "differential-geometry/isotropic-subspace", "differential-geometry/coisotropic-subspace", "linear-algebra/inner-product"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \((V,\omega)\) be a finite-dimensional [[differential-geometry/symplectic-vector-space|symplectic vector space]]. A [[convex-analysis/linear-subspace|linear subspace]] \(L\subseteq V\) is **Lagrangian** if
\[
L=L^\omega,
\]
where \(L^\omega\) is its [[differential-geometry/symplectic-orthogonal-complement|symplectic orthogonal complement]]. Equivalently, if \(\dim V=2n\), then \(L\) is an [[differential-geometry/isotropic-subspace|isotropic subspace]] of dimension \(n\). Thus \(\omega\) vanishes on \(L\times L\), and \(L\) has the largest dimension permitted by that condition. A Lagrangian subspace is simultaneously isotropic and [[differential-geometry/coisotropic-subspace|coisotropic]].
No complementary subspace, basis, or [[linear-algebra/inner-product|inner product]] is included in the data.

## Equivalent characterizations

For a subspace \(L\subseteq V\), the following are equivalent:

- \(L=L^\omega\);
- \(L\) is isotropic and \(\dim L=\frac12\dim V\);
- \(L\) is maximal among isotropic subspaces under inclusion; and
- \(L\) is coisotropic and \(\dim L=\frac12\dim V\).

The finite-dimensional hypothesis matters: it supplies \(\dim L+\dim L^\omega=\dim V\), which turns the relevant inclusion and half-dimension condition into equality.

## Normal form and complements

Every Lagrangian subspace has a Lagrangian complement \(L'\) such that \(V=L\oplus L'\). Choosing dual bases \(e_1,\ldots,e_n\) of \(L\) and \(f_1,\ldots,f_n\) of \(L'\) with \(\omega(e_i,f_j)=\delta_{ij}\) produces a [[differential-geometry/symplectic-basis|symplectic basis]] of \(V\). The complement is generally not unique.

The [[lie-groups/symplectic-group|symplectic group]] acts transitively on the set of Lagrangian subspaces. After choosing one symplectic basis, every Lagrangian subspace is therefore equivalent to the span of \(e_1,\ldots,e_n\).

## Examples and near-misses

In \(\mathbb R^{2n}\) with \(\omega=\sum_i dq_i\wedge dp_i\), the \(q\)-coordinate subspace \(\{p=0\}\) and the \(p\)-coordinate subspace \(\{q=0\}\) are complementary Lagrangian subspaces. In \(T^*Q\) at a point, the [[fiber-bundles/vertical-tangent-space|vertical tangent space]] is the standard geometric example.

The line \(\operatorname{span}(e_1)\) in a symplectic vector space of dimension at least four is isotropic but not Lagrangian: it fails the half-dimension, maximality, and coisotropy conditions.

## Conventions and scope

This knowl uses finite-dimensional real symplectic linear algebra. Over any field of characteristic different from two, the same definition works for a nondegenerate alternating form. In infinite-dimensional symplectic spaces, maximal isotropic, self-orthogonal, and complemented formulations may diverge, so the ambient topology and chosen definition must be stated separately.

## References

1. Ana Cannas da Silva, *Lectures on Symplectic Geometry*, Lecture Notes in Mathematics 1764, Springer, 2001. [DOI record](https://doi.org/10.1007/978-3-540-45330-7). Relevant: Chapter 1 and Homework 1, isotropic, coisotropic, and Lagrangian subspaces.
2. Dusa McDuff and Dietmar Salamon, *Introduction to Symplectic Topology*, 3rd ed., Oxford University Press, 2017. [DOI record](https://doi.org/10.1093/oso/9780198794899.001.0001). Relevant: §2.3, Lagrangian subspaces.
