+++
id = "proofs/grh/derivatives-vacuum/dual-vectors"
title = "The dual vectors of the powers of zeta"
kind = "definition"
summary = "The basis of E over K dual to the powers of zeta under the trace, multiplied by a power of the conjugate of beta that puts it in the lattice a0."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Parameters.dualVector", "New.Parameters.cyclotomicQuotient", "New.Parameters.ceilLogQ₁", "New.Parameters.X_sub_C_mul_cyclotomicQuotient", "New.Parameters.natDegree_cyclotomicQuotient", "New.Parameters.monic_cyclotomicQuotient"]
lean_files = ["src/New/Derivatives/Vacuum/ShortVectors.lean"]
+++

Let \(P\) be [[?lean:New.Parameters|parameters]], \(s\in\mathbb{N}\), \(E=K(\zeta)\) with \(\zeta\) a primitive \(q_1\)-th root of unity, \(\Phi_{q_1}\) the \(q_1\)-th [[?c:Cyclotomic polynomial|cyclotomic polynomial]], \(g=\Phi_{q_1}'(\zeta)\) and \(\beta=(1+\sqrt{-d})/2\in\mathcal{O}_K\). Let

* \(j\) be the least integer with \(2^j\ge q_1\);
* \(Q(X)=\Phi_{q_1}(X)/(X-\zeta)=\sum_{i}b_iX^i\in\mathcal{O}_E[X]\), a monic polynomial of degree \(\varphi(q_1)-1\).

The **dual vectors** are
\[ e_i=\frac{\bar\beta^{\,j}\,b_i}{g}\in E,\qquad i\in\mathbb{N} \]
(they vanish for \(i\ge\varphi(q_1)\)).

## References

1. Lean: `New.Parameters.dualVector`, `New.Parameters.cyclotomicQuotient`, `New.Parameters.ceilLogQ₁`, `New.Parameters.X_sub_C_mul_cyclotomicQuotient`, `New.Parameters.natDegree_cyclotomicQuotient`, `New.Parameters.monic_cyclotomicQuotient` in `src/New/Derivatives/Vacuum/ShortVectors.lean`.
