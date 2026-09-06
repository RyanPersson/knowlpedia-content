+++
id = "differential-geometry/c-infinity-ring"
title = "C-infinity ring"
kind = "definition"
summary = "An algebraic object carrying an operation for every smooth map between finite-dimensional real affine spaces."
aliases = ["C∞-ring", "C-infty ring"]
domains = ["differential-geometry", "algebra-rings"]
prerequisites = ["linear-algebra/euclidean-space"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

A **\(C^\infty\)-ring** is a set \(A\) equipped, for every smooth map
\[
f:\mathbb R^n\longrightarrow\mathbb R,
\]
with an \(n\)-ary operation
\(\Phi_f:A^n\to A\). These operations satisfy
\[
\Phi_{\pi_i}(a_1,\ldots,a_n)=a_i
\]
for the coordinate projections and
\[
\Phi_{g\circ(f_1,\ldots,f_m)}
=\Phi_g\circ(\Phi_{f_1},\ldots,\Phi_{f_m})
\]
for composites of smooth maps. Nullary operations encode real constants.
Equivalently, a \(C^\infty\)-ring is a product-preserving functor from the
category of [[linear-algebra/euclidean-space|Euclidean spaces]] and smooth maps to sets.

## Underlying ordinary algebra

Applying the definition to \(x+y\), \(xy\), \(-x\), and constant functions
gives \(A\) an underlying commutative unital \(\mathbb R\)-algebra. The
\(C^\infty\)-structure contains more information: it also permits
\(\Phi_{\sin}\), \(\Phi_{\exp}\), and every other smooth functional
calculus. Consequently, an arbitrary homomorphism of the underlying
\(\mathbb R\)-algebras need not be a \(C^\infty\)-ring morphism.

A **morphism of \(C^\infty\)-rings** \(u:A\to B\) commutes with every smooth
operation:
\[
u\bigl(\Phi_f(a_1,\ldots,a_n)\bigr)
=\Phi_f\bigl(u(a_1),\ldots,u(a_n)\bigr).
\]

## Basic examples

For a [[fiber-bundles/smooth-manifold|smooth manifold]] \(M\), the
[[differential-geometry/algebra-of-smooth-functions|algebra
\(C^\infty(M)\)]] is a \(C^\infty\)-ring under pointwise smooth functional
calculus:
\[
\Phi_f(a_1,\ldots,a_n)(p)
=f(a_1(p),\ldots,a_n(p)).
\]
The quotient of a \(C^\infty\)-ring by an ideal inherits a canonical
\(C^\infty\)-ring structure. Such quotients provide examples far beyond
algebras of functions on manifolds.

## References

1. Ieke Moerdijk and Gonzalo E. Reyes, *Models for Smooth Infinitesimal Analysis*, Springer, 1991. [DOI record](https://doi.org/10.1007/978-1-4757-4148-6). Relevant: Chapter I, algebraic theories of smooth functions and \(C^\infty\)-rings.
2. Dominic Joyce, “Algebraic Geometry over \(C^\infty\)-rings,” *Memoirs of the AMS* 260 (2019). [arXiv version](https://arxiv.org/abs/1001.0023). Relevant: §2, definitions and examples of \(C^\infty\)-rings.
