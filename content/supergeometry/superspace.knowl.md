+++
id = "supergeometry/superspace"
title = "Superspace"
kind = "definition"
summary = "A locally superringed space, the ambient geometric object from which supermanifolds are selected by a local model condition."
aliases = ["locally superringed space", "super ringed space"]
domains = ["supergeometry"]
section_mode = "progressive"
+++

In smooth real supergeometry, a **superspace** is a pair
\[
(|X|,\mathcal O_X)
\]
consisting of a topological space \(|X|\) and a sheaf
\(\mathcal O_X=\mathcal O_{X,\bar 0}\oplus\mathcal O_{X,\bar 1}\) of
[[supergeometry/supercommutative-algebra|supercommutative real
superalgebras]] whose stalks are local superalgebras. Thus each stalk has a
unique maximal homogeneous ideal, and its residue field is \(\mathbb R\).

A morphism \(f:X\to Y\) is a continuous map
\(|f|:|X|\to |Y|\) together with a parity-preserving local morphism of
sheaves
\[
f^\sharp:\mathcal O_Y\longrightarrow |f|_*\mathcal O_X.
\]
The direction of \(f^\sharp\) is contravariant: functions on the target pull
back to functions on the source.

## Scope of the term

This is the locally superringed-space usage. A
[[supergeometry/supermanifold|supermanifold]] is a superspace satisfying a
finite-dimensional local model condition. In physics, “superspace” often
means an affine supermanifold carrying a supersymmetry action, and especially
[[supergeometry/super-minkowski-space|super-Minkowski space]]. That narrower
usage should not be substituted for the general definition.

Complex-analytic, algebraic, DeWitt, and Rogers superspaces have related but
different structure sheaves or test categories. They are not silently
identified with the smooth real Berezin–Leites/Kostant model used here.

## References

1. V. S. Varadarajan, *Supersymmetry for Mathematicians: An Introduction*, Courant Lecture Notes 11, American Mathematical Society, 2004. [Publisher record](https://doi.org/10.1090/cln/011). Relevant: Chapters 3–4.
2. C. Carmeli, L. Caston, and R. Fioresi, *Mathematical Foundations of Supersymmetry*, EMS, 2011. [Publisher record](https://doi.org/10.4171/097). Relevant: Chapters 3–4.
