+++
id = "proofs/grh/upper-elementary-divisors/consequences-of-large-degree"
title = "Numerical consequences of large degree"
kind = "lemma"
summary = "Inequalities between N, k, n, r, theta, P, q, the multinomial exponent, the divisor constant and the defect threshold that follow from the conditions of large degree."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.FrobeniusCycle.IsLargeDegree.two_le_rank", "New.FrobeniusCycle.IsLargeDegree.four_le_mul", "New.FrobeniusCycle.IsLargeDegree.mul_pow_le_degree", "New.FrobeniusCycle.IsLargeDegree.twenty_seven_le_log_q", "New.FrobeniusCycle.IsLargeDegree.mul_degree_add_lt_P_pow", "New.FrobeniusCycle.IsLargeDegree.one_lt_degree", "New.FrobeniusCycle.IsLargeDegree.degree_lt_q", "New.FrobeniusCycle.IsLargeDegree.mul_log_pow_mul_le", "New.FrobeniusCycle.IsLargeDegree.multinomialExponent_mul_le_degree", "New.FrobeniusCycle.IsLargeDegree.mul_multinomialExponent_le_divisorConstant", "New.FrobeniusCycle.IsLargeDegree.mul_defectThreshold_le_mul_degree", "New.FrobeniusCycle.multinomialExponent_le_mul_log", "New.FrobeniusCycle.congruencePrecision_le_mul_log", "New.FrobeniusCycle.two_le_mul_multinomialExponent"]
lean_files = ["src/New/UpperBound/ElementaryDivisors/ElementaryDivisorTheorem.lean"]
proof_status = "outline"
+++

**Lemma.** Let \(T\) be a [[proofs/grh/upper-elementary-divisors/frobenius-cycle|Frobenius cycle]] with \(N\ge1\) letters and let the degree be [[proofs/grh/upper-elementary-divisors/large-degree-conditions|large]] for \((k,n,r,\theta)\). Put \(c_0=k^{2}fN\), \(c=5Nc_0\), \(c^{*}=3kc\), and \(\Delta=\Delta_T(k,n,r)=Nn(P^{-2r}+r^{2}/(kP))\) (the [[proofs/grh/upper-elementary-divisors/sum-of-dimensions-of-deep-forms|divisor constant]]). Then:

1. \(k\ge2\), \(Nk\ge4\), \(Nc_0\ge2\) (the last for any \(k\ge2\));
2. \((Nk)^{5}\le n\), in particular \(n>1\); and \(n<q\); and \(\log q\ge27\);
3. if \(N=2\ell\): \(N\,k\,(\ell+2)\,n+n+k<P^{\ell}\);
4. \(c_0\le\tfrac32k^{2}\log q\) and \(c\le\tfrac{15}2k^{2}N\log q\) (for any cycle);
5. \(c_0\,P^{2r}\le n\), and \(N\,c_0\le\Delta\);
6. \(8\,N\,k\,c^{*}\,P^{2r}\le\theta\,n\).

## Proof

Outline only. The first statement of 1 is \(k\ge2r\ge2\); \(N\ge2\) because \(N\) is even and positive; \(Nc_0\ge k^{2}\ge2\) as \(f,N\ge1\) (\(P=p^{f}\ge5\) forces \(f\ge1\)). For 2: \(q\ge5\) gives \(\log q\ge1\), so condition 4 of large degree with \(\theta\le1\), \(P^{3r}\ge1\) gives \((Nk)^{5}\le n\); \(n<n^{4}\le q\) for \(n>1\); and \(q\ge n^{4}\ge4^{20}\). For 4: \(c_0=k^{2}\log_pq\) and \(\log p\ge\log2\ge\tfrac23\). The remaining inequalities (3, 5, 6, and the constant in 2) are elementary real arithmetic from the four conditions; their proofs were not transcribed here and are asserted on the authority of the formal proofs (for 3, the source indicates the route \(P^{\ell}=\sqrt q\ge n^{2}\) and \(n\ge(Nk)^{2}+2\)). The declarations concerned are listed in the References.

## References

1. Lean: `New.FrobeniusCycle.IsLargeDegree.two_le_rank`, `New.FrobeniusCycle.IsLargeDegree.four_le_mul`, `New.FrobeniusCycle.IsLargeDegree.mul_pow_le_degree`, `New.FrobeniusCycle.IsLargeDegree.twenty_seven_le_log_q`, `New.FrobeniusCycle.IsLargeDegree.mul_degree_add_lt_P_pow`, `New.FrobeniusCycle.IsLargeDegree.one_lt_degree`, `New.FrobeniusCycle.IsLargeDegree.degree_lt_q`, `New.FrobeniusCycle.IsLargeDegree.mul_log_pow_mul_le`, `New.FrobeniusCycle.IsLargeDegree.multinomialExponent_mul_le_degree`, `New.FrobeniusCycle.IsLargeDegree.mul_multinomialExponent_le_divisorConstant`, `New.FrobeniusCycle.IsLargeDegree.mul_defectThreshold_le_mul_degree`, `New.FrobeniusCycle.multinomialExponent_le_mul_log`, `New.FrobeniusCycle.congruencePrecision_le_mul_log`, `New.FrobeniusCycle.two_le_mul_multinomialExponent` in `src/New/UpperBound/ElementaryDivisors/ElementaryDivisorTheorem.lean`.
2. Asserted without transcribed proof: `New.FrobeniusCycle.IsLargeDegree.mul_degree_add_lt_P_pow` (item 3), `New.FrobeniusCycle.IsLargeDegree.multinomialExponent_mul_le_degree` and `New.FrobeniusCycle.IsLargeDegree.mul_multinomialExponent_le_divisorConstant` (item 5), `New.FrobeniusCycle.IsLargeDegree.mul_defectThreshold_le_mul_degree` (item 6), `New.FrobeniusCycle.IsLargeDegree.twenty_seven_le_log_q` (the constant 27 in item 2).
