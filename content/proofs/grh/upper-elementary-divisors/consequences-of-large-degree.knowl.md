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
proof_status = "full"
+++

**Lemma.** Let \(T\) be a [[proofs/grh/upper-elementary-divisors/frobenius-cycle|Frobenius cycle]] with \(N\ge1\) letters and let the degree be [[proofs/grh/upper-elementary-divisors/large-degree-conditions|large]] for \((k,n,r,\theta)\). Put \(c_0=k^{2}fN\), \(c=5Nc_0\), \(c^{*}=3kc\), and \(\Delta=\Delta_T(k,n,r)=Nn(P^{-2r}+r^{2}/(kP))\) (the [[proofs/grh/upper-elementary-divisors/sum-of-dimensions-of-deep-forms|divisor constant]]). Then:

1. \(k\ge2\), \(Nk\ge4\), \(Nc_0\ge2\) (the last for any \(k\ge2\));
2. \((Nk)^{5}\le n\), in particular \(n>1\); and \(n<q\); and \(\log q\ge27\);
3. if \(N=2\ell\): \(N\,k\,(\ell+2)\,n+n+k<P^{\ell}\);
4. \(c_0\le\tfrac32k^{2}\log q\) and \(c\le\tfrac{15}2k^{2}N\log q\) (for any cycle);
5. \(c_0\,P^{2r}\le n\), and \(N\,c_0\le\Delta\);
6. \(8\,N\,k\,c^{*}\,P^{2r}\le\theta\,n\).

## Proof

Write \(\mathsf{L}=\log q\) and \(u=N\,k\,\mathsf{L}\). Recall \(P=p^{f}\ge5\), so \(f\ge1\) and \(P\ge1\), and \(q=P^{N}\).

(1) \(k\ge2r\ge2\). The number \(N\) is positive and even (half of the letters are even), so \(N\ge2\) and \(Nk\ge4\). For any \(k\ge2\): \(Nc_0=N\cdot k^{2}fN\ge k^{2}\ge2\).

(2) Since \(q\ge5>e\), \(\mathsf{L}\ge1\). As \(0<\theta\le1\) and \(P^{3r}\ge1\), \((Nk)^{5}\le(u/\theta)^{5}P^{3r}\le n\). Hence \(n\ge4^{5}>1\), and \(n<n^{4}\le q\). Moreover \(q\ge n^{4}\ge(4^{5})^{4}=2^{40}\), so \(\mathsf{L}\ge40\log2\ge27\) (as \(\log2>0.69\)).

(3) Let \(N=2\ell\). From \((P^{\ell})^{2}=q\ge n^{4}\) we get \(P^{\ell}\ge n^{2}\). Also \(\ell+2\le Nk\) (as \(Nk\ge2N=4\ell\ge\ell+2\) for \(\ell\ge1\)), \((Nk)^{2}+2\le(Nk)^{2}\cdot4^{3}\le(Nk)^{5}\le n\), and \(k<n\). Therefore
\[
Nk(\ell+2)n+n+k<(Nk)^{2}n+2n=\bigl((Nk)^{2}+2\bigr)n\le n^{2}\le P^{\ell}.
\]

(4) \(\mathsf{L}=fN\log p\) and \(\log p\ge\log2\ge\tfrac23\), so \(fN\le\tfrac32\mathsf{L}\), \(c_0=k^{2}fN\le\tfrac32k^{2}\mathsf{L}\), and \(c=5Nc_0\le\tfrac{15}2k^{2}N\mathsf{L}=\tfrac{15}2\,k\,u\).

(5) First, clearing the denominator in condition 4 of large degree and using \(\theta^{5}\le\theta\),
\[
u^{5}P^{3r}=\theta^{5}\,(u/\theta)^{5}P^{3r}\le\theta^{5}n\le\theta\,n.\tag{*}
\]
By (2), \(N\cdot N\mathsf{L}\ge4\cdot27\ge\tfrac32\) and \(u\ge1\). Hence, with (4),
\[
c_0P^{2r}\le\tfrac32k^{2}\mathsf{L}\,P^{2r}\le N(N\mathsf{L})k^{2}\mathsf{L}\,P^{2r}=u^{2}P^{2r}\le u^{5}P^{3r}\le\theta n\le n .
\]
Dividing by \(P^{2r}\) and multiplying by \(N\): \(Nc_0\le Nn/P^{2r}\le Nn\bigl(P^{-2r}+r^{2}/(kP)\bigr)=\Delta\).

(6) By (2), \(u\ge27Nk\). Since \(N\ge2\) and \(k\ge2\), \(180\le27^{4}N^{3}k\), so \(180Nk^{3}\le(27Nk)^{4}\le u^{4}\). With \(c^{*}=3kc\) and (4),
\[
8Nkc^{*}P^{2r}=24Nk^{2}c\,P^{2r}\le24Nk^{2}\cdot\tfrac{15}2ku\cdot P^{2r}=180Nk^{3}u\,P^{2r}\le u^{5}P^{3r}\le\theta n
\]
by \((*)\). \(\square\)

## References

1. Lean: `New.FrobeniusCycle.IsLargeDegree.two_le_rank`, `New.FrobeniusCycle.IsLargeDegree.four_le_mul`, `New.FrobeniusCycle.IsLargeDegree.mul_pow_le_degree`, `New.FrobeniusCycle.IsLargeDegree.twenty_seven_le_log_q`, `New.FrobeniusCycle.IsLargeDegree.mul_degree_add_lt_P_pow`, `New.FrobeniusCycle.IsLargeDegree.one_lt_degree`, `New.FrobeniusCycle.IsLargeDegree.degree_lt_q`, `New.FrobeniusCycle.IsLargeDegree.mul_log_pow_mul_le`, `New.FrobeniusCycle.IsLargeDegree.multinomialExponent_mul_le_degree`, `New.FrobeniusCycle.IsLargeDegree.mul_multinomialExponent_le_divisorConstant`, `New.FrobeniusCycle.IsLargeDegree.mul_defectThreshold_le_mul_degree`, `New.FrobeniusCycle.multinomialExponent_le_mul_log`, `New.FrobeniusCycle.congruencePrecision_le_mul_log`, `New.FrobeniusCycle.two_le_mul_multinomialExponent` in `src/New/UpperBound/ElementaryDivisors/ElementaryDivisorTheorem.lean`.
