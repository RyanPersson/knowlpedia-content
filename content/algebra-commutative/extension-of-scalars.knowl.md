+++
id = "algebra-commutative/extension-of-scalars"
title = "Extension of scalars"
kind = "knowl"
summary = "Given a ring map R→S, the S-module S⊗_R M obtained from an R-module M by base change."
aliases = ["extension-of-scalars", "Extension of scalars"]
domains = ["algebra-commutative"]
prerequisites = ["algebra-rings/commutative-ring"]
dependency_review_count = 1
legacy_source_path = "algebra-commutative/extension-of-scalars.md"
+++

Let \(f:R\to S\) be a homomorphism of [[algebra-rings/commutative-ring|commutative rings]], and let \(M\) be an \(R\)-module. The **extension of scalars** (or **base change**) of \(M\) along \(f\) is the \(S\)-module
\[
S\otimes_R M,
\]
where \(S\) acts on the left tensor factor by
\[
s\cdot(s'\otimes m)=(ss')\otimes m.
\]

There is a canonical \(R\)-linear map
\[
\eta_M: M \longrightarrow S\otimes_R M,\qquad m\longmapsto 1\otimes m,
\]
where \(S\otimes_R M\) is viewed as an \(R\)-module via \(f\).

## Universal property

For every \(S\)-module \(N\), extension of scalars is left adjoint to [[algebra-commutative/restriction-of-scalars|restriction of scalars]]: there is a natural bijection
\[
\mathrm{Hom}_S(S\otimes_R M,\;N)\ \cong\ \mathrm{Hom}_R(M,\;\mathrm{Res}_f N),
\]
where \(\mathrm{Res}_f N\) denotes \(N\) viewed as an \(R\)-module via \(f\).

If \(U\subseteq R\) is a [[algebra-commutative/multiplicative-set|multiplicative set]], extension of scalars along \(R\to U^{-1}R\) recovers [[algebra-commutative/localization-module|localization of modules]]:
\[
(U^{-1}R)\otimes_R M \cong U^{-1}M.
\]

## Examples

1. **Quotient base change.** Let \(S=R/I\) and let \(f:R\to R/I\) be the quotient map. Then
   \[
   (R/I)\otimes_R M \cong M/IM.
   \]
   In particular, \((\mathbb Z/n\mathbb Z)\otimes_{\mathbb Z} M \cong M/nM\).

2. **Field extension.** If \(k\subseteq K\) is a field extension and \(V\) is a \(k\)-vector space, then \(K\otimes_k V\) is the corresponding \(K\)-vector space. If \(V\cong k^d\), then \(K\otimes_k V\cong K^d\).

3. **Localization.** Let \(R=k[x]\), let \(U=\{1,x,x^2,\dots\}\), and set \(R'=U^{-1}R\cong k[x,x^{-1}]\). For \(M=R/(x)\),
   \[
   R'\otimes_R M \cong U^{-1}M = 0,
   \]
   since \(x\) becomes invertible after localization but annihilates \(M\).
