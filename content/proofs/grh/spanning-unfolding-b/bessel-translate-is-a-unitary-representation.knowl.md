+++
id = "proofs/grh/spanning-unfolding-b/bessel-translate-is-a-unitary-representation"
title = "The twisted translations form a unitary representation of the reduced Bessel group"
kind = "theorem"
summary = "The operators r_psi vanish off the reduced Bessel group, are given by the unitary matrix of a rational term in the Bessel subgroup, are multiplicative, and satisfy r_psi(s)* = r_psi(s^-1)."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.besselTranslate_eq_zero", "New.Filling.besselTranslate_apply", "New.Filling.besselTranslate_one", "New.Filling.besselTranslate_mul", "New.Filling.besselTranslate_mul_left", "New.Filling.adjoint_besselTranslate", "New.Filling.hilbertSchmidtNorm_besselTranslate_comp", "New.Filling.trace_besselTranslate"]
lean_files = ["src/New/Spanning/Unfolding/Moments.lean"]
proof_status = "full"
+++

**Theorem.** Let \(E\) contain a primitive \(5040\)-th root of unity and let \(S\) be an [[proofs/grh/spanning-unfolding-b/filling-admissible|admissible]] [[proofs/grh/spanning-unfolding-b/filling-data|filling datum]]. Let \(r_\psi(s)\) be the [[proofs/grh/spanning-unfolding-b/bessel-translate|twisted translations]] on the source \(\mathcal{X}\) and \(\bar R_0\) the reduced image of the Bessel subgroup.

1. \(r_\psi(s)=0\) for \(s\notin\bar R_0\) (this needs neither hypothesis).
2. If \(\gamma\in\mathsf{S}(E)\) is a term over \((c,s,c')\) and \(W(\gamma_\infty y)=MW(y)\) for the full Bessel function, then \(\bigl(r_\psi(s)\varphi\bigr)(c,i)=\sum_j\overline{M_{ij}}\,\varphi(c',j)\) for all \(\varphi\in\mathcal{X}\).
3. \(r_\psi(1)=1\); \(r_\psi(st)=r_\psi(s)r_\psi(t)\) for \(s,t\in\bar R_0\); and \(r_\psi(ts)=r_\psi(t)r_\psi(s)\) for \(t\in\bar R_0\) and all \(s\in\bar G\).
4. \(r_\psi(s)^*=r_\psi(s^{-1})\) for all \(s\). Hence \(r_\psi(t)\) is unitary for \(t\in\bar R_0\), and \(\lVert r_\psi(t)A\rVert=\lVert A\rVert\) in Hilbert–Schmidt norm for every operator \(A\) of \(\mathcal{X}\).
5. \(\operatorname{tr}r_\psi(s)=\nu^{-1}\sum_{c,i}A_{\mathsf{S}}(c,s^{-1},c)_{(i,i)}\).

## Proof

All parts use [[proofs/grh/spanning-unfolding-b/blocks-of-the-bessel-subgroup|the blocks of the Bessel subgroup]]. (1) \(A_{\mathsf{S}}(c,s,c')=0\) for \(s\notin\bar R_0\). (2) \(A_{\mathsf{S}}(c,s,d)_{(i,j)}=\nu M_{ij}\) for \(d=c'\) and \(0\) otherwise; insert into the matrix of \(r_\psi(s)\). (3) For \(s=1\) take \(\gamma=1\), a term over \((c,1,c)\) with \(M=1\). For \(s,t\in\bar R_0\) and a class \(c\), choose \(\gamma\in\mathsf{S}(E)\) over \((c,s,c')\) and \(\delta\in\mathsf{S}(E)\) over \((c',t,c'')\) ([[proofs/grh/spanning-unfolding-b/bessel-subgroup-reductions-reached-by-rational-terms|reductions of the Bessel subgroup are reached]]), acting by unitary \(M,N\); then \(\gamma\delta\) is a term over \((c,st,c'')\) acting by \(MN\), and (2) gives \((r_\psi(st)\varphi)(c,i)=\sum_k\overline{(MN)_{ik}}\varphi(c'',k)=(r_\psi(s)r_\psi(t)\varphi)(c,i)\). If \(t\in\bar R_0\) and \(s\notin\bar R_0\), then \(ts\notin\bar R_0\) and both sides vanish by (1). (4) The matrix of \(r_\psi(s)^*\) is the conjugate transpose, and \(A_{\mathsf{S}}(c',s^{-1},c)_{(j,i)}=\overline{A_{\mathsf{S}}(c,s,c')_{(i,j)}}\). For \(t\in\bar R_0\): \(r_\psi(t)^*r_\psi(t)=r_\psi(t^{-1}t)=1\), so \(r_\psi(t)\) preserves norms of vectors, and both \(\lVert r_\psi(t)A\rVert\le\lVert A\rVert\) and the reverse hold. (5) Sum the diagonal entries and use the symmetry of (4).

## References

1. Lean: `New.Filling.besselTranslate_apply`, `New.Filling.besselTranslate_mul`, `New.Filling.besselTranslate_mul_left`, `New.Filling.adjoint_besselTranslate`, `New.Filling.hilbertSchmidtNorm_besselTranslate_comp`, `New.Filling.trace_besselTranslate` in `src/New/Spanning/Unfolding/Moments.lean`.
