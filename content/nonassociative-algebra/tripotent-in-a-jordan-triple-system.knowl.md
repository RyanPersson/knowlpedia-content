+++
id = "nonassociative-algebra/tripotent-in-a-jordan-triple-system"
title = "Tripotent in a Jordan triple system"
kind = "definition"
summary = "An element e of a Jordan triple system satisfying {e,e,e}=e, the triple-system analogue of an idempotent."
aliases = ["tripotent", "Jordan tripotent", "triple-system tripotent"]
domains = ["nonassociative-algebra", "functional-analysis"]
prerequisites = ["nonassociative-algebra/hermitian-jordan-triple-system", "nonassociative-algebra/jordan-idempotent"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(V\) be a
[[nonassociative-algebra/hermitian-jordan-triple-system|Hermitian Jordan triple
system]] with triple product \(\{x,y,z\}\). A **tripotent** is an element
\(e\in V\) satisfying

\[
\{e,e,e\}=e.
\]

It is the ternary analogue of a
[[nonassociative-algebra/jordan-idempotent|Jordan idempotent]], but its
definition requires neither a binary product nor a distinguished unit.

## Operator example

For the normalized triple product on operators,

\[
\{x,y,z\}=\frac12(xy^*z+zy^*x),
\]

the tripotent equation becomes \(ee^*e=e\). Thus the tripotents are exactly
the [[functional-analysis/partial-isometry|partial isometries]]. Projections
are tripotents, but a tripotent need not be self-adjoint and therefore need
not be a projection.

## Peirce decomposition

Set \(D(e,e)z=\{e,e,z\}\). For the normalization above, \(D(e,e)\) has
possible eigenvalues \(1,\tfrac12,0\), giving the Peirce decomposition

\[
V=V_2(e)\oplus V_1(e)\oplus V_0(e),
\qquad
V_j(e)=\{z:D(e,e)z=\tfrac j2z\}.
\]

The indices \(2,1,0\) are traditional and record twice the eigenvalue. The
triple product obeys Peirce arithmetic:

\[
\{V_i(e),V_j(e),V_k(e)\}
\subseteq V_{i-j+k}(e),
\]

with a summand interpreted as zero when its index is outside
\(\{0,1,2\}\). The top space \(V_2(e)\) is a unital complex [[nonassociative-algebra/jordan-algebra|Jordan algebra]]
under
\[
x\circ_e z=\{x,e,z\},
\]
with unit \(e\).

## Orthogonality and rank

Two tripotents \(e,f\) are **orthogonal** when \(D(e,e)f=0\); in positive
Hermitian Jordan triples this relation is symmetric. Sums of pairwise
orthogonal tripotents are again tripotents. A nonzero tripotent is **minimal**
when \(V_2(e)=\mathbb Ce\), and it is **complete** when \(V_0(e)=0\). Maximal
families of mutually orthogonal minimal tripotents play the role of Jordan
frames and define the rank of a finite-dimensional positive triple system.

## Normalization warning

Some sources use the doubled product
\(xy^*z+zy^*x\). Under that convention the tripotent equation is
\(\{e,e,e\}=2e\), and the Peirce eigenvalues are \(2,1,0\). Formulas must not
be moved between the two conventions without this rescaling.

## References

1. Ottmar Loos, *Bounded Symmetric Domains and Jordan Pairs*, University of
   California, Irvine, 1977, Parts I–II. [Catalog record](https://books.google.com/books?id=CL4rAAAAYAAJ).
2. Harald Upmeier, *Symmetric Banach Manifolds and Jordan C*-Algebras*,
   North-Holland, 1985, Chapters 2–4. [Publisher record](https://www.sciencedirect.com/bookseries/north-holland-mathematics-studies/vol/104/suppl/C).
