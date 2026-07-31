+++
id = "algebraic-geometry-foundations/pointed-algebraic-curve"
title = "Pointed algebraic curve"
kind = "definition"
summary = "An algebraic curve equipped with an ordered or labeled collection of marked points."
aliases = ["marked algebraic curve"]
domains = ["algebraic-geometry-foundations", "langlands"]
section_mode = "progressive"
+++

A **pointed algebraic curve** over a scheme \(S\) is a family of algebraic
curves \(\pi:X\to S\) together with specified sections
\(x_1,\ldots,x_n:S\to X\). Conditions such as pairwise disjointness of the
sections or their passage through the smooth locus are additional hypotheses.

Over a field, pairwise distinct rational marked points determine the reduced
effective divisor
\[
D=x_1+\cdots+x_n
\]
and the complement
[[algebraic-geometry-foundations/punctured-algebraic-curve|punctured curve]]
\(U=X\setminus D\).

The sections may be ordered, labeled, or merely collected into a divisor;
these are different moduli problems. Stability is not part of the bare
definition.

## Langlands role

Ramified geometric Langlands studies local systems on \(U\) with specified
behavior around \(D\), and \(G\)-bundles on \(X\) with compatible
[[langlands/level-structure-on-g-bundle|level or parabolic structure]] at the
marked points.

## References

1. Pierre Deligne and David Mumford, “The irreducibility of the space of
   curves of given genus,” *Publications Mathématiques de l’IHÉS* 36 (1969),
   75–109. [DOI](https://doi.org/10.1007/BF02684599).
