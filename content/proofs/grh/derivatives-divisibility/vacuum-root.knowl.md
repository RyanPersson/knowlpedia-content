+++
id = "proofs/grh/derivatives-divisibility/vacuum-root"
title = "The number s_0 and the absolute values of its conjugates"
kind = "theorem"
summary = "The number s_0 is the principal f-th root of the inverse of chi_f(alpha); for every automorphism sigma of C over K, the square of the absolute value of sigma(s_0) is the root discriminant of E divided by the square root of d."
aliases = ["vacuum root", "number s_0"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Parameters.vacuumRoot", "New.Parameters.norm_gal_vacuumRoot", "New.Parameters.vacuumRoot_pow_numInfPlaces", "New.Parameters.exists_chiFin_alpha_pow_mem", "New.Parameters.exists_vacuumRoot_pow_mem", "New.Parameters.ideleAbs_alpha_eq_prod"]
lean_files = ["src/New/Derivatives/Field/WeilData.lean"]
proof_status = "full"
+++

**Definition.** Let \(E=K(\zeta)\) with \(f\) infinite places, and \((\jmath,\alpha,\upsilon)\) its [[proofs/grh/derivatives-divisibility/weil-data-of-e|Weil data]]. Let \(\chi_f(x)=\upsilon(x)\,\lvert x\rvert^{-1/2}\) for a finite idele \(x\), extended by \(1\) at the infinite places, where \(\lvert\cdot\rvert\) is the [[?c:idele norm|idele norm]] (this is the [[?lean:New.chiFin|character \(\chi_f\)]]). The number
\[
s_0=\bigl(\chi_f(\alpha)^{-1}\bigr)^{1/f}\in\mathbb{C}
\]
is the principal \(f\)-th root; so \(s_0^{\,f}=\chi_f(\alpha)^{-1}=\upsilon(\alpha)^{-1}\lvert\alpha\rvert^{1/2}\).

**Theorem.** For every field automorphism \(\sigma\) of \(\mathbb{C}\) over \(K\),
\[
\lvert\sigma(s_0)\rvert^2=\frac{\mathrm{rd}_E}{\sqrt d},
\]
where \(\mathrm{rd}_E\) is the root discriminant of \(E\).

## Proof

*A power of \(s_0\) lies in \(K\).* By the [[?lean:New.WeilData.exists_chiFin_pow_eq_prod|algebraicity of \(\chi_f\)]], there are \(k>0\) and \(y\in E^\times\) with \(\chi_f(\alpha)^k=\prod_v\Phi_v(\bar y)=N_{E/K}(\bar y)\in K\). Hence \(s_0^{fk}\in K\) is fixed by \(\sigma\), so \(\lvert\sigma s_0\rvert^{fk}=\lvert s_0\rvert^{fk}\) and \(\lvert\sigma s_0\rvert=\lvert s_0\rvert\).

*The idele norm of \(\alpha\).* Since \(\lvert\upsilon\rvert=1\), \(\lvert s_0\rvert^{2f}=\lvert\chi_f(\alpha)\rvert^{-2}=\lvert\alpha\rvert\). Consider the idele \(x=\alpha\bar\alpha P'(\zeta)\) (with \(P'(\zeta)\) embedded diagonally). By the product formula and \(\lvert\bar\alpha\rvert=\lvert\alpha\rvert\), \(\lvert x\rvert=\lvert\alpha\rvert^2\). The finite components of \(x\) are units (see the Weil data), and its component at an infinite place \(v\) is \(\Phi_v(P'(\zeta))\), contributing \(\lvert P'(\zeta)\rvert_v^2\). So \(\lvert\alpha\rvert=\prod_v\lvert P'(\zeta)\rvert_v\).

*Conclusion.* By part 5 of the [[proofs/grh/derivatives-divisibility/different-of-e|theorem on the different]], \(\prod_v\lvert P'(\zeta)\rvert_v=\prod_v\lvert\delta_E\rvert_v/\sqrt d^{\,f}=(\mathrm{rd}_E/\sqrt d)^f\). Taking \(f\)-th roots of positive numbers, \(\lvert s_0\rvert^2=\mathrm{rd}_E/\sqrt d\). \(\blacksquare\)

## References

1. Lean: `New.Parameters.vacuumRoot`, `New.Parameters.norm_gal_vacuumRoot`, `New.Parameters.ideleAbs_alpha_eq_prod` in `src/New/Derivatives/Field/WeilData.lean`.
