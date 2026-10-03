+++
id = "algebra-rings/definite-quaternion-algebra"
title = "Definite quaternion algebra"
kind = "definition"
summary = "A quaternion algebra over a totally real number field that ramifies at every real place."
aliases = ["definite quaternion algebra", "totally definite quaternion algebra", "indefinite quaternion algebra"]
domains = ["algebra-rings"]
section_mode = "progressive"
prerequisites = ["algebra-rings/quaternion-real-place-ramification", "algebra-fields-galois/number-field"]
dependency_heuristic = "semantic-transcript-review-v1"
dependency_review_count = 1
+++

Let \(K\) be a totally real [[algebra-fields-galois/number-field|number field]], meaning that every embedding \(K\hookrightarrow\mathbb C\) lands in \(\mathbb R\). A [[algebra-rings/quaternion-algebra|quaternion algebra]] \(B/K\) is **totally definite** if it is [[algebra-rings/quaternion-real-place-ramification|ramified at every real place]]. It is **indefinite** if it splits at at least one real place.

Over \(\mathbb Q\), there is one real place: “definite” means \(B\otimes_{\mathbb Q}\mathbb R\cong\mathbb H\), and “indefinite” means \(B\otimes_{\mathbb Q}\mathbb R\cong M_2(\mathbb R)\).

## Norm interpretation

In the definite rational case, the reduced norm on the real scalar extension is a positive-definite [[linear-algebra/quadratic-form|quadratic form]]. The [[catalog/arithmetic/rational-hamilton-quaternions|rational Hamilton algebra]] is the basic example. In the split real algebra, determinant is not positive definite.

## Scope of the convention

The definition above fixes a totally real base. Having no real places, as for an [[algebra-fields-galois/imaginary-quadratic-field|imaginary quadratic field]], does not make an algebra totally definite by a vacuous condition: complex places are split. Equivalently, a totally definite quaternion algebra over an arbitrary number field must ramify at all archimedean places, which forces the field to be totally real.

## References

1. John Voight, *Quaternion Algebras*, [author's text](https://jvoight.github.io/quat-book.pdf), Definition 14.5.7 and §14.5.8.
