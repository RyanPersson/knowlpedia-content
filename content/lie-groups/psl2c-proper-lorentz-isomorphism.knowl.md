+++
id = "lie-groups/psl2c-proper-lorentz-isomorphism"
title = "PSL(2,C)–proper Lorentz isomorphism"
kind = "theorem"
summary = "Quotienting the SL(2,C) spin cover gives PSL(2,C)ℝ≅SO⁺(1,3) as real Lie groups."
aliases = ["PSL2C isomorphism with SO+(1,3)", "projective spin-Lorentz isomorphism"]
domains = ["lie-groups", "mathematical-physics"]
section_mode = "progressive"
prerequisites = ["lie-groups/sl2c-spin-cover-of-lorentz-group", "lie-groups/psl2-complex", "lie-groups/proper-orthochronous-lorentz-group", "linear-algebra/matrix"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

The spin covering descends to an isomorphism
\[
\boxed{\;
PSL(2,\mathbb C)_{\mathbb R}
\xrightarrow{\;\sim\;}
SO^+(1,3)
\;}
\]
in the category of real Lie groups. Explicitly, a class \([A]\) acts on Hermitian \(2\times2\) matrices by \(X\mapsto AXA^\dagger\).

## Why the qualifiers matter

The map \(SL(2,\mathbb C)\to SO^+(1,3)\) itself is not an isomorphism: it has kernel \(\{\pm I\}\). Quotienting by this kernel gives [[lie-groups/psl2-complex|\(PSL(2,\mathbb C)\)]]. The subscript \(\mathbb R\) records that its [[differential-geometry/complex-manifold|complex manifold]] structure has been forgotten; \(SO^+(1,3)\) is not a [[lie-groups/complex-lie-group|complex Lie group]] in this statement.

The target is also only the identity component of \(O(1,3)\). Spatial parity and time reversal lie in other components and are not represented by \(PSL(2,\mathbb C)\).

## Compatible boundary action

Projectivizing the future null cone identifies the [[differential-geometry/celestial-sphere|celestial sphere]] with \(\mathbb{CP}^1\). Under that identification, this Lorentz action becomes the Möbius action of \(PSL(2,\mathbb C)\).

## References

1. Roger Penrose and Wolfgang Rindler, *Spinors and Space-Time*, Vol. 1, Cambridge University Press, 1984, §§1.2–1.3. [Publisher record](https://doi.org/10.1017/CBO9780511564048).
2. Gregory L. Naber, *The Geometry of Minkowski Spacetime*, 2nd ed., Springer, 2012, Chapter 2. [Publisher record](https://doi.org/10.1007/978-1-4419-7838-7).
