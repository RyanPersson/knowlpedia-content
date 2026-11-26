+++
id = "proofs/grh/derivatives-vacuum/errors-covered-by-the-loss-product"
title = "The errors at one place are covered by the loss product"
kind = "lemma"
summary = "For a prime p at most k the three error terms at one place add up to at most 3b/(kp), which is at most the valuation of the loss product."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.error_le_padicValNat_lossProduct"]
lean_files = ["src/New/Derivatives/Sharpness/NearPairs.lean"]
proof_status = "outline"
+++

**Lemma.** Let \(D\) be admissible data, \(p\le k\) a prime and \(l\in\mathbb{N}\). Then
\[ 3(\log b+2)+x^{42}+1+l_0\,\frac{a}{x_1}+\frac{2b}{kp}\ \le\ v_p\bigl(B(l)\bigr), \]
with \(B(l)\) the [[proofs/grh/derivatives-vacuum/loss-product|loss product]].

## Proof

Three scale inequalities of the data are used; they are verified in Lean by the magnitude calculus ([[?lean:New.Data.le_of_hasLogBound|comparison of logarithmic sizes]]) and asserted here:
\[ 3(\log b+2)+x^{42}+1\le\frac{a}{x_1},\qquad 1\le\frac{a}{x_1},\qquad(81s+1)\frac{a}{x_1}\le\frac{b}{k^2}. \]
With \(l_0\le81s\) and \(p\le k\), the last gives \((l_0+1)a/x_1\le b/(kp)\). So the left side is at most \((l_0+1)a/x_1+2b/(kp)\le3b/(kp)\). On the other hand \(n^\sharp/p\ge6b/(kp)\), so \(3b/(kp)\le n^\sharp/p-3b/(kp)\le n^\sharp/p-1\) (using \(1\le(l_0+1)a/x_1\le b/(kp)\)), and \(n^\sharp/p-1\le v_p(B(l))\) by property 3 of the loss product.

## References

1. Lean: `New.Data.error_le_padicValNat_lossProduct` in `src/New/Derivatives/Sharpness/NearPairs.lean`.
