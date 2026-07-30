+++
id = "algebraic-geometry-foundations/borel-subgroup"
title = "Borel subgroup"
kind = "definition"
summary = "A maximal connected solvable subgroup of a connected linear algebraic group."
aliases = ["Borel subgroup"]
domains = ["algebraic-geometry-foundations", "langlands"]
section_mode = "progressive"
+++

Let \(G\) be a connected linear algebraic group over an algebraically closed
field. A **Borel subgroup** \(B\subseteq G\) is a maximal connected solvable
closed subgroup.

For a reductive group, a Borel subgroup contains a maximal torus \(T\), and the
choice \(T\subseteq B\) determines a set of positive roots. Any two Borel
subgroups are conjugate over an algebraically closed field.

## Examples

In \(GL_n\), the invertible upper-triangular matrices form a Borel subgroup.
Its image in \(PGL_n\) is again a Borel subgroup. For \(SL_2\), the
upper-triangular subgroup stabilizes the line spanned by the first standard
basis vector.

## Relation to flag varieties

The quotient \(G/B\) is the complete [[algebraic-geometry-foundations/flag-variety|flag variety]] of \(G\).
Over a field that is not algebraically closed, one distinguishes Borel
subgroups defined over the base field from geometric Borel subgroups after
base change.

## References

1. Armand Borel, “Groupes linéaires algébriques,” *Annals of Mathematics* 64
   (1956), 20–82. [DOI](https://doi.org/10.2307/1969949).
