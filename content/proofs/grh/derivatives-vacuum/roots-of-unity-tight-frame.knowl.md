+++
id = "proofs/grh/derivatives-vacuum/roots-of-unity-tight-frame"
title = "The powers of a primitive root of unity form a tight frame"
kind = "lemma"
summary = "The q1 powers of a primitive q1-th root of unity of E are a tight frame of length q1 in the lattice a0, and repeating every vector k times gives length k q1."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Parameters.isTightFrame_pow", "New.Parameters.isTightFrame_zeta_pow", "New.IsTightFrame.mul_left", "New.Parameters.finiteImage_coe_mem", "New.Parameters.eq_of_phi_eq_of_isPrimitiveRoot"]
lean_files = ["src/New/Derivatives/Vacuum/TightFrames.lean"]
proof_status = "full"
+++

Notation as in [[proofs/grh/derivatives-vacuum/hermitian-product-of-lattice-vectors-is-integral|the lemma on hermitian products]]. Recall that a finite family \((w_i)_{i\in I}\) of elements of \(E\) with multiplicities \(m_i\in\mathbb{N}\) is a [[?lean:New.IsTightFrame|tight frame of length \(M\)]] if every \(w_i\) lies in \(\mathfrak{a}_0\) and \(\sum_i m_i\,\Phi_\sigma(w_i)\overline{\Phi_\tau(w_i)}=M\,\delta_{\sigma\tau}\) for all infinite places \(\sigma,\tau\) of \(E\).

**Lemma.** Let \(z\in E\) be a [[?c:Primitive root of unity|primitive \(q_1\)-th root of unity]].

1. The family \((z^i)_{0\le i<q_1}\), with all multiplicities \(1\), is a tight frame of length \(q_1\).
2. If \((w_i)\) with multiplicities \((m_i)\) is a tight frame of length \(M\) and \(k\in\mathbb{N}\), then \((w_i)\) with multiplicities \((k\,m_i)\) is a tight frame of length \(kM\). In particular \((\zeta^i)_{0\le i<q_1}\) with all multiplicities \(k\) is a tight frame of length \(k\,q_1\).

## Proof

1. *Membership.* \(z^i\) is an algebraic integer and \(\alpha^{-1}\) is an integral adele, so \(\alpha^{-1}z^i\in\widehat{\mathcal{O}}_E\).

*Frame identity.* For every \(\tau\), \(\Phi_\tau(z)\) is a primitive \(q_1\)-th root of unity in \(\mathbb{C}\), so \(\overline{\Phi_\tau(z)}=\Phi_\tau(z)^{-1}\) and
\[ \sum_{i=0}^{q_1-1}\Phi_\sigma(z^i)\overline{\Phi_\tau(z^i)}=\sum_{i=0}^{q_1-1}\rho^{\,i},\qquad \rho=\Phi_\sigma(z)\Phi_\tau(z)^{-1}. \]
If \(\sigma=\tau\) then \(\rho=1\) and the sum is \(q_1\). If \(\sigma\ne\tau\) then \(\rho\ne1\): otherwise \(\Phi_\sigma\) and \(\Phi_\tau\), which are \(K\)-algebra maps, agree on the generator \(z\) of \(E\) over \(K\), hence are equal, and distinct infinite places have distinct embeddings in the CM type. As \(\rho^{q_1}=1\), the geometric sum is \((\rho^{q_1}-1)/(\rho-1)=0\). (This is orthogonality of characters of \(\mathbb{Z}/q_1\).)

2. Both conditions are linear in the multiplicities: membership is unchanged, and the frame sums are multiplied by \(k\). The last assertion is 1 for \(z=\zeta\) followed by this.

## References

1. Lean: `New.Parameters.isTightFrame_pow`, `New.Parameters.isTightFrame_zeta_pow`, `New.IsTightFrame.mul_left`, `New.Parameters.finiteImage_coe_mem`, `New.Parameters.eq_of_phi_eq_of_isPrimitiveRoot` in `src/New/Derivatives/Vacuum/TightFrames.lean`.
