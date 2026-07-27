+++
id = "algebra-commutative/localization-ring"
title = "Localization of a ring"
kind = "knowl"
summary = "The universal ring in which every element of a multiplicative subset becomes invertible."
aliases = ["localization-ring", "Localization of a ring"]
domains = ["algebra-commutative"]
legacy_source_path = "algebra-commutative/localization-ring.md"
+++

Let \(R\) be a [[algebra-rings/commutative-ring|commutative ring]] and \(S\subseteq R\) a [[algebra-commutative/multiplicative-set|multiplicative set]]. A **localization of \(R\) at \(S\)** is a commutative ring \(S^{-1}R\) with a homomorphism
\[
\iota:R\longrightarrow S^{-1}R
\]
such that every \(\iota(s)\), for \(s\in S\), is a unit and the following universal property holds: if \(\varphi:R\to A\) sends every element of \(S\) to a unit of a commutative ring \(A\), there is a unique homomorphism \(\widetilde\varphi:S^{-1}R\to A\) satisfying \(\widetilde\varphi\circ\iota=\varphi\).

## Construction by fractions

As a set, \(S^{-1}R\) can be constructed from pairs \((r,s)\in R\times S\) modulo the equivalence relation
\[
(r,s)\sim (r',s') \quad \Longleftrightarrow \quad \exists\,t\in S\text{ such that } t(rs'-r's)=0 \text{ in }R.
\]
Write the class of \((r,s)\) as \(\frac{r}{s}\). Addition and multiplication are defined by
\[
\frac{r}{s}+\frac{r'}{s'}=\frac{rs'+r's}{ss'},\qquad
\frac{r}{s}\cdot\frac{r'}{s'}=\frac{rr'}{ss'}.
\]
The canonical map is \(\iota(r)=\frac{r}{1}\).

If \(0\in S\), then \(S^{-1}R\) is the zero ring.

## Universal map

The homomorphism supplied by the universal property is explicitly
\[
\widetilde\varphi\!\left(\frac{r}{s}\right)=\varphi(r)\,\varphi(s)^{-1}.
\]

This same “invert \(S\)” construction for modules is treated in [[algebra-commutative/localization-module|localization of a module]].

A basic structural fact is that primes of \(S^{-1}R\) correspond to primes of \(R\) disjoint from \(S\); see [[algebra-commutative/localization-prime-correspondence|prime correspondence under localization]].

## Examples

1. **Inverting a prime number.** Take \(R=\mathbb Z\) and \(S=\{1,p,p^2,\dots\}\). Then
   \[
   S^{-1}\mathbb Z \cong \mathbb Z\!\left[\frac{1}{p}\right]
   =\left\{\frac{a}{p^n}:a\in\mathbb Z,\ n\ge 0\right\}\subseteq\mathbb Q.
   \]

2. **Laurent polynomials.** If \(R=k[x]\) and \(S=\{1,x,x^2,\dots\}\), then
   \[
   S^{-1}R \cong k[x,x^{-1}],
   \]
   since \(x\) becomes invertible.

3. **Localizing at a prime ideal.** If \(\mathfrak p\subset R\) is prime and \(S=R\setminus\mathfrak p\), then \(S^{-1}R\) is the [[algebra-commutative/localization-at-prime|localization at the prime]] \(R_{\mathfrak p}\), which is a [[algebra-commutative/local-ring|local ring]].
