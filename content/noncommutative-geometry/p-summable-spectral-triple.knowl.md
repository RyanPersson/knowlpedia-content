+++
id = "noncommutative-geometry/p-summable-spectral-triple"
title = "p-summable spectral triple"
kind = "definition"
summary = "A spectral triple whose regularized inverse Dirac operator belongs to a specified Schatten class."
aliases = ["p-summability", "strictly p-summable spectral triple"]
domains = ["noncommutative-geometry", "functional-analysis"]
section_mode = "progressive"
+++

Let \(0<p<\infty\). A [[noncommutative-geometry/spectral-triple|spectral triple]] \((\mathcal A,H,D)\) is **\(p\)-summable** if
\[
(1+D^2)^{-1/2}\in\mathcal L^p(H),
\]
where \(\mathcal L^p(H)\) is the [[functional-analysis/schatten-class-operator|Schatten class]]. Equivalently,
\[
\operatorname{Tr}\!\left((1+D^2)^{-p/2}\right)<\infty.
\]
This is a quantitative compact-resolvent condition: the singular values of the regularized inverse of \(D\) are \(p\)-summable, with multiplicity. The regularization by \(1+D^2\) treats \(\ker D\) harmlessly. For an invertible \(D\), it may be replaced by \(|D|^{-1}\) without changing membership in the relevant ideal.

## Equivalent spectral tests

When \(D\) has [[functional-analysis/compact-resolvent|compact resolvent]] and
eigenvalues \(\lambda_n\), repeated with
multiplicity, \(p\)-summability is equivalent to
\[
\sum_n(1+\lambda_n^2)^{-p/2}<\infty.
\]
It is also equivalent to finiteness of the spectral zeta function
\(\operatorname{Tr}(|D|^{-p})\) after omitting the finite-dimensional kernel,
provided \(D\) is invertible away from zero. These equivalences follow
directly from functional calculus and the definition of Schatten ideals.

If the triple is \(p\)-summable, then it is \(q\)-summable for every
\(q>p\). The converse can fail at the endpoint, so the value \(p\) must not
be inferred merely from summability at all larger exponents.

## Examples and consequences

The canonical spin spectral triple on a closed \(n\)-dimensional manifold is
\(p\)-summable for every \(p>n\), by Weyl eigenvalue asymptotics. At the
critical exponent \(p=n\), its inverse
[[noncommutative-geometry/dirac-operator|Dirac operator]] generally belongs only
to a [[operator-algebras/weak-schatten-ideal|weak Schatten ideal]], while its
\(n\)th power supports a [[operator-algebras/dixmier-trace|Dixmier trace]].
Thus saying that the triple has dimension \(n\) is not the same as saying it
is strictly \(n\)-summable.

[[noncommutative-geometry/finitely-summable-spectral-triple|Finite summability]]
implies [[noncommutative-geometry/theta-summable-spectral-triple|theta summability]]
because exponential decay
dominates every negative power. It also makes sufficiently long products of
Dirac or bounded-transform commutators trace class, enabling finite-degree
[[noncommutative-geometry/chern-character-fredholm-module|cyclic Chern characters]].

## Conventions and scope

**Warning.** Some authors call the weak endpoint condition
\((1+D^2)^{-1/2}\in\mathcal L^{p,\infty}\) “\(p\)-summability.” The core uses
strict Schatten summability; weak \(p\)-summability should be named
explicitly. Another convention calls a triple \(p^+\)-summable when it is
\(q\)-summable for every \(q>p\).

For \(0<p<1\), the same trace formula defines membership in a quasi-Banach
Schatten ideal rather than a Banach ideal. This extension is included in the
core convention and in the linked Schatten-class convention.
[[noncommutative-geometry/semifinite-spectral-triple|Semifinite spectral triples]]
replace the [[operator-algebras/operator-trace|canonical operator trace]] by a
specified faithful normal
semifinite trace.

## References

1. A. Connes, *Noncommutative Geometry*, Academic Press, 1994. [Author-hosted text](https://alainconnes.org/wp-content/uploads/book94bigpdf.pdf). Relevant: Chapter IV, §§1–2 on summable Fredholm modules and trace ideals.
2. J. M. Gracia-Bondía, J. C. Várilly, and H. Figueroa, *Elements of Noncommutative Geometry*, Birkhäuser, 2001. [DOI record](https://doi.org/10.1007/978-1-4612-0005-5). Relevant: §10.1 on summability of spectral triples.
