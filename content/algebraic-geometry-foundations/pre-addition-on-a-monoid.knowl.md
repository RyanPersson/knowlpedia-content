+++
id = "algebraic-geometry-foundations/pre-addition-on-a-monoid"
title = "Pre-addition on a monoid"
kind = "definition"
summary = "An additive and multiplicative equivalence relation on formal sums of elements of a monoid with zero."
aliases = ["pre-addition of a blueprint", "blueprint pre-addition"]
domains = ["algebraic-geometry-foundations", "algebra-rings"]
prerequisites = ["algebra-groups/commutative-monoid", "shared-foundations/equivalence-relation"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(A\) be a [[algebra-groups/commutative-monoid|commutative monoid with zero]], and let \(\mathbb N[A]\) denote the semiring of finite formal sums of elements of \(A\). A **pre-addition** on \(A\) is an [[shared-foundations/equivalence-relation|equivalence relation]] \(\mathcal R\) on \(\mathbb N[A]\), written
\[
\sum a_i\equiv\sum b_j,
\]
with the following properties:

1. relations may be added and multiplied termwise;
2. the empty sum is equivalent to the one-term sum \(0\);
3. if the one-term sums \(a\) and \(b\) are equivalent, then \(a=b\) in \(A\).

Explicitly, if \(\sum a_i\equiv\sum b_j\) and \(\sum c_k\equiv\sum d_\ell\), then
\[
\sum a_i+\sum c_k\equiv\sum b_j+\sum d_\ell
\]
and
\[
\sum_{i,k}a_ic_k\equiv\sum_{j,\ell}b_jd_\ell.
\]
The third condition says that the pre-addition is **proper**: it does not identify distinct elements of the underlying monoid.

## Role in a blueprint

A [[algebraic-geometry-foundations/blueprint|blueprint]] \(A/\!/\mathcal R\) records the multiplication of \(A\) together with the additive relations in \(\mathcal R\). Quotienting all formal sums by \(\mathcal R\) produces its [[algebraic-geometry-foundations/semiring-completion-of-a-blueprint|semiring completion]].

## References
Oliver Lorscheid, [*The geometry of blueprints, Part I: Algebraic background and scheme theory*, §1.1](https://arxiv.org/abs/1103.1745).
