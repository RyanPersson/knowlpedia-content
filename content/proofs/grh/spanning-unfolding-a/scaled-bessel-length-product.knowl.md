+++
id = "proofs/grh/spanning-unfolding-a/scaled-bessel-length-product"
title = "Product of the scaled Bessel lengths"
kind = "definition"
summary = "The product over the infinite places of max(1, besselLength(y_v) / b^(6n))."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.scaledBesselLengthProd", "New.Filling.one_le_scaledBesselLengthProd", "New.Filling.scaledBesselLength_le_scaledBesselLengthProd"]
lean_files = ["src/New/Spanning/Unfolding/AmplitudeSums.lean"]
+++

Let \(S\) be [[?lean:New.Filling|filling data]] over a [[?c:CM field|CM field]] \(E\), with parameter \(b\) and \(n=\varrho+1\). For \(y=(y_v)_v\in G_\infty=\prod_vG_1\), the **product of the scaled Bessel lengths** is
\[
P(y)=\prod_{v}\max\Bigl(1,\ \frac{\ell(y_v)}{b^{6n}}\Bigr),
\]
where the product is over the [[?c:Infinite place of a number field|infinite places]] of \(E\) and \(\ell(x)=\inf_{s}(\lVert s\,x\rVert+1)\) is the [[?lean:New.besselLength|Bessel length]] of \(x\in G_1\) (infimum of [[?c:Operator norm|operator norms]] over the Bessel subgroup); each factor is the [[?lean:New.scaledBesselLength|scaled Bessel length]].

## Properties

\(P(y)\ge1\), and each factor is at most \(P(y)\), since all factors are at least \(1\). In particular \(P(y)\le R\) implies \(\ell(y_v)\le b^{6n}R\) for every \(v\).

## References

1. Lean: `New.Filling.scaledBesselLengthProd` in `src/New/Spanning/Unfolding/AmplitudeSums.lean`.
2. Lean: `New.Filling.one_le_scaledBesselLengthProd` in `src/New/Spanning/Unfolding/AmplitudeSums.lean`.
3. Lean: `New.Filling.scaledBesselLength_le_scaledBesselLengthProd` in `src/New/Spanning/Unfolding/AmplitudeSums.lean`.
