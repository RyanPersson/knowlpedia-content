+++
id = "harmonic-analysis/number-field-torus-characters"
title = "Characters of a number-field torus"
kind = "theorem"
summary = "The character group of the number-field torus is its codifferent lattice."
aliases = []
domains = ["harmonic-analysis"]
section_mode = "progressive"
prerequisites = ["ergodic-theory/number-field-torus", "algebra-fields-galois/codifferent", "algebra-fields-galois/archimedean-trace-pairing", "harmonic-analysis/pontryagin-dual"]
+++

For \(X=(K_\infty/\mathcal O_K)^d\), all [[harmonic-analysis/unitary-character|continuous unitary characters]] are
\[
\chi_a([x])=\exp\bigl(2\pi i\operatorname{Tr}_\infty(a\cdot x)\bigr),
\qquad a\in(\mathcal O_K^\vee)^d.
\]
Thus \(\widehat X\cong(\mathcal O_K^\vee)^d\). Here the ring of integers and codifferent are identified with their Minkowski images.

## Why the formula descends

Adding \(\ell\in\mathcal O_K^d\) changes the exponent divided by \(2\pi i\) by the integer \(\operatorname{Tr}(a\cdot\ell)\). Hence the value is independent of representatives.

Choose an integral basis and its trace-dual basis. In these real coordinates the displayed functions are precisely the integer Fourier modes of a real \(md\)-torus, so they include every character. They form an orthonormal basis for Haar \(L^2\).

## References

1. Keith Conrad, [*The Different Ideal*](https://kconrad.math.uconn.edu/blurbs/gradnumthy/different.pdf). §3, trace-dual bases; the torus statement follows by the coordinate calculation above.
