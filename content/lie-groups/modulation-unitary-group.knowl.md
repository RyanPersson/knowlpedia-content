+++
id = "lie-groups/modulation-unitary-group"
title = "Modulation as a strongly continuous unitary group"
kind = "example"
summary = "Multiplication by e^{itx} is strongly continuous but stays operator-norm distance two from the identity for t ≠ 0."
aliases = ["modulation representation", "strongly continuous but not norm continuous example"]
domains = ["lie-groups"]
section_mode = "progressive"
prerequisites = ["lie-groups/strongly-continuous-unitary-representation", "functional-analysis/multiplication-operator", "lie-groups/stone-theorem-one-parameter-unitary-groups", "measure-theory/dominated-convergence-theorem"]
+++

On \(H=L^2(\mathbb R,dx)\), define
\[
(M_t f)(x)=e^{itx}f(x),\qquad t\in\mathbb R.
\]
The **modulation group** \((M_t)_{t\in\mathbb R}\) is a [[lie-groups/strongly-continuous-unitary-representation|strongly continuous unitary representation]] of \((\mathbb R,+)\), but it is not operator-norm continuous:
\[
\|M_t-I\|_{\mathrm{op}}=2\qquad(t\ne0).
\]

## Two continuity calculations

For a fixed \(f\in L^2\),
\[
\|(M_t-I)f\|_2^2=\int_{\mathbb R}|e^{itx}-1|^2|f(x)|^2\,dx\longrightarrow0
\]
by [[measure-theory/dominated-convergence-theorem|dominated convergence]], using the integrable bound \(4|f|^2\). By contrast, the norm of a bounded [[functional-analysis/multiplication-operator|multiplication operator]] is the essential supremum of its multiplier. For nonzero \(t\), the values of \(|e^{itx}-1|\) approach \(2\) on sets of positive measure, giving the operator-norm formula.

## Generator and its domain

With the [[lie-groups/stone-theorem-one-parameter-unitary-groups|Stone convention]] \(M_t=e^{itQ}\),
\[
Qf=xf,\qquad\operatorname{Dom}(Q)=\{f\in L^2:xf\in L^2\}.
\]
The norm derivative is \(Kf=ixf\) on this domain. On it, \(|(e^{itx}-1)/t|\leq |x|\) proves convergence of the difference quotient in \(L^2\); conversely an \(L^2\) derivative forces the pointwise candidate \(ixf\) to lie in \(L^2\).

## Finite versus infinite differentiability

The [[lie-groups/ck-vector-unitary-representation|\(C^k\) vectors]] are exactly \(\{f:x^k f\in L^2\}\). For example, \((1+x^2)^{-1}\) is a \(C^1\) vector but not a \(C^2\) vector. The smooth vectors for this one-parameter group have every polynomial weight in \(L^2\); no spatial differentiability is required until translation operators are also included.
