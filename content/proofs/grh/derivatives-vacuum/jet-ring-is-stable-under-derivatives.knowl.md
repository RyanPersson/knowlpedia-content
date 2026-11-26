+++
id = "proofs/grh/derivatives-vacuum/jet-ring-is-stable-under-derivatives"
title = "The jet ring has integral constant terms and is stable under derivatives"
kind = "lemma"
summary = "Elements of the jet ring have integral constant terms, and if the linear forms are d times integral forms the jet ring is stable under all partial derivatives."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.CMLattice.pderiv_mem_jetRing", "New.CMLattice.norm_constantCoeff_le_of_mem_jetRing", "New.CMLattice.smul_derivative_derivative_negLogTheta_mem"]
lean_files = ["src/New/Derivatives/Vacuum/JetIntegrality.lean"]
proof_status = "outline"
+++

Notation as in [[proofs/grh/derivatives-vacuum/jet-ring|the definition of the jet ring]]; \(d\) is a prime \(\equiv7\bmod8\).

**Lemma.**

1. Every \(F\in\mathcal{J}_C(\mu)\) has \(\lvert F(0)\rvert_p\le1\).
2. \(d\,g''\) is an integral power series in \(y\) (it lies in the [[?lean:New.CMLattice.integralSeriesRing|ring \(\mathcal{O}[\![y]\!]\)]]).
3. If \(\mu=d\,\nu\) with \(\lvert\nu_{i,x}\rvert_p\le1\) for all \(i,x\), then \(\partial_xF\in\mathcal{J}_C(\mu)\) for all \(F\in\mathcal{J}_C(\mu)\) and \(x\in X\).

## Proof

1. The series with integral constant term form a subring, so it suffices to check generators: integral series in the \(y(\mu_iz)\) (asserted: Lean `norm_constantCoeff_le_of_mem_multiSeriesRing`; \(y(0)=0\)), \(\theta(0)=1\), and \(g'(0)=0\) because the coefficient of \(T\) in \(g\) vanishes (asserted: Lean `coeff_one_negLogTheta`).

2. One has \(g''=2g_2+x\), where \(g_2\) is the coefficient of \(T^2\) in \(g\) and \(x\) is the Taylor series, read through \(\iota_p\), of the translated coordinate function \(x\) of \(C\) (Lean `translatedX`; the identity is Lean `derivative_derivative_negLogTheta`, asserted here). The series \(x\) lies in \(\mathcal{O}[\![y]\!]\), and \(\lvert\iota_p(\sqrt{-d})\cdot2g_2\rvert_p\le1\) (Lean `taylorVia_translatedX_mem_integralSeriesRing`, `norm_sqrt_mul_coeff_two_negLogTheta_le_one`; both asserted here). Since \(\sqrt{-d}\) maps the lattice to itself it is \(p\)-integral, and \(d=-(\sqrt{-d})^2\); so \(d\cdot2g_2\) is integral and \(d\,g''=d\cdot2g_2+d\,x\in\mathcal{O}[\![y]\!]\).

3. The set of \(F\) with all \(\partial_xF\) in the ring is closed under sums, negatives and, by the Leibniz rule, products; so check generators. Note \(\lvert\mu_{i,x}\rvert_p\le1\).
* \(F\in\mathcal{O}[\![y(\mu z)]\!]\): this ring is stable under \(\partial_x\) for integral \(\mu\) (asserted: Lean `pderiv_mem_multiSeriesRing`).
* \(F=\theta(\mu_iz)\): by the chain rule and \(\theta'=-\theta g'\), \(\partial_xF=-\mu_{i,x}\,\theta(\mu_iz)\,g'(\mu_iz)\).
* \(F=g'(\mu_iz)\): \(\partial_xF=\mu_{i,x}\,g''(\mu_iz)=\nu_{i,x}\cdot(d\,g'')(\mu_iz)\), and \((d\,g'')(\mu_iz)\in\mathcal{O}[\![y(\mu z)]\!]\) by 2 (substituting \(\mu_iz\) into an integral series in \(y\)). The factor \(d\) of the linear form clears the denominator of \(g''\).

## References

1. Lean: `New.CMLattice.pderiv_mem_jetRing`, `New.CMLattice.norm_constantCoeff_le_of_mem_jetRing`, `New.CMLattice.smul_derivative_derivative_negLogTheta_mem` in `src/New/Derivatives/Vacuum/JetIntegrality.lean`.
