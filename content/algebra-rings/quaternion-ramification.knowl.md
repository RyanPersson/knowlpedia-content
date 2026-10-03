+++
id = "algebra-rings/quaternion-ramification"
title = "Ramification of a quaternion algebra at a place"
kind = "definition"
summary = "A quaternion algebra is ramified at a place when its completed scalar extension is a division algebra."
aliases = ["quaternion ramification", "ramified place of a quaternion algebra", "ramification set of a quaternion algebra"]
domains = ["algebra-rings"]
section_mode = "progressive"
prerequisites = ["algebra-rings/quaternion-algebra", "algebra-fields-galois/place-of-global-field", "algebra-fields-galois/completion-at-place", "algebra-modules/tensor-product-algebras", "algebra-rings/division-ring"]
dependency_heuristic = "semantic-transcript-review-v1"
dependency_review_count = 1
+++

Let \(B\) be a [[algebra-rings/quaternion-algebra|quaternion algebra]] over a [[algebra-fields-galois/number-field|number field]] \(K\), and let \(v\) be a [[algebra-fields-galois/place-of-global-field|place]] of \(K\), with [[algebra-fields-galois/completion-at-place|completion]] \(K_v\). The algebra is **ramified at \(v\)** if
\[
B_v=B\otimes_K K_v
\]
is a division algebra. It is **split at \(v\)** if \(B_v\cong M_2(K_v)\). These are the only two possibilities, and \(\operatorname{Ram}(B)\) denotes the set of ramified places.

## Finite and infinite places

At a real place, ramification means \(B_v\cong\mathbb H\), as in [[algebra-rings/quaternion-real-place-ramification|real-place ramification]]. A complex place is always split. At a finite place, the definition concerns the quaternion algebra over the corresponding [[algebra-fields-galois/nonarchimedean-local-field|nonarchimedean local field]].

For a number field, \(\operatorname{Ram}(B)\) is finite, has even cardinality, and determines \(B\) up to \(K\)-algebra isomorphism.

## Rational Hamilton example

For \(B=(-1,-1)_{\mathbb Q}\),
\[
\operatorname{Ram}(B)=\{2,\infty\}.
\]
At odd primes the parameters are units and the local [[algebra-rings/hilbert-symbol|Hilbert symbol]] is \(+1\). At \(2\) and \(\infty\) it is \(-1\). The [[algebra-rings/quaternion-discriminant|algebra discriminant]] records the finite prime \(2\), whereas the full ramification set also records \(\infty\).

## References

1. John Voight, *Quaternion Algebras*, [author's text](https://jvoight.github.io/quat-book.pdf), Definition 14.5.1, Lemma 14.5.3, and Main Theorem 14.6.1; §§12.4.12–12.4.14 for the local calculation.
