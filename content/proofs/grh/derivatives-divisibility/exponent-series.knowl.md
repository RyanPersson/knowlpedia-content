+++
id = "proofs/grh/derivatives-divisibility/exponent-series"
title = "The exponent series of the theta function"
kind = "definition"
summary = "The part of g = -log theta in the degrees congruent to p+1 modulo q_p - 1, and the series Xi_1 = -g_flat(varpi z)/c_varpi; theta(varpi z) is integral up to exp(c_varpi Xi_1)."
aliases = ["exponent series", "flat part of -log theta", "least flat degree"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.CMLattice.negLogThetaPart", "New.CMLattice.exponentSeries", "New.leastFlatDegree", "New.CMLattice.expSubst_negLogThetaPart_sub_mem", "New.CMLattice.exists_rescale_theta_eq_mul_expSubst", "New.CMLattice.smul_exponentSeries", "New.CMLattice.coeff_exponentSeries_eq_zero_of_lt", "New.leastFlatDegree_lt", "New.add_one_modEq_leastFlatDegree"]
lean_files = ["src/New/Derivatives/FormalGroup/Exponent.lean"]
+++

**Definition (exponent series).** Let \(d\equiv7\pmod 8\) be a prime, \(C\) a CM lattice with theta function \(\theta\) and \(g=-\log\theta\in\mathbb{C}_p[\![z]\!]\) (see the [[proofs/grh/derivatives-divisibility/cm-curve-setting|CM lattice]]), and \(p\) a prime with a \(p\)-adic place; \(q_p\), \(\rho_p\), \(c_\varpi=\varpi^{p+1}/p\) are as in the [[proofs/grh/derivatives-divisibility/p-adic-setting|\(p\)-adic setting]].

* The **flat part** \(g^\flat\) of \(g\) is the series whose coefficient of \(z^n\) is that of \(g\) if \(n\equiv p+1\pmod{q_p-1}\), and \(0\) otherwise.
* For \(\varpi\in\mathbb{C}_p\), \(\varpi\ne0\), the **exponent series** is \(\Xi_1=\Xi_1(\varpi)=-c_\varpi^{-1}\,g^\flat(\varpi z)\), so that \(c_\varpi\Xi_1=-g^\flat(\varpi z)\).
* The **least flat degree** is \(i_0=2\) if \(p=d\) and \(i_0=p+1\) otherwise.

## Properties

1. If \(\chi_K(p)\ne1\): \(i_0<q_p-1\) and \(i_0\equiv p+1\pmod{q_p-1}\); so \(i_0\) is the least positive degree in which \(g^\flat\), and \(\Xi_1\), can have a nonzero coefficient.
2. For every prime \(p\): \(\exp(g^\flat-g)\in\mathcal{O}[\![y]\!]\).
3. For every prime \(p\): if \(0<\lvert\varpi\rvert\le p^{-\rho_p}\), there is an integral series \(W\in\mathcal{O}[\![z]\!]\) with
\[
\theta(\varpi z)=W\cdot\exp\bigl(c_\varpi\,\Xi_1(\varpi)\bigr).
\]

## Proof

1. If \(p=d\), then \(q_p-1=p-1\), \(p+1\equiv2\), and \(2<p-1\) as \(p=d\equiv 7 \pmod 8\). If \(p\) is inert, \(p\ge3\) and \(p+1<p^2-1\).

2. Let \(\zeta\in\mathbb{C}_p\) be a primitive \((q_p-1)\)-th root of unity. Averaging over the powers of \(\zeta\) [[?lean:New.congruencePart_eq_sum|extracts a congruence class of degrees]]: \((q_p-1)\,g^\flat=\sum_{i<q_p-1}\zeta^{-i(p+1)}g(\zeta^iz)\). Hence
\[
\exp(g^\flat-g)^{\,q_p-1}=\prod_{i<q_p-1}\exp\bigl(\zeta^{-i(p+1)}g(\zeta^iz)-g(z)\bigr),
\]
and each factor lies in \(\mathcal{O}[\![y]\!]\) by fact 6 of the setting. As \(q_p-1\) is prime to \(p\), fact 7 gives \(\exp(g^\flat-g)\in\mathcal{O}[\![y]\!]\).

3. Since \(\theta=\exp(-g)=\exp(g^\flat-g)\cdot\exp(-g^\flat)\), scaling the variable by \(\varpi\) gives \(\theta(\varpi z)=\exp(g^\flat-g)(\varpi z)\cdot\exp(-g^\flat(\varpi z))\). The first factor is integral by 2 and fact 3 of the setting; the second is \(\exp(c_\varpi\Xi_1)\). \(\blacksquare\)

## References

1. Lean: `New.CMLattice.negLogThetaPart`, `New.CMLattice.exponentSeries`, `New.leastFlatDegree`, `New.CMLattice.expSubst_negLogThetaPart_sub_mem`, `New.CMLattice.exists_rescale_theta_eq_mul_expSubst` in `src/New/Derivatives/FormalGroup/Exponent.lean`.
