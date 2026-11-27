+++
id = "proofs/grh/upper-objects/vacuum-data-of-functions-modulo-an-ideal"
title = "Data from functions modulo an ideal are standard data and vacuum combinations"
kind = "lemma"
summary = "The datum given by a function of matrices modulo a modulus at the places dividing it and the vacuum elsewhere: an explicit integer multiple is a standard datum at primes away from the denominators, and it is a combination of translates of the integral vacuum with coefficients of controlled size."
aliases = ["vacuum datum is standard"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Parameters.smul_vacuumDatum_mem_standardData", "New.Parameters.smul_schrodingerOp_mem_standardData", "New.Parameters.vacuumScale_pow_smul_vacuumDatum", "New.Parameters.isVacuumCombination_vacuumDatum", "New.Parameters.isAdmissibleCombination_vacuumDatum", "New.Parameters.isAdmissibleCombination_vacuumDatum_of_sum_le", "New.Parameters.isAdmissibleCombination_vacuumDatum_indicator", "New.Parameters.absNorm_span_natCast_eq_pow_numInfPlaces", "New.Modulus.card_residueRing_le"]
lean_files = ["src/New/UpperBound/Kernels/ThetaLiftGauge.lean"]
proof_status = "outline"
+++

Let \(E=E_s\) with \(f_E\) infinite places, \(\mathfrak m\) a [[?lean:New.Modulus|modulus]] of \(E\) (a nonzero ideal such that no prime divides both it and its conjugate), \(n,n'\) finite index sets, and \(\Psi\) a complex function on \(n'\times n\) matrices over \(\mathcal O_E/\mathfrak m\). Its [[?lean:New.vacuumDatum|vacuum datum]] \(\Psi\otimes\mathrm{vac}\) on \(\operatorname{Hom}(I_n,I_{n'})\) is \(\Psi\) (of the reductions, zero off the integral matrices) at the places dividing \(\mathfrak m\) and the vacuum elsewhere. Let \(\varsigma\) be the [[?lean:New.Parameters.vacuumScale|vacuum scale]], so that \(\varsigma^{\lvert n'\rvert\lvert n\rvert}\mathrm{vac}\) is the integral vacuum.

**Lemma.**

1. Let \(N_0,q\) be natural numbers with \(qN_0\in\mathfrak m\), let the values of \(\Psi\) be [[?lean:New.Seesaw.integralAway|integral away from \(q\)]], and let \(l\) be a prime not dividing \(q\). Then
\[
N_0^{\,2f_E\lvert n'\rvert\lvert n\rvert}\cdot\varsigma^{\lvert n'\rvert\lvert n\rvert}\cdot(\Psi\otimes\mathrm{vac})
\]
is a [[?lean:New.Parameters.standardData|standard datum]] for \(N_0\) at the chosen place above \(l\).
2. If \(\lvert\sigma(\Psi(x))\rvert\le M_0\) for all automorphisms \(\sigma\) of \(\mathbb C\) and all \(x\), then \(\varsigma^{\lvert n'\rvert\lvert n\rvert}(\Psi\otimes\mathrm{vac})\) is a [[proofs/grh/upper-objects/archimedean-bounds-for-jets|vacuum combination]] of size \(M_0\cdot\#\{\text{matrices modulo }\mathfrak m\}\); more precisely of size \(B\) if \(\sum_x\lvert\sigma(\Psi(x))\rvert\le B\) for all \(\sigma\). For the indicator of one matrix the size is \(1\).
3. If a positive integer \(k\) lies in \(\mathfrak m\), then \(\lvert\mathcal O_E/\mathfrak m\rvert\le k^{2f_E}\).

## Proof

The input, cited from the area of the seesaw (Lean: `New.Seesaw.isAdmissibleCombination_schrodingerOp`, "Fourier inversion modulo \(\mathfrak m\)"), is: if \(N_0q\in\mathfrak m\) and the values of \(\Psi\) are integral away from \(q\), then the Schrödinger operator of the lift of \(\Psi\) at the places of \(\mathfrak m\), applied to a vector that is the vacuum at these places, is a finite combination \(\sum_yr_y\varrho^{\mathrm{fin}}(y)(\cdot)\) over vectors \(y\) with \(N_0y\) integral at the places not dividing \(q\), with \(\operatorname{N}(N_0)^{\lvert I\rvert}r_y\) integral away from \(q\), where \(I\) is the index set of the vectors (here \(I=n'\times n\), so the exponent is \(\lvert n'\rvert\lvert n\rvert\)); and \(\sum_y\lvert\sigma(r_y)\rvert\le B\) for all \(\sigma\) whenever \(\sum_x\lvert\sigma(\Psi(x))\rvert\le B\) for all \(\sigma\).

*1.* \(\varsigma^{\lvert n'\rvert\lvert n\rvert}(\Psi\otimes\mathrm{vac})\) is that Schrödinger operator applied to the integral vacuum (unfolding the definitions). A place above \(l\) does not divide \(q\), so each translate occurring is a standard datum for \(N_0\) at \(l\); and the absolute norm of the ideal \((N_0)\) of \(\mathcal O_E\) is \(N_0^{2f_E}\), so multiplying by \(N_0^{2f_E\lvert n'\rvert\lvert n\rvert}\) makes the coefficients integral at \(l\).

*2.* Apply the input with \(q=0\) and \(N_0=0\): no prime is coprime to \(0\), so the integrality conditions are empty, and only the size statement remains; then forget the support condition. For bounded values, \(\sum_x\lvert\sigma\Psi(x)\rvert\le M_0\cdot\#\{x\}\); for an indicator the sum is \(1\).

*3.* \(\lvert\mathcal O_E/\mathfrak m\rvert\) is the absolute norm of \(\mathfrak m\), which divides that of \((k)\), namely \(k^{2f_E}\). \(\square\)

## References

1. Lean: `New.Parameters.smul_vacuumDatum_mem_standardData`, `New.Parameters.isVacuumCombination_vacuumDatum` in `src/New/UpperBound/Kernels/ThetaLiftGauge.lean`.
