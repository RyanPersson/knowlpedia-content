+++
id = "langlands-letter/knowls/adeles-restricted-product"
title = "Adeles and Restricted Products"
kind = "definition"
summary = "The restricted product of all completions of a number field, with its restricted-product topology."
aliases = ["adeles-restricted-product", "Adeles and Restricted Products"]
domains = ["langlands-letter"]
legacy_source_path = "langlands-letter/knowls/adeles-restricted-product.md"
+++

Let \(F\) be a number field. For each finite place \(v\), let \(F_v\) be its completion and \(\mathcal O_v\subset F_v\) its ring of integers. The **finite adele ring** is the restricted product
\[
\mathbb A_{F,f}
=
\prod_{v\nmid\infty}'F_v
=
\left\{(x_v)_v:x_v\in\mathcal O_v
\text{ for all but finitely many }v\right\}.
\]
Addition and multiplication are defined componentwise.

Writing
\[
F_\infty:=\prod_{v\mid\infty}F_v,
\]
the **adele ring** of \(F\) is
\[
\mathbb A_F=F_\infty\times\mathbb A_{F,f}.
\]

## Restricted-product topology

A basic open set in \(\mathbb A_{F,f}\) is a product
\[
\prod_{v\nmid\infty}U_v,
\]
where each \(U_v\subseteq F_v\) is open and \(U_v=\mathcal O_v\) for all but finitely many \(v\). This topology makes \(\mathbb A_F\) a locally compact topological ring.

## Diagonal embedding

The diagonal map \(F\hookrightarrow\mathbb A_F\) has discrete image, and the quotient \(\mathbb A_F/F\) is compact. These two properties combine the local completions into a global locally compact object.

For an algebraic group \(G\), automorphic forms live on
\[
G(F)\backslash G(\mathbb A_F);
\]
see [[langlands-letter/knowls/automorphic-form-hecke-eigen|automorphic forms and Hecke eigenvalues]].
