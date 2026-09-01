+++
id = "differential-geometry/symplectic-subspace"
title = "Symplectic subspace"
kind = "definition"
summary = "A linear subspace on which the ambient symplectic form remains nondegenerate."
aliases = ["nondegenerate subspace"]
domains = ["differential-geometry", "linear-algebra"]
prerequisites = ["differential-geometry/symplectic-vector-space", "convex-analysis/linear-subspace", "differential-geometry/symplectic-orthogonal-complement"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \((V,\omega)\) be a finite-dimensional [[differential-geometry/symplectic-vector-space|symplectic vector space]]. A [[convex-analysis/linear-subspace|linear subspace]] \(W\subseteq V\) is a **symplectic subspace** if the restricted alternating form \(\omega|_{W\times W}\) is nondegenerate. Equivalently,
\[
W\cap W^\omega=\{0\},
\]
where \(W^\omega\) is the [[differential-geometry/symplectic-orthogonal-complement|symplectic orthogonal complement]]. With the restricted form, \(W\) is itself a symplectic vector space, so it has even dimension. The term describes nondegeneracy of the restriction; it does not mean merely that \(W\) lies inside a symplectic vector space.

## Orthogonal splitting

For a symplectic subspace \(W\), dimension counting and \(W\cap W^\omega=0\) give
\[
V=W\oplus W^\omega.
\]
The restriction of \(\omega\) to \(W^\omega\) is also nondegenerate. Thus a symplectic subspace always has a canonical complementary symplectic subspace determined by the ambient form.

## Equivalent tests

The following conditions are equivalent: the restricted form on \(W\) is nondegenerate; \(W\cap W^\omega=0\); and the map \(W\to W^*\), \(w\mapsto\omega(w,\mathord{-})|_W\), is an isomorphism. In a [[differential-geometry/symplectic-basis|symplectic basis]] for \(V\), the span of any collection of complete pairs \(e_i,f_i\) is symplectic.

## Contrasts

A nonzero [[differential-geometry/isotropic-subspace|isotropic subspace]] cannot be symplectic, since its restricted form is zero. A [[differential-geometry/coisotropic-subspace|coisotropic subspace]] instead satisfies \(W^\omega\subseteq W\) and may have a nontrivial kernel for its restricted form. The zero subspace is symplectic under the usual vacuous nondegeneracy convention.

## References

1. Ana Cannas da Silva, *Lectures on Symplectic Geometry*, Lecture Notes in Mathematics 1764, Springer, 2001. [DOI record](https://doi.org/10.1007/978-3-540-45330-7). Relevant: §1.1, symplectic orthogonals and subspaces.
2. Dusa McDuff and Dietmar Salamon, *Introduction to Symplectic Topology*, 3rd ed., Oxford University Press, 2017. [DOI record](https://doi.org/10.1093/oso/9780198794899.001.0001). Relevant: Chapter 2, linear symplectic geometry.
