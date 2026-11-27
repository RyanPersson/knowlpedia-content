+++
id = "proofs/grh/derivatives-vacuum/resolution-from-tight-frame"
title = "A tight frame of square length gives a resolution of the identity"
kind = "lemma"
summary = "Dividing the vectors of a tight frame of length b^2 by b k and placing them in each coordinate of E^n gives a resolution of the identity with all multiplicities k^2."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.IsTightFrame.isResolution", "New.resolutionVectors", "New.dagger_resolutionVectors", "New.Parameters.isResolution_resolutionVectors_zeta_pow"]
lean_files = ["src/New/Derivatives/Vacuum/StandardDataProducts.lean"]
proof_status = "full"
+++

Let \(E\) be a CM field with CM type \((\Phi_\tau)_{\tau\in\Sigma}\) and [[?lean:New.WeilData|Weil data]], and \(n\) a finite set. For \(u\in E^n\) the linear form \(u^\dagger\) on \(\mathbb{C}^{\Sigma\times n}\) has coefficients \(u^\dagger_{(\tau,c)}=\overline{\Phi_\tau(u_c)}\). A family \((u_j)_{j\in J}\) in \(E^n\) with multiplicities \(m_j\in\mathbb{N}\) is a [[?lean:New.IsResolution|resolution of the identity]] if \(\sum_jm_j\,\Phi_\sigma(u_{j,c})\,u^\dagger_{j,(\tau,c')}=\delta_{(\sigma,c),(\tau,c')}\), i.e. \(z=\sum_jm_j(u_j^\dagger z)u_j\) for all \(z\).

For a family \((w_i)_{i\in I}\) in \(E\) and an integer \(\nu\ge1\), the **resolution vectors** are \(u_{(i,c)}=(w_i/\nu)\,\mathbf{e}_c\in E^n\) for \((i,c)\in I\times n\) (the vector with \(w_i/\nu\) in coordinate \(c\) and \(0\) elsewhere; in Lean \(\nu=0\) is allowed and gives the zero vector, which is never used).

**Lemma.** Let \((w_i)\) with multiplicities \(1\) be a [[?lean:New.IsTightFrame|tight frame]] of length \(b^2\), \(b\ne0\), and let \(k\ne0\). Then the resolution vectors of \(w\) for \(\nu=bk\), with all multiplicities \(k^2\), are a resolution of the identity. In particular the vectors \((\zeta^i/q_1)\mathbf{e}_c\), each taken \(q_1\) times, are a resolution of the identity on \(E^n\) for the field \(E=K(\zeta)\) of the parameters.

## Proof

\(u^\dagger_{(i,c),(\tau,c')}=\delta_{cc'}\overline{\Phi_\tau(w_i)}/(bk)\). So the sum is \(\delta_{cc'}\cdot k^2\sum_i\Phi_\sigma(w_i)\overline{\Phi_\tau(w_i)}/(bk)^2=\delta_{cc'}\delta_{\sigma\tau}\). For the last statement use [[proofs/grh/derivatives-vacuum/roots-of-unity-tight-frame|the frame of the powers of \(\zeta\)]] with multiplicities \(q_1\), written with repeated vectors: length \(q_1^2\); take \(b=q_1\), \(k=1\).

## References

1. Lean: `New.IsTightFrame.isResolution`, `New.resolutionVectors`, `New.dagger_resolutionVectors`, `New.Parameters.isResolution_resolutionVectors_zeta_pow` in `src/New/Derivatives/Vacuum/StandardDataProducts.lean`.
