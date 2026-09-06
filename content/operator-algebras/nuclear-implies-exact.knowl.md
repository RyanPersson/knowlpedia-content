+++
id = "operator-algebras/nuclear-implies-exact"
title = "Nuclear C*-algebras are exact"
kind = "theorem"
summary = "Every nuclear C-star algebra is exact, although exact C-star algebras need not be nuclear."
aliases = ["nuclearity implies exactness"]
domains = ["operator-algebras"]
section_mode = "progressive"
prerequisites = ["operator-algebras/nuclear-cstar-algebra", "operator-algebras/exact-cstar-algebra", "operator-algebras/cstar-exact-sequence", "operator-algebras/maximal-cstar-tensor-product"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Every [[operator-algebras/nuclear-cstar-algebra|nuclear \(C^*\)-algebra]] is
an [[operator-algebras/exact-cstar-algebra|exact \(C^*\)-algebra]].
Explicitly, if \(A\) is nuclear and
\[
0\longrightarrow I\longrightarrow B\longrightarrow B/I\longrightarrow 0
\]
is a [[operator-algebras/cstar-exact-sequence|short exact sequence of
\(C^*\)-algebras]], then
\[
0\longrightarrow I\otimes_{\min}A\longrightarrow
B\otimes_{\min}A\longrightarrow (B/I)\otimes_{\min}A
\longrightarrow 0
\]
is exact. Nuclearity is strictly stronger: exactness alone neither forces the
minimal and [[operator-algebras/maximal-cstar-tensor-product|maximal tensor products]] with \(A\) to agree nor supplies
completely positive finite-dimensional approximations.

## Proof idea

Nuclearity identifies the minimal tensor product with a tensor product whose
quotient behavior is controlled by completely positive approximations.
Equivalently, approximate the identity map on \(A\) pointwise in norm by
[[operator-algebras/completely-positive-contraction|completely positive contractions]] through matrix algebras. Tensoring those
factorizations with the given extension reduces the kernel calculation to
matrix amplifications, which preserve exactness. Passing to the point-norm
limit proves that the kernel in \(B\otimes_{\min}A\) is exactly
\(I\otimes_{\min}A\).

## Strictness of the implication

Commutative \(C^*\)-algebras and compact-operator algebras are nuclear, hence
exact. The converse fails: \(C_r^*(\mathbb F_2)\), the
[[operator-algebras/reduced-group-cstar-algebra|reduced
\(C^*\)-algebra]] of the [[algebra-groups/free-group|free group]] on two
generators, is exact but not nuclear. In the reduced group setting,
nuclearity detects amenability,
whereas exactness holds for a broader class of groups.

## Logical role

This result is an implication between properties, not an alternative
definition of nuclearity. In arguments about extensions, exactness is often
the precise hypothesis needed; assuming nuclearity may introduce unnecessary
structure.

## References

1. Nathanial P. Brown and Narutaka Ozawa, *C*-Algebras and Finite-Dimensional Approximations*, American Mathematical Society, 2008. [AMS DOI record](https://doi.org/10.1090/gsm/088). Relevant: §2.3, especially Proposition 2.3.8, on nuclearity and exactness.
