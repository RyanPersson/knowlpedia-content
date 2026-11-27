+++
id = "proofs/grh/spanning-unfolding-b/freeness-in-small-rank"
title = "Freeness of the level in rank at most k"
kind = "lemma"
summary = "For an admissible filling datum over a CM field containing a primitive 5040-th root of unity, a rational element of a definite unitary group of rank at most k whose conjugate is integral and reduces to one at the chosen places above one level prime is trivial."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.eq_one_of_reduceAt_eq_one"]
lean_files = ["src/New/Spanning/Unfolding/BesselLevelStructure.lean"]
proof_status = "full"
+++

**Lemma.** Let \(E\) be a CM field containing a primitive \(5040\)-th root of unity ([[?lean:New.HasPrimitiveRoot5040|stably unramified]]) and \(S\) an [[proofs/grh/spanning-unfolding-b/filling-admissible|admissible]] [[proofs/grh/spanning-unfolding-b/filling-data|filling datum]] over \(E\). Let \(n\) be a finite set with \(\lvert n\rvert\le k\), let \(\gamma\) be a rational point of the unitary group of the standard hermitian form on \(E^n\), and \(g\) a finite adelic point of that group. Let \(i\in\{0,1\}\). If \(g^{-1}\gamma g\) is integral (it and its inverse have entries in \(\widehat{\mathcal{O}}\)) and reduces to the identity modulo every chosen place \(w\in C_i\), then \(\gamma=1\).

## Proof

By the [[?lean:New.Variety.eq_one_of_reduceAt_eq_one|freeness criterion for the definite standard space]], it suffices that the places \(w\in C_i\) are distinct and that the product of their residue cardinalities exceeds \((2\lvert n\rvert)^{[E:\mathbb{Q}]}\). There are \(f=[E:\mathbb{Q}]/2\) places in \(C_i\), each of residue cardinality \(p_i\), so the product is \(p_i^{f}\), and \((2\lvert n\rvert)^{[E:\mathbb{Q}]}=\bigl((2\lvert n\rvert)^2\bigr)^{f}\). So it suffices that \((2\lvert n\rvert)^2<p_i\). Since \(1000(2\varrho+2)\le k\) forces \(k\ge2\), we get \(2\lvert n\rvert\le2k\le k^2\) and
\[
(2\lvert n\rvert)^2\le k^4<k^{10}\le b^{10}\le p_i ,
\]
using \(k\le b\) and \(b^{10}\le p_i\) from the size conditions of a filling datum.

## Remarks

The Lean proof does not use the admissibility hypothesis beyond the conditions of the filling datum; it is carried as an instance argument. The criterion compares the trace of \(\gamma-1\), an algebraic integer divisible by the product of the chosen places whose conjugates have modulus at most \(2\lvert n\rvert\), with its norm.

## References

1. Lean: `New.Filling.eq_one_of_reduceAt_eq_one` in `src/New/Spanning/Unfolding/BesselLevelStructure.lean`; it applies `New.Variety.eq_one_of_reduceAt_eq_one` in `src/Lib/Shimura/HeckeTower/HeckeData.lean`.
