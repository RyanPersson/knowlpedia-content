+++
id = "algebraic-geometry-foundations/levi-subgroup"
title = "Levi subgroup"
kind = "definition"
summary = "A reductive complement to the unipotent radical of a parabolic subgroup."
aliases = ["Levi factor", "Levi component", "Levi decomposition of a parabolic"]
domains = ["algebraic-geometry-foundations", "algebra-groups", "langlands"]
section_mode = "progressive"
prerequisites = ["algebraic-geometry-foundations/reductive-algebraic-group", "algebraic-geometry-foundations/parabolic-subgroup", "algebra-groups/semidirect-product", "algebraic-geometry-foundations/unipotent-radical"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(G\) be a connected
[[algebraic-geometry-foundations/reductive-algebraic-group|reductive group]]
and let
\(P\subseteq G\) be a [[algebraic-geometry-foundations/parabolic-subgroup|parabolic subgroup]].
A **Levi subgroup** of \(P\) is a reductive closed subgroup \(M\subseteq P\)
for which multiplication induces an isomorphism

\[
M\ltimes R_u(P)\xrightarrow{\sim}P,
\]

where \(\ltimes\) denotes a
[[algebra-groups/semidirect-product|semidirect product]] and \(R_u(P)\) is
the
[[algebraic-geometry-foundations/unipotent-radical|unipotent radical]].

## Existence and nonuniqueness

Parabolic subgroups of connected reductive groups over a field admit Levi
subgroups over that field.  Any two Levi subgroups of a fixed \(P\) are
conjugate by an element of \(R_u(P)\).  Thus “the Levi of \(P\)” usually means
a choice, while its [[algebra-groups/conjugacy-class|conjugacy class]] inside
\(P\) is canonical.

If \(P=P_G(\lambda)\) is defined by a
[[langlands-letter/knowls/maximal-torus-weight-lattice|cocharacter]]
\(\lambda:\mathbb G_m\to G\), then the
[[algebra-groups/centralizer|centralizer]]
\(Z_G(\lambda)\) is a Levi subgroup and \(R_u(P)=U_G(\lambda)\).

## Representation-theoretic role

Over a nonarchimedean local field,
[[harmonic-analysis/normalized-parabolic-induction-p-adic-group|parabolic
induction]] starts with a representation of \(M(F)\), inflates it to
\(P(F)\), and induces it to \(G(F)\).  The adjoint construction is the
[[harmonic-analysis/jacquet-module|Jacquet module]].  Levi subgroups also
index the terms in the [[langlands/arthur-selberg-trace-formula|trace formula]]
and the blocks in the [[harmonic-analysis/bernstein-decomposition|Bernstein
decomposition]].

## References

1. Brian Conrad, *Reductive Group Schemes*, §5.4.
   [Author notes](https://math.stanford.edu/~conrad/papers/luminysga3.pdf).
2. Armand Borel and Jacques Tits, “Groupes réductifs,” *Publications
   Mathématiques de l'IHÉS* 27 (1965), 55–150.
   [Numdam](https://www.numdam.org/item/PMIHES_1965__27__55_0/).
