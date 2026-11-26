+++
id = "proofs/grh/reduction-main/one-sided-bound"
title = "The one-sided bound for the prime remainder"
kind = "theorem"
summary = "For q0 a multiple of 18480, a prime d congruent to q0/2 - 1 mod q0 and every epsilon > 0, R_{q0}(y) <= y^(-1/2 + epsilon) for all large real y."
aliases = ["one-sided bound", "eventually_primeRemainder_le_rpow"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.eventually_primeRemainder_le_rpow", "New.eventually_primeRemainder_natCast_le", "New.eventually_exists_data_scales", "New.eventually_abs_primeRemainder_exp_le", "New.primeRemainder_sub_primeRemainder_floor_le", "New.natFloor_rpow_le_two_mul_rpow", "New.dvd_two_mul_succ_and_not_dvd_succ"]
lean_files = ["src/New/Reduction/OneSidedBound.lean"]
proof_status = "full"
+++

**Theorem (one-sided bound).** Let \(q_0\ge1\) be a multiple of \(18480\), let \(d\) be a prime with \(d\equiv q_0/2-1\pmod{q_0}\), and let \(\varepsilon>0\). Let
\[
R(y)=R_{q_0}(y)=\sum_{n\le y,\ n\equiv1\,(q_0)}\Lambda(n)\bigl(1-(\tfrac nd)\bigr)\Bigl(\frac1n-\frac1y\Bigr)-\frac{\log y}{\varphi(q_0)}-c_{q_0}
\]
be the [[?lean:New.primeRemainder|prime remainder]]. Then there is \(y_0\) such that \(R(y)\le y^{-1/2+\varepsilon}\) for all **real** \(y\ge y_0\).

The intermediate statement at integers is: for parameters \(P=(q_0,d)\) and \(0<\varepsilon<1/100\),
\[
R(x)\le\bigl(64\varphi(q_0)+3\bigr)\,x^{-1/2+6\varepsilon}\qquad\text{for all large integers } x .
\]

## Proof

Complete relative to the main inequality, the existence of the data, and two results on \(R_q\) from the chapter on zeros.

**Step 0: parameters.** Since \(q_0\) is even, \(d\equiv q_0/2-1\) gives \(d+1\equiv q_0/2\pmod{q_0}\); so \(q_0\mid2(d+1)\) and \(q_0\nmid d+1\). Thus \(P=(q_0,d)\) are [[proofs/grh/reduction-main/parameters|parameters]].

**Step 1: at integers.** Let \(0<\varepsilon<1/100\). For every large integer \(x\) there are [[proofs/grh/reduction-main/data-exist|data \(D\)]] with scale \(x\), \(\log b\le x^\varepsilon+1\le2x^\varepsilon\), \(m\ge\sqrt x\) and \(\log x_1\ge x^{\varepsilon/6}-1\ge x^{\varepsilon/12}\) (for \(x^{\varepsilon/12}\ge2\)). By the [[?lean:New.eventually_abs_primeRemainder_le|prime number theorem for \(R_q\)]] (for an odd prime \(d\) and \(q\) prime to \(d\): \(\lvert R_q(y)\rvert\le(\log y)^{-B}\) for large \(y\), any fixed \(B\)), applied with \(q\in\{q_0,1\}\) and an integer \(B\ge24/\varepsilon\): for large \(x\) and all \(l\ge x^{\varepsilon/12}\), \(\lvert R_q(e^l)\rvert\le l^{-B}\le x^{-\varepsilon B/12}\le x^{-2}\). In particular \(\lvert R_{q_0}(x_1)\rvert,\lvert R_1(x_1)\rvert\le x^{-2}\). Insert into the [[proofs/grh/reduction-main/prime-remainder-bound-from-data|bound through the data]]:
\[
R(x)\le\frac{\varphi(q_0)(2x^\varepsilon)^6}{\sqrt x}+x^{-2}+2x^\varepsilon x^{-2}\le\bigl(64\varphi(q_0)+3\bigr)x^{-1/2+6\varepsilon}.
\]

**Step 2: from integers to real numbers.** This is the bridge needed by the [[?lean:New.LFunction_ne_zero_of_primeRemainder_le|one-sided criterion]], whose hypothesis is a bound for all large *real* arguments, while the data (and hence Step 1) exist only at integer \(x\). The Lean proof bridges it by the slow variation of \(R\): [[?lean:New.abs_primeRemainder_sub_le|\(\lvert R_q(z)-R_q(y)\rvert\le13(z-y)/y\) for \(1\le y\le z\)]]. Applied to \(\lfloor y\rfloor\le y\) with \(y\ge2\) (so \(\lfloor y\rfloor\ge y/2\) and \(y-\lfloor y\rfloor<1\)):
\[
R(y)\le R(\lfloor y\rfloor)+\frac{26}{y}.
\]
Choose \(\delta=\min(1/200,\varepsilon/7)\), so \(0<\delta<1/100\) and \(7\delta\le\varepsilon\); put \(t=-\tfrac12+6\delta\in[-1,0]\) and \(C=64\varphi(q_0)+3\). As \(y\to\infty\), \(\lfloor y\rfloor\to\infty\) through integers, so Step 1 (with \(\delta\)) gives \(R(\lfloor y\rfloor)\le C\lfloor y\rfloor^{t}\) for large \(y\); and \(\lfloor y\rfloor^t\le(y/2)^t\le2y^t\) since \(-1\le t\le0\). Also \(26/y\le26y^t\). Hence for large \(y\)
\[
R(y)\le(2C+26)\,y^{t}\le y^{\delta}y^{t}=y^{-1/2+7\delta}\le y^{-1/2+\varepsilon},
\]
using \(2C+26\le y^\delta\) for large \(y\) and \(y\ge1\).

## References

1. Lean: `New.eventually_primeRemainder_le_rpow` (real \(y\)), `New.eventually_primeRemainder_natCast_le` (integers), `New.eventually_exists_data_scales`, `New.eventually_abs_primeRemainder_exp_le`, `New.primeRemainder_sub_primeRemainder_floor_le`, `New.natFloor_rpow_le_two_mul_rpow`, `New.dvd_two_mul_succ_and_not_dvd_succ` in `src/New/Reduction/OneSidedBound.lean`.
