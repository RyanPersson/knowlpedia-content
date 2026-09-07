+++
id = "shale-paper/schrodinger-representation"
title = "Schrödinger representation"
kind = "definition"
summary = "The standard Weyl representation on L²(ℝⁿ) by translations and modulations."
aliases = ["schrodinger-representation", "Schrödinger representation"]
domains = ["shale-paper", "mathematical-physics"]
prerequisites = ["measure-theory/lp-space", "functional-analysis/unitary-operator", "shale-paper/weyl-ccr-quantization"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

For \(q,p\in\mathbb R^n\), the **Schrödinger representation** of the [[shale-paper/weyl-ccr-quantization|Weyl
relations]] on [[measure-theory/lp-space|\(L^2(\mathbb R^n)\)]] (with Lebesgue measure) is the [[functional-analysis/unitary-operator|unitary operator]]-valued map
\[
 [V(q,p)f](x)=\exp\!\left(i\left(q\mathbin{\cdot}x+\tfrac12q\mathbin{\cdot}p\right)\right)f(x+p).
\]
## Weyl relation

With \(B((q,p),(q',p'))=q\mathbin{\cdot}p'-p\mathbin{\cdot}q'\), it satisfies
\[
 V(q,p)V(q',p')=e^{-iB((q,p),(q',p'))/2}V(q+q',p+p').
\]

## Why the phase has this sign

The formula is the exponential form \(V(q,p)=e^{i(q\cdot Q+p\cdot P)}\),
where \(Q_jf(x)=x_jf(x)\) and \(P_jf(x)=-i\,\partial_jf(x)\) on their
standard common smooth core. Direct multiplication gives
\[
 [V(q,p)V(q',p')f](x)
 =e^{i((q+q')\cdot x+(q\cdot p+q'\cdot p')/2+q'\cdot p)}f(x+p+p'),
\]
whose extra phase relative to \(V(q+q',p+p')\) is
\(e^{i(q'\cdot p-q\cdot p')/2}=e^{-iB((q,p),(q',p'))/2}\).

## Properties

Translations and modulations are unitary on \(L^2(\mathbb R^n)\), and their
dependence on \((q,p)\) is strongly continuous. In finite dimension this is
the standard irreducible model singled out, up to unitary equivalence, by the
[[lie-groups/stone-von-neumann-theorem|Stone–von Neumann theorem]].

## References

1. Gerald B. Folland, *Harmonic Analysis in Phase Space*, Annals of Mathematics Studies 122, Princeton University Press, 1989, Chapter 1, §1.3, beginning on p. 21 (the Schrödinger representation). [Electronic edition](https://doi.org/10.1515/9781400882427).
