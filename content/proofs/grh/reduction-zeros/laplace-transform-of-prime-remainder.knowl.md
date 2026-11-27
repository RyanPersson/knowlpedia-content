+++
id = "proofs/grh/reduction-zeros/laplace-transform-of-prime-remainder"
title = "The Laplace transform of the remainder"
kind = "proposition"
summary = "For odd d prime to q and Re s > 2 the transform of R_q(e^v) against e^((1-s)v) is (G_q(s)/s - c_q)/(s-1)."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.integral_primeRemainder", "New.laplace_pow"]
lean_files = ["src/New/Reduction/Zeros/PrimeError.lean", "src/Lib/Analytic/EntireLFunction.lean"]
proof_status = "full"
+++

**Proposition.** Let \(d\) be an odd prime, \(q\ge1\) prime to \(d\), and \(R_q\), \(c_q\), \(G_q\) as in the [[proofs/grh/reduction-zeros/prime-remainder|definition of the remainder]]. For \(\operatorname{Re}s>2\),
\[
\int_0^\infty R_q(e^{v})\,e^{(1-s)v}\,dv=\frac{G_q(s)/s-c_q}{s-1}.
\]

## Proof

Write \(D(s)=\dfrac{s}{\varphi(q)(s-1)}+G_q(s)\). By the [[proofs/grh/reduction-zeros/dirichlet-series-of-weight|two formulas for the Dirichlet series]] (with \(r=0\) and \(r=1\)),
\[
\int_0^\infty S_0(e^v)e^{(1-s)v}dv=\frac{D(s)}{s-1},\qquad\int_0^\infty S_1(e^v)e^{(1-s)v}dv=\frac{D(s)}{s}.
\]
All integrals converge absolutely by the [[proofs/grh/reduction-zeros/growth-of-prime-remainder|growth bounds]]. Moreover \(\int_0^\infty v^{k}e^{-(s-1)v}dv=k!/(s-1)^{k+1}\) for \(k=0,1\). Since \(R_q(e^{v})=S_0(e^v)-S_1(e^v)-v/\varphi(q)-c_q\),
\[
\int_0^\infty R_q(e^{v})e^{(1-s)v}dv=\frac{D(s)}{s(s-1)}-\frac{1}{\varphi(q)(s-1)^2}-\frac{c_q}{s-1}.
\]
Now \(\dfrac{D(s)}{s(s-1)}=\dfrac{1}{\varphi(q)(s-1)^2}+\dfrac{G_q(s)}{s(s-1)}\), so the right side is \(\bigl(G_q(s)/s-c_q\bigr)/(s-1)\). \(\blacksquare\)

## References

1. Lean: `New.integral_primeRemainder` in `src/New/Reduction/Zeros/PrimeError.lean`; `New.laplace_pow` in `src/Lib/Analytic/EntireLFunction.lean`.
