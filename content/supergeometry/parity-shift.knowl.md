+++
id = "supergeometry/parity-shift"
title = "Parity shift"
kind = "construction"
summary = "The functor that interchanges the even and odd parts of a super vector space."
aliases = ["parity reversal", "Pi functor"]
domains = ["supergeometry", "linear-algebra"]
prerequisites = ["supergeometry/super-vector-space"]
dependency_review_count = 1
section_mode = "progressive"
+++

For a [[supergeometry/super-vector-space|super vector space]]
\(V=V_{\bar0}\oplus V_{\bar1}\), its **parity shift** or **parity reversal**
\(\Pi V\) is defined by
\[
(\Pi V)_{\bar0}=V_{\bar1},
\qquad
(\Pi V)_{\bar1}=V_{\bar0}.
\]
On even linear maps, \(\Pi f:\Pi V\to\Pi W\) has the same underlying linear
map as \(f\). This defines an even functor \(\Pi\) with
\(\Pi^2\cong\operatorname{id}\).

## Odd maps as even maps

An odd linear map \(f:V\to W\) can be regarded as an even map
\[
V\longrightarrow\Pi W
\qquad\text{or}\qquad
\Pi V\longrightarrow W.
\]
This is one reason parity shift is useful: it converts degree-one data into
ordinary degree-zero morphisms. Formulas involving shifted tensor products
may place signs in the identifications above; authors should state the chosen
sign convention when those identifications enter a calculation.

## No canonical even identification

The underlying ungraded vector spaces of \(V\) and \(\Pi V\) are the same, but
the identity of that underlying vector space is odd, not even. Consequently
there is generally no canonical isomorphism \(V\cong\Pi V\) in the
[[supergeometry/category-of-super-vector-spaces|category of super vector
spaces]].

## References

1. V. S. Varadarajan, *Supersymmetry for Mathematicians: An Introduction*,
   American Mathematical Society, 2004. [DOI
   record](https://doi.org/10.1090/cour/011). Relevant: Section 1.1.
2. C. Carmeli, L. Caston, and R. Fioresi, *Mathematical Foundations of
   Supersymmetry*, European Mathematical Society, 2011. [DOI
   record](https://doi.org/10.4171/097). Relevant: Chapter 1.
