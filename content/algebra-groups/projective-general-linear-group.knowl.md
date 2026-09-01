+++
id = "algebra-groups/projective-general-linear-group"
title = "Projective general linear group"
kind = "definition"
summary = "The quotient of a general linear group by its subgroup of nonzero scalar maps."
aliases = ["PGL", "projective linear group", "full projective group"]
domains = ["algebra-groups", "algebraic-geometry-foundations"]
prerequisites = ["linear-algebra/vector-space", "algebra-groups/quotient-group"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(V\) be a nonzero finite-dimensional [[linear-algebra/vector-space|vector space]] over a field \(k\). The **projective general linear group** is the [[algebra-groups/quotient-group|quotient group]]
\[
\operatorname{PGL}(V)
:=\operatorname{GL}(V)/(k^\times I),
\]
where \(k^\times I=\{\lambda I_V:\lambda\in k^\times\}\) is the central subgroup of nonzero scalar maps. For \(V=k^n\), it is denoted \(\operatorname{PGL}_n(k)\).

## Action on projective space

The action of \(\operatorname{GL}(V)\) on [[algebraic-geometry-foundations/projective-space|\(\mathbb P(V)\)]] has kernel \(k^\times I\), so it descends to a faithful action of \(\operatorname{PGL}(V)\). Its elements are exactly the [[algebraic-geometry-foundations/projective-transformation|projective transformations]] induced by invertible linear maps.

For \(\dim_kV\ge2\), this action is sharply determined by its effect on a projective frame. It is generally smaller than the full collineation group when \(k\) has nontrivial [[algebra-fields-galois/field-automorphism|field automorphisms]]; the latter is the [[algebraic-geometry-foundations/projective-semilinear-group|projective semilinear group]].

## Relation to \(\operatorname{PSL}\)

The image of \(\operatorname{SL}_n(k)\) in \(\operatorname{PGL}_n(k)\) is the [[algebra-groups/projective-special-linear-group|projective special linear group]]. It need not be all of \(\operatorname{PGL}_n(k)\). The obstruction is measured by determinant modulo \(n\)-th powers in the [[algebra-groups/pgl-psl-comparison|\(\operatorname{PGL}\)–\(\operatorname{PSL}\) comparison]].

## References

1. James S. Milne, *Algebraic Groups: The Theory of Group Schemes of Finite Type over a Field*, Cambridge University Press, 2017. [Author-maintained text](https://www.jmilne.org/math/CourseNotes/ala.html). Relevant: classical algebraic groups and central quotients.
2. Emil Artin, *Geometric Algebra*, Interscience, 1957. Relevant: Chapter II, projective transformations.
