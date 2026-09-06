+++
id = "algebraic-geometry-foundations/regular-scheme"
title = "Regular scheme"
kind = "definition"
summary = "A locally Noetherian scheme whose local rings are regular."
aliases = ["regular scheme", "nonsingular scheme"]
domains = ["algebraic-geometry-foundations"]
prerequisites = ["algebraic-geometry-foundations/scheme", "algebraic-geometry-foundations/regular-local-ring"]
dependency_heuristic = "semantic-spotcheck-review-v1"
dependency_review_count = 2
+++

A [[algebraic-geometry-foundations/scheme|scheme]] \(X\) is **regular** if it is locally Noetherian and each local ring \(\mathcal O_{X,x}\) is a [[algebraic-geometry-foundations/regular-local-ring|regular local ring]]. Here locally Noetherian means that every point has an affine open neighborhood with Noetherian coordinate ring.

## Interpretation

The local rings are the stalks of the structure sheaf of the underlying [[algebraic-geometry-foundations/locally-ringed-space|locally ringed space]]. Thus this definition concerns the scheme itself and does not require a chosen base field.

## Reference

[Stacks Project, Regular schemes, Tag 02IR](https://stacks.math.columbia.edu/tag/02IR).
