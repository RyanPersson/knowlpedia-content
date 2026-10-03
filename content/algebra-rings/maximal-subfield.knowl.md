+++
id = "algebra-rings/maximal-subfield"
title = "Maximal subfield of an algebra"
kind = "definition"
summary = "A field subalgebra containing the scalar field and contained in no larger field subalgebra."
aliases = ["maximal subfield", "maximal field subalgebra"]
domains = ["algebra-rings"]
section_mode = "progressive"
prerequisites = ["algebra-modules/algebra-over-ring", "algebra-fields-galois/field-extension"]
dependency_heuristic = "semantic-transcript-review-v1"
dependency_review_count = 1
+++

Let \(A\) be an associative unital [[algebra-modules/algebra-over-ring|algebra]] over a field \(F\). A **maximal subfield** of \(A\) is a [[algebra-fields-galois/field-extension|field extension]] \(L/F\) realized as a subalgebra \(L\subseteq A\) with the same identity, such that \(L\) is not properly contained in another field subalgebra of \(A\) containing \(F1_A\).

Maximality is by inclusion among field subalgebras. It does not mean that \(L\) is algebraically closed or is a maximal proper subring of \(A\).

## Quaternion division algebras

In a quaternion division algebra over a field of characteristic different from two, each nonscalar element \(x\) generates a quadratic field \(F[x]\), and these are exactly the maximal subfields. The reduced characteristic polynomial has degree two, and division excludes a product decomposition or a nonzero nilpotent.

For the rational Hamilton algebra, \(\mathbb Q(i)\) and \(\mathbb Q(i+j+k)\cong\mathbb Q(\sqrt{-3})\) are examples. The latter follows from \((i+j+k)^2=-3\).

## Split warning

A nonscalar element of \(M_2(F)\) need not generate a field. For example \(\operatorname{diag}(0,1)\) generates a subalgebra isomorphic to \(F\times F\). The division hypothesis in the preceding characterization is essential.

## References

1. John Voight, *Quaternion Algebras*, [author's text](https://jvoight.github.io/quat-book.pdf), Corollary 4.4.5 and Proposition 7.7.8, quadratic subfields and centralizers.
2. The rational examples follow by direct quaternion multiplication; the split example follows by polynomial evaluation at \(0\) and \(1\).
