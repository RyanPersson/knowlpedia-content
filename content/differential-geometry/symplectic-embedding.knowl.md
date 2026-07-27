+++
id = "differential-geometry/symplectic-embedding"
title = "Symplectic embedding"
kind = "definition"
summary = "A smooth embedding that preserves the symplectic forms by pullback."
aliases = ["symplectic inclusion"]
domains = ["differential-geometry"]
section_mode = "progressive"
+++

Let \((M,\omega_M)\) and \((N,\omega_N)\) be [[differential-geometry/symplectic-manifold|symplectic manifolds]]. A **symplectic embedding** is a [[fiber-bundles/smooth-embedding|smooth embedding]] \(\iota:M\hookrightarrow N\) satisfying
\[
\iota^*\omega_N=\omega_M.
\]
Equivalently, it is a [[differential-geometry/symplectic-map|symplectic map]] that is an embedding. Thus the differential \(d\iota_x\) identifies each [[fiber-bundles/tangent-space-at-a-point|tangent space]] \(T_xM\) with a symplectic linear subspace of \(T_{\iota(x)}N\), while the embedding condition also controls the topology of the image. The definition permits positive codimension but forces \(\dim M\leq\dim N\).

## Basic properties

The composite of symplectic embeddings is a symplectic embedding. If the source and target have equal dimension, a symplectic embedding is a [[differential-geometry/symplectomorphism|symplectomorphism]] onto an open subset of the target. Restricting the target form to the image recovers the source form exactly; preservation merely up to a nonzero scalar is not enough.

## Examples and non-examples

The standard inclusion \(\mathbb R^{2k}\hookrightarrow\mathbb R^{2n}\), with coordinates paired in the same order and the standard forms, is symplectic. The inclusion of a [[differential-geometry/symplectic-submanifold|symplectic submanifold]] equipped with the restricted form is another example. An embedding whose tangent images are [[differential-geometry/isotropic-subspace|isotropic subspaces]] cannot be symplectic in positive dimension, because the pulled-back form then vanishes.

## Role in symplectic geometry

Existence of a symplectic embedding is more rigid than existence of a smooth embedding. Symplectic capacities and Gromov's non-squeezing theorem supply obstructions invisible to dimension and topology; see [McDuff and Salamon, Chapter 12](https://doi.org/10.1093/oso/9780198794899.001.0001).

## References

1. Dusa McDuff and Dietmar Salamon, *Introduction to Symplectic Topology*, 3rd ed., Oxford University Press, 2017. [Publisher record](https://doi.org/10.1093/oso/9780198794899.001.0001). Relevant: Chapters 1 and 12, symplectic embeddings and embedding obstructions.
2. Ana Cannas da Silva, *Lectures on Symplectic Geometry*, Lecture Notes in Mathematics 1764, Springer, 2001. [DOI record](https://doi.org/10.1007/978-3-540-45330-7). Relevant: §1.1, symplectic maps and submanifolds.
