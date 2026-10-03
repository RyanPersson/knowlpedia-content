+++
id = "catalog/finite-groups/sporadic/mathieu-point-stabilizers"
title = "Mathieu point stabilizers"
kind = "theorem"
summary = "The inclusions M11 in M12 and M22 in M23 in M24 from natural permutation actions."
aliases = ["Mathieu point stabilizers"]
domains = ["catalog", "algebra-groups", "finite-groups"]
section_mode = "progressive"
prerequisites = ["catalog/finite-groups/sporadic/m11", "catalog/finite-groups/sporadic/m12", "catalog/finite-groups/sporadic/m22", "catalog/finite-groups/sporadic/m23", "catalog/finite-groups/sporadic/m24", "algebra-groups/stabilizer", "algebra-groups/group-homomorphism"]
dependency_heuristic = "finite-catalog-semantic-core-v1"
dependency_review_count = 1
+++

In the natural permutation actions, a [[algebra-groups/stabilizer|point stabilizer]] in [[catalog/finite-groups/sporadic/m12|\(M_{12}\)]] is isomorphic to [[catalog/finite-groups/sporadic/m11|\(M_{11}\)]], one in [[catalog/finite-groups/sporadic/m23|\(M_{23}\)]] is isomorphic to [[catalog/finite-groups/sporadic/m22|\(M_{22}\)]], and one in [[catalog/finite-groups/sporadic/m24|\(M_{24}\)]] is isomorphic to \(M_{23}\). Hence there are injective [[algebra-groups/group-homomorphism|group homomorphisms]]
\[
\begin{gathered}
M_{11}\hookrightarrow M_{12},\quad [M_{12}:M_{11}]=12,\\
M_{22}\hookrightarrow M_{23},\quad [M_{23}:M_{22}]=23,\\
M_{23}\hookrightarrow M_{24},\quad [M_{24}:M_{23}]=24.
\end{gathered}
\]
Each inclusion uses a chosen point and an isomorphism from the named source group to its stabilizer.

## Why the indices are the degrees

The actions are transitive, so the [[algebra-groups/orbit-stabilizer-theorem|orbit–stabilizer theorem]] identifies each set of [[algebra-groups/coset|left cosets]] with the relevant point set. Each action is at least doubly transitive, hence primitive, and its point stabilizer is maximal. Composing the last two embeddings also gives a copy of \(M_{22}\) in \(M_{24}\) of index \(23\cdot24=552\).

## Scope

These are specified subgroup constructions. They do not classify all embeddings or all homomorphisms between the Mathieu groups, and the \(M_{11}\subset M_{12}\) relation belongs to a separate stabilizer chain.

## References

1. [ATLAS M12G1-p12aB0](https://brauer.maths.qmul.ac.uk/Atlas/v3/permrep/M12G1-p12aB0), Properties: transitivity and point stabilizer.
2. [ATLAS M23G1-p23B0](https://brauer.maths.qmul.ac.uk/Atlas/v3/permrep/M23G1-p23B0), Properties: transitivity and point stabilizer.
3. [ATLAS M24G1-p24B0](https://brauer.maths.qmul.ac.uk/Atlas/v3/permrep/M24G1-p24B0), Properties: transitivity and point stabilizer.
