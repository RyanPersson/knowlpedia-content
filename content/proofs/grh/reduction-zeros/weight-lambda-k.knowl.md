+++
id = "proofs/grh/reduction-zeros/weight-lambda-k"
title = "The weight on prime powers in the class 1 that do not split"
kind = "definition"
summary = "The function Lambda(n)(1 - (n/d)) on integers n congruent to 1 modulo q, and 0 elsewhere."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.lambdaKResidueClass", "New.one_sub_chiK_mem_Icc", "New.lambdaKResidueClass_nonneg", "New.lambdaKResidueClass_le_two_mul_vonMangoldt", "New.lambdaKResidueClass_le_two_mul"]
lean_files = ["src/New/Reduction/Zeros/PrimeError.lean"]
+++

Let \(d\) be a prime, \(q\ge1\) an integer, \(\Lambda\) the [[?c:von Mangoldt function|von Mangoldt function]] and \(\chi_K(n)=(n/d)\) the [[?c:Legendre symbol|Legendre symbol]] ([[?lean:New.chiK|the character \(\chi_K\)]]; for \(d\equiv3\pmod4\) it is the quadratic character of \(K=\mathbb{Q}(\sqrt{-d})\)). The **weight** \(\lambda=\lambda_{d,q}\colon\mathbb{N}\to\mathbb{R}\) is
\[
\lambda(n)=\begin{cases}\Lambda(n)\,\bigl(1-\chi_K(n)\bigr)&\text{if }n\equiv1\pmod q,\\[2pt] 0&\text{otherwise.}\end{cases}
\]

## Properties

Since \(\chi_K(n)\in\{0,1,-1\}\), we have \(0\le1-\chi_K(n)\le2\). Hence, for all \(n\),
\[
0\le\lambda(n)\le2\Lambda(n)\le2\log n\le2n\qquad(n\ge1),\qquad \lambda(0)=0 .
\]
The weight is supported on prime powers \(p^k\equiv1\pmod q\) with \(\chi_K(p^k)\neq1\): it vanishes when \(p\) splits in \(K\), and when \(p\) is inert and \(k\) is even.

## References

1. Lean: `New.lambdaKResidueClass` and the lemmas following it in `src/New/Reduction/Zeros/PrimeError.lean`.
