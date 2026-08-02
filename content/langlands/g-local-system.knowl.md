+++
id = "langlands/g-local-system"
title = "G-local system"
kind = "definition"
summary = "A principal G-bundle with flat connection; over the complex numbers, Riemann-Hilbert comparison relates it to a G-valued monodromy representation."
aliases = ["G local system", "principal G-local system"]
domains = ["langlands", "fiber-bundles"]
section_mode = "progressive"
+++

Let \(G\) be an [[algebraic-geometry-foundations/algebraic-group|algebraic group]] and \(X\) a smooth complex curve. A
**\(G\)-local system** in the de Rham sense is a
[[algebraic-geometry-foundations/principal-g-bundle-on-scheme|principal
\(G\)-bundle]] \(P\) on \(X\) equipped with an integrable, or flat,
connection.

In the Betti sense, it is a \(G\)-valued
[[fiber-bundles/local-system|local system]], described after choosing a base
point by a representation
\[
\rho:\pi_1(X,x)\longrightarrow G(\mathbb C)
\]
up to conjugation.

## Comparison

Analytic horizontal transport takes a de Rham local system to its monodromy
representation. If \(X\) is smooth projective, the algebraic
[[langlands/riemann-hilbert-correspondence|Riemann–Hilbert correspondence]]
compares the de Rham and Betti moduli problems over
\(\mathbb C\). More generally, for an open curve
\(U\subset\overline X\), this comparison with ordinary Betti local systems
applies to connections that are
[[langlands/regular-singular-connection|regular singular]] along
\(\overline X\setminus U\).
[[langlands/irregular-singular-connection|Irregular connections]] require
enhanced Betti data, including [[langlands/stokes-data|Stokes data]];
ordinary monodromy alone does not recover them. Even in the regular-singular
case, the comparison is analytic and does not identify the algebraic
structures on the two moduli spaces.

## Langlands role

For a [[algebraic-geometry-foundations/reductive-algebraic-group|reductive group]] \(G\), the spectral parameter in geometric Langlands is
a local system for the
[[langlands-letter/knowls/langlands-dual-group|Langlands dual group]]
\(\widehat G\), not generally for \(G\) itself.

## References

1. Pierre Deligne, *Équations différentielles à points singuliers réguliers*,
   Lecture Notes in Mathematics 163, Springer, 1970.
   [DOI](https://doi.org/10.1007/BFb0061194).
2. Carlos T. Simpson, “Moduli of representations of the fundamental group of
   a smooth projective variety I,” *Publications Mathématiques de l’IHÉS* 79
   (1994), 47–129. [DOI](https://doi.org/10.1007/BF02698887).
