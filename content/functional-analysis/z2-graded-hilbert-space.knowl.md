+++
id = "functional-analysis/z2-graded-hilbert-space"
title = "Z/2-graded Hilbert space"
kind = "definition"
summary = "A Hilbert space decomposed orthogonally into closed even and odd subspaces."
aliases = ["even Hilbert space", "graded Hilbert space", "super Hilbert space"]
domains = ["functional-analysis"]
section_mode = "progressive"
+++

A **\(Z/2\)-graded Hilbert space** is a
[[linear-algebra/hilbert-space|Hilbert space]] \(H\) with an orthogonal
decomposition
\[
H=H^{0}\oplus H^{1}
\]
into closed subspaces, called the even and odd parts. Equivalently, it is a
Hilbert space equipped with a grading operator \(\Gamma\) satisfying
\[
\Gamma=\Gamma^*,\qquad \Gamma^2=1,
\]
where \(H^0=\ker(\Gamma-1)\) and \(H^1=\ker(\Gamma+1)\). This is the
topological, inner-product-compatible version of a
[[algebra-modules/graded-module|\(Z/2\)-graded module]]: closedness and
orthogonality ensure that the decomposition is a Hilbert direct sum.

## Even and odd operators

A bounded operator \(T\) is even when \(T\Gamma=\Gamma T\), equivalently when
it preserves \(H^0\) and \(H^1\). It is odd when
\(T\Gamma=-\Gamma T\), equivalently when it exchanges the two parts. For an
unbounded operator, either assertion also requires
\(\Gamma\operatorname{Dom}(T)\subseteq\operatorname{Dom}(T)\), and the
commutation relation is imposed on that domain. These are the parity
conventions encoded by an
[[operator-algebras/graded-operator|even or odd operator]].

## Spectral-triple convention

An [[noncommutative-geometry/even-spectral-triple|even spectral triple]]
\((\mathcal A,H,D,\Gamma)\) requires the represented algebra to act evenly,
\([\Gamma,\pi(a)]=0\), and the [[noncommutative-geometry/dirac-operator|Dirac operator]] to act oddly,
\(\Gamma D=-D\Gamma\) on \(\operatorname{Dom}(D)\). The latter statement
includes invariance of the domain under \(\Gamma\). By contrast, an
[[noncommutative-geometry/odd-spectral-triple|odd spectral triple]] normally
means that no grading operator is part of the data; it does not mean that
\(D\) is even.

## Examples and conventions

For any Hilbert spaces \(K_0\) and \(K_1\), the direct sum
\(K_0\oplus K_1\) is graded by
\(\Gamma(\xi_0,\xi_1)=(\xi_0,-\xi_1)\). Differential forms are graded by even
and odd degree, with the parity operator acting by \((-1)^k\) on \(k\)-forms.
Authors also write \(\mathbb Z_2\), \(\mathbb Z/2\), or “super” Hilbert space;
in analytic \(K\)-homology these expressions refer to the same two-term
orthogonal grading.

## References

1. Nigel Higson and John Roe, *Analytic K-Homology*, Oxford University Press, 2000. [Publisher record](https://doi.org/10.1093/oso/9780198511762.001.0001). Relevant: Chapter 8 on graded Hilbert spaces and cycles.
2. José M. Gracia-Bondía, Joseph C. Várilly, and Héctor Figueroa, *Elements of Noncommutative Geometry*, Birkhäuser, 2001. [DOI record](https://doi.org/10.1007/978-1-4612-0005-5). Relevant: §3.2 on \(Z/2\)-gradings and operator parity.
