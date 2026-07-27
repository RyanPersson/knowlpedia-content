+++
id = "langlands-letter/knowls/euler-product-and-local-factor"
title = "Euler Product and Determinant Local \\(L\\)-Factor"
kind = "knowl"
summary = "An L-function expressed as a product of determinant local factors at unramified primes."
aliases = ["euler-product-and-local-factor", "Euler Product and Determinant Local \\(L\\)-Factor"]
domains = ["langlands-letter"]
legacy_source_path = "langlands-letter/knowls/euler-product-and-local-factor.md"
+++

An **Euler product** is a product over primes or places of local factors, typically convergent in a right half-plane \(\operatorname{Re}(s)\gg0\).

Given a representation \(\pi\) of the [[langlands-letter/knowls/l-group-satake-parameter|\(L\)-group]] and an unramified Satake parameter \(\alpha_p\), the local factor is
\[
L_p(s)=\det\!\bigl(1-\pi(\alpha_p)\,p^{-s}\bigr)^{-1}.
\]

The global \(L\)-function is \(L(s)=\prod_p L_p(s)\), with the factors at finitely many ramified primes specified separately or omitted.

## Remarks

Changing auxiliary choices typically affects only finitely many local factors.
