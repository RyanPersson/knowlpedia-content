+++
id = "algebra-groups/first-isomorphism-theorem-groups"
title = "First Isomorphism Theorem (Groups)"
kind = "knowl"
summary = "A group homomorphism induces an isomorphism from the quotient by its kernel to its image."
aliases = ["first-isomorphism-theorem-groups", "First Isomorphism Theorem (Groups)"]
domains = ["algebra-groups"]
legacy_source_path = "algebra-groups/first-isomorphism-theorem-groups.md"
+++

Let \(f:G\to H\) be a [[algebra-groups/group-homomorphism|group homomorphism]]. Its [[algebra-groups/kernel-group|kernel]] \(K=\ker(f)\) is a [[algebra-groups/normal-subgroup|normal subgroup]] of \(G\), and \(f\) induces a [[algebra-groups/group-isomorphism|group isomorphism]]
\[
\bar f:G/K\longrightarrow \operatorname{im}(f),\qquad \bar f(gK)=f(g).
\]
In particular, if \(f\) is surjective, then \(G/\ker(f)\cong H\).

## Remarks

This is the basic “quotient equals image” principle. With \(I=\operatorname{im}(f)\), it can be expressed by the [[algebra-groups/exact-sequence-groups|short exact sequence]]
\[
1\longrightarrow K\longrightarrow G\longrightarrow I\longrightarrow 1.
\]
