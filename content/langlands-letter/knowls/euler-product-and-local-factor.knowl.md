+++
id = "langlands-letter/knowls/euler-product-and-local-factor"
title = "Euler Product and Determinant Local \\(L\\)-Factor"
kind = "definition"
summary = "The determinant local L-factor attached to a Satake parameter and its Euler product over unramified places."
aliases = ["euler-product-and-local-factor", "Euler Product and Determinant Local \\(L\\)-Factor"]
domains = ["langlands-letter"]
legacy_source_path = "langlands-letter/knowls/euler-product-and-local-factor.md"
+++

Let \(F_v\) be a nonarchimedean local field with residue-field cardinality \(q_v\). Let \(\Pi_v\) be an unramified representation with [[langlands-letter/knowls/l-group-satake-parameter|Satake parameter]] \(\alpha_v\), and let
\[
r:{}^LG\longrightarrow\mathrm{GL}(V_r)
\]
be a finite-dimensional complex representation. The **unramified local \(L\)-factor** is
\[
L_v(s,\Pi_v,r)
=
\det\!\left(1-r(\alpha_v)q_v^{-s}\mid V_r\right)^{-1}.
\]
It depends only on the conjugacy class of \(\alpha_v\).

## Euler product

For a global automorphic representation \(\Pi=\bigotimes'_v\Pi_v\), choose a finite set \(S\) containing the archimedean and ramified places. The associated **incomplete Euler product** is
\[
L^S(s,\Pi,r)
=
\prod_{v\notin S}L_v(s,\Pi_v,r).
\]
When convergence is known, this product converges in a right half-plane. A completed \(L\)-function also includes the archimedean and ramified local factors.

## Ramified local factors

If the local Langlands parameter at \(v\) yields a Weil–Deligne representation \((\rho_v,N_v)\) on \(V_r\), the standard ramified factor is
\[
L_v(s,\Pi_v,r)
=
\det\!\left(
1-q_v^{-s}\rho_v(\operatorname{Fr}_v)
\;\middle|\;
(\ker N_v)^{I_v}
\right)^{-1},
\]
with the inverse Frobenius convention adjusted if arithmetic rather than geometric Frobenius is used.

The unramified formula is the special case in which inertia acts trivially and \(N_v=0\).
