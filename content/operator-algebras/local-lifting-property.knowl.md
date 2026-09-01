+++
id = "operator-algebras/local-lifting-property"
title = "Local lifting property"
kind = "definition"
summary = "A C*-algebraic property requiring completely positive quotient maps to lift on every finite-dimensional operator subsystem."
aliases = ["LLP"]
domains = ["operator-algebras"]
prerequisites = ["operator-algebras/cstar-algebra", "algebra-rings/two-sided-ideal", "operator-algebras/completely-positive-map", "convex-analysis/linear-subspace"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

A unital [[operator-algebras/cstar-algebra|\(C^*\)-algebra]] \(A\) has the
**local lifting property** (**LLP**) if the following holds. For every unital
\(C^*\)-algebra \(B\), closed [[algebra-rings/two-sided-ideal|two-sided ideal]] \(J\triangleleft B\), unital
[[operator-algebras/completely-positive-map|completely positive map]]
\(\phi:A\to B/J\), and finite-dimensional operator system \(E\subseteq A\)
(that is, a unital self-adjoint [[convex-analysis/linear-subspace|linear subspace]]), there is a unital
completely positive map
\[
\widetilde\phi_E:E\longrightarrow B
\]
such that \(q\circ\widetilde\phi_E=\phi|_E\), where \(q:B\to B/J\) is the
quotient map. The lift may depend on \(E\); no single lift on all of \(A\) is
required. Thus LLP is local in the finite-dimensional domain, while the
quotient and target remain arbitrary.

## Local versus global lifting

The lifting property (LP) requires one unital completely positive lift
\(\widetilde\phi:A\to B\) for the whole map. Hence LP implies LLP. The
converse is false in general: compatible local lifts need not assemble into
a global lift.

Every separable nuclear \(C^*\)-algebra has LP by the Choi–Effros lifting
theorem and therefore has LLP. The full group algebra
\(C^*(\mathbb F_\infty)\) is an important nonnuclear example with LLP, so LLP
is not a form of nuclearity.

## Tensor-product characterization

Kirchberg's characterization says that \(A\) has LLP exactly when, for an
infinite-dimensional [[linear-algebra/hilbert-space|Hilbert space]] \(H\), the canonical map identifies
\[
A\otimes_{\max}B(H)=A\otimes_{\min}B(H)
\]
isometrically. In other words, \(A\) and \(B(H)\) form a nuclear pair even
though neither algebra need be nuclear. This connects a local
[[operator-algebras/quotient-cstar-algebra|quotient-lifting]] condition to
the comparison of maximal and minimal \(C^*\)-tensor norms.

## Nonunital convention

For a nonunital \(C^*\)-algebra, LLP is normally defined by requiring its
unitization to have LLP. Equivalent formulations use completely positive
contractive maps on finite-dimensional self-adjoint subspaces. Stating the
unitization convention prevents ambiguity about where the order unit in the
local operator system comes from.

## References

1. Nathanial P. Brown and Narutaka Ozawa, *\(C^*\)-Algebras and Finite-Dimensional Approximations*, Graduate Studies in Mathematics 88, American Mathematical Society, 2008. [AMS chapter record](https://doi.org/10.1090/gsm/088/19). Relevant: Chapter 13, especially §13.1 on LLP and §13.2 on tensorial characterizations.
2. Gilles Pisier, *Introduction to Operator Space Theory*, London Mathematical Society Lecture Note Series 294, Cambridge University Press, 2003. [Publisher record](https://www.cambridge.org/core/books/introduction-to-operator-space-theory/DE174FA28C7DBC243FBEA3911E97EA4E). Relevant: Chapter 16 on the local lifting property.
