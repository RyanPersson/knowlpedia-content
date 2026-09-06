+++
id = "lie-groups/spin9-spin-representation"
title = "Spin representation of Spin(9)"
kind = "definition"
summary = "The real 16-dimensional spin representation of Spin(9), realized on the octonionic plane."
aliases = ["16-dimensional spin representation of Spin(9)", "Spin(9) action on O^2", "real Spin(9) spin module"]
domains = ["lie-groups", "representation-theory", "nonassociative-algebra"]
section_mode = "progressive"
prerequisites = ["lie-groups/spin-group", "lie-groups/maximal-compact-subgroup-real-reductive-group", "lie-groups/octonionic-special-linear-group"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

The compact [[lie-groups/spin-group|spin group]]
\(\operatorname{Spin}(9)\) has a real irreducible **spin representation**
\[
\Delta_9\cong\mathbb R^{16}\cong\mathbb O^2.
\]
It is the restriction to the
[[lie-groups/maximal-compact-subgroup-real-reductive-group|maximal compact
subgroup]] of the defining
16-dimensional real action of
[[lie-groups/octonionic-special-linear-group|\(SL_2(\mathbb O)\cong
\operatorname{Spin}(9,1)\)]].

## Transitive sphere action

The action is orthogonal and transitive on the
[[linear-algebra/unit-sphere|unit sphere]]
\(S^{15}\subset\Delta_9\); the stabilizer of a unit spinor is isomorphic to
\(\operatorname{Spin}(7)\). Hence
\[
S^{15}\cong\operatorname{Spin}(9)/\operatorname{Spin}(7).
\]
This is one of the exceptional
[[algebra-groups/transitive-action|transitive actions]] of a compact connected Lie
group on a sphere.

## Octonionic geometry

The action descends through the octonionic Hopf fibration to a transitive
action on [[differential-geometry/octonionic-projective-line|
\(\mathbb OP^1\cong S^8\)]]. It preserves octonionic-line geometry and is the
symmetry responsible for the invariance of the
[[convex-analysis/octonionic-pseudovolume|octonionic pseudovolume]].

## Two appearances of Spin(9)

This spin action on \(\mathbb O^2\) is different from the nine-dimensional
vector representation obtained from
\(\operatorname{Spin}(9)\to SO(9)\). It is also compatible with, but should
not be conflated with, the appearance of \(\operatorname{Spin}(9)\) as the
stabilizer of a point in the Cayley plane.

## References

1. John C. Baez, “The Octonions,” *Bulletin of the American Mathematical Society* 39 (2002), 145–205. [DOI record](https://doi.org/10.1090/S0273-0979-01-00934-X). Relevant: §4.2.
2. Semyon Alesker, “Plurisubharmonic functions on the octonionic plane and \(\operatorname{Spin}(9)\)-invariant valuations on convex sets,” *Journal of Geometric Analysis* 18 (2008), 651–686. [arXiv record](https://arxiv.org/abs/0707.4385). Relevant: §§1.3–1.4.
