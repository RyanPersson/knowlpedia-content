+++
id = "proofs/grh/spanning-unfolding-b/equivariance-of-maps-with-amplitude-blocks"
title = "Equivariance of maps with amplitude blocks under the reduced Bessel group"
kind = "theorem"
summary = "For a map P with amplitude blocks, P_(st) = P_s r_psi(t), and for a unitary representation rho(t) P = P r_psi(t) and P_(ts) = r_psi(t) P_s, for t in the reduced Bessel group."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.HasAmplitudeBlocks.adjoint_comp_rep_mul_right", "New.Filling.HasAmplitudeBlocks.rep_comp_eq_comp_besselTranslate", "New.Filling.HasAmplitudeBlocks.adjoint_comp_rep_mul_left"]
lean_files = ["src/New/Spanning/Unfolding/Moments.lean"]
proof_status = "full"
+++

**Theorem.** Let \(E\) contain a primitive \(5040\)-th root of unity, \(S\) an [[proofs/grh/spanning-unfolding-b/filling-admissible|admissible]] [[proofs/grh/spanning-unfolding-b/filling-data|filling datum]], and \((\rho,P)\) a pair that [[proofs/grh/spanning-unfolding-b/amplitude-blocks|has amplitude blocks]], with \(V\) finite-dimensional and \(P_s=P^*\rho(s)P\). Let \(t\in\bar R_0\) and \(s\in\bar G\).

1. \(P_{st}=P_s\,r_\psi(t)\).
2. If \(\rho\) is unitary, then \(\rho(t)P=P\,r_\psi(t)\).
3. If \(\rho\) is unitary, then \(P_{ts}=r_\psi(t)\,P_s\).

## Proof

(1) Fix a basis vector \(e_{(d,j)}\). Choose \(\delta\in\mathsf{S}(E)\), a term over \((d,t^{-1},d')\), acting on the Bessel function by a unitary matrix \(N\) ([[proofs/grh/spanning-unfolding-b/bessel-subgroup-reductions-reached-by-rational-terms|reaching reductions]], [[proofs/grh/spanning-unfolding-b/blocks-of-the-bessel-subgroup|blocks of the Bessel subgroup]]). By parts 3 and 4 of the theorem on blocks, \(\overline{A_{\mathsf{S}}(e,t,d)_{(k,j)}}=A_{\mathsf{S}}(d,t^{-1},e)_{(j,k)}=\nu N_{jk}\) if \(e=d'\) and \(0\) otherwise; so \(r_\psi(t)e_{(d,j)}=\sum_kN_{jk}e_{(d',k)}\). By part 5 of that theorem for the stable set of all terms (with \(t^{-1}\) in place of \(t\)),
\[
A(c,st,d)_{(i,j)}=\sum_k\overline{N_{jk}}\,A(c,s,d')_{(i,k)} .
\]
Hence \(\langle P_{st}e_{(d,j)},e_{(c,i)}\rangle=\nu^{-1}A(c,st,d)_{(i,j)}=\sum_k\overline{N_{jk}}\langle P_se_{(d',k)},e_{(c,i)}\rangle=\langle P_sr_\psi(t)e_{(d,j)},e_{(c,i)}\rangle\).

(2) For \(\varphi\in\mathcal{X}\) put \(d=\rho(t)P\varphi-Pr_\psi(t)\varphi\). For all \(s\) and \(\varphi'\): \(\langle\rho(s)P\varphi',d\rangle=\langle\varphi',P^*\rho(s^{-1})d\rangle\) by unitarity, and \(P^*\rho(s^{-1})d=P_{s^{-1}t}\varphi-P_{s^{-1}}r_\psi(t)\varphi=0\) by (1). Taking \((s,\varphi')=(t,\varphi)\) and \((1,r_\psi(t)\varphi)\) gives \(\langle d,d\rangle=0\).

(3) Apply (2) to \(t^{-1}\) and take adjoints, using \(\rho(t^{-1})^*=\rho(t)\) and \(r_\psi(t^{-1})^*=r_\psi(t)\) ([[proofs/grh/spanning-unfolding-b/bessel-translate-is-a-unitary-representation|unitarity of \(r_\psi\)]]): \(P^*\rho(t)=r_\psi(t)P^*\). Then \(P_{ts}=P^*\rho(t)\rho(s)P=r_\psi(t)P_s\).

## References

1. Lean: `New.Filling.HasAmplitudeBlocks.adjoint_comp_rep_mul_right`, `New.Filling.HasAmplitudeBlocks.rep_comp_eq_comp_besselTranslate`, `New.Filling.HasAmplitudeBlocks.adjoint_comp_rep_mul_left` in `src/New/Spanning/Unfolding/Moments.lean`.
