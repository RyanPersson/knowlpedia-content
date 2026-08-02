+++
id = "lie-groups/sl2c-spin-cover-of-lorentz-group"
title = "SL(2,C) spin cover of the Lorentz group"
kind = "theorem"
summary = "The Hermitian-matrix action gives a two-to-one covering SL(2,C)→SO⁺(1,3)."
aliases = ["spin covering of SO+(1,3)", "SL2C Lorentz double cover"]
domains = ["lie-groups", "mathematical-physics"]
section_mode = "progressive"
+++

Under the [[lie-groups/hermitian-matrix-model-of-minkowski-space|Hermitian matrix model]], the action
\[
X\longmapsto AXA^\dagger
\]
defines a surjective real [[lie-groups/lie-group-homomorphism|Lie group homomorphism]]
\[
\rho:SL(2,\mathbb C)_{\mathbb R}\longrightarrow SO^+(1,3)
\]
whose kernel is \(\{\pm I\}\). Hence \(\rho\) is a two-sheeted covering and realizes
\[
SL(2,\mathbb C)_{\mathbb R}\cong\operatorname{Spin}^+(1,3).
\]

## Kernel, image, and differential

If \(AXA^\dagger=X\) for every Hermitian \(X\), then \(A\) commutes with the resulting full matrix algebra and is scalar; determinant one leaves \(A=\pm I\). The image lies in the identity component because \(SL(2,\mathbb C)\) is connected. Its differential is an injective map between real [[lie-groups/lie-algebra|Lie algebras]] of dimension \(6\), so the image is open; connectedness and the standard structure of \(SO^+(1,3)\) give surjectivity.

Differentiating yields the real [[lie-groups/lie-algebra-isomorphism|Lie algebra isomorphism]]
\[
\mathfrak{sl}_2(\mathbb C)_{\mathbb R}
\xrightarrow{\;\sim\;}
\mathfrak{so}(1,3),
\qquad
X\longmapsto\bigl(H\mapsto XH+HX^\dagger\bigr).
\]
This is not an isomorphism of complex Lie algebras because \(\mathfrak{so}(1,3)\) is here a real Lie algebra.

## References

1. Roger Penrose and Wolfgang Rindler, *Spinors and Space-Time*, Vol. 1, Cambridge University Press, 1984, §§1.2–1.3. [Publisher record](https://doi.org/10.1017/CBO9780511564048).
2. H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry*, Princeton University Press, 1989, Chapter II, §5. [Publisher record](https://doi.org/10.1515/9781400883912).
