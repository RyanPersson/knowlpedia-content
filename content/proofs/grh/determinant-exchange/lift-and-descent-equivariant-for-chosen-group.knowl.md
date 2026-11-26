+++
id = "proofs/grh/determinant-exchange/lift-and-descent-equivariant-for-chosen-group"
title = "Lift and descent commute with the finite group of the chosen places"
kind = "lemma"
summary = "Right translation by an integral point of U(W) corresponds, under the theta lift and under the normalized descent, to the action of its reduction at the chosen places on the forms on V."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.DescentPair.omega_fockDatum_eq_inv_prod_smul", "New.DescentPair.coe_formAction", "New.DescentPair.normalizedDescent_mul_eq_normalizedDescent_formAction", "New.DescentPair.thetaLift_formRep"]
lean_files = ["src/New/Determinant/Norms/AdjointThetaLift.lean"]
proof_status = "full"
+++

**Lemma.** Let \(O\) be a [[?lean:New.DescentPair|descent pair]] with spaces \(W\) (rank \(r\ge1\)) and \(V=I_n\), chosen places \(M\), and tame parts \(\psi_w\). Let \(k\) be a finite adelic point of \(U(W)\) in the stabiliser \(K_0\) of the standard lattice, and let \(s=(s_w)_{w\in M}\in\prod_{w\in M}GL_r(k_w)\) be its reduction at the chosen places. Put \(\chi(s)=\prod_{w\in M}\psi_w(\det s_w)\), and let \(k'\) be an integral point of \(U(V)(\mathbb{A}_f)\) whose reduction is \(\operatorname{diag}(s_w,1)\) at each \(w\in M\) (the block \(s_w\) on the basis vectors that come from \(W\)) and \(1\) at the places of the twist. Then:

1. (datum) for every vector \(\xi\) of the weight representation, the [[?c:Weil representation|Weil representation]] of the pair satisfies \(\omega(k,k')\varphi_\xi=\chi(s)^{-1}\varphi_\xi\) for the [[?lean:New.DescentPair.fockDatum|datum]] \(\varphi_\xi\);
2. (action) the [[?lean:New.DescentPair.formAction|action]] of \(s\) on a form \(\Xi\) on \(V\) is \(\chi(s)\) times right translation of \(\Xi\) by \(k'\);
3. (descent) for every form \(\Xi\) on \(V\) and \(g\in U(W)(\mathbb{A})\), the [[?lean:New.DescentPair.normalizedDescent|normalized descent]] satisfies \((\theta\Xi)(gk)=\theta(s\cdot\Xi)(g)\);
4. (lift) if \(l\) fits the pair and \(y\) is a form on \(W\) of parameter \(l\), the [[proofs/grh/determinant-exchange/theta-lift-of-descent-pair|theta lift]] satisfies \(\Theta_W(R(k)y)=s\cdot\Theta_W(y)\), where \(R(k)\) is right translation.

## Proof

(1) Finite adelic points act only on the finite part \(\Psi_{\mathrm{bl}}\otimes\mathrm{vac}\) of the datum. The transformation law of the block datum under pairs of integral points with matching reductions ([[?lean:New.DescentPair.omega_blockDatum_eq_smul|transformation law of the block datum]]) gives the factor \(\chi(s)^{-1}\).

(2) This is the definition of the action: it is built from right translation by a lift of the family \(\operatorname{diag}(s_w,1)\), multiplied by \(\chi(s)\) so that it does not depend on the lift.

(4) Let \(L\) be the lift by \(\varphi_0=\varphi_{\xi_0}\), so that \((Ly)(h)=\int_{[U(W)]}y(g)\,\theta(\omega(g,h)\varphi_0)\,dg\). Replacing \(g\) by \(gk\) in the integral and using (1),
\[
(Ly)(hk')=\int y(gk)\,\theta\bigl(\omega(g,h)\omega(k,k')\varphi_0\bigr)\,dg=\chi(s)^{-1}\,L(R(k)y)(h)
\]
([[?lean:New.IsArrow.formRep_formLift_of_eq_smul|equivariance of the lift by an arrow]]). The passage to algebraic forms commutes with right translation by finite points, so \(R(k')\Theta_Wy=\chi(s)^{-1}\Theta_W(R(k)y)\). By (2), \(s\cdot\Theta_Wy=\chi(s)R(k')\Theta_Wy=\Theta_W(R(k)y)\); here \(\chi(s)\neq0\) because each \(\det s_w\) is a unit.

(3) The normalized descent is a scalar multiple of the complex conjugate of the transposed lift (from \(V\) to \(W\)) of the conjugate form, by the datum \(\varphi_{\xi_0}\) of the highest vector ([[?lean:New.DescentPair.normalizedDescent_eq_smul_star_lift_swap|descent as conjugate transposed lift]]). The transposed lift is equivariant under the pair \((k',k)\), which by (1) scales the datum by \(\chi(s)^{-1}\). On the other side, by (2), \(s\cdot\Xi=\chi(s)R(k')\Xi\); conjugating the form turns \(\chi(s)\) into \(\overline{\chi(s)}=\chi(s)^{-1}\), since \(\chi(s)\) is a product of values of characters of finite groups. The two scalars agree, which is the claim.

## References

1. Lean: `New.DescentPair.normalizedDescent_mul_eq_normalizedDescent_formAction`, `New.DescentPair.thetaLift_formRep` in `src/New/Determinant/Norms/AdjointThetaLift.lean`.
