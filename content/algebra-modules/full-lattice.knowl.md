+++
id = "algebra-modules/full-lattice"
title = "Full lattice over an integral domain"
kind = "definition"
summary = "A finitely generated submodule spanning a finite-dimensional vector space over the fraction field."
aliases = ["full lattice", "R-lattice", "full Z-lattice"]
domains = ["algebra-modules"]
section_mode = "progressive"
prerequisites = ["algebra-rings/fraction-field", "algebra-modules/finitely-generated-module", "algebra-modules/submodule", "linear-algebra/vector-space"]
dependency_heuristic = "semantic-transcript-review-v1"
dependency_review_count = 1
+++

Let \(R\) be an integral domain with [[algebra-rings/fraction-field|fraction field]] \(K\), and let \(V\) be a finite-dimensional \(K\)-[[linear-algebra/vector-space|vector space]]. A **full \(R\)-lattice** in \(V\) is an \(R\)-[[algebra-modules/submodule|submodule]] \(L\subseteq V\) that is [[algebra-modules/finitely-generated-module|finitely generated]] and satisfies \(KL=V\).

Equivalently, the scalar-extension map \(K\otimes_R L\to V\), \(a\otimes\ell\mapsto a\ell\), is an isomorphism.

## Integral coordinates

For \(R=\mathbb Z\) and \(K=\mathbb Q\), a full lattice is free of rank \(\dim_{\mathbb Q}V\). For example, \(\mathbb Z e_1\oplus\tfrac12\mathbb Z e_2\) is a full lattice in \(\mathbb Q^2\).

Over a general [[algebra-commutative/dedekind-domain|Dedekind domain]], a full lattice is finitely generated and projective, but need not be free. An integral basis is therefore not part of the definition.

## Related meanings

An [[algebra-rings/order-in-algebra|order in an algebra]] is a full lattice also closed under multiplication and containing the identity. A [[algebra-modules/lie-order|Lie order]] is closed under the Lie bracket instead.

An [[linear-algebra/euclidean-lattice|Euclidean lattice]] additionally lives in a real inner-product space; no topology or inner product is required here. This is unrelated to an order-theoretic [[shared-foundations/lattice|lattice]].

## References

1. John Voight, *Quaternion Algebras*, [author's text](https://jvoight.github.io/quat-book.pdf), Definition 9.3.1, Remark 9.3.4, and Theorem 9.3.6.
