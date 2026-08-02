+++
id = "langlands-letter/knowls/langlands-functoriality-l-homomorphism"
title = "Langlands Functoriality and \\(L\\)-Homomorphisms"
kind = "knowl"
summary = "An L-group homomorphism that predicts transfer of automorphic representations and their local parameters."
aliases = ["langlands-functoriality-l-homomorphism", "Langlands Functoriality and \\(L\\)-Homomorphisms"]
domains = ["langlands-letter"]
legacy_source_path = "langlands-letter/knowls/langlands-functoriality-l-homomorphism.md"
+++

Let \(G'\) and \(G\) be connected reductive groups over a local or global field \(F\), with \(L\)-groups
\[
{}^LG'=\widehat G'\rtimes W_F,
\qquad
{}^LG=\widehat G\rtimes W_F.
\]
An **\(L\)-homomorphism**
\[
\omega:{}^LG'\longrightarrow{}^LG
\]
is a continuous group homomorphism that commutes with the projections to the Weil group \(W_F\) and whose restriction
\[
\widehat G'\longrightarrow\widehat G
\]
is a homomorphism of complex algebraic groups. It is normally considered up to conjugation by \(\widehat G\).

## Functorial transfer

Langlands functoriality predicts that \(\omega\) transfers suitable automorphic representations
\[
\Pi'\ \text{of }G'(\mathbb A_F)
\quad\longmapsto\quad
\Pi\ \text{of }G(\mathbb A_F).
\]
At every place \(v\) where both representations and groups are unramified, their Satake parameters should satisfy
\[
\alpha_v(\Pi)\sim\omega\!\left(\alpha_v(\Pi')\right)
\]
as semisimple conjugacy classes in \({}^LG\). This is a conjectural transfer statement, not merely the application of \(\omega\) to a single automorphic function.

## Compatibility with L-functions

If \(r:{}^LG\to\mathrm{GL}(V)\) is a finite-dimensional complex representation, the unramified local factors are predicted to obey
\[
L_v(s,\Pi,r)
=
L_v(s,\Pi',r\circ\omega).
\]

## Role in the letter

This is the letter's “second question,” expressed as the transfer of automorphic data whose unramified parameters are pushed forward by \(\omega\).
