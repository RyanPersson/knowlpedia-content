+++
id = "proofs/grh/upper-objects/jointly-invariant-combination"
title = "Jointly invariant combination of chain data"
kind = "definition"
summary = "A finite combination of tuples of theta data with linear coefficients that is unchanged, tested against all linear maps, by the joint action of the levels on consecutive data."
aliases = ["jointly invariant", "joint invariance"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.IsJointlyInvariant"]
lean_files = ["src/New/UpperBound/Objects/LiftChains.lean"]
+++

Notation as in [[proofs/grh/upper-objects/chain-of-lifts|chain of lifts]]. Let \(m\ge0\), let \(\mathsf M\) be a complex vector space, \(s\) a finite set, and for each \(x\in s\) let \(L_x\colon\mathcal V_m\to\mathsf M\) be linear and \(\Phi_x=(\Phi_{x,j})_j\) a family of data, \(\Phi_{x,j}\in S_j\).

**Definition.** The combination \(\sum_{x\in s}L_x\otimes\Phi_{x,m-1}\otimes\dots\otimes\Phi_{x,0}\) is **jointly invariant** (for the levels \(K_j\)) if for every tuple \(a=(a_j)\) with \(a_j\in K_j\) and \(a_j=1\) for \(j\ge m\), and every linear map \(\beta\colon S_{m-1}\otimes\dots\otimes S_0\to\mathcal V_m\),
\[
\sum_{x\in s}L_x\Big(\beta\big(\textstyle\bigotimes_{j<m}\omega_j(a_j,a_{j+1})\Phi_{x,j}\big)\Big)=\sum_{x\in s}L_x\Big(\beta\big(\textstyle\bigotimes_{j<m}\Phi_{x,j}\big)\Big).
\]

## Remarks

Equivalently, the element \(\sum_xL_x\otimes\bigotimes_j\Phi_{x,j}\) of \(\operatorname{Hom}(\mathcal V_m,\mathsf M)\otimes S_{m-1}\otimes\dots\otimes S_0\) is fixed by the joint action; the definition is phrased with test maps \(\beta\) to avoid the tensor product with the coefficients.

## References

1. Lean: `New.IsJointlyInvariant` in `src/New/UpperBound/Objects/LiftChains.lean`.
