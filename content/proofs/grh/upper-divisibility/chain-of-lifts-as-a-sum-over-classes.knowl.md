+++
id = "proofs/grh/upper-divisibility/chain-of-lifts-as-a-sum-over-classes"
title = "A chain of lifts is a plain sum over classes"
kind = "theorem"
summary = "For jointly invariant data, the value of a combination of chains of m theta lifts is a finite sum, over tuples of classes and over the support, of products of kernels applied to a value of the source form."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.chainCombination_eq_sum"]
lean_files = ["src/New/UpperBound/Divisibility/ChainValuation.lean"]
proof_status = "outline"
+++

**Theorem.** Let \(D\) be [[?lean:New.Data|admissible data]], \(\vartheta\) a [[?lean:New.Data.Twist|twist]], and for \(j\ge0\) let \(\mathcal K_j\) be the [[?lean:New.Data.liftKernel|theta kernel]] from forms on \(X_j\) to forms on \(X_{j+1}\) for \(\vartheta\). Let \(\Psi\) be a finitely supported complex function on the [[?lean:New.Data.Translations|tuples of translations]] \(x=(x_j)\), and for each \(x\) and \(j\) let \(\Phi_{x,j}\) be a datum (a vector of the finite part of the Weil representation of \(\operatorname{Hom}(X_j,X_{j+1})\)). Assume that the tensor \(\sum_x\Psi(x)\,\Phi_{x,m-1}\otimes\cdots\otimes\Phi_{x,0}\) is [[?lean:New.IsJointlyInvariant|jointly invariant]] under the levels \(K_j\) of the stages \(j<m\). Let \(\varphi\) be a source form and \(g_j\in G_f(X_j)\) points. Then the [[?lean:New.Data.chainCombination|combination of chains]]
\[
C_\Psi(\varphi)=\sum_x\Psi(x)\,\bigl(\text{lift with }\Phi_{x,m-1}\bigr)\circ\cdots\circ\bigl(\text{lift with }\Phi_{x,0}\bigr)(\varphi)
\]
has the value
\[
C_\Psi(\varphi)(g_m)=\sum_{c=(c_j)_{j<m}}\ \sum_{x\in\operatorname{supp}\Psi}\Psi(x)\cdot\mathcal K_{m-1}\bigl(\Phi_{x,m-1};h_{m-1},g_m\bigr)\cdots\mathcal K_0\bigl(\Phi_{x,0};h_0,h_1\bigr)\,\varphi(h_0),
\]
where \(c_j\) runs over the classes \(\Gamma_j\backslash G_f(X_j)/K_j\), and \(h_j\) is the representative point of \(c_j\) (the [[?lean:New.classPoints|class points]] of \(c\) and \(g\)).

## Proof

Each single lift is by definition a sum over classes of the lower group weighted by the reciprocal of the order of the automorphism group \(\Gamma\cap hK_jh^{-1}\) of the class. For \(j<m\) the level \(K_j\) lies in the principal congruence subgroup at the chosen places and the rank \(n_j\le2n_m\), so these groups are trivial ([[?lean:New.Data.classAut_eq_bot_of_le_chosenLevel|`classAut_eq_bot_of_le_chosenLevel`]], quoted): the sums are plain. That, for jointly invariant data, the iterated class sums combine into the displayed sum over tuples of classes is [[?lean:New.IsJointlyInvariant.sum_chain_eq_sum_kernelProduct|`IsJointlyInvariant.sum_chain_eq_sum_kernelProduct`]] (quoted; individual terms \(\Phi_{x,j}\) need not be invariant, only the combination, and the intermediate forms are fixed by the levels only after summation over \(x\)). \(\blacksquare\)

*Status.* This file only specialises the quoted general statement to the data, supplying the freeness of the levels.

## References

1. Lean: `New.Data.chainCombination_eq_sum` in `src/New/UpperBound/Divisibility/ChainValuation.lean`.
