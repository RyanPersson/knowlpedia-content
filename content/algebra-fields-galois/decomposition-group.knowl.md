+++
id = "algebra-fields-galois/decomposition-group"
title = "Decomposition group"
kind = "definition"
summary = "The subgroup of a Galois group that stabilizes a chosen prime above a prime of the base field."
aliases = ["decomposition subgroup", "decomposition group at a place", "D_w"]
domains = ["algebra-fields-galois", "langlands"]
prerequisites = ["langlands-letter/knowls/galois-extension-and-group", "langlands-letter/knowls/global-local-fields-completions", "algebra-fields-galois/completion-at-place", "algebra-commutative/residue-field", "algebra-fields-galois/inertia-subgroup"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(L/K\) be a finite [[langlands-letter/knowls/galois-extension-and-group|Galois extension]] of
[[langlands-letter/knowls/global-local-fields-completions|global fields]],
let \(v\) be a nonarchimedean place of \(K\), and choose a place
\(w\) of \(L\) above \(v\).  The **decomposition group at \(w\)** is the
stabilizer

\[
D_w=\{\sigma\in\operatorname{Gal}(L/K):\sigma w=w\}.
\]

Restriction to the
[[algebra-fields-galois/completion-at-place|completion]]
identifies \(D_w\simeq\operatorname{Gal}(L_w/K_v)\). Its action on
[[algebra-commutative/residue-field|residue fields]] gives a
surjection

\[
D_w\longrightarrow\operatorname{Gal}(k_w/k_v)
\]

whose kernel is the [[algebra-fields-galois/inertia-subgroup|inertia subgroup]]
\(I_w\).

## Dependence on the chosen place

The [[algebra-fields-galois/galois-group|Galois group]] acts transitively on
the places above \(v\). Replacing \(w\)
by \(\tau w\) replaces \(D_w\) by the conjugate \(\tau D_w\tau^{-1}\).
Consequently the decomposition group attached to \(v\) is canonical only up
to conjugacy.

For a separable closure \(\overline K/K\) and an extension \(\overline v\) of
\(v\), the same stabilizer construction gives an absolute decomposition group
\(D_{\overline v}\subset\operatorname{Gal}(\overline K/K)\), canonically
isomorphic to the [[langlands-letter/knowls/galois-extension-and-group|absolute
Galois group]] of \(K_v\) after the choice of \(\overline v\).

## References

1. The Stacks Project Authors, “Fundamental Groups of Schemes,” §58.13,
   “Ramification theory.” [Stacks Project](https://stacks.math.columbia.edu/tag/0BSD).
2. Jean-Pierre Serre, *Local Fields*, Graduate Texts in Mathematics 67,
   Springer, 1979, Chapter I, §7.
