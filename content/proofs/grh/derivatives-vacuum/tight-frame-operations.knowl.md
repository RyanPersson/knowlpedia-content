+++
id = "proofs/grh/derivatives-vacuum/tight-frame-operations"
title = "Unions of tight frames and replacing pairs by their sums"
kind = "lemma"
summary = "Disjoint unions of tight frames add their lengths, and replacing disjoint pairs of members of a tight frame by their sums changes the length by the integer t when the cross terms sum to t times the identity."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.IsTightFrame.sumElim", "New.IsTightFrame.join_family", "New.IsTightFrame.replace_pairs", "New.finiteImage_add_mem", "New.finiteImage_mul_mem", "New.sum_mul_conj_eq_ofReal_iff"]
lean_files = ["src/New/Derivatives/Vacuum/ShortVectors.lean"]
proof_status = "full"
+++

Let \(E\) be a CM field with CM type \((\Phi_\tau)\) and [[?lean:New.WeilData|Weil data]], and \(\mathfrak{a}_0=E\cap\alpha\widehat{\mathcal{O}}_E\); it is an \(\mathcal{O}_E\)-submodule of \(E\). [[?lean:New.IsTightFrame|Tight frames]] are as recalled in [[proofs/grh/derivatives-vacuum/roots-of-unity-tight-frame|the tight frame of roots of unity]].

**Lemma.**

1. If \((w_i)_{i\in I}\) with multiplicities \((m_i)\) has length \(M\) and \((w'_j)_{j\in J}\) with multiplicities \((m'_j)\) has length \(M'\), their disjoint union has length \(M+M'\).
2. If for each \(i\in I\) the family \((v_{i,j})_{j\in J}\) is a tight frame of length \(L_i\) with multiplicities \(1\), then \((v_{i,j})_{(i,j)\in I\times J}\) is a tight frame of length \(\sum_iL_i\) with multiplicities \(1\).
3. Let \((w_i)_{i\in I}\) be a tight frame of length \(M\) with multiplicities \(1\), and let \((a_j,b_j)_{j\in J}\) be pairwise disjoint pairs of distinct indices (an injection \(J\sqcup J\to I\)). Suppose that for an integer \(t\) and all infinite places \(\sigma,\tau\)
\[ \sum_{j\in J}\Bigl(\Phi_\sigma(w_{a_j})\overline{\Phi_\tau(w_{b_j})}+\Phi_\sigma(w_{b_j})\overline{\Phi_\tau(w_{a_j})}\Bigr)=t\,\delta_{\sigma\tau}. \]
Then \(L=M+t\ge0\), and the family consisting of the unpaired \(w_i\) and the sums \(w_{a_j}+w_{b_j}\), all with multiplicity \(1\), is a tight frame of length \(L\).

## Proof

1 and 2: membership in \(\mathfrak{a}_0\) is inherited, and the frame sums add.

3. Membership: \(\mathfrak{a}_0\) is closed under addition. Expanding \(\Phi_\sigma(w_a+w_b)\overline{\Phi_\tau(w_a+w_b)}\) gives the two diagonal terms, which together with the unpaired members reproduce the frame sum \(M\delta_{\sigma\tau}\) of \(w\), plus the two cross terms, which sum to \(t\delta_{\sigma\tau}\). So the new frame sum is \((M+t)\delta_{\sigma\tau}\). For \(\sigma=\tau\) it is a sum of squared absolute values, hence \(M+t\ge0\).

## References

1. Lean: `New.IsTightFrame.sumElim`, `New.IsTightFrame.join_family`, `New.IsTightFrame.replace_pairs`, `New.finiteImage_add_mem`, `New.finiteImage_mul_mem`, `New.sum_mul_conj_eq_ofReal_iff` in `src/New/Derivatives/Vacuum/ShortVectors.lean`.
