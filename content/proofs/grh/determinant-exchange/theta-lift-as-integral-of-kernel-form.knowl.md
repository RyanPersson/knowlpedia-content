+++
id = "proofs/grh/determinant-exchange/theta-lift-as-integral-of-kernel-form"
title = "The theta lift is the integral against the kernel form"
kind = "lemma"
summary = "The theta lift of a form y on W is the integral over [U(W)] of y(g) times the kernel form at g, as a vector-valued integral in the space of forms on V."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.DescentPair.thetaLift_eq_integral", "New.DescentPair.integrable_smul_vectorKernelForm", "New.DescentPair.ofAlgForm_vectorKernelForm"]
lean_files = ["src/New/Determinant/Norms/AdjointThetaLift.lean"]
proof_status = "full"
+++

**Lemma.** Let \(O\) be a [[?lean:New.DescentPair|descent pair]] with spaces \(W\) (rank \(r\ge1\)) and \(V=I_n\), let \(l\) fit the pair and let \(y\) be a form on \(W\) of parameter \(l\). Let \(\theta_W(g,\cdot)\) be the [[proofs/grh/determinant-exchange/vector-kernel-equivariance|kernel form]] at \(g\in U(W)(\mathbb{A})\). Then \(g\mapsto y(g)\,\theta_W(g,\cdot)\) is integrable on \([U(W)]\) for the measure of the Petersson product, with values in the finite-dimensional space of forms on \(V\), and
\[
\Theta_Wy=\int_{[U(W)]}y(g)\,\theta_W(g,\cdot)\,dg
\]
([[measure-theory/bochner-integral|Bochner integral]]), where \(\Theta_W\) is the [[proofs/grh/determinant-exchange/theta-lift-of-descent-pair|theta lift]] of the pair.

## Proof

*The kernel form as a scalar kernel.* Let \(\xi_0\) be the highest weight vector and \(\varphi_0=\varphi_{\xi_0}\). The function on \(U(V)(\mathbb{A})\) attached to an algebraic form \(\Xi\) is \((x,k)\mapsto\langle\xi_0,\rho(x)^{-1}\Xi(k)\rangle\), for \(x\) in the compact real group and \(k\) finite. For the kernel form this is
\[
\langle\xi_0,\rho(x^{-1})\theta_W(g,k)\rangle=\langle\rho(x)\xi_0,\theta_W(g,k)\rangle=\theta_{\varphi_{\overline{\rho(x)\xi_0}}}(g,(1,k)) .
\]
The real point \(x\) acts on data by \(\omega(1,x)\varphi_{\xi}=\varphi_{\overline{\rho(x)\bar\xi}}\) ([[?lean:New.DescentPair.omega_fockDatum_star|action of real points on the datum]]), and \(\xi_0\) is real, so the right side is \(\theta_{\omega(1,x)\varphi_0}(g,(1,k))=\theta_{\varphi_0}(g,(x,k))\). Thus the function attached to the kernel form at \(g\) is \(h\mapsto\theta_{\varphi_0}(g,h)\).

*Integrability.* Let \((b_i)\) be an orthonormal basis of the forms on \(V\). By the [[proofs/grh/determinant-exchange/descent-as-pairing-with-kernel-form|pairing formula]], the coordinate of \(\theta_W(g,\cdot)\) along \(b_i\) is \(\langle b_i,\theta_W(g,\cdot)\rangle=\overline{(\theta b_i)(g)}\). By [[proofs/grh/determinant-exchange/descent-adjoint-to-theta-lift|the adjointness theorem]] \(\theta b_i\) is a form on \(W\), and forms are square integrable, so \(y\cdot\overline{\theta b_i}\) is integrable. Summing over the finitely many \(i\) gives the integrability of \(g\mapsto y(g)\theta_W(g,\cdot)\).

*The formula.* The passage from algebraic forms to functions on \(U(V)(\mathbb{A})\) is injective, so it suffices to compare values of the attached functions at each \(h\). Evaluation at \(h\) of the attached function is a continuous linear functional on the space of forms, so it commutes with the integral; by the first step it sends the right side to \(\int y(g)\theta_{\varphi_0}(g,h)\,dg\), which is the value at \(h\) of the lift of \(y\) by \(\varphi_0\), the function attached to \(\Theta_Wy\).

## References

1. Lean: `New.DescentPair.thetaLift_eq_integral`, `New.DescentPair.ofAlgForm_vectorKernelForm` in `src/New/Determinant/Norms/AdjointThetaLift.lean`.
