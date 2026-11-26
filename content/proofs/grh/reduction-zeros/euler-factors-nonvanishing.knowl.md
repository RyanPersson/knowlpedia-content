+++
id = "proofs/grh/reduction-zeros/euler-factors-nonvanishing"
title = "Inverse Euler factors do not vanish off the imaginary axis"
kind = "lemma"
summary = "For a Dirichlet character and Re s nonzero, a finite product of factors 1 - chi(p) p^(-s) is nonzero."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.prod_euler_factor_ne_zero"]
lean_files = ["src/Lib/Analytic/ZeroSymmetry.lean"]
proof_status = "full"
+++

**Lemma.** Let \(\chi\) be a complex [[?c:Dirichlet character|Dirichlet character]] modulo \(N\), let \(M\ge1\) be an integer and let \(s\in\mathbb{C}\) with \(\operatorname{Re}s\ne0\). Then
\[
\prod_{p\mid M}\bigl(1-\chi(p)\,p^{-s}\bigr)\neq0 ,
\]
the product being over the primes dividing \(M\).

## Proof

It suffices to show that no factor vanishes. Suppose \(1-\chi(p)p^{-s}=0\) for a prime \(p\). Then \(\chi(p)=p^{s}\), so \(\lvert\chi(p)\rvert=p^{\operatorname{Re}s}>0\). A value of a Dirichlet character is \(0\) or a root of unity, so \(\lvert\chi(p)\rvert=1\), hence \(p^{\operatorname{Re}s}=1\) and \(\operatorname{Re}s=0\) because \(p>1\). This contradicts the hypothesis. \(\blacksquare\)

## References

1. Lean: `New.prod_euler_factor_ne_zero` in `src/Lib/Analytic/ZeroSymmetry.lean`.
