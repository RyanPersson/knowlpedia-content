+++
id = "operator-algebras/graded-cstar-algebra"
title = "Graded C*-algebra"
kind = "definition"
summary = "A C-star algebra decomposed into even and odd closed subspaces compatible with multiplication and involution."
aliases = ["Z/2-graded C*-algebra", "super C*-algebra"]
domains = ["operator-algebras", "algebra-representation-theory"]
prerequisites = ["operator-algebras/cstar-algebra"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

A **graded \(C^*\)-algebra** is a
[[operator-algebras/cstar-algebra|\(C^*\)-algebra]] \(A\) with closed linear
subspaces \(A^0,A^1\) such that
\[
A=A^0\oplus A^1,\qquad A^iA^j\subseteq A^{i+j},\qquad
(A^i)^*\subseteq A^i,
\]
where indices are taken modulo \(2\). Elements of \(A^0\) are **even** and
elements of \(A^1\) are **odd**; either kind is homogeneous, of degree \(0\)
or \(1\). A homomorphism of graded \(C^*\)-algebras is graded when it
preserves degrees. The **trivial grading** is \(A^0=A\), \(A^1=0\).

## Grading automorphism

Equivalently, a grading is a
[[operator-algebras/star-automorphism|\(*\)-automorphism]]
\(\gamma:A\to A\) satisfying \(\gamma^2=\operatorname{id}_A\). Its
\(+1\)-eigenspace is \(A^0\), its \(-1\)-eigenspace is \(A^1\), and
\[
a^0=\frac{a+\gamma(a)}2,\qquad
a^1=\frac{a-\gamma(a)}2
\]
recover the homogeneous parts of \(a\). This formulation also shows that
both summands are closed and that the decomposition is unique.

## Graded signs and tensor products

For homogeneous elements, the graded commutator is
\([a,b]_{\mathrm{gr}}=ab-(-1)^{|a||b|}ba\). The algebraic graded tensor
product uses
\[
(a\widehat\otimes b)(a'\widehat\otimes b')
=(-1)^{|b||a'|}aa'\widehat\otimes bb',
\]
with a corresponding sign in the involution. These signs are structural:
forgetting them produces the ordinary tensor product, not the graded one.

## Examples and scope

Every \(C^*\)-algebra has the trivial grading. A
[[operator-algebras/bounded-operator-cstar-algebra|bounded-operator algebra]]
on a [[functional-analysis/z2-graded-hilbert-space|graded Hilbert space]] is
graded by conjugation with the grading operator; its even operators preserve
the two summands and its odd operators interchange them. Gradings by larger
groups require additional homogeneous components and are not meant by
“graded” here unless explicitly stated.

## References

1. Bruce Blackadar, *K-Theory for Operator Algebras*, 2nd ed., Cambridge University Press, 1998. [Publisher DOI record](https://doi.org/10.1017/9781009701907). Relevant: §14.4 on graded \(C^*\)-algebras and graded tensor products.
2. Nigel Higson and John Roe, *Analytic K-Homology*, Oxford University Press, 2000. [Publisher DOI record](https://doi.org/10.1093/oso/9780198511762.001.0001). Relevant: Chapter 8 on graded algebras, modules, and operators.
