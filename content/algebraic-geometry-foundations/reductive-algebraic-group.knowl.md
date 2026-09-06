+++
id = "algebraic-geometry-foundations/reductive-algebraic-group"
title = "Reductive algebraic group"
kind = "definition"
summary = "A smooth connected affine algebraic group with trivial geometric unipotent radical."
aliases = ["reductive group", "reductive algebraic group"]
domains = ["algebraic-geometry-foundations", "langlands"]
section_mode = "progressive"
prerequisites = ["algebraic-geometry-foundations/algebraic-group", "algebra-fields-galois/algebraic-closure", "algebraic-geometry-foundations/unipotent-radical"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(k\) be a field. A **reductive algebraic group** over \(k\) is a smooth,
connected, affine [[algebraic-geometry-foundations/algebraic-group|algebraic
group]] \(G\) whose geometric unipotent radical is trivial:
\[
R_u(G_{\overline k})=1.
\]

Passing to an [[algebra-fields-galois/algebraic-closure|algebraic closure]] in this definition makes reductivity a
geometric property. A connected semisimple group is reductive, as is a torus;
\(GL_n\), \(SL_n\), \(PGL_n\), and \(Sp_{2n}\) are standard examples.

## Role of Borel and parabolic subgroups

After [[algebraic-geometry-foundations/base-change|base change]] to an algebraic closure, \(G\) has
[[algebraic-geometry-foundations/borel-subgroup|Borel subgroups]].
Its [[algebraic-geometry-foundations/parabolic-subgroup|parabolic subgroups]]
give projective homogeneous quotients \(G/P\).

## References

1. Brian Conrad, “Reductive group schemes,” in *Autour des schémas en
   groupes*, Panoramas et Synthèses 42–43 (2014), 93–444.
