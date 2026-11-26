+++
id = "proofs/grh/reduction-main/prime-sum"
title = "Prime sum, jet size, direction amount and error unit"
kind = "definition"
summary = "The sum s_fin(y, sigma) of Lambda_K(nu)(y/nu - kappa(-nu sigma))_+ over nu up to a; the size s_inf(j) of a derivative; the direction amount; and the unit f a log^3 b of the errors."
aliases = ["primeSum", "s_fin", "jetSize", "s_inf", "directionAmount", "errorUnit"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.primeSum", "New.Data.jetSize", "New.Data.directionAmount", "New.Data.errorUnit"]
lean_files = ["src/New/Reduction/Data/AdmissibleData.lean"]
+++

Let \(D\) be [[proofs/grh/reduction-main/data|data]] with the [[proofs/grh/reduction-main/data-derived-quantities|derived quantities]] \(a=xb\), \(f\), \(M\), weight \(\kappa\), and \(\Omega=\Omega_s\) as in [[proofs/grh/reduction-main/field-e-and-its-places|the field \(E\)]]. Let \(\Lambda\) be the [[?c:von Mangoldt function|von Mangoldt function]], \(\chi_K=(\tfrac\cdot d)\) the Legendre symbol, and
\[
\Lambda_K(\nu):=\Lambda(\nu)\bigl(1-\chi_K(\nu)\bigr)\in[0,2\Lambda(\nu)] .
\]
Write \(u_+=\max(u,0)\).

- The **prime sum** at an order \(y\in\mathbb R\) and a place \(\sigma\in\Phi\) is
\[
s_{\mathrm{fin}}(y,\sigma):=\sum_{\nu=1}^{a}\Lambda_K(\nu)\Bigl(\frac y\nu-\kappa(-\nu\sigma)\Bigr)_+ ,
\]
where \(-\nu\sigma=\operatorname{place}(-\nu)\cdot\sigma\) (so \(-\nu\sigma=\sigma\) when \(\gcd(\nu,q_1)\ne1\)).
- The **jet size** of a derivative of order \(j\in\mathbb N\) is \(s_\infty(j):=\log j!+j\log(M/\Omega)\).
- The **direction amount** is \(h_{\mathrm{dir}}:=\sum_{\sigma\in\Phi}\bigl(s_\infty(\kappa(\sigma))-s_{\mathrm{fin}}(\kappa(\sigma),\sigma)\bigr)\).
- The **error unit** is \(f\,a\,(\log b)^3\).

## References

1. Lean: `New.Data.primeSum`, `New.Data.jetSize`, `New.Data.directionAmount`, `New.Data.errorUnit` in `src/New/Reduction/Data/AdmissibleData.lean`; \(\Lambda_K\) is `New.lambdaKResidueClass d 1` of `src/New/Reduction/Zeros/PrimeError.lean`.
