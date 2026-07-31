+++
id = "functional-analysis/open-mapping-theorem"
title = "Open mapping theorem"
kind = "theorem"
summary = "A surjective bounded linear operator between Banach spaces maps open sets to open sets."
aliases = ["Banach–Schauder theorem"]
domains = ["functional-analysis"]
section_mode = "progressive"
+++

Let \(X\) and \(Y\) be
[[linear-algebra/banach-space|Banach spaces]] over the same scalar field
\(\mathbb R\) or \(\mathbb C\). If \(T:X\to Y\) is a surjective
[[functional-analysis/bounded-linear-operator|bounded linear operator]], then
\(T\) is an **open map**: \(T(U)\) is open in \(Y\) whenever \(U\) is open in
\(X\). Equivalently, there is a constant \(c>0\) such that
\[
B_Y(0,c)\subseteq T(B_X(0,1)).
\]
By scaling and translation, this quantitative inclusion gives openness at
every point. Surjectivity is essential: a proper [[convex-analysis/linear-subspace|linear subspace]] need not be
open [Conway, Chapter VI].

## Proof mechanism

Because \(T\) is surjective, \(Y\) is the union of the closures of the sets
\(T(nB_X(0,1))\). The
[[topology/baire-category-theorem|Baire category theorem]] gives one such
closure nonempty interior. Linearity then produces a ball about \(0\) in the
closure of \(T(B_X(0,1))\), and an iterative correction argument removes the
closure. Completeness is used both in the category step and when the
corrections are summed.

## Consequences and scope

A bounded linear bijection between Banach spaces has a bounded inverse.
Likewise, if \(M\) is a
[[linear-algebra/closed-linear-subspace|closed subspace]] of \(X\), the
quotient projection \(X\to X/M\) is open; this identifies the quotient norm
topology with the topology forced by the projection.

Completeness cannot simply be omitted. The identity from \(\ell^1\) with its
\(\ell^1\)-norm onto the same [[linear-algebra/vector-space|vector space]] equipped with the \(\ell^2\)-norm
is a bounded bijection, but its target is incomplete and the inverse is
unbounded. This does not conflict with the theorem because the target is not
Banach.

## References

1. John B. Conway, *A Course in Functional Analysis*, 2nd ed., Graduate Texts in Mathematics 96, Springer, 1990. [Springer DOI record](https://doi.org/10.1007/978-1-4757-4383-8). Relevant: Chapter VI, “Linear Operators on a Banach Space.”
2. Walter Rudin, *Functional Analysis*, 2nd ed., McGraw–Hill, 1991. [WorldCat record](https://search.worldcat.org/title/21163277). Relevant: Chapter 2, the open mapping theorem and its consequences.
