+++
id = "differential-geometry/symplectic-vector-space"
title = "Symplectic vector space"
kind = "definition"
summary = "A finite-dimensional real vector space equipped with a nondegenerate alternating bilinear form."
aliases = ["linear symplectic space"]
domains = ["differential-geometry", "linear-algebra"]
section_mode = "progressive"
+++

A **symplectic vector space** is a pair \((V,\omega)\) consisting of a finite-dimensional real [[linear-algebra/vector-space|vector space]] \(V\) and a [[linear-algebra/bilinear-form|bilinear form]] \(\omega:V\times V\to\mathbb R\) such that:

1. \(\omega(v,v)=0\) for every \(v\in V\), so \(\omega\) is alternating; and
2. if \(\omega(v,w)=0\) for every \(w\in V\), then \(v=0\), so \(\omega\) is nondegenerate.

Equivalently, the [[linear-algebra/linear-map|linear map]] \(V\to V^*\), \(v\mapsto\omega(v,\mathord{-})\), is an isomorphism. No [[linear-algebra/inner-product|inner product]], complex structure, or preferred basis is part of the data.

## Normal form and dimension

Every symplectic vector space has even dimension \(2n\) and admits a basis \(e_1,\ldots,e_n,f_1,\ldots,f_n\) with
\[
\omega(e_i,e_j)=\omega(f_i,f_j)=0,\qquad \omega(e_i,f_j)=\delta_{ij}.
\]
Consequently, all real symplectic vector spaces of a fixed finite dimension are symplectically isomorphic.

## Subspaces

For a subspace \(W\subseteq V\), its [[differential-geometry/symplectic-orthogonal-complement|symplectic orthogonal]] is
\[
W^\omega=\{v\in V:\omega(v,w)=0\text{ for every }w\in W\}.
\]
The relations \(W\subseteq W^\omega\), \(W^\omega\subseteq W\), and \(W=W^\omega\) define isotropic, coisotropic, and [[differential-geometry/lagrangian-subspace|Lagrangian subspaces]], respectively. A Lagrangian subspace has dimension \(n\).

## Conventions and scope

**Warning.** This knowl adopts the finite-dimensional real convention used in symplectic geometry. Algebraic treatments may work over any field of characteristic different from two. Infinite-dimensional symplectic [[functional-analysis/topological-vector-space|topological vector spaces]] require additional continuity and nondegeneracy choices and are not covered by this definition.

## References

1. Ana Cannas da Silva, *Lectures on Symplectic Geometry*, Lecture Notes in Mathematics 1764, Springer, 2001. [DOI record](https://doi.org/10.1007/978-3-540-45330-7). Relevant: §1.1, symplectic vector spaces, normal forms, and subspaces.
2. Victor Guillemin and Shlomo Sternberg, *Symplectic Techniques in Physics*, Cambridge University Press, 1984. [Publisher record](https://doi.org/10.1017/CBO9780511624112). Relevant: Chapter 1, linear symplectic geometry.
