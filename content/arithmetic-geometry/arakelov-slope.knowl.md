+++
id = "arithmetic-geometry/arakelov-slope"
title = "Arakelov slope"
kind = "definition"
summary = "The normalized arithmetic degree of a nonzero Hermitian vector bundle over a number ring divided by its rank."
aliases = ["Arakelov slopes", "arithmetic slope"]
domains = ["arithmetic-geometry"]
section_mode = "progressive"
prerequisites = ["arithmetic-geometry/arakelov-degree", "algebra-modules/projective-module"]
+++

A Hermitian vector bundle \(\overline V\) over the ring of integers of \(K\) consists of a finitely generated [[algebra-modules/projective-module|projective module]] \(V\) equipped with compatible Hermitian norms at the complex embeddings. Its **Arakelov slope** is \(\widehat\mu(\overline V)=\widehat{\deg}_{\mathrm n}(\det\overline V)/\operatorname{rank}V\), for positive rank. The numerator is the [[arithmetic-geometry/arakelov-degree|normalized Arakelov degree]] of the determinant line, the top exterior power of \(V\) with its induced norms. It measures the integral determinant lattice together with its [[arithmetic-geometry/archimedean-size|archimedean norms]].

## A lattice you can measure

Over \(\mathbb Z\), equip \(V\otimes\mathbb R\) with a Euclidean metric. The arithmetic degree is then \(-\log\operatorname{covol}(V)\), where the covolume is the volume of a fundamental parallelepiped. A rank-one lattice with basis vector of length \(2\) has slope \(-\log 2\). Passing to the index-two sublattice halves the density of points and subtracts another \(\log 2\) from its slope.

## References

- Éric Gaudron, [Pentes des fibrés vectoriels adéliques sur un corps global, §§4–5, degrees and slopes](https://arxiv.org/pdf/math/0605408).
