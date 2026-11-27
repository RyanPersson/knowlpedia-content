+++
id = "proofs/grh/derivatives-vacuum/modulus-of-jet-scale"
title = "The modulus of the jet scale"
kind = "theorem"
summary = "The squared absolute value of the jet scale is the inverse of the constant Omega = exp(gamma - Re L'/L(1, chi_K)) 2 pi / rd_E."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Parameters.norm_jetScale_sq", "New.CMLattice.area_eq_of_a₁_eq"]
lean_files = ["src/New/Derivatives/Vacuum/Scale.lean"]
proof_status = "outline"
+++

**Theorem.** For parameters \(P\) and \(s\in\mathbb{N}\), the [[proofs/grh/derivatives-vacuum/jet-scale|jet scale]] \(\lambda\) satisfies
\[ \lvert\lambda\rvert^2=\Omega^{-1},\qquad\Omega=e^{\gamma-\operatorname{Re}\frac{L'}{L}(1,\chi_K)}\cdot\frac{2\pi}{\mathrm{rd}_E} \]
([[?lean:New.Parameters.bigOmega|the constant \(\Omega\)]]).

## Proof

In the proof of [[proofs/grh/derivatives-vacuum/conjugates-of-jets-of-translates|the theorem on conjugates of jets]] it is shown that for \(\sigma\in\operatorname{Aut}(\mathbb{C}/K)\) and \(\Omega_\sigma\in\mathbb{C}^\times\) with \(\operatorname{area}(\mathcal{E}^\sigma)=\lvert\Omega_\sigma\rvert^2\sqrt d/2\) one has \(\lvert\sigma(\varpi)c_A/\Omega_\sigma\rvert^2=\Omega^{-1}\) (from \(\lvert\sigma s_0\rvert^2=\mathrm{rd}_E/\sqrt d\) and the Chowla–Selberg formula). Apply this with \(\sigma=1\) and \(\Omega_\sigma=\Omega_0\): then the left side is \(\lvert\lambda\rvert^2\). It remains to see \(\operatorname{area}(\mathcal{E}^{1})=\lvert\Omega_0\rvert^2\sqrt d/2\), the area of \(\Lambda_{\mathcal{E}}=\Omega_0\mathcal{O}_K\).

The conjugate \(\mathcal{E}^{1}\) is a chosen CM lattice, not literally \(\mathcal{E}\); what is known is that its invariant \(a_1\) (a square root of \(12\wp(t)\) for the marked point \(t\) of order two) is \(\sigma(a_1)=a_1\). Two CM lattices \(C,D\) for \(d\) with the same \(a_1\) have the same area: by a Lib lemma on isogenies between CM lattices with matching invariants (Lean `New.exists_isIsogeny_of_mul_mem_lattice` for period pairs and `New.conj_isogeny_mul_mem_lattice`, the latter applied to the identity isogeny, which gives the inclusion of the period lattices; asserted here) each area is a natural-number multiple of the other, \(\operatorname{area}(C)=N\operatorname{area}(D)\) and \(\operatorname{area}(D)=N'\operatorname{area}(C)\), so \(NN'=1\) and \(N=N'=1\).

## References

1. Lean: `New.Parameters.norm_jetScale_sq`, `New.CMLattice.area_eq_of_a₁_eq` in `src/New/Derivatives/Vacuum/Scale.lean`.
