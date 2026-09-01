+++
id = "algebra-commutative/integral-closure"
title = "Integral closure"
kind = "knowl"
summary = "The subring of an overring consisting of all elements integral over a given ring."
aliases = ["integral-closure", "Integral closure"]
domains = ["algebra-commutative"]
prerequisites = ["algebra-rings/commutative-ring", "algebra-commutative/integral-element", "algebra-commutative/integrally-closed-domain"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
legacy_source_path = "algebra-commutative/integral-closure.md"
+++

Let \(R\) be a [[algebra-rings/commutative-ring|commutative ring]], and let \(A\) be a commutative \(R\)-algebra.

An element \(a\in A\) is [[algebra-commutative/integral-element|integral]] over \(R\) if it satisfies a monic polynomial equation
\[
a^n + r_{n-1}a^{n-1}+\cdots + r_1 a + r_0 = 0 \quad \text{with } r_i\in R.
\]

The **integral closure of \(R\) in \(A\)** is
\[
\overline{R}^{\,A} \;=\; \{\, a\in A : a \text{ is integral over } R \,\}.
\]
It is a subring of \(A\) containing the image of \(R\).

When \(R\) is a domain with fraction field \(K\), the integral closure of \(R\) **in \(K\)** is often called the *normalization* of \(R\). The domain \(R\) is [[algebra-commutative/integrally-closed-domain|integrally closed]] precisely when its integral closure in its fraction field equals \(R\).

## Properties
- If \(R\subseteq A\) is an [[algebra-commutative/integral-extension|integral extension]], then every element of \(A\) is integral over \(R\), hence \(\overline{R}^{\,A}=A\).
- If \(B\subseteq A\) is any subring containing \(R\) and consisting of elements integral over \(R\), then \(B\subseteq \overline{R}^{\,A}\) (maximality of the integral closure).

## Examples
1. **Integers inside rationals.**
   Take \(R=\mathbb{Z}\) and \(A=\mathbb{Q}\). If \(a/b\in \mathbb{Q}\) (in lowest terms) is integral over \(\mathbb{Z}\), then it satisfies a monic polynomial with integer coefficients, forcing \(b=\pm 1\). Hence \(\overline{\mathbb{Z}}^{\,\mathbb{Q}}=\mathbb{Z}\).

2. **A non-normal affine subring.**
   Let \(k\) be a [[algebra-rings/field|field]] and consider \(R=k[x^2,x^3]\subseteq A=k(x)\) (the rational function field in \(x\)). The element \(x\in k(x)\) satisfies the monic equation \(T^2-x^2=0\) with \(x^2\in R\), so \(x\) is integral over \(R\). Thus the integral closure contains \(k[x]\). In fact one checks \(\overline{R}^{\,k(x)}=k[x]\).

3. **Localization.**
   If \(R\) is a domain, \(S\subseteq R\) is a [[algebra-commutative/multiplicative-set|multiplicative set]] of nonzero elements, and \(\overline R\) is the integral closure of \(R\) in its fraction field, then the integral closure of \(S^{-1}R\) in that field is \(S^{-1}\overline R\). Thus integral closure commutes with [[algebra-commutative/localization-ring|localization]].
