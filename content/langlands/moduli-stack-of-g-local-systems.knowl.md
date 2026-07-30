+++
id = "langlands/moduli-stack-of-g-local-systems"
title = "Moduli stack of G-local systems"
kind = "definition"
summary = "The derived moduli stack LocSys_G(X) of principal G-bundles with flat connection."
aliases = ["LocSys_G", "stack of G-local systems"]
domains = ["langlands", "algebraic-geometry-foundations"]
section_mode = "progressive"
+++

Let \(X\) be a smooth curve and \(G\) a reductive algebraic group. The
**moduli stack of \(G\)-local systems**, denoted
\(\operatorname{LocSys}_G(X)\), parametrizes
[[langlands/g-local-system|\(G\)-local systems]] on \(X\) in families.

In the de Rham version, its objects are principal \(G\)-bundles with flat
connection. In the Betti version over \(\mathbb C\), it is modeled by the
derived character stack
\[
\operatorname{Map}(X_{\mathrm{Betti}},BG),
\]
whose classical points are representations of \(\pi_1(X)\) in \(G\) modulo
conjugation.

## Why the derived stack matters

Automorphisms and deformation-obstruction groups are part of the moduli
problem. The derived enhancement records them and makes
\(\operatorname{LocSys}_G\) quasi-smooth in the setting used to define
nilpotent singular support.

## Spectral role

Geometric Langlands uses
\(\operatorname{LocSys}_{\widehat G}(X)\), where \(\widehat G\) is the
[[langlands-letter/knowls/langlands-dual-group|dual group]]. Its relevant
sheaf category is generally
[[langlands/ind-coherent-sheaves-with-nilpotent-singular-support|\(\operatorname{IndCoh}_{\mathcal N}\)]],
not merely quasi-coherent sheaves.

## References

1. Dima Arinkin and Dennis Gaitsgory, “Singular support of coherent sheaves,
   and the geometric Langlands conjecture,” *Selecta Mathematica* 21 (2015),
   1–199. [arXiv](https://arxiv.org/abs/1201.6343).
