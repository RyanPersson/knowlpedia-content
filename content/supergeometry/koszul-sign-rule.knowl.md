+++
id = "supergeometry/koszul-sign-rule"
title = "Koszul sign rule"
kind = "definition"
summary = "The sign convention in which exchanging homogeneous factors of parities p and q contributes (-1)^(pq)."
aliases = ["Koszul rule of signs", "super sign rule"]
domains = ["supergeometry", "algebra-category-theory"]
section_mode = "progressive"
+++

In the [[supergeometry/category-of-super-vector-spaces|category of super
vector spaces]], the **Koszul sign rule** assigns the sign
\[
(-1)^{|v||w|}
\]
whenever homogeneous pieces \(v\) and \(w\) are interchanged. It is the
symmetry
\[
v\otimes w\longmapsto(-1)^{|v||w|}w\otimes v
\]
of the symmetric monoidal category, rather than a correction added after a
calculation.

For homogeneous maps \(f:V\to V'\) and \(g:W\to W'\), the tensor product is
therefore evaluated by
\[
(f\otimes g)(v\otimes w)
=(-1)^{|g||v|}f(v)\otimes g(w).
\]
In particular, two odd pieces acquire a minus sign when exchanged, while an
even piece can cross any homogeneous piece without a sign.

## References

1. P. Deligne and J. W. Morgan, “Notes on supersymmetry (following Joseph
   Bernstein),” in *Quantum Fields and Strings: A Course for Mathematicians*,
   Volume 1, American Mathematical Society, 1999, pp. 41–97. Relevant:
   Sections 1–2.
2. C. Carmeli, L. Caston, and R. Fioresi, *Mathematical Foundations of
   Supersymmetry*, European Mathematical Society, 2011. [Publisher
   record](https://doi.org/10.4171/097). Relevant: Chapter 1.
