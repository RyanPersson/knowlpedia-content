+++
id = "differential-geometry/bianchi-cusp-ideal-class-correspondence"
title = "Bianchi cusps and ideal classes"
kind = "theorem"
summary = "The cusp orbits of a Bianchi group correspond bijectively to ideal classes."
aliases = []
domains = ["differential-geometry"]
section_mode = "progressive"
prerequisites = ["differential-geometry/bianchi-orbifold", "differential-geometry/hyperbolic-orbifold-cusp", "algebra-fields-galois/ideal-class-group", "algebra-fields-galois/class-number", "algebraic-geometry-foundations/projective-space"]
+++

For \(K=\mathbb Q(\sqrt{-d})\) and \(\Gamma=\operatorname{PSL}_2(\mathcal O_K)\), the [[differential-geometry/hyperbolic-orbifold-cusp|cusps]] of the [[differential-geometry/bianchi-orbifold|Bianchi orbifold]] admit bijections
\[
\{\text{cusps}\}\ \cong\ \Gamma\backslash\mathbb P^1(K)
\ \xrightarrow{\ \sim\ }\operatorname{Cl}(K),
\qquad [a:b]\longmapsto[a\mathcal O_K+b\mathcal O_K].
\]
Here \((a,b)\ne(0,0)\); homogeneous coordinates are taken up to simultaneous nonzero scaling. The right side is the [[algebra-fields-galois/ideal-class-group|ideal class group]]. In particular the number of cusps equals the [[algebra-fields-galois/class-number|class number]] \(h_K\).

## Why the displayed map is well defined

Scaling \((a,b)\) multiplies its fractional ideal by a principal factor, leaving its class unchanged. A determinant-one integral matrix replaces \(a,b\) by integral linear combinations; its integral inverse proves that the generated ideal is unchanged.

This checks well-definedness, not the whole bijection: identifying all cusp orbits and proving surjectivity and injectivity requires the ideal-class theorem.

## The standard cusp

The boundary point \(\infty=[1:0]\) maps to the principal ideal class. Thus class number one means precisely that every cusp is equivalent to this standard cusp.

## References

1. T. Church, B. Farb, and A. Putman, *Integrality in the Steinberg module and the top-dimensional cohomology of SL_n O_K*, Example 5.6, p. 31 of the linked version. [Author-hosted paper](https://math.uchicago.edu/~farb/papers/Steinberg2.pdf)
