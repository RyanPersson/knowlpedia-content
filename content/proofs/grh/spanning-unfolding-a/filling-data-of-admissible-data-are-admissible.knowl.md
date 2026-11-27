+++
id = "proofs/grh/spanning-unfolding-a/filling-data-of-admissible-data-are-admissible"
title = "The filling data of admissible data satisfy the standing hypotheses"
kind = "theorem"
summary = "For admissible data D the filling data satisfy IsAdmissible: level, surjective reduction and all size inequalities."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.instIsAdmissibleFilling", "New.Data.filling_reduction_surjective", "New.Data.N_le_pow", "New.Data.pow_div_le_pow_sub_one"]
lean_files = ["src/New/Spanning/Unfolding/FillingAdmissible.lean"]
proof_status = "full"
+++

**Theorem.** Let \(D\) be [[?lean:New.Data|admissible data]]. Its [[?lean:New.Data.filling|filling data]] \(S_D\) satisfy the [[?lean:New.Filling.IsAdmissible|standing hypotheses]] of the filling theorem, namely:

1. the source level is the preimage in \(U(X_0)(\mathbb A_f)\) of the [[?c:Principal congruence subgroup|principal congruence subgroup]] \(K(M)\);
2. reduction at the chosen places maps the lattice stabiliser \(K\) onto the residue group \(\prod_wGL_r(k_w)\);
3. \(\lvert\varpi\rvert_v\le b\), and \(1\le\lvert\kappa_v\rvert\le b^{23}\) at every [[?c:Infinite place of a number field|infinite place]], where \(\lvert\kappa_v\rvert=M\lvert\varpi\rvert_v/(2\pi)\);
4. \(N\le b^{60n}\), \(n=\varrho+1\);
5. \(b^{11kf}\,\mathcal I\le\mathcal M\le(M/b^6)^{kf}\,\mathcal I\) for the main and identity second moments;
6. the number of tuples of Bessel coordinates is at most \(b^{2kf}\);
7. \((N^k/b)^f\le[K_0:\iota^{-1}(K)]\);
8. the bound for the scaled Siegel constant.

## Proof

1. This is the identification of the level of \(X_0\) ([[?lean:New.Data.levelX_zero_eq_comap|the level of \(X_0\) as a preimage]]).
2. Given residues \(x\), lift them to an integral finite adelic point of the group of \(Y_0\) in orthonormal local bases ([[?lean:New.liftResidue|lifting residues]]) and transport it by the identification \(\psi\) of the [[proofs/grh/spanning-unfolding-a/filling-data-fit-the-space-y0|fitting]] space, which preserves integrality and reductions ([[proofs/grh/spanning-unfolding-a/space-fitting-filling-data|property 2 of fitting spaces]]).
3. \(\lvert\varpi\rvert_v\le b\) is the lemma on the [[proofs/grh/spanning-unfolding-a/size-of-different-generator-at-infinite-places|size of the generator of the different]]; the bounds for \(\kappa_v\) are comparisons of the size calculus of the data ([[?lean:New.Data.le_of_hasLogBound|comparison of logarithmic bounds]]).
4. \(\log N\le30\,m\log b\) with \(m=2\varrho+2\) ([[?lean:New.Data.log_N_mem_Icc|range of \(\log N\)]]), and \(30(2\varrho+2)=60n\).
5. The theorem on the [[proofs/grh/spanning-unfolding-a/ratio-of-main-and-identity-second-moments|ratio of the second moments]], with \(\mathcal I>0\).
6. The lemma on the [[proofs/grh/spanning-unfolding-a/number-of-bessel-coordinates|number of Bessel coordinates]].
7. The index is \((N^k-1)^f\) ([[proofs/grh/spanning-unfolding-a/number-of-classes-of-the-source-level|number of classes]], item 1), and \(N^k/b\le N^k/2\le N^k-1\) because \(b\ge2\) and \(N^k\ge2\).
8. The lemma on the [[proofs/grh/spanning-unfolding-a/scaled-siegel-constant-bound|scaled Siegel constant]].

## References

1. Lean: the instance `D.filling.IsAdmissible` (anonymous instance in namespace `New.Data`; the name `New.Data.instIsAdmissibleFilling` in the front matter is the expected auto-generated name and was not checked), with `New.Data.filling_reduction_surjective`, `New.Data.N_le_pow`, `New.Data.pow_div_le_pow_sub_one`, in `src/New/Spanning/Unfolding/FillingAdmissible.lean`.
