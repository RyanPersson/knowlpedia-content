+++
id = "proofs/grh/derivatives-vacuum/dual-vectors-properties"
title = "Properties of the dual vectors"
kind = "lemma"
summary = "The dual vectors are a multiple of the trace-dual basis of the powers of zeta, satisfy biorthogonality relations over the CM type with the powers of the inverse of zeta, and lie in the lattice a0."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Parameters.trace_coeff_cyclotomicQuotient_div_mul_pow", "New.Parameters.sum_dualVector_mul_conj", "New.Parameters.sum_mul_conj_dualVector", "New.Parameters.finiteImage_dualVector_mem", "New.Parameters.q₁_dvd_pow_ceilLogQ₁"]
lean_files = ["src/New/Derivatives/Vacuum/ShortVectors.lean"]
proof_status = "full"
+++

Notation as in [[proofs/grh/derivatives-vacuum/dual-vectors|the definition of the dual vectors]]; \(\varphi=\varphi(q_1)\), and \(\beta\) also denotes \((1+i\sqrt d)/2\in\mathbb{C}\), the common image of \(\beta\) under all \(\Phi_\tau\).

**Lemma.**

1. (Euler's formula.) For \(0\le i,k<\varphi\): \(\operatorname{Tr}_{E/K}\bigl((b_i/g)\,\zeta^k\bigr)=\delta_{ik}\).
2. For infinite places \(\sigma,\tau\):
\[ \sum_{i<\varphi}\Phi_\sigma(e_i)\,\overline{\Phi_\tau(\zeta^{-i})}=\bar\beta^{\,j}\delta_{\sigma\tau},\qquad\sum_{i<\varphi}\Phi_\sigma(\zeta^{-i})\,\overline{\Phi_\tau(e_i)}=\beta^{\,j}\delta_{\sigma\tau}. \]
3. \(e_i\in\mathfrak{a}_0\) for all \(i\).

## Proof

1. \(\Phi_{q_1}\) is irreducible over \(K\) ([[?lean:New.Parameters.irreducible_cyclotomic|irreducibility]]), so it is the minimal polynomial of \(\zeta\) over \(K\) and \(1,\zeta,\dots,\zeta^{\varphi-1}\) is a basis of \(E/K\). The statement is the classical formula for the [[?c:Dual basis for the trace form|trace-dual basis]] of a power basis: if \(f\) is the minimal polynomial of \(\zeta\) and \(f(X)/(X-\zeta)=\sum b_iX^i\), the dual basis is \(b_i/f'(\zeta)\).

2. Let \(A_{i\rho}=\Phi_\rho(b_i/g)\) and \(B_{\rho k}=\Phi_\rho(\zeta^k)\), square matrices of size \(\varphi=[E:K]\) (the number of infinite places). Since the trace is the sum over the CM type, 1 says \(AB=1\); hence \(BA=1\), i.e. \(\sum_i\Phi_\tau(\zeta^i)\Phi_\sigma(b_i/g)=\delta_{\tau\sigma}\). Now \(\overline{\Phi_\tau(\zeta^{-i})}=\Phi_\tau(\zeta^i)\) and \(\Phi_\sigma(e_i)=\bar\beta^{\,j}\Phi_\sigma(b_i/g)\), which gives the first formula. The second is the complex conjugate of the first with \(\sigma,\tau\) exchanged.

3. Use the place-by-place criterion of [[proofs/grh/derivatives-vacuum/lattice-a0-is-galois-stable|the lemma on \(\mathfrak{a}_0\)]]. If \(\beta\in w\): \(ge_i=\bar\beta^{\,j}b_i\in\mathcal{O}_E\). If \(\beta\notin w\): every prime \(p\mid q_1\) divides \((d+1)/4=\beta\bar\beta\) and has exponent \(k\) in \(q_1\) with \(2^k\le p^k\le q_1\le2^j\), so \(q_1\mid(\beta\bar\beta)^j\); also \(g\mid q_1\) in \(\mathcal{O}_E\) ([[?lean:New.Parameters.relDifferentGen_dvd_q₁|\(g\) divides \(q_1\)]]). Thus \(\beta^j\bar\beta^{\,j}=gc\) with \(c\in\mathcal{O}_E\), so \(\beta^je_i=cb_i\) is integral, and \(\beta\) is a unit at \(w\).

## References

1. Lean: `New.Parameters.trace_coeff_cyclotomicQuotient_div_mul_pow`, `New.Parameters.sum_dualVector_mul_conj`, `New.Parameters.sum_mul_conj_dualVector`, `New.Parameters.finiteImage_dualVector_mem`, `New.Parameters.q₁_dvd_pow_ceilLogQ₁` in `src/New/Derivatives/Vacuum/ShortVectors.lean`.
