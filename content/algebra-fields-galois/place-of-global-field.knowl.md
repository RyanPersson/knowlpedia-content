+++
id = "algebra-fields-galois/place-of-global-field"
title = "Place of a global field"
kind = "definition"
summary = "An equivalence class of nontrivial absolute values on a global field."
aliases = ["place", "places", "place of a number field", "place of a function field"]
domains = ["algebra-fields-galois", "langlands"]
prerequisites = ["langlands-letter/knowls/global-local-fields-completions"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(F\) be a
[[langlands-letter/knowls/global-local-fields-completions|global field]]. A
**place of \(F\)** is an equivalence class of nontrivial absolute values on
\(F\), where two absolute values are equivalent when they induce the same
topology on \(F\).

Choosing a representative \(|\cdot|_v\) gives a metric and hence the
[[algebra-fields-galois/completion-at-place|completion]] \(F_v\); equivalent
representatives give canonically isomorphic topological fields.

## Archimedean and nonarchimedean places

The archimedean places occur only for
[[algebra-fields-galois/number-field|number fields]] and come from real or
complex embeddings. Every other place is represented by a
[[algebra-fields-galois/non-archimedean-absolute-value|nonarchimedean absolute
value]], equivalently by a discrete valuation after normalization.

For a [[algebra-fields-galois/global-function-field|global function field]],
the places correspond to closed points of its smooth projective curve.

## Normalization

An equivalence class does not choose a numerical scale. In global arithmetic
one normally selects representatives satisfying the product formula. Local
formulas involving \(q_v\), Frobenius, or Haar measure therefore state their
normalization separately.

## References

1. Jürgen Neukirch, *Algebraic Number Theory*, Springer, 1999, Chapter II,
   §§4--5.
2. André Weil, *Basic Number Theory*, third edition, Springer, 1974,
   Chapter I.
