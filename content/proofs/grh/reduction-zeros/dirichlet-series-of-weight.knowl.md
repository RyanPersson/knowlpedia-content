+++
id = "proofs/grh/reduction-zeros/dirichlet-series-of-weight"
title = "The Dirichlet series of the weight"
kind = "proposition"
summary = "For odd d prime to q and Re s > 1 the Dirichlet series of the weight is s/(phi(q)(s-1)) + G_q(s); for Re s > 2 it is (s + r - 1) times a Laplace transform of S_r."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.LSeries_lambdaKResidueClass_eq_add_logDerivMean", "New.LSeries_lambdaKResidueClass"]
lean_files = ["src/New/Reduction/Zeros/PrimeError.lean"]
proof_status = "full"
+++

**Proposition.** Let \(d\) be a prime, \(q\ge1\), \(\lambda\) the [[proofs/grh/reduction-zeros/weight-lambda-k|weight]], \(S_r\) the sums of the [[proofs/grh/reduction-zeros/prime-remainder|remainder]] and \(G_q\) the [[proofs/grh/reduction-zeros/log-deriv-mean|mean of logarithmic derivatives]].

1. (Partial summation.) For every integer \(r\ge0\) and \(\operatorname{Re}s>2\),
\[
\sum_{n\ge1}\lambda(n)n^{-s}=(s+r-1)\int_0^\infty S_r(e^{v})\,e^{(1-s)v}\,dv .
\]
2. If \(d\ne2\) and \(\gcd(q,d)=1\), then for \(\operatorname{Re}s>1\),
\[
\sum_{n\ge1}\lambda(n)n^{-s}=\frac{s}{\varphi(q)(s-1)}+G_q(s).
\]

## Proof

1. Put \(f(n)=\lambda(n)n^{r-1}\) and \(w=s+r-1\). Then \(\sum\lambda(n)n^{-s}=\sum f(n)n^{-w}\). By the [[proofs/grh/reduction-zeros/growth-of-prime-remainder|growth bound]], \(\sum_{k\le n}\lvert f(k)\rvert=n^{r}S_r(n)\le2n^{r+1}\), and \(\operatorname{Re}w>r+1\). The [[?c:Abel summation formula|Abel summation formula]] gives
\(\sum f(n)n^{-w}=w\int_1^\infty\bigl(\sum_{k\le t}f(k)\bigr)t^{-w-1}dt\). Substituting \(t=e^{v}\), with \(\sum_{k\le e^v}f(k)=e^{rv}S_r(e^v)\), the integrand becomes \(e^{rv}S_r(e^{v})e^{-(s+r)v}e^{v}=S_r(e^v)e^{(1-s)v}\).

2. By [[?c:orthogonality of Dirichlet characters|orthogonality]], \(\frac1{\varphi(q)}\sum_{\psi}\psi(n)\) is \(1\) if \(n\equiv1\pmod q\) and \(0\) otherwise. Since \((\psi\chi_K)(n)=\psi(n)(n/d)\) ([[proofs/grh/reduction-zeros/quad-twist-not-principal|values of the twist]]),
\[
\lambda(n)=\frac1{\varphi(q)}\sum_{\psi\bmod q}\bigl(\psi(n)\Lambda(n)-(\psi\chi_K)(n)\Lambda(n)\bigr).
\]
By the [[proofs/grh/reduction-zeros/dirichlet-series-of-chi-lambda|series of \(\chi\Lambda\)]], for \(\operatorname{Re}s>1\) the series of \(\psi\Lambda\) is \(\delta_\psi/(s-1)-E_\psi'/E_\psi(s)\), and that of \((\psi\chi_K)\Lambda\) is \(-E_{\psi\chi_K}'/E_{\psi\chi_K}(s)\), because no twist is principal (\(d\) odd, prime to \(q\)). Summing over \(\psi\), only \(\psi=1\) contributes a term \(1/(s-1)\):
\[
\sum\lambda(n)n^{-s}=\frac1{\varphi(q)}\Bigl(\frac1{s-1}+\sum_\psi\Bigl(\frac{E_{\psi\chi_K}'}{E_{\psi\chi_K}}-\frac{E_\psi'}{E_\psi}\Bigr)(s)\Bigr)=\frac1{\varphi(q)}\Bigl(\frac1{s-1}+1\Bigr)+G_q(s),
\]
and \(\frac1{s-1}+1=\frac s{s-1}\). \(\blacksquare\)

## References

1. Lean: `New.LSeries_lambdaKResidueClass`, `New.LSeries_lambdaKResidueClass_eq_add_logDerivMean` in `src/New/Reduction/Zeros/PrimeError.lean`.
2. H. Davenport, *Multiplicative Number Theory* (as cited in the head of the Lean file).
