+++
id = "proofs/grh/determinant-exchange/vector-kernel-equivariance"
title = "Equivariance of the vector-valued theta kernel; the kernel as an algebraic form"
kind = "lemma"
summary = "The vector-valued theta kernel transforms by the weight representation under rational points and by the level character under the level, so it is an algebraic form on V."
aliases = ["vector kernel form"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.DescentPair.vectorKernel_equivariant", "New.DescentPair.vectorKernel_rational_mul", "New.DescentPair.vectorKernel_mul_level", "New.DescentPair.vectorKernelForm", "New.DescentPair.vectorKernelForm_apply"]
lean_files = ["src/New/Determinant/Norms/VectorKernel.lean"]
proof_status = "full"
+++

**Lemma.** Let \(O\) be a [[?lean:New.DescentPair|descent pair]] over a [[?c:CM field|CM field]] \(E\) with Weil data, with spaces \(W\) and \(V=I_n\), and let \(\theta_W\) be its [[proofs/grh/determinant-exchange/vector-valued-theta-kernel|vector-valued theta kernel]]. Let \(\rho\) be the representation of \(U(V)(E)\) of the weight \((k,e)\) of the pair, let \(K\) be the [[?lean:New.DescentPair.levelGroup|level]] of the pair in \(U(V)(\mathbb{A}_f)\) and \(c:K\to\mathbb{C}^\times\) its [[?lean:New.DescentPair.levelChar|level character]]
\[
c(k)=\prod_{w\in Q}\psi_w^{-1}(\det k_w),
\]
where \(Q\) is the family of places of the twist, \(\psi_w\) is the tame part of the character of the pair at \(w\) and \(k_w\) is the diagonal block, on the basis vectors of \(V\) that come from \(W\), of the reduction of \(k\) at \(w\). Then for every \(g\in U(W)(\mathbb{A})\), every rational point \(\gamma\in U(V)(E)\), every \(x\in U(V)(\mathbb{A}_f)\) and every \(k\in K\),
\[
\theta_W(g,\gamma xk)=c(k)\,\rho(\gamma)\,\theta_W(g,x).
\]
In particular \(\theta_W(g,\gamma x)=\rho(\gamma)\theta_W(g,x)\) and \(\theta_W(g,xk)=c(k)\theta_W(g,x)\), so for each \(g\) the function \(\theta_W(g,\cdot)\) is one of the [[?lean:New.DescentPair.FormV|algebraic forms on \(V\)]] of the pair (weight \((k,e)\), level \(K\), character \(c\)). This form is called the **kernel form** at \(g\).

## Proof

Write \(\langle\cdot,\cdot\rangle\) for the Gram pairing and \(\kappa_{g,h}\) for the conjugate kernel, so that \(\langle\theta_W(g,h),\xi\rangle=\kappa_{g,h}(\xi)\). The input from the definition of the pair is the equivariance of the conjugate kernel ([[?lean:New.DescentPair.conjKernel_equivariant|equivariance of the conjugate kernel]]):
\[
\kappa_{g,\gamma xk}\bigl(c(k)\rho(\gamma)v\bigr)=\kappa_{g,x}(v)\qquad\text{for all }v .
\]
The character \(c\) has finite order, so \(\lvert c(k)\rvert=1\), and \(\rho(\gamma)\) preserves the Gram pairing. Hence the operator \(A=c(k)\rho(\gamma)\) is unitary for the pairing; it is onto, with \(A^{-1}=\overline{c(k)}\rho(\gamma^{-1})\).

Since the Gram pairing is nondegenerate, it suffices to show \(\langle\zeta,\theta_W(g,\gamma xk)\rangle=\langle\zeta,A\theta_W(g,x)\rangle\) for all \(\zeta\). Write \(\zeta=Av\). Then
\[
\langle Av,\theta_W(g,\gamma xk)\rangle=\overline{\kappa_{g,\gamma xk}(Av)}=\overline{\kappa_{g,x}(v)}=\langle v,\theta_W(g,x)\rangle=\langle Av,A\theta_W(g,x)\rangle .
\]
The two special cases are \(k=1\) and \(\gamma=1\). For the last statement, \(\theta_W(g,\cdot)\) is an eigenfunction of right translation by the open subgroup \(K\), hence smooth, and it has the two transformation laws that define the forms on \(V\).

## References

1. Lean: `New.DescentPair.vectorKernel_equivariant`, `New.DescentPair.vectorKernelForm` in `src/New/Determinant/Norms/VectorKernel.lean`.
