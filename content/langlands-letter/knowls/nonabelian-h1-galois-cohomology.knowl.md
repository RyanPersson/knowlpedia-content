+++
id = "langlands-letter/knowls/nonabelian-h1-galois-cohomology"
title = "Nonabelian \\(H^1(\\\\Gamma,G)\\) and 1-Cocycles"
kind = "definition"
summary = "The pointed set of Galois 1-cocycles modulo twisted conjugacy, classifying torsors under the coefficient group."
aliases = ["nonabelian-h1-galois-cohomology", "Nonabelian \\(H^1(\\\\Gamma,G)\\) and 1-Cocycles"]
domains = ["langlands-letter"]
legacy_source_path = "langlands-letter/knowls/nonabelian-h1-galois-cohomology.md"
+++

Let \(K/k\) be a finite Galois extension with group
\(\Gamma=\operatorname{Gal}(K/k)\), and let an algebraic \(k\)-group \(G\) give the natural action of \(\Gamma\) on \(G(K)\).

A **nonabelian \(1\)-cocycle** is a map \(a:\Gamma\to G(K)\) satisfying
\[
a_{\sigma\tau}=a_\sigma\cdot {}^\sigma a_\tau.
\]

Two cocycles are **cohomologous** if
\[
a'_\sigma=g^{-1}a_\sigma\,{}^\sigma g
\]
for some \(g\in G(K)\). The quotient is the **nonabelian cohomology set**
\[
H^1(\Gamma,G(K)).
\]
It is a pointed set, whose distinguished point is the class of the trivial cocycle \(a_\sigma=1\).

## Torsors and forms

The set \(H^1(k,G)\) classifies \(G\)-torsors over \(k\) up to isomorphism. It should not be identified indiscriminately with the set of inner forms of \(G\):

- forms of \(G\) are classified by \(H^1(k,\operatorname{Aut}(G_{k_s}))\);
- inner forms are represented by classes coming from
  \(H^1(k,G_{\mathrm{ad}})\) through the conjugation map
  \(G_{\mathrm{ad}}\to\operatorname{Aut}(G)\);
- a cocycle with values in \(G\) itself defines the more restrictive notion of a **pure inner twist**.

Thus the coefficient group is part of the statement and must be recorded.

## Absolute Galois version

For the absolute Galois group
\(\Gamma_k=\operatorname{Gal}(k_s/k)\), cocycles
\(\Gamma_k\to G(k_s)\) are required to be continuous. A finite-extension set
\(H^1(\operatorname{Gal}(K/k),G(K))\) records classes that become trivial after base change to \(K\).

## Role in the letter

An inner twisting in the letter is specified by a cocycle in the appropriate inner-automorphism group. “Splitting locally at almost all \(p\)” means that the restricted class becomes trivial for the corresponding local decomposition groups.
