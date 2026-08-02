+++
id = "noncommutative-geometry/cyclic-cohomology"
title = "Cyclic cohomology"
kind = "definition"
summary = "A cohomology theory of associative algebras built from multilinear cochains invariant under cyclic permutation."
aliases = ["Connes cyclic cohomology", "(b,B)-cohomology"]
domains = ["noncommutative-geometry", "algebra-homological"]
section_mode = "progressive"
+++

Let \(A\) be a unital algebra over a field of characteristic zero. A **cyclic \(n\)-cochain** is a multilinear map \(\varphi:A^{n+1}\to k\) satisfying
\[
\varphi(a_n,a_0,\ldots,a_{n-1})
=(-1)^n\varphi(a_0,\ldots,a_n).
\]
The Hochschild coboundary is
\[
\begin{aligned}
(b\varphi)(a_0,\ldots,a_{n+1})
={}&\sum_{j=0}^{n}(-1)^j
\varphi(a_0,\ldots,a_ja_{j+1},\ldots,a_{n+1})\\
&+(-1)^{n+1}\varphi(a_{n+1}a_0,a_1,\ldots,a_n).
\end{aligned}
\]
It preserves cyclic cochains and satisfies \(b^2=0\). The **cyclic cohomology**
\(HC^n(A)\) is the \(n\)th [[algebra-homological/cohomology-module|cohomology]]
of this subcomplex of the dual [[noncommutative-geometry/hochschild-chain-complex|Hochschild complex]].

## Mixed-complex formulation

Over a characteristic-zero field, the cyclic-cochain definition agrees with
the cohomology obtained from Connes's \((b,B)\)-bicomplex, where \(B\) is the
cyclic operator that shifts degree oppositely to \(b\). The mixed-complex
viewpoint naturally produces [[noncommutative-geometry/periodic-cyclic-cohomology|periodic cyclic cohomology]] and the long exact
SBI sequence relating Hochschild and cyclic theories.

## Pairings and geometric role

Cyclic cocycles pair with algebraic \(K\)-theory classes: even cocycles pair
with idempotents and odd cocycles with invertibles. In noncommutative geometry,
these pairings generalize [[differential-geometry/integration-of-differential-forms|integration of differential forms]] and express index
pairings. The cyclic [[noncommutative-geometry/chern-character-fredholm-module|Chern character of a Fredholm module]] is a central example.

## Conventions and scope

**Warning.** Algebraic, continuous, entire, and periodic cyclic cohomology use
different cochain spaces or completions and need not agree. For a nonunital
algebra, cyclic cohomology is commonly defined relative to a unitization.
Coefficient conventions and cohomological grading must be stated before using
the notation \(HC^\bullet(A)\).

## References

1. A. Connes, “Non-Commutative Differential Geometry,” *Publications Mathématiques de l'IHÉS* 62 (1985), 41–144. [DOI record](https://doi.org/10.1007/BF02698807). Relevant: §§II.1–II.3 on cyclic cohomology, the bicomplex, and Chern characters.
2. J.-L. Loday, *Cyclic Homology*, 2nd ed., Springer, 1998. [Publisher record](https://doi.org/10.1007/978-3-662-11389-9). Relevant: chapters 2–5 on cyclic modules, the \((b,B)\)-bicomplex, and cyclic cohomology.
