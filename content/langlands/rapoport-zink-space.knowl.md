+++
id = "langlands/rapoport-zink-space"
title = "Rapoport–Zink space"
kind = "definition"
summary = "A formal moduli space of p-divisible groups quasi-isogenous to a fixed framing object, often with additional structure."
aliases = ["Rapoport-Zink space", "Rapoport–Zink formal scheme", "RZ space"]
domains = ["langlands", "algebraic-geometry-foundations", "number-theory"]
prerequisites = ["algebra-fields-galois/perfect-field", "algebraic-geometry-foundations/formal-scheme"]
dependency_review_count = 1
section_mode = "progressive"
+++

Fix a [[algebra-fields-galois/perfect-field|perfect field]] \(k\) of
characteristic \(p\) and a \(p\)-divisible group \(\mathbb X\) over \(k\).
Here a \(p\)-divisible group is a compatible system of finite flat group
schemes \(X[p^n]\) of order \(p^{nh}\), with
\(X[p^n]=X[p^{n+1}][p^n]\). In its basic form, the **Rapoport–Zink functor**
assigns to a \(p\)-adically nilpotent test
[[algebraic-geometry-foundations/formal-scheme|formal scheme]] \(S\) the pairs
\((X,\rho)\), where \(X\) is a \(p\)-divisible group over \(S\) and

\[
\rho:\mathbb X_{\bar S}\dashrightarrow X_{\bar S}
\]

is a quasi-isogeny over the special fiber.  Under the standard hypotheses this
functor is represented by a formal scheme, a **Rapoport–Zink space**.

EL and PEL versions impose endomorphisms, polarizations, and determinant
conditions.  More general group-theoretic versions are described by local
Shimura data.

## Generic fiber and level tower

The [[algebraic-geometry-foundations/adic-space|adic generic fiber]] is a
rigid-analytic space. Adding level structure on
the rational Tate module produces a tower with actions by a
[[langlands-letter/knowls/p-adic-field|\(p\)-adic]]
[[algebraic-geometry-foundations/reductive-algebraic-group|reductive group]]
and by the group of self-quasi-isogenies of \(\mathbb X\).
At infinite level many such towers become
[[algebraic-geometry-foundations/perfectoid-space|perfectoid]].

## Examples

The Lubin–Tate deformation space of a one-dimensional
[[formal-groups/formal-group|formal group]] is the
basic EL example.  Drinfeld's formal half-space gives a closely related tower.
These spaces are primary examples of
[[langlands/local-shimura-variety|local Shimura varieties]].

## References

1. Michael Rapoport and Thomas Zink, *Period Spaces for \(p\)-divisible
   Groups*, Annals of Mathematics Studies 141, Princeton University Press,
   1996.
2. Peter Scholze and Jared Weinstein, “Moduli of \(p\)-divisible groups,”
   *Cambridge Journal of Mathematics* 1 (2013), 145–237.
   [arXiv](https://arxiv.org/abs/1211.6357).
