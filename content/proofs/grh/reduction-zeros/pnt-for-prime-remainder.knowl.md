+++
id = "proofs/grh/reduction-zeros/pnt-for-prime-remainder"
title = "The prime number theorem for the remainders R_q"
kind = "theorem"
summary = "For odd d prime to q the remainder R_q(y) is at most (log y)^(-B) in absolute value for every B and all large y; in particular it tends to 0."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.eventually_abs_primeRemainder_le", "New.tendsto_primeRemainder"]
lean_files = ["src/New/Reduction/Zeros/PrimeNumberTheorem.lean"]
proof_status = "full"
+++

**Theorem.** Let \(d\) be an odd prime and \(q\ge1\) an integer prime to \(d\). For every integer \(B\ge0\) there is \(y_0\) such that the [[proofs/grh/reduction-zeros/prime-remainder|remainder]] satisfies
\[
\lvert R_q(y)\rvert\le(\log y)^{-B}\qquad\text{for all }y\ge y_0 .
\]
In particular \(R_q(y)\to0\) as \(y\to\infty\); so \(c_q\) is the limit of \(\sum_{n\le y}\lambda(n)(1/n-1/y)-\log y/\varphi(q)\).

## Proof

Apply the [[proofs/grh/reduction-zeros/tauberian-theorem|Tauberian theorem]] to \(R(v)=R_q(e^{v})\) and \(F(s)=G_q(s)/s\), with \(L=26\) and \(A=26\). Its hypotheses hold:

* \(R\) is measurable, and \(\lvert R(v)-R(u)\rvert\le26(v-u)\) for \(0\le u\le v\le u+1\) by [[proofs/grh/reduction-zeros/prime-remainder-varies-slowly|slow variation]];
* for \(\operatorname{Re}s>2\), \(\int_0^\infty R(v)e^{(1-s)v}dv=\dfrac{G_q(s)/s-c_q}{s-1}=\dfrac{F(s)-F(1)}{s-1}\), by the [[proofs/grh/reduction-zeros/laplace-transform-of-prime-remainder|transform of the remainder]] and \(F(1)=G_q(1)=c_q\) ([[proofs/grh/reduction-zeros/g-q-at-one-is-real|\(G_q(1)\) is real]]);
* for all large \(l\), \(F\) is holomorphic and at most \(l^{26}\) on \(\operatorname{Re}s\ge1-l^{-26}\), \(\lvert s\rvert\le e^{l}\), by the [[proofs/grh/reduction-zeros/bound-for-log-deriv-mean-near-one|bound for \(G_q(s)/s\)]].

Hence \(\lvert R_q(e^{v})\rvert\le v^{-B}\) for all large \(v\); put \(v=\log y\). The limit follows from the case \(B=1\). \(\blacksquare\)

## Remarks

This is a case of the [[?c:Siegel–Walfisz theorem|prime number theorem in arithmetic progressions]] for a fixed modulus, for the smoothed sum over prime powers \(n\equiv1\pmod q\) with the weights \(1-(n/d)\).

## References

1. Lean: `New.eventually_abs_primeRemainder_le`, `New.tendsto_primeRemainder` in `src/New/Reduction/Zeros/PrimeNumberTheorem.lean`.
2. H. L. Montgomery, R. C. Vaughan, *Multiplicative Number Theory I*, 2007, Corollary 11.19 (as cited in the head of the Lean file).
