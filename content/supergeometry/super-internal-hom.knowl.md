+++
id = "supergeometry/super-internal-hom"
title = "Super internal Hom"
kind = "definition"
summary = "The super vector space whose even and odd parts are the parity-preserving and parity-reversing linear maps."
aliases = ["graded internal Hom", "internal Hom of super vector spaces"]
domains = ["supergeometry", "algebra-category-theory"]
section_mode = "progressive"
+++

For [[supergeometry/super-vector-space|super vector spaces]] \(V\) and \(W\),
their **super internal Hom** is the super vector space defined by
\[
\underline{\operatorname{Hom}}(V,W)_{\bar\epsilon}
=
\left\{
f:V\to W:
f(V_{\bar i})\subseteq W_{\bar i+\bar\epsilon}
\right\}.
\]
Its even part consists of parity-preserving maps and is the morphism space
\(\operatorname{Hom}_{\mathbf{SuperVect}}(V,W)\). Its odd part consists of
parity-reversing maps.

Evaluation is an even map
\[
\underline{\operatorname{Hom}}(V,W)\otimes V\longrightarrow W,
\qquad f\otimes v\longmapsto f(v).
\]
Together with the [[supergeometry/koszul-sign-rule|Koszul sign rule]], this
object makes the category of super vector spaces closed symmetric monoidal.
The [[supergeometry/parity-shift|parity shift]] identifies odd maps
\(V\to W\) with even maps \(V\to\Pi W\), up to the chosen sign convention for
the natural identifications.

## References

1. V. S. Varadarajan, *Supersymmetry for Mathematicians: An Introduction*,
   American Mathematical Society, 2004. [Publisher
   record](https://doi.org/10.1090/cour/011). Relevant: Chapter 1.
2. P. Deligne and J. W. Morgan, “Notes on supersymmetry (following Joseph
   Bernstein),” in *Quantum Fields and Strings: A Course for Mathematicians*,
   Volume 1, American Mathematical Society, 1999. Relevant: Sections 1–2.
