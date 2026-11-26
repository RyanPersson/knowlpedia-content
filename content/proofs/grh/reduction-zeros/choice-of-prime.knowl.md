+++
id = "proofs/grh/reduction-zeros/choice-of-prime"
title = "Choice of a prime whose twists have no zero in a box"
kind = "theorem"
summary = "In an invertible class modulo N whose primes are 7 mod 8 and prime to N there is a prime d such that no L(s, xi (./d)), xi modulo N, vanishes in Re s >= beta, |Im s| <= H, for given beta > 1/2."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.exists_entireL_quadTwist_ne_zero"]
lean_files = ["src/Lib/Analytic/QuadraticTwist.lean"]
proof_status = "full"
+++

**Theorem (choice of the prime).** Let \(N\ge1\), \(\beta>\tfrac12\), \(H\in\mathbb{R}\), and let \(a\) be an invertible residue class modulo \(N\) such that every prime \(d\equiv a\pmod N\) satisfies \(d\equiv7\pmod 8\) and \(\gcd(N,d)=1\). Then there is a prime \(d\equiv a\pmod N\) such that for every Dirichlet character \(\xi\) modulo \(N\) and every \(s\) with \(\operatorname{Re}s\ge\beta\), \(\lvert\operatorname{Im}s\rvert\le H\):
\[
E_{\xi\chi_K}(s)\ne0 ,
\]
where \(\xi\chi_K\) is the [[?lean:New.quadTwist|twist]] by \((\cdot/d)\) and \(E\) is [[?lean:New.entireL|the \(L\)-function with the pole removed]] (here simply \(L(s,\xi\chi_K)\), as the twists are not principal).

## Proof

Put \(\delta=(\beta-\tfrac12)/9>0\), so \(\beta=\tfrac12+9\delta\). Suppose the conclusion fails for every prime \(d\equiv a\pmod N\). For such \(d\), \(d\) is odd and prime to \(N\), so \(\xi\chi_K\) is [[proofs/grh/reduction-zeros/quad-twist-not-principal|not principal]] and \(E_{\xi\chi_K}=L(\cdot,\xi\chi_K)\); thus every prime of the class is [[proofs/grh/reduction-zeros/bad-primes-are-rare|bad]]. By the theorem on bad primes, the number of primes \(p\le X\) with \(p\equiv a\pmod N\) is \(O(X^{1-\delta/2})\).

Let \(f(n)=1\) if \(n\) is a prime \(\equiv a\pmod N\) and \(f(n)=0\) otherwise. Since \(\sum_{n\le X}\lvert f(n)\rvert=O(X^{1-\delta/2})\), the [[?c:Dirichlet series|Dirichlet series]] \(\sum f(n)n^{-s}\) converges absolutely for \(\operatorname{Re}s>1-\delta/2\), so its [[?c:abscissa of absolute convergence|abscissa of absolute convergence]] is \(<1\). The same holds for \(\sum f(n)\log n\cdot n^{-s}\); in particular
\[
\sum_{p\equiv a\ (N)}\frac{\log p}{p}<\infty .
\]
But for an invertible class \(a\) [[?c:divergence of the sum of log p / p over a residue class|this series diverges]] (Dirichlet). Contradiction. \(\blacksquare\)

## Remarks

* The hypothesis on the class holds if \(8\mid N\) and \(a\) is the class of a number \(\equiv7\pmod8\) prime to \(N\); this is how the [[proofs/grh/reduction-zeros/one-sided-criterion|one-sided criterion]] uses it.
* Only the divergence of \(\sum\log p/p\) over the class is used, not the prime number theorem for progressions.
* The source first reduces to \(\beta<1\) (a smaller \(\beta\) gives a larger box); the argument above does not need this.

## References

1. Lean: `New.exists_entireL_quadTwist_ne_zero` in `src/Lib/Analytic/QuadraticTwist.lean`.
