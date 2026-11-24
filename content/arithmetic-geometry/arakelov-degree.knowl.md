+++
id = "arithmetic-geometry/arakelov-degree"
title = "Normalized Arakelov degree of a Hermitian line"
kind = "definition"
summary = "A logarithmic measure combining the finite index of a section and its norms at the infinite places."
aliases = ["arithmetic degree", "normalized arithmetic degree", "Arakelov degree"]
domains = ["arithmetic-geometry"]
section_mode = "progressive"
prerequisites = ["algebra-fields-galois/ring-of-integers", "arithmetic-geometry/archimedean-size"]
+++

Let \(K\) be a number field with [[algebra-fields-galois/ring-of-integers|ring of integers]] \(\mathcal O_K\). A Hermitian line \(\bar L\) consists of a rank-one projective \(\mathcal O_K\)-module \(L\) and a norm at each embedding \(\sigma:K\hookrightarrow\mathbb C\), compatible with complex conjugation. For any nonzero \(s\in L\), its **normalized Arakelov degree** is
\[
\widehat{\deg}_{\mathrm n}(\bar L)
=\frac{\log\#(L/\mathcal O_Ks)-\sum_{\sigma:K\hookrightarrow\mathbb C}\log\|s\|_\sigma}{[K:\mathbb Q]}.
\]
The first term measures a finite index. The sum measures [[arithmetic-geometry/archimedean-size|archimedean sizes]], counting both members of each complex pair.

## Independence of the section

Multiplying \(s\) by a nonzero algebraic integer \(a\) multiplies the index by the absolute [[algebra-fields-galois/norm-field|field norm]] \(|N_{K/\mathbb Q}(a)|\). The product of the norms of \(s\) changes by exactly the same factor. Any two nonzero sections have a common nonzero integral multiple, so they give the same degree. Over \(\mathbb Z\), a basis of length \(r\) gives degree \(-\log r\).

## References

- Éric Gaudron, [Pentes des fibrés vectoriels adéliques sur un corps global, §4, degrees](https://arxiv.org/pdf/math/0605408).
