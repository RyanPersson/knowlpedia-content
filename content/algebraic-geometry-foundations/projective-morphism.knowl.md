+++
id = "algebraic-geometry-foundations/projective-morphism"
title = "Projective morphism"
kind = "definition"
summary = "A scheme morphism that factors as a closed immersion into relative projective space."
aliases = ["projective map of schemes", "projective morphism"]
domains = ["algebraic-geometry-foundations"]
section_mode = "progressive"
prerequisites = ["algebraic-geometry-foundations/scheme", "algebraic-geometry-foundations/scheme-over-a-base"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

A morphism of schemes \(f:X\to S\) is **projective** if there is an integer
\(n\geq0\) and a factorization
\[
X\hookrightarrow\mathbb P^n_S\longrightarrow S
\]
in which the first map is a closed immersion and the second is the canonical
projection.

Projective morphisms are proper and of finite type. They are preserved by
[[algebraic-geometry-foundations/base-change|base change]] and composition. If the base is locally Noetherian, then a
projective morphism is also of finite presentation.

## Relative ample line bundles

Under standard quasi-compactness hypotheses, projectivity can equivalently be
characterized by the existence of a relatively ample invertible sheaf. This
formulation does not change the defining factorization above.

## References

1. The Stacks Project Authors, “Projective morphisms,”
   [Tag 01W7](https://stacks.math.columbia.edu/tag/01W7).
