+++
id = "nonassociative-algebra/jordan-subalgebra"
title = "Jordan subalgebra"
kind = "definition"
summary = "A linear subspace closed under the Jordan product, with unit preservation stated separately."
aliases = ["Jordan subalgebra", "Jordan-subalgebra"]
domains = ["nonassociative-algebra"]
section_mode = "progressive"
prerequisites = ["nonassociative-algebra/jordan-algebra", "convex-analysis/linear-subspace"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

A **Jordan subalgebra** of a [[nonassociative-algebra/jordan-algebra|Jordan
algebra]] \(J\) over \(k\) is a [[convex-analysis/linear-subspace|linear subspace]] \(B\subseteq J\) such that
\[
x,y\in B\quad\Longrightarrow\quad x\circ y\in B.
\]
With the restricted product, \(B\) is itself a Jordan algebra.

## The unit convention

If \(J\) is unital, closure under \(\circ\) does **not** require \(B\) to
contain the ambient unit \(e_J\). A subalgebra can have no unit, or can have a
unit \(e_B\) different from \(e_J\). Authors who require subalgebras of unital
Jordan algebras to contain \(e_J\) are using the stronger phrase **unital
Jordan subalgebra**.

For example, the upper-left \(2\times2\) Hermitian corner inside
\(\mathfrak h_3(\mathbb O)\) is closed under the Jordan product. Its unit is
\(\operatorname{diag}(1,1,0)\), not the ambient unit
\(\operatorname{diag}(1,1,1)\). This is the convention relevant to matrix
corner inclusions
\[
\mathfrak h_2(\mathbb C)\subset
\mathfrak h_3(\mathbb C)\subset
\mathfrak h_3(\mathbb O).
\]

## Embeddings

An injective
[[nonassociative-algebra/jordan-algebra-homomorphism|Jordan algebra
homomorphism]] identifies its source with a Jordan subalgebra of its target.
For unital algebras, the embedding is **unital** precisely when it sends the
source unit to the target unit. Thus “embedding” alone should not be read as
“unital embedding.”

## Stabilizers of subalgebras

If a group \(G\) acts by Jordan automorphisms on \(J\), the setwise stabilizer
of \(B\) is
\[
\operatorname{Stab}_G(B)=\{g\in G:g(B)=B\}.
\]
This is different from the pointwise stabilizer, whose elements fix every
element of \(B\). In the [[nonassociative-algebra/exceptional-jordan-algebra|exceptional Jordan algebra]], stabilizers of selected
complex and octonionic matrix subalgebras recover important [[lie-groups/compact-lie-group|compact Lie groups]].

## References

1. Tonny A. Springer and Ferdinand D. Veldkamp, *Octonions, Jordan Algebras and Exceptional Groups*, Springer, 2000. [Publisher record](https://link.springer.com/book/10.1007/978-3-662-12622-6).
2. John C. Baez and Paul Schwahn, “The Standard Model Gauge Group from the Exceptional Jordan Algebra,” 2026. [arXiv:2606.15235](https://arxiv.org/abs/2606.15235).
