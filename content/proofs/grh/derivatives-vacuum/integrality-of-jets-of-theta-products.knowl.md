+++
id = "proofs/grh/derivatives-vacuum/integrality-of-jets-of-theta-products"
title = "Integrality of the jets of theta products"
kind = "theorem"
summary = "For linear forms that are d times integral forms, all jets along integral polynomials of a power of a product of series theta(mu_i z) times an integral series in the y(mu_i z) are p-integral."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.CMLattice.norm_jet_thetaProd_pow_mul_le_one"]
lean_files = ["src/New/Derivatives/Vacuum/JetIntegrality.lean"]
proof_status = "full"
+++

Notation as in [[proofs/grh/derivatives-vacuum/jet-ring|the definition of the jet ring]].

**Theorem.** Let \(d\) be a prime \(\equiv7\bmod8\), \(C\) a CM lattice for \(d\), \(\iota_p\) a \(p\)-adic place. Let \(\nu_{i,x}\in\mathbb{C}_p\) with \(\lvert\nu_{i,x}\rvert_p\le1\) and \(\mu=d\,\nu\); let \(m_i\in\mathbb{N}\), \(N\in\mathbb{N}\), and \(H\in\mathcal{O}[\![y(\mu z)]\!]\). Let \(R\) be a commutative ring, \(\varphi\colon R\to\mathbb{C}_p\) a ring homomorphism with integral values and \(Q\in R[z_x]\). Then
\[ \Bigl\lvert\Bigl(\varphi(Q)(\partial)\Bigl[\Bigl(\prod_{i\in I}\theta(\mu_iz)^{m_i}\Bigr)^{N}H\Bigr]\Bigr)(0)\Bigr\rvert_p\le1. \]

## Proof

The series in brackets lies in the jet ring \(\mathcal{J}_C(\mu)\). By [[proofs/grh/derivatives-vacuum/jet-ring-is-stable-under-derivatives|the lemma on the jet ring]] this ring has integral constant terms and is stable under partial derivatives; apply [[proofs/grh/derivatives-vacuum/jets-integral-in-derivative-stable-ring|the lemma on derivative-stable rings]].

## References

1. Lean: `New.CMLattice.norm_jet_thetaProd_pow_mul_le_one` in `src/New/Derivatives/Vacuum/JetIntegrality.lean`.
