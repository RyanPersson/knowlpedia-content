+++
id = "langlands/cohomological-automorphic-representation"
title = "Cohomological automorphic representation"
kind = "knowl"
summary = "An automorphic representation whose archimedean components have nonzero relative Lie algebra cohomology with algebraic coefficients."
aliases = ["cohomological representation", "cohomological automorphic representations"]
domains = ["langlands", "number-theory", "representation-theory"]
prerequisites = ["algebraic-geometry-foundations/reductive-algebraic-group", "algebra-fields-galois/number-field", "langlands/automorphic-representation", "lie-groups/complexification-of-a-real-lie-algebra", "lie-groups/maximal-compact-subgroup-real-reductive-group"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(G\) be a connected [[algebraic-geometry-foundations/reductive-algebraic-group|reductive group]] over a
[[algebra-fields-galois/number-field|number field]]
\(F\), and write
\(\pi=\bigotimes_v'\pi_v\) for an
[[langlands/automorphic-representation|automorphic representation]]. It is
**cohomological** if, for every archimedean place \(v\), there is a
finite-dimensional algebraic representation \(E_v\) of \(G(F_v)\) and an
integer \(q\geq 0\) such that

\[
H^q(\mathfrak g_v,K_v;\pi_v\otimes E_v)\neq 0.
\]

Here \(\mathfrak g_v\) is the
[[lie-groups/complexification-of-a-real-lie-algebra|complexified Lie algebra]]
and \(K_v\) is a
[[lie-groups/maximal-compact-subgroup-real-reductive-group|maximal compact
subgroup]], with the usual modification for a disconnected
\(K_v\).

## Geometric role

[[lie-groups/relative-lie-algebra-cohomology|Relative Lie algebra cohomology]]
connects automorphic representations to the
cohomology of locally symmetric spaces. With suitable level \(K_f\), a
cohomological \(\pi\) can contribute to the cohomology of

\[
G(F)\backslash G(\mathbb A_F)/(K_\infty K_f)
\]

with the [[fiber-bundles/local-system|local system]] determined by the algebraic coefficient
representation.

## Algebraicity

Every cohomological automorphic representation is
[[langlands/c-algebraic-automorphic-representation|\(C\)-algebraic]]. The
converse requires additional hypotheses and is not true as a bare statement
for arbitrary reductive groups. For regular algebraic representations of
\(\operatorname{GL}_n\), the two notions are closely related, up to familiar
twists.

## Coefficient convention

Some authors put \(E_v^\vee\), rather than \(E_v\), in the cohomology group.
This changes the recorded [[lie-groups/highest-weight|highest weight]] but not the substantive existence
condition once the convention is stated. Cohomological degree and
infinitesimal-character normalization must also be tracked in explicit
formulas.

## References

1. A. Borel and N. Wallach, *Continuous Cohomology, Discrete Subgroups, and
   Representations of Reductive Groups*, second edition, AMS, 2000.
   [AMS](https://bookstore.ams.org/surv-67).
2. Kevin Buzzard and Toby Gee, “The conjectural connections between
   automorphic representations and Galois representations,” §7.2.
   [arXiv](https://arxiv.org/abs/1009.0785).
