+++
id = "differential-geometry/symplectic-linear-map"
title = "Symplectic linear map"
kind = "definition"
summary = "A linear map that pulls the target symplectic form back to the source symplectic form."
aliases = ["linear symplectic map"]
domains = ["differential-geometry", "linear-algebra"]
section_mode = "progressive"
+++

Let \((V,\omega_V)\) and \((W,\omega_W)\) be finite-dimensional [[differential-geometry/symplectic-vector-space|symplectic vector spaces]]. A **symplectic linear map** is a [[linear-algebra/linear-map|linear map]] \(T:V\to W\) satisfying
\[
T^*\omega_W=\omega_V,
\]
or equivalently
\[
\omega_W(Tv,Tv')=\omega_V(v,v')
\quad\text{for all }v,v'\in V.
\]
Bijectivity is not part of the definition. Nevertheless, nondegeneracy of \(\omega_V\) forces \(T\) to be injective: if \(Tv=0\), then \(\omega_V(v,v')=0\) for every \(v'\), hence \(v=0\).
Thus \(T\) identifies \(V\) with a symplectic subspace of \(W\).

## Functorial properties

Identity maps are symplectic linear, and composites of symplectic linear maps are symplectic linear because pullbacks compose. The image \(T(V)\) carries the restricted form nondegenerately, and \(T:V\to T(V)\) is a [[differential-geometry/linear-symplectomorphism|linear symplectomorphism]]. If \(\dim V=\dim W\), injectivity makes \(T\) bijective.

## Matrix criterion

Choose bases in which the two forms have matrices \(J_V\) and \(J_W\), and let \(A\) represent \(T\). The defining equation becomes
\[
A^{\mathsf T}J_WA=J_V.
\]
For the standard spaces \(\mathbb R^{2m}\to\mathbb R^{2n}\), this criterion shows directly that \(m\leq n\). When \(m=n\), its solutions are the matrices in the real [[lie-groups/symplectic-group|symplectic group]].

## Examples and scope

The inclusion of a [[differential-geometry/symplectic-subspace|symplectic subspace]] with its restricted form is symplectic linear. A scalar multiple \(cI\) on a nonzero real symplectic vector space is symplectic precisely when \(c^2=1\). This linear notion is the tangent-space model for a [[differential-geometry/symplectic-map|symplectic map]] between [[differential-geometry/symplectic-manifold|symplectic manifolds]].

## References

1. Ana Cannas da Silva, *Lectures on Symplectic Geometry*, Lecture Notes in Mathematics 1764, Springer, 2001. [DOI record](https://doi.org/10.1007/978-3-540-45330-7). Relevant: §1.1, symplectic linear maps and matrices.
2. Maurice A. de Gosson, *Symplectic Geometry and Quantum Mechanics*, Birkhäuser, 2006. [DOI record](https://doi.org/10.1007/3-7643-7575-2). Relevant: Chapter 1, symplectic spaces and the symplectic group.
