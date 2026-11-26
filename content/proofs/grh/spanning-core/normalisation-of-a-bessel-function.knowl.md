+++
id = "proofs/grh/spanning-core/normalisation-of-a-bessel-function"
title = "Normalisation of a Bessel function and of its cut"
kind = "theorem"
summary = "For an integrable Bessel function of irreducible type the operator integral of W tensor W* over the quotient by the unipotent group is a scalar; it is 1 for the full function of a Bessel system and between 0 and 1 for its cut."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.IsBesselFunction.integral_mul_conj_eq", "New.IsBesselFunction.integral_mul_conj_embedH_mul", "New.BesselSystem.orthonormal", "New.IsCutPair.integrable_cut", "New.IsCutPair.exists_integral_cut_mul_conj_eq", "New.IsCutPair.lintegral_sq_inner_cut_le"]
lean_files = ["src/New/Spanning/Bessel/Orthonormality.lean"]
proof_status = "full"
+++

**Theorem.** Let \(G_1\), \(\mathsf U\), \(U(\kappa)\) and the measure \(\mu\) for \(\mathsf U\backslash G_1\) be as for [[proofs/grh/spanning-core/cut-pair-of-bessel-functions|cut pairs]]. Let \(I\) be a finite nonempty set and \(\mathrm{rep}\colon U(\kappa)\to U(I)\) a homomorphism such that every \(I\times I\) matrix commuting with all \(\mathrm{rep}(h)\) is scalar.

1. Let \(W\colon G_1\to\mathbb{C}^I\) be a [[?lean:New.IsBesselFunction|Bessel function of type \(\mathrm{rep}\)]] that is \(\mu\)-integrable. Then for \(i,j\in I\)
\[
\int W_i(y)\overline{W_j(y)}\,d\mu(y)=\delta_{ij}\cdot\frac1{\lvert I\rvert}\int\lVert W(y)\rVert^2d\mu(y).
\]
2. For a [[proofs/grh/spanning-core/bessel-system|Bessel system]], the coordinates of the full function are orthonormal: \(\int W_i\overline{W_j}\,d\mu=\delta_{ij}\).
3. For a cut pair \((W,W^\flat)\) of type \(\mathrm{rep}\), \(W^\flat\) is \(\mu\)-integrable, and there is \(c\in[0,1]\) with \(\int W^\flat_i\overline{W^\flat_j}\,d\mu=c\,\delta_{ij}\). Consequently, for every \(v\in\mathbb{C}^I\),
\[
\int\lvert\langle v,W^\flat(y)\rangle\rvert^2d\mu(y)\le\lVert v\rVert^2 .
\]

## Proof

(1) The products \(W_i\overline{W_j}\) are integrable (integrable times bounded). Let \(M_{ij}=\int W_i\overline{W_j}\,d\mu\).

*Invariance.* For \(s\in U(\kappa)\), \(\int W_i(sy)\overline{W_j(sy)}\,d\mu(y)=\int W_i\overline{W_j}\,d\mu\). Indeed the function \(y\mapsto W_i(y)\overline{W_j(y)}\) is left \(\mathsf U\)-invariant, because the character values \(\psi(u)\overline{\psi(u)}=1\) cancel; \(s\) normalises \(\mathsf U\), conjugation by \(s\) preserves the Haar measure of \(\mathsf U\) (library statement `New.RealPlace.measurePreserving_conj_bessel`), left translation preserves the Haar measure of \(G_1\), and \(s(uy)=(sus^{-1})(sy)\); for such data the measure \(\mu\) gives the same integral to a \(\mathsf U\)-invariant function and its translate (library statement `New.identDistrib_orbitMeasure_comp`).

*Commutation.* With \(R=\mathrm{rep}(s)\), \(W(sy)=RW(y)\), so \(W_p(sy)\overline{W_q(sy)}=\sum_{k,l}R_{pk}W_k(y)\overline{W_l(y)}\,\overline{R_{ql}}\). Integrating and using invariance, \(RMR^*=M\); as \(R\) is unitary, \(M\) commutes with \(R\). By hypothesis \(M=c\cdot1\), and \(c\lvert I\rvert=\operatorname{tr}M=\int\lVert W\rVert^2d\mu\).

(2) By the definition of a cut pair, \(W\) is integrable and \(\int\lVert W\rVert^2d\mu=\lvert I\rvert\); the type of a Bessel system is irreducible in the stated sense.

(3) With a decay majorant \((A,a)\): \(\lVert W^\flat(y)\rVert\le\ell_b(y)^{3r^3f}\lVert W^\flat(y)\rVert\le A(y)\) since \(\ell_b\ge1\), and \(\int A\,d\mu<\infty\) (if \(a=0\) then \(A=0\); otherwise \(a\int A\,d\mu<\infty\) with \(0<a<\infty\)). So \(W^\flat\) is integrable and (1) applies with \(c=\lvert I\rvert^{-1}\int\lVert W^\flat\rVert^2d\mu\in[0,1]\). Finally \(\lvert\langle v,W^\flat(y)\rangle\rvert^2=\sum_{i,j}\overline{v_i}v_jW^\flat_i(y)\overline{W^\flat_j(y)}\) integrates to \(c\lVert v\rVert^2\le\lVert v\rVert^2\). \(\blacksquare\)

## References

1. Lean: `New.IsBesselFunction.integral_mul_conj_eq`, `New.BesselSystem.orthonormal`, `New.IsCutPair.exists_integral_cut_mul_conj_eq`, `New.IsCutPair.lintegral_sq_inner_cut_le` in `src/New/Spanning/Bessel/Orthonormality.lean`.
