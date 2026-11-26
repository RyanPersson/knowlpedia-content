+++
id = "proofs/grh/derivatives-vacuum/tight-frame-of-length-prime-to-q1"
title = "A tight frame of length prime to q1"
kind = "theorem"
summary = "There is a tight frame in the lattice a0, with multiplicities one, whose length is the dual resolution factor, a natural number prime to q1, and which contains the vector zeta e_(phi(q1)-1)."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Parameters.exists_isTightFrame_coprime", "New.Parameters.dualResolutionFactor", "New.Parameters.isTightFrame_sumElim_inv_pow_orbit", "New.Parameters.exists_isTightFrame_factor_eq_add", "New.Parameters.isCoprime_of_pow_add_conj_pow_eq", "New.Parameters.exists_pow_add_conj_pow_eq_intCast", "New.Parameters.one_lt_q₁"]
lean_files = ["src/New/Derivatives/Vacuum/ShortVectors.lean"]
proof_status = "full"
+++

Notation as in [[proofs/grh/derivatives-vacuum/dual-vectors|the definition of the dual vectors]]. The **dual resolution factor** is
\[ h_0=q_1\Bigl(1+\sum_{i<\varphi(q_1)}\sum_\tau\lvert\Phi_\tau(e_i)\rvert^2\Bigr)+\beta^{\,j}+\bar\beta^{\,j}\in\mathbb{C}. \]

**Theorem.** For all parameters \(P\) and \(s\in\mathbb{N}\) there are a natural number \(h\), a finite set \(I\) and a family \((v_i)_{i\in I}\) in \(E\) such that: \((v_i)\) with multiplicities \(1\) is a [[?lean:New.IsTightFrame|tight frame]] of length \(h\); \(h=h_0\); \(\gcd(h,q_1)=1\); and \(v_i=\zeta\,e_{\varphi(q_1)-1}\) for some \(i\).

## Proof

Put \(\varphi=\varphi(q_1)\), \(\nu_i=\sum_\tau\lvert\Phi_\tau(e_i)\rvert^2\in\mathbb{N}\) (by [[proofs/grh/derivatives-vacuum/dual-vectors-properties|\(e_i\in\mathfrak{a}_0\)]] and [[proofs/grh/derivatives-vacuum/lattice-a0-is-galois-stable|integrality of norms]]), and \(t=\beta^j+\bar\beta^{\,j}\), a real element of \(\mathcal{O}_K\), hence an integer.

*A first frame.* The powers \(\zeta^{-i}\), \(i<q_1\) (a tight frame of length \(q_1\), \(\zeta^{-1}\) being primitive) together with the [[proofs/grh/derivatives-vacuum/orbit-tight-frame|orbits]] of \(e_0,\dots,e_{\varphi-1}\) (lengths \(q_1\nu_i\)) form, by [[proofs/grh/derivatives-vacuum/tight-frame-operations|unions]], a tight frame of length \(q_1(1+\sum_i\nu_i)\) with multiplicities \(1\).

*Pairing.* For \(i<\varphi\) pair the member \(\zeta^{-i}\) with the member \(e_i\) of the orbit of \(e_i\) (index \((0,1)\)). By [[proofs/grh/derivatives-vacuum/dual-vectors-properties|the biorthogonality relations]] the cross terms sum to \((\beta^j+\bar\beta^{\,j})\delta_{\sigma\tau}=t\,\delta_{\sigma\tau}\). By [[proofs/grh/derivatives-vacuum/tight-frame-operations|replacing pairs by sums]] we get a tight frame of length \(h=q_1(1+\sum\nu_i)+t=h_0\). The member \(\zeta\,e_{\varphi-1}\) of the orbit of \(e_{\varphi-1}\) (index \((1,1)\); note \(q_1>1\)) is not in a pair, so it survives.

*Coprimality.* \(h\equiv t\bmod q_1\), so it suffices that no prime \(p\mid q_1\) divides \(t\). Such \(p\) divides \((d+1)/4=\beta(1-\beta)\) (recall \(\bar\beta=1-\beta\)). Let \(\mathfrak{p}\) be a prime of \(\mathcal{O}_K\) above \(p\); then \(\beta\equiv0\) or \(\beta\equiv1\bmod\mathfrak{p}\), and since \(j\ge1\) (as \(q_1>1\)), \(t=\beta^j+(1-\beta)^j\equiv1\bmod\mathfrak{p}\). If \(p\mid t\) then \(t\equiv0\bmod\mathfrak{p}\), a contradiction.

## References

1. Lean: `New.Parameters.exists_isTightFrame_coprime`, `New.Parameters.dualResolutionFactor`, `New.Parameters.isTightFrame_sumElim_inv_pow_orbit`, `New.Parameters.exists_isTightFrame_factor_eq_add`, `New.Parameters.isCoprime_of_pow_add_conj_pow_eq`, `New.Parameters.exists_pow_add_conj_pow_eq_intCast`, `New.Parameters.one_lt_q₁` in `src/New/Derivatives/Vacuum/ShortVectors.lean`.
