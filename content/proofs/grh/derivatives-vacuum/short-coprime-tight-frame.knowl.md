+++
id = "proofs/grh/derivatives-vacuum/short-coprime-tight-frame"
title = "A short tight frame of length prime to q1 for admissible data"
kind = "theorem"
summary = "For admissible data there is a tight frame with multiplicities one whose length h is prime to q1 and at most b, and at every p-adic place one of its members or a power of zeta has a unit linear form."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.exists_short_isTightFrame_coprime", "New.Data.le_b_of_eq_dualResolutionFactor", "New.Data.hasLogUpper_pow_ceilLogQ₁", "New.Data.one_le_norm_phi_relDifferentGen", "New.Parameters.norm_phi_dualVector_le", "New.Parameters.norm_phi_coeff_cyclotomicQuotient_le", "New.Parameters.norm_coeff_cyclotomic_le", "New.Parameters.norm_quadGen_le", "New.Parameters.ceilLogQ₁_le"]
lean_files = ["src/New/Derivatives/Vacuum/ShortVectors.lean"]
proof_status = "outline"
+++

Let \(D\) be [[?lean:New.Data|admissible data]] for the parameters \(P\), with \(s\) the tower exponent, \(E=K(\zeta)\), \(q_1\), the number \(f\) of infinite places of \(E\), and the weight \(b\).

**Theorem.** There are \(h\in\mathbb{N}\), a finite set \(I\) and \((v_i)_{i\in I}\) in \(E\) with: \(\gcd(h,q_1)=1\); \(1\le h\le b\); \((v_i)\) with multiplicities \(1\) is a tight frame of length \(h\); and for every prime \(p\) and \(p\)-adic place \(\iota_p\) there is \(y\) among the powers \(\zeta^i\) (\(i<q_1\)) and the \(v_i\) that [[proofs/grh/derivatives-vacuum/unit-linear-form|has a unit linear form]] at \(\iota_p\).

## Proof

Take the frame of [[proofs/grh/derivatives-vacuum/tight-frame-of-length-prime-to-q1|the frame of length prime to \(q_1\)]], of length \(h=h_0\). Then \(h\ge1\) because \(\gcd(0,q_1)=q_1>1\). The unit linear form is supplied by [[proofs/grh/derivatives-vacuum/existence-of-vector-with-unit-linear-form|the two explicit vectors]]: \(1=\zeta^0\) and \(\zeta e_{\varphi(q_1)-1}\), which is a member of the frame.

*The bound \(h\le b\).* The explicit estimates are:

* the coefficients of \(\Phi_{q_1}\) are at most \(2^{q_0}\) in absolute value: \(\Phi_{q_1}(X)=\Phi_{q_0}(X^{q_1/q_0})\) (every prime of \(q_1\) divides \(q_0\)), and a monic polynomial of degree \(\varphi(q_0)\) with roots on the unit circle has coefficients bounded by binomial coefficients \(\le2^{\varphi(q_0)}\);
* \(b_i=\sum_{l=i+1}^{\varphi(q_1)}\zeta^{\,l-i-1}c_l\) (\(c_l\) the coefficients of \(\Phi_{q_1}\)), so \(\lvert\Phi_\tau(b_i)\rvert\le q_12^{q_0}\);
* \(\lvert\beta\rvert\le d\);
* \(\lvert\Phi_\tau(g)\rvert\ge1\) for every \(\tau\). This is asserted here: it is deduced in Lean from \(\lvert\tau(\delta_E)\rvert=\lvert\tau(g)\rvert\sqrt d\) and the lower bound for \(\lvert\tau(\delta_E)\rvert\) recorded in the magnitude calculus of the data (`New.Data.one_le_norm_phi_relDifferentGen`).

Hence \(\lvert\Phi_\tau(e_i)\rvert\le d^jq_12^{q_0}\) and
\[ h\le q_1\bigl(1+q_1f\,(d^jq_12^{q_0})^2\bigr)+2d^j . \]
Moreover \(j\le q_0+3s+10\) (from \(q_1=q_0\cdot3^{\lfloor\log_3s\rfloor+5}2^s\le2^{q_0}4^{s+5}2^s\)), and \(d^j\le e^{dj}\le b^{1/100}\). The final comparison of the displayed polynomial expression with \(b\), and the inequality \((q_0+3s+10)d\le\log b/100\), are instances of the scale inequalities of the data and are verified in Lean by its magnitude calculus ([[?lean:New.Data.le_of_hasLogBound|comparison of logarithmic sizes]]); they are asserted here.

## References

1. Lean: `New.Data.exists_short_isTightFrame_coprime`, `New.Data.le_b_of_eq_dualResolutionFactor`, `New.Data.hasLogUpper_pow_ceilLogQ₁`, `New.Data.one_le_norm_phi_relDifferentGen`, `New.Parameters.norm_phi_dualVector_le`, `New.Parameters.norm_phi_coeff_cyclotomicQuotient_le`, `New.Parameters.norm_coeff_cyclotomic_le`, `New.Parameters.norm_quadGen_le`, `New.Parameters.ceilLogQ₁_le` in `src/New/Derivatives/Vacuum/ShortVectors.lean`.
