+++
id = "lie-groups/celestial-sphere-and-mobius-action"
title = "Celestial sphere and Möbius action"
kind = "theorem"
summary = "The proper Lorentz action on future null directions becomes the PSL(2,C) Möbius action on CP¹."
aliases = ["Lorentz action as Möbius transformations", "celestial Möbius action"]
domains = ["lie-groups", "complex-analysis", "mathematical-physics"]
section_mode = "progressive"
prerequisites = ["lie-groups/proper-orthochronous-lorentz-group", "differential-geometry/celestial-sphere"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Under the identifications
\[
SO^+(1,3)\cong PSL(2,\mathbb C)_{\mathbb R},
\qquad
\mathscr C\cong\mathbb{CP}^1,
\]
the action of the [[lie-groups/proper-orthochronous-lorentz-group|proper orthochronous Lorentz group]] on the [[differential-geometry/celestial-sphere|celestial sphere]] is the standard Möbius action. If
\[
A=\begin{pmatrix}a&b\\c&d\end{pmatrix},
\]
then in the affine coordinate \(\zeta=z_1/z_2\) the action is
\[
\zeta\longmapsto\frac{a\zeta+b}{c\zeta+d},
\]
with the usual interpretation at infinity.

## Derivation from spinors

A null ray is represented by \(zz^\dagger\), and \(A(zz^\dagger)A^\dagger=(Az)(Az)^\dagger\). Projectivizing therefore sends \([z]\) to \([Az]\). The central matrices \(\pm I\) act trivially, so the action factors precisely through \(PSL(2,\mathbb C)\).

The resulting transformations preserve the conformal structure of the round \(2\)-sphere, though not generally a chosen round metric. Orientation-reversing [[differential-geometry/conformal-map|conformal maps]] require complex conjugation and lie outside \(SO^+(1,3)\).

## References

1. Alan F. Beardon, *The Geometry of Discrete Groups*, Springer, 1983, Chapter 3. [Publisher record](https://doi.org/10.1007/978-1-4612-1146-4).
2. Roger Penrose and Wolfgang Rindler, *Spinors and Space-Time*, Vol. 1, Cambridge University Press, 1984, §1.3. [Publisher record](https://doi.org/10.1017/CBO9780511564048).
