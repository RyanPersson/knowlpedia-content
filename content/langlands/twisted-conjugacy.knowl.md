+++
id = "langlands/twisted-conjugacy"
title = "Twisted conjugacy"
kind = "definition"
summary = "Conjugacy modified by an automorphism, including Frobenius and sigma-conjugacy as basic cases."
aliases = ["theta-conjugacy", "twisted conjugacy class", "sigma-conjugacy"]
domains = ["langlands", "algebra-groups"]
section_mode = "progressive"
+++

Let \(G\) be a group and let \(\theta\) be an
[[algebra-groups/automorphism-group|automorphism]] of \(G\). Two
elements \(x,y\in G\) are **\(\theta\)-conjugate** if

\[
y=gx\theta(g)^{-1}
\]

for some \(g\in G\). Equivalently, they lie in the same
[[fiber-bundles/orbit-map|orbit]] for the twisted
action \(g\mathbin{\cdot_\theta}x=gx\theta(g)^{-1}\).  When \(\theta\) is the
identity this is ordinary conjugacy.

The **twisted centralizer** of \(x\) is the
[[algebra-groups/stabilizer|stabilizer]]
\(G_{x,\theta}=\{g:gx\theta(g)^{-1}=x\}\).

## Frobenius and sigma-conjugacy

If \(G\) is defined over a
[[algebra-fields-galois/finite-field|finite field]] or
[[algebra-fields-galois/local-field|local field]] and
\(\sigma\) is
[[algebra-fields-galois/frobenius-endomorphism|Frobenius]],
then twisted conjugacy is usually called **\(\sigma\)-conjugacy**.  The
[[langlands/kottwitz-set-b-g|Kottwitz set \(B(G)\)]] is the set of
\(\sigma\)-conjugacy classes in \(G(\breve F)\).

Twisted conjugacy also appears in the nonidentity components of
[[algebra-groups/semidirect-product|semidirect products]] such as
\(\widehat G\rtimes\langle\theta\rangle\): ordinary conjugacy within the
coset of the
[[langlands-letter/knowls/langlands-dual-group|dual group]]
\(\widehat G\theta\) becomes
\(\theta\)-conjugacy in \(\widehat G\).

## Stable variant

For [[algebraic-geometry-foundations/algebraic-group|algebraic groups]] one
can likewise compare twisted conjugacy over the base field with twisted
conjugacy over an
[[algebra-fields-galois/algebraic-closure|algebraic closure]]. The latter gives
stable twisted classes, whose rational orbits are controlled by Galois
[[langlands-letter/knowls/nonabelian-h1-galois-cohomology|Galois
cohomology]] of the twisted centralizer.

## References

1. Robert E. Kottwitz, “Isocrystals with additional structure,”
   *Compositio Mathematica* 56 (1985), 201–220.
   [Numdam](https://www.numdam.org/item/CM_1985__56_2_201_0/).
2. Robert E. Kottwitz, “Stable trace formula: cuspidal tempered terms,”
   *Duke Mathematical Journal* 51 (1984), 611–650.
