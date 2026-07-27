+++
id = "operator-algebras/k1-cstar-algebra"
title = "K_1 of a C*-algebra"
kind = "definition"
summary = "The stable homotopy group of unitary elements over a C*-algebra."
aliases = ["operator K-one", "unitary K-theory", "odd K-theory"]
domains = ["operator-algebras", "k-theory"]
section_mode = "progressive"
+++

Let \(A\) be a unital [[operator-algebras/cstar-algebra|\(C^*\)-algebra]], and
form
\[
U_\infty(A)=\bigcup_{n\geq1}U(M_n(A))
\]
using the inclusions \(u\mapsto\operatorname{diag}(u,1)\). The group
\(K_1(A)\) is the set of path components of \(U_\infty(A)\), with addition
induced by block sum. Equivalently, its elements are stable homotopy classes
of [[operator-algebras/unitary-element|unitaries]] in
[[operator-algebras/matrix-cstar-algebra|matrix \(C^*\)-algebras]] over \(A\).
For nonunital \(A\), define
\[
K_1(A)=\ker\bigl(K_1(\widetilde A)\to K_1(\mathbb C)\bigr)
\]
using the scalar quotient from the
[[operator-algebras/unitization|unitization]].

## Representative calculus

A nonunital class can be represented by a unitary
\(u\in M_n(\widetilde A)\) whose scalar image is \(1_n\). Stabilization permits
adjoining identity blocks, and homotopy is taken through unitaries after a
common stabilization. Although block sum defines the group law,
\([uv]=[u]+[v]\) for stabilized unitaries. These equivalent models are proved
in [Blackadar, Chapter IV](https://doi.org/10.1017/9781009701907).

## Basic properties and examples

The functor \(K_1\) is homotopy invariant, matrix stable, and strongly Morita
invariant. One has \(K_1(\mathbb C)=0\), while the winding number gives
\[
K_1(C(S^1))\cong\mathbb Z.
\]
Continuous \(*\)-homomorphisms carry unitary representatives to unitary
representatives and therefore induce group homomorphisms on \(K_1\).

## Conventions and scope

For a nonunital algebra, a \(K_1\)-representative generally belongs to a matrix
algebra over \(\widetilde A\), not to \(A\) itself. Definitions using connected
components of stable invertibles instead of stable unitaries give the same
group by polar decomposition. The adjective “odd” reflects Bott periodicity
and the odd index pairing; it is not an additional grading on \(A\).

## References

1. Bruce Blackadar, *K-Theory for Operator Algebras*, 2nd ed., Cambridge University Press, 1998. [DOI record](https://doi.org/10.1017/9781009701907). Relevant: Chapter IV on \(K_1\), stable unitary groups, and Bott periodicity.
2. N. E. Wegge-Olsen, *K-Theory and C*-Algebras: A Friendly Approach*, Oxford University Press, 1993. [DOI record](https://doi.org/10.1093/oso/9780198596943.001.0001). Relevant: Chapter 7 on \(K_1\) and suspensions.
