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

A single lift is a class integral: the value of the lift of a form \(\psi\) at \(g'\) is the integral over \(\Gamma_j\backslash G_f(X_j)\) of \(h\mapsto\mathcal K_j(\Phi;h,g')\psi(h)\). For a single \(x\) the integrand of the composite need not be invariant under the level \(K_j\) on the right, because \(\Phi_{x,j}\) is not assumed invariant. So one proceeds as follows ([[?lean:New.IsJointlyInvariant.sum_chain_eq_sum_kernelProduct|`IsJointlyInvariant.sum_chain_eq_sum_kernelProduct`]], quoted from the chapter on the objects of the upper bound).

1. Write the value \(C_\Psi(\varphi)(g_m)\) as an iterated class integral of the integrand \(\sum_{x}\Psi(x)\,\mathcal K_{m-1}(\Phi_{x,m-1};h_{m-1},g_m)\cdots\mathcal K_0(\Phi_{x,0};h_0,h_1)\varphi(h_0)\), the sum over \(x\in\operatorname{supp}\Psi\) taken inside, with the last kernel included.
2. Joint invariance of the tensor \(\sum_x\Psi(x)\Phi_{x,m-1}\otimes\cdots\otimes\Phi_{x,0}\), together with the invariance of \(\varphi\) under \(K_0\), shows that this summed integrand is invariant under right translation of each variable \(h_j\) by \(K_j\), \(j<m\).
3. For \(j<m\) the level \(K_j\) lies in the principal congruence subgroup at the chosen places and \(n_j\le2n_m\), so the groups \(\Gamma_j\cap hK_jh^{-1}\) are trivial ([[?lean:New.Data.classAut_eq_bot_of_le_chosenLevel|`classAut_eq_bot_of_le_chosenLevel`]], quoted). Hence the integral of a right \(K_j\)-invariant function is the unweighted sum of its values at the representatives of the classes.

This gives the displayed sum over tuples of classes. \(\blacksquare\)

*Status.* This file only specialises the quoted general statement to the data, supplying the freeness of the levels; the three steps describe the quoted proof.

## References

1. Lean: `New.Data.chainCombination_eq_sum` in `src/New/UpperBound/Divisibility/ChainValuation.lean`.
