+++
id = "algebraic-geometry-foundations/pointed-algebraic-curve"
title = "Pointed algebraic curve"
kind = "definition"
summary = "An algebraic curve equipped with an ordered or labeled collection of marked points."
aliases = ["marked algebraic curve", "punctured algebraic curve"]
domains = ["algebraic-geometry-foundations", "langlands"]
section_mode = "progressive"
+++

A **pointed algebraic curve** is an
[[algebraic-geometry-foundations/algebraic-curve|algebraic curve]] \(X\)
together with marked sections \(x_1,\ldots,x_n\). Over a field, one often
writes the associated reduced divisor as
\[
D=x_1+\cdots+x_n
\]
and calls \(U=X\setminus D\) the punctured curve.

The points may be ordered, labeled, or merely collected into a divisor; these
are different moduli problems. Stability of a pointed curve is an additional
condition, not part of the bare definition.

## Langlands role

Ramified geometric Langlands studies local systems on \(U\) with specified
behavior around \(D\), and \(G\)-bundles on \(X\) with compatible
[[langlands/level-structure-on-g-bundle|level or parabolic structure]] at the
marked points.

## References

1. Pierre Deligne and David Mumford, “The irreducibility of the space of
   curves of given genus,” *Publications Mathématiques de l’IHÉS* 36 (1969),
   75–109. [DOI](https://doi.org/10.1007/BF02684599).
