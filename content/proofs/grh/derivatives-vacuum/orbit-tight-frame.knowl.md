+++
id = "proofs/grh/derivatives-vacuum/orbit-tight-frame"
title = "The orbit of a lattice vector is a tight frame"
kind = "lemma"
summary = "For y in the lattice a0 with norm sum nu, the vectors zeta^i rho(y) for i below q1 and rho in Gal(E/K) form a tight frame of length q1 nu."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Parameters.orbit", "New.Parameters.isTightFrame_orbit"]
lean_files = ["src/New/Derivatives/Vacuum/ShortVectors.lean"]
proof_status = "full"
+++

Notation as in [[proofs/grh/derivatives-vacuum/lattice-a0-is-galois-stable|the lemma on Galois stability]]. The infinite places of \(E\) form a group identified with \(\operatorname{Gal}(E/K)\), \(\rho\mapsto g_\rho\), such that \(\Phi_\sigma\circ g_\rho=\Phi_{\sigma\rho}\). The **orbit** of \(y\in E\) is the family \(\bigl(\zeta^i g_\rho(y)\bigr)\) indexed by \(0\le i<q_1\) and \(\rho\).

**Lemma.** Let \(y\in\mathfrak{a}_0\) and \(\nu=\sum_\tau\lvert\Phi_\tau(y)\rvert^2\in\mathbb{N}\). Then the orbit of \(y\), with multiplicities \(1\), is a tight frame of length \(q_1\nu\).

## Proof

Each member is in \(\mathfrak{a}_0\) by Galois stability and because \(\mathfrak{a}_0\) is an \(\mathcal{O}_E\)-module. The frame sum factors:
\[ \sum_{i,\rho}\Phi_\sigma(\zeta^ig_\rho y)\overline{\Phi_\tau(\zeta^ig_\rho y)}=\Bigl(\sum_i\Phi_\sigma(\zeta^i)\overline{\Phi_\tau(\zeta^i)}\Bigr)\Bigl(\sum_\rho\Phi_{\sigma\rho}(y)\overline{\Phi_{\tau\rho}(y)}\Bigr). \]
The first factor is \(q_1\delta_{\sigma\tau}\) by [[proofs/grh/derivatives-vacuum/roots-of-unity-tight-frame|the tight frame of roots of unity]]. For \(\sigma=\tau\) the second is \(\sum_\rho\lvert\Phi_{\tau\rho}(y)\rvert^2=\nu\), since \(\rho\mapsto\tau\rho\) is a bijection.

## References

1. Lean: `New.Parameters.orbit`, `New.Parameters.isTightFrame_orbit` in `src/New/Derivatives/Vacuum/ShortVectors.lean`.
