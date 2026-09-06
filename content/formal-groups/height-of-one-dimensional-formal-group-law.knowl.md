+++
id = "formal-groups/height-of-one-dimensional-formal-group-law"
title = "Height of a one-dimensional formal group law"
kind = "definition"
summary = "The exponent of the first nonzero term of the p-series of a one-dimensional commutative formal group law in characteristic p."
aliases = ["height of a formal group law", "formal group height"]
domains = ["formal-groups"]
prerequisites = ["formal-groups/one-dimensional-formal-group-law"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(F\) be a one-dimensional commutative
[[formal-groups/one-dimensional-formal-group-law|formal group law]] over a
field \(k\) of characteristic \(p>0\). Its **height** is defined from the
\(p\)-series \([p]_F(X)\). If \([p]_F(X)=0\), then
\[
\operatorname{ht}(F)=\infty.
\]
Otherwise there is a unique integer \(h\geq1\) such that
\[
[p]_F(X)=aX^{p^h}+\text{terms of higher degree},
\qquad a\in k^\times,
\]
and \(\operatorname{ht}(F)=h\).

## Invariance

A formal-group-law isomorphism \(f:F\to G\) intertwines the \(p\)-series:
\[
f([p]_F(X))=[p]_G(f(X)).
\]
Because \(f\) has an invertible linear coefficient, the first nonzero
exponent is unchanged. Height is therefore an isomorphism invariant and is
preserved by [[algebra-fields-galois/field-extension|field extension]].

## Standard examples

For the additive and multiplicative laws,
\[
[p]_{F_a}(X)=0,
\qquad
[p]_{F_m}(X)=X^p.
\]
Thus \(F_a\) has height \(\infty\) and \(F_m\) has height \(1\). Their tangent
Lie algebras are nevertheless isomorphic, giving the basic
[[formal-groups/positive-characteristic-warning|failure of tangent
classification in positive characteristic]].

## References

1. Michiel Hazewinkel, *Formal Groups and Applications*, AMS Chelsea Publishing, 2012. [AMS book record](https://bookstore.ams.org/chel-375-h). Relevant: Chapters 3–5.
2. J. F. Adams, *Stable Homotopy and Generalised Homology*, University of Chicago Press, 1974. Relevant: Part II.
