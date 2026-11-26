+++
id = "proofs/grh/upper-elementary-divisors/number-of-flags-bound"
title = "Parahoric index times the number of flags of the Levi subgroup"
kind = "lemma"
summary = "The index of a two-block parahoric subgroup of GL_k(W) times the index of the lower Iwahori subgroup in its Levi subgroup is at most the number of full flags over the residue field."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.FrobeniusCycle.index_mul_relIndex_le", "New.index_borel_le"]
lean_files = ["src/New/UpperBound/ElementaryDivisors/DefectCount.lean"]
proof_status = "full"
+++

**Lemma.** Let \(W\) be a local ring whose residue field \(\kappa\) is finite with \(q\) elements, \(0\le r\), and in \(\mathrm{GL}_k(W)\) let \(\mathrm{Par}_r\) be the parahoric subgroup of the blocks \(\{b<r\},\{b\ge r\}\), \(L_r\) the block diagonal subgroup, and \(\mathrm{Iw}^{-}\) the lower Iwahori subgroup. Then
\[
[\mathrm{GL}_k(W):\mathrm{Par}_r]\cdot[L_r:L_r\cap\mathrm{Iw}^{-}]\ \le\ \prod_{l=0}^{k-1}\frac{q^{l+1}-1}{q-1}.
\]

## Proof

\(L_r\subseteq\mathrm{Par}_r\) and \(\mathrm{Iw}^{-}\subseteq\mathrm{Par}_r\) (if \(i<r\le j\) then \(i<j\)), so \([L_r:L_r\cap\mathrm{Iw}^{-}]\le[\mathrm{Par}_r:\mathrm{Iw}^{-}]\) and the left side is at most \([\mathrm{GL}_k(W):\mathrm{Iw}^{-}]\). \(\mathrm{Iw}^{-}\) is the preimage of the group \(B^{-}(\kappa)\) of lower triangular matrices under reduction \(\mathrm{GL}_k(W)\to\mathrm{GL}_k(\kappa)\), so its index is at most \([\mathrm{GL}_k(\kappa):B^{-}(\kappa)]\). Finally \(\#B^{-}(\kappa)\ge\prod_{i<k}(q-1)q^{i}\) (a unit on the diagonal and \(i\) free entries to its left in row \(i\)) and \(\#\mathrm{GL}_k(\kappa)=\prod_{i<k}q^{i}(q^{i+1}-1)\) ([[?c:Order of the general linear group over a finite field|order of \(\mathrm{GL}_k(\mathbb{F}_q)\)]]); divide. \(\square\)

## References

1. Lean: `New.FrobeniusCycle.index_mul_relIndex_le`, `New.index_borel_le` in `src/New/UpperBound/ElementaryDivisors/DefectCount.lean`.
