+++
id = "proofs/grh/derivatives-divisibility/p-adic-setting"
title = "The p-adic setting for derivatives of theta functions"
kind = "notation"
summary = "Conventions for integral power series over the p-adic complex numbers, jets, and the numbers attached to a prime in an imaginary quadratic field."
aliases = ["integral power series over C_p", "p-adic place of the complex numbers"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = []
lean_files = ["src/New/Derivatives/Divisibility/NormalForm.lean", "src/New/Derivatives/Divisibility/Count.lean", "src/New/Derivatives/FormalGroup/Exponent.lean"]
+++

**Notation (the \(p\)-adic setting).** Fix a prime number \(p\).

1. \(\mathbb{C}_p\) is the [[?c:field of p-adic complex numbers|field of \(p\)-adic complex numbers]] with its [[algebra-fields-galois/non-archimedean-absolute-value|non-Archimedean absolute value]] \(\lvert\cdot\rvert\), normalised by \(\lvert p\rvert=p^{-1}\); \(v(x)=-\log_p\lvert x\rvert\) is the valuation with \(v(p)=1\). Its [[algebra-fields-galois/valuation-ring|valuation ring]] is \(\mathcal{O}=\{x:\lvert x\rvert\le 1\}\). For \(a,b\in\mathcal{O}\), \(a\) divides \(b\) in \(\mathcal{O}\) exactly when \(\lvert b\rvert\le\lvert a\rvert\).
2. A [[algebra-rings/multivariable-formal-power-series-ring|formal power series]] over \(\mathbb{C}_p\), in any finite set of variables, is **integral** if all its coefficients lie in \(\mathcal{O}\). For \(\pi\in\mathcal{O}\) and integral series \(F,G\), the congruence \(F\equiv G \pmod{\pi}\) means that \(\pi\) divides every coefficient of \(F-G\).
3. For a series \(g\) without constant term, \(\exp(g)=\sum_{j\ge 0}g^j/j!\) is the [[algebra-rings/substitution-of-formal-power-series|substitution]] of \(g\) into the exponential series.
4. For a polynomial \(Q\) and a power series \(F\) in the same variables, the **jet** of \(F\) along \(Q\) is
\[
Q(\partial)F(0)=\sum_{d} d!\,Q_d\,F_d ,
\]
the sum over all multi-indices \(d\), where \(Q_d,F_d\) are the coefficients of the monomial \(z^d\) and \(d!=\prod_x d_x!\).
5. A **\(p\)-adic place of \(\mathbb{C}\)** is a ring homomorphism \(\iota_p\colon\mathbb{C}\to\mathbb{C}_p\). One such homomorphism is fixed; a complex number is read in \(\mathbb{C}_p\) through it, and the Taylor series at \(0\) of a function holomorphic near \(0\) is read in \(\mathbb{C}_p[[z]]\) by applying \(\iota_p\) to its coefficients.

Let moreover \(d\) be a prime with \(d\equiv 7\pmod 8\), \(K=\mathbb{Q}(\sqrt{-d})\) the [[algebra-fields-galois/imaginary-quadratic-field|imaginary quadratic field]], and \(\chi_K(p)=\left(\frac{p}{d}\right)\) the [[?c:Legendre symbol|Legendre symbol]], which is \(1\), \(-1\), \(0\) according as \(p\) is split, inert or ramified (\(p=d\)) in \(K\). The numbers attached to \(p\) are:

| Symbol | Value | \(p\) inert | \(p=d\) | \(p\) split |
|---|---|---|---|---|
| \(\pi_p\) | \(\sqrt{-d}\) if \(p=d\), else \(p\) | \(p\) | \(\sqrt{-d}\) | \(p\) |
| \(q_p\) | \(p^2\) if \(\chi_K(p)=-1\), else \(p\) | \(p^2\) | \(p\) | \(p\) |
| \(v(\pi_p)\) | \(\tfrac12\) if \(p=d\), else \(1\) | \(1\) | \(\tfrac12\) | \(1\) |
| \(\rho_p=v(\pi_p)/(q_p-1)\) | | \(\tfrac{1}{p^2-1}\) | \(\tfrac{1}{2p-2}\) | \(\tfrac{1}{p-1}\) |
| \(\gamma_p=\tfrac{1}{p-1}-\rho_p\) | | \(\tfrac{p}{p^2-1}\) | \(\tfrac{1}{2p-2}\) | \(0\) |
| \(I_p^\circ\) | exponents \(e\ge 0\) | the odd \(e\) | all \(e\) | none |
| \(I_p\) | the positive elements of \(I_p^\circ\) | the odd \(e\) | all \(e\ge 1\) | none |

The number \(\pi_p\) is read in \(\mathcal{O}\) through \(\iota_p\); it divides \(p\) there and \(\lvert\iota_p\pi_p\rvert=p^{-v(\pi_p)}\). For \(\varpi\in\mathbb{C}_p\) put \(c_\varpi=\varpi^{p+1}/p\).

## Remarks

These objects are defined in the supporting library of the proof: the valuation ring is [[?lean:New.valRingCp|the ring \(\mathcal{O}\)]], the jet is [[?lean:New.jet|the pairing \(Q(\partial)F(0)\)]], the exponential is [[?lean:New.expSubst|\(\exp(g)\)]], the place is [[?lean:New.PadicPlace|\(\iota_p\)]], and the numbers are [[?lean:New.chiK|\(\chi_K\)]], [[?lean:New.piPrime|\(\pi_p\)]], [[?lean:New.primeNorm|\(q_p\)]], [[?lean:New.piPrimeValuation|\(v(\pi_p)\)]], [[?lean:New.varpiValuation|\(\rho_p\)]], [[?lean:New.gammaPrime|\(\gamma_p\)]], [[?lean:New.partnerExponents|\(I_p^\circ\)]] and [[?lean:New.positivePartnerExponents|\(I_p\)]].

The source does not ask \(\iota_p\) to be continuous or surjective; only that it is a ring homomorphism. Since \(2\) splits in \(K\) (as \(d\equiv 7 \pmod 8\)), every prime with \(\chi_K(p)\ne 1\) is odd, and then \(v(\pi_p)\ge\tfrac12\ge\tfrac{1}{p-1}\), that is \(\lvert\iota_p\pi_p\rvert\le p^{-1/(p-1)}\).

A sum of infinitely many power series is always meant coefficientwise; in every sum used here only finitely many terms have order at most \(n\), for each \(n\), so each coefficient is a finite sum.

## References

1. Lean: `New.valRingCp` (`src/Lib/General/Algebra/AdicCompletion.lean`), `New.jet` (`src/Lib/GLn/SchurModule/Basic.lean`), `New.expSubst` (`src/Lib/General/Algebra/IntegralPowerSeries.lean`), `New.piPrime`, `New.piPrimeValuation`, `New.varpiValuation`, `New.gammaPrime`, `New.partnerExponents`, `New.positivePartnerExponents` (`src/Lib/CM/FormalGroup/PrimeNotation.lean`), `New.chiK`, `New.primeNorm` (`src/Lib/General/NumberTheory/ImaginaryQuadraticField.lean`).
