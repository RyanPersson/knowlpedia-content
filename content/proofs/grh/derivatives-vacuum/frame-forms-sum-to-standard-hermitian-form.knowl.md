+++
id = "proofs/grh/derivatives-vacuum/frame-forms-sum-to-standard-hermitian-form"
title = "The forms of a tight frame sum to the standard hermitian form"
kind = "lemma"
summary = "Pulling the hermitian forms of a CM lattice of the right area back along the linear forms of a tight frame and summing gives the standard hermitian form."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Parameters.sum_pullForm_resolutionLinearForm_apply"]
lean_files = ["src/New/Derivatives/Vacuum/TightFrames.lean"]
proof_status = "full"
+++

Notation as in [[proofs/grh/derivatives-vacuum/resolution-product|the definition of resolution products]]. The hermitian form of the CM lattice \(C\) of area \(A\) is \(H_C(l,z)=(\pi/A)\,\bar l\,z\).

**Lemma.** Let \((w_j)_{j\in I}\) with multiplicities \((m_j)\) be a [[?lean:New.IsTightFrame|tight frame of length \(M\)]], and suppose \(A=\lvert b\rvert^2M\sqrt d/2\). Then for all \(u,v\in\mathbb{C}^{\Sigma\times n}\)
\[ \sum_{i=(j,k)\in I\times n}m_j\,H_C\bigl(A_i^{\,b/c_A}(u),A_i^{\,b/c_A}(v)\bigr)=\sum_{p\in\Sigma\times n}\overline{u_p}\,v_p . \]

## Proof

Since \(A>0\), we have \(b\ne0\) and \(M\ne0\). With \(c_A^2=2\pi/\sqrt d\),
\[ \frac{\pi}{A}\Bigl\lvert\frac{b}{c_A}\Bigr\rvert^2=\frac{\pi\lvert b\rvert^2\sqrt d}{2\pi}\cdot\frac{2}{\lvert b\rvert^2M\sqrt d}=\frac1M . \]
Hence the term \(i=(j,k)\) equals
\[ \frac{m_j}{M}\sum_{\sigma,\tau}\overline{u_{(\tau,k)}}\,v_{(\sigma,k)}\,\Phi_\tau(w_j)\overline{\Phi_\sigma(w_j)} . \]
Summing over \(j\) and using the frame identity \(\sum_jm_j\Phi_\tau(w_j)\overline{\Phi_\sigma(w_j)}=M\delta_{\tau\sigma}\) leaves \(\sum_k\sum_\tau\overline{u_{(\tau,k)}}v_{(\tau,k)}\).

## References

1. Lean: `New.Parameters.sum_pullForm_resolutionLinearForm_apply` in `src/New/Derivatives/Vacuum/TightFrames.lean`.
