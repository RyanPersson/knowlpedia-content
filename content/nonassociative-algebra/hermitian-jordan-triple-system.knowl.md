+++
id = "nonassociative-algebra/hermitian-jordan-triple-system"
title = "Hermitian Jordan triple system"
kind = "definition"
summary = "A complex vector space with a symmetric outer, conjugate-linear middle triple product satisfying the Jordan triple identity."
aliases = ["positive Hermitian Jordan triple system", "Hermitian Jordan triple"]
domains = ["nonassociative-algebra", "complex-analysis"]
prerequisites = ["linear-algebra/vector-space"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

A **Hermitian Jordan triple system** is a complex [[linear-algebra/vector-space|vector space]] \(V\) with a
sesquilinear triple product
\[
\{x,y,z\}:V\times V\times V\longrightarrow V
\]
that is complex-linear in \(x,z\), conjugate-linear in \(y\), symmetric in the
outer variables, and satisfies the Jordan triple identity
\[
\{x,y,\{u,v,w\}\}
=\{\{x,y,u\},v,w\}
-\{u,\{y,x,v\},w\}
+\{u,v,\{x,y,w\}\}.
\]
In the finite-dimensional **positive** case, the Hermitian trace form
\[
(x\mid y)=\operatorname{tr}D(x,y),
\qquad D(x,y)z=\{x,y,z\},
\]
is positive definite.

## Operator-algebra example

If \(V\) is an associative complex \(*\)-algebra, or a complex vector subspace
of one that is closed under the following operation, then
\[
\{x,y,z\}=\frac12(xy^*z+zy^*x)
\]
defines a Hermitian Jordan triple product. In particular, rectangular complex
matrices form a triple system even though ordinary matrix multiplication does
not close on a rectangular matrix space. A [[operator-algebras/cstar-algebra|C*-algebra]]
with this triple product is a basic analytic example.

## Relation to Jordan algebras

A unital Hermitian [[nonassociative-algebra/jordan-algebra|Jordan algebra]] gives a triple system, but the triple-system
language does not require a distinguished unit or even a binary product.
Conversely, choosing a suitable tripotent can produce Peirce spaces and binary
Jordan products on appropriate components. Thus a Hermitian Jordan triple
system should not be identified with a [[nonassociative-algebra/jordan-algebra|Jordan
algebra]] without extra data.

## Geometry

Finite-dimensional positive Hermitian Jordan triple systems classify bounded
symmetric domains: the open unit ball for the associated spectral norm is a
bounded symmetric domain, and every bounded symmetric domain arises this way
up to biholomorphism. Simple triple systems correspond to irreducible bounded
symmetric domains.

## Convention warning

Some authors reverse which outer variable is linear or rescale the triple
product. The Jordan triple identity must be read with the same convention.
The adjective **Hermitian** records the conjugate-linearity; an algebraic
Jordan triple system over a general field is linear in all variables and is a
different notion.

## References

1. Ottmar Loos, *Bounded Symmetric Domains and Jordan Pairs*, University of
   California, Irvine, 1977, Parts I–II.
2. Harald Upmeier, *Symmetric Banach Manifolds and Jordan C*-Algebras*,
   North-Holland, 1985, Chapters 2–4.
3. John C. Baez, Eric H. Bokor, and Latham Boyle, “Jordan Pair Quantum
   Mechanics and the Standard Model,” 2026.
   [arXiv:2607.10833](https://arxiv.org/abs/2607.10833).
