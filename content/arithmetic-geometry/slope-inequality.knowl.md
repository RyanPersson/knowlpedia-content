+++
id = "arithmetic-geometry/slope-inequality"
title = "Arakelov slope inequality"
kind = "proposition"
summary = "The size of a nonzero integral map constrains the difference of arithmetic slopes."
aliases = ["Bost slope inequality", "divisibility versus size"]
domains = ["arithmetic-geometry"]
section_mode = "progressive"
prerequisites = ["arithmetic-geometry/arakelov-slope"]
+++

A **slope inequality** bounds the [[arithmetic-geometry/arakelov-slope|arithmetic slopes]] of Hermitian lattices using the size of a map between them. In rank one over a number ring, an integral nonzero map \(f:L\to M\) satisfies
\[
\widehat{\deg}_{\mathrm n} L\le \widehat{\deg}_{\mathrm n} M
+\frac{1}{[K:\mathbb Q]}\sum_{\sigma:K\hookrightarrow\mathbb C}\log\|f_\sigma\|.
\]
Here \(\widehat{\deg}_{\mathrm n}\) is the [[arithmetic-geometry/arakelov-degree|normalized Arakelov degree]] over the number field \(K\), and \(\|f_\sigma\|\) is the operator norm for the metrics on \(L\) and \(M\). The finite index of \(f(L)\) in \(M\) accounts for the inequality.

## Why divisibility costs size

For ordinary integers, let \(f\) multiply by \(12\) on \(\mathbb Z\) with its usual metric. At \(2\) and \(3\) the [[arithmetic-geometry/inert-prime-divisibility|prescribed valuations]] contribute \(2\log 2+\log 3=\log12\). Counting only the factors at \(2\) gives a lower bound for the same archimedean size. In higher rank the analogous comparison uses determinants and slopes of subspaces or quotients.

## References

- Éric Gaudron, [Pentes des fibrés vectoriels adéliques sur un corps global, §6, slope inequalities](https://arxiv.org/pdf/math/0605408).
