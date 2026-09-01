+++
id = "langlands/artin-conductor"
title = "Artin conductor"
kind = "definition"
summary = "A nonnegative integer measuring the tame and wild ramification of a local Galois or Weil representation."
aliases = ["Artin conductor exponent", "conductor of a Galois representation", "local Artin conductor"]
domains = ["langlands", "algebra-fields-galois", "number-theory"]
prerequisites = ["algebra-fields-galois/nonarchimedean-local-field", "langlands-letter/knowls/galois-extension-and-group", "langlands/weil-group", "algebra-fields-galois/galois-extension", "algebra-fields-galois/inertia-subgroup"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(F\) be a
[[algebra-fields-galois/nonarchimedean-local-field|nonarchimedean local field]], and let \(r\) be a finite-dimensional representation of its
[[langlands-letter/knowls/galois-extension-and-group|absolute Galois group]]
or [[langlands/weil-group|Weil group]] with finite inertia image. Choose a
finite [[algebra-fields-galois/galois-extension|Galois extension]] through which the
[[algebra-fields-galois/inertia-subgroup|inertia action]] factors, and write
\(G_i\) for its lower-numbered ramification groups, with \(G_0\) the inertia
group. The **Artin conductor exponent** is

\[
a(r)=
\sum_{i\geq 0}
\frac{|G_i|}{|G_0|}
\operatorname{codim} V^{G_i}.
\]

This integer is independent of the chosen finite extension. It is zero
exactly when \(r\) is unramified.

## Tame and wild parts

The term for \(i=0\) is
\(\dim V-\dim V^{I_F}\) and measures tame failure of inertia invariance. The
remaining sum is the **Swan conductor**, which measures
[[langlands/wild-ramification|wild ramification]]. Thus

\[
a(r)=\operatorname{codim}V^{I_F}+\operatorname{Swan}(r).
\]

The conductor is additive in
[[algebra-modules/short-exact-sequence|short exact sequences]] and direct
sums.

## Weil–Deligne form

For a [[langlands/weil-deligne-representation|Weil–Deligne representation]]
\((r,N)\), the conductor also detects monodromy:

\[
a(r,N)
=
a(r)+\dim V^{I_F}-\dim(\ker N)^{I_F}.
\]

This is the exponent that appears in the power of \(q_F^{-s}\) in a
[[langlands/local-epsilon-factor|local epsilon factor]]. It also records the
ramification contribution of a local parameter to its
[[langlands-letter/knowls/euler-product-and-local-factor|local
\(L\)-function]].

## Global conductor

For a global representation unramified outside finitely many finite places,
the local exponents assemble into the conductor ideal
\[
\mathfrak f(r)=\prod_v\mathfrak p_v^{a(r_v)}.
\]
The global conductor is therefore arithmetic data assembled from local
ramification, not a separate choice of normalization.

## References

1. Jean-Pierre Serre, *Local Fields*, Graduate Texts in Mathematics 67,
   Springer, 1979, Chapter VI, §2.
   [Springer](https://link.springer.com/book/10.1007/978-1-4757-5673-9).
2. Pierre Deligne, “Les constantes des équations fonctionnelles des
   fonctions \(L\),” in *Modular Functions of One Variable II*, Lecture
   Notes in Mathematics 349, Springer, 1973, 501–597.
   [IAS copy](https://publications.ias.edu/sites/default/files/Number20.pdf).
