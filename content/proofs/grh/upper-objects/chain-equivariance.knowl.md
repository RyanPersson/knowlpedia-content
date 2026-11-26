+++
id = "proofs/grh/upper-objects/chain-equivariance"
title = "Equivariance of a chain of lifts"
kind = "lemma"
summary = "Moving the data of a chain of lifts by a tuple of group elements and translating the source form by the first element translates the result by the last; hence an element acting trivially through every kernel may be moved to the source."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.TensorChain.lift_kernelLift_map_omega", "New.TensorChain.lift_algFormRep_of_map_eq", "New.chain_equivariant"]
lean_files = ["src/New/UpperBound/Objects/LiftChains.lean"]
proof_status = "full"
+++

Notation as in [[proofs/grh/upper-objects/chain-of-lifts|chain of lifts]]; \(R(a)\) denotes right translation of algebraic forms by \(a\). For a tensor \(t\in S_{m-1}\otimes\dots\otimes S_0\) write \(\operatorname{chain}_m(t)\) for the linear extension of the chain to tensors of data.

**Lemma.** Let \(a_j\in G_j\) for all \(j\).

1. For all \(\varphi\in\mathcal A_0\), \(m\ge0\) and \(t\): \(\operatorname{chain}_m\big((\textstyle\bigotimes_{i<m}\omega_i(a_i,a_{i+1}))\,t\big)\big(R(a_0)\varphi\big)=R(a_m)\operatorname{chain}_m(t)\varphi\).
2. If \(\varphi\) is fixed by \(K_0\) and \(a_j\in K_j\) for all \(j\), then \(\operatorname{chain}_j\big((\omega_i(a_i,a_{i+1})\Phi_i)_i\big)\varphi=R(a_j)\operatorname{chain}_j(\Phi)\varphi\).
3. Let \(z_i\in G_i\) with \(\omega_i(z_i,z_{i+1})=1\) for all \(i\), let \(j<m\) and let \(t\) be fixed by \(\omega_j(1,z_{j+1})\) acting on the factor \(S_j\) alone. Then \(\operatorname{chain}_m(t)(R(z_0)\varphi)=\operatorname{chain}_m(t)\varphi\).

## Proof

*1.* Induction on \(m\); for \(m=0\) the tensor is a scalar. For the step both sides are linear in \(t\), so take \(t=s\otimes r\) with \(s\in S_m\): by the induction hypothesis the inner chain is \(R(a_m)\operatorname{chain}_m(r)\varphi\), and one lift is equivariant: \(k_m.\mathrm{lift}(\omega_m(a_m,a_{m+1})s)(R(a_m)\psi)=R(a_{m+1})\,k_m.\mathrm{lift}(s)\psi\) ([[?lean:New.Kernel.lift_equivariant|equivariance of the lift]]; a change of variables in the class integral).

*2.* Special case of 1 with a pure tensor, since \(R(a_0)\varphi=\varphi\).

*3.* Put \(a_i=z_i^{-1}\) for \(i\le j\) and \(a_i=1\) for \(i>j\). Since \(\omega_i(z_i,z_{i+1})=1\), \(\omega_i(g,g')=\omega_i(gz_i,g'z_{i+1})\). Hence \(\omega_i(a_i,a_{i+1})=1\) for \(i<j\) and for \(i>j\), and \(\omega_j(a_j,a_{j+1})=\omega_j(z_j^{-1},1)=\omega_j(1,z_{j+1})\). So the tensor of these operators fixes \(t\), and 1 applied to \(R(z_0)\varphi\) gives \(\operatorname{chain}_m(t)(R(z_0^{-1})R(z_0)\varphi)=R(a_m)\operatorname{chain}_m(t)(R(z_0)\varphi)\) with \(a_m=1\) as \(j<m\). \(\square\)

## References

1. Lean: `New.TensorChain.lift_kernelLift_map_omega`, `New.TensorChain.lift_algFormRep_of_map_eq`, `New.chain_equivariant` in `src/New/UpperBound/Objects/LiftChains.lean`.
