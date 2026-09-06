+++
id = "algebraic-geometry-foundations/smooth-morphism"
title = "Smooth morphism"
kind = "definition"
summary = "A locally finitely presented flat morphism with geometrically regular fibers."
aliases = ["smooth map of schemes", "smooth morphism"]
domains = ["algebraic-geometry-foundations"]
section_mode = "progressive"
prerequisites = ["algebraic-geometry-foundations/flat-morphism", "algebraic-geometry-foundations/locally-of-finite-presentation", "algebraic-geometry-foundations/geometric-fiber", "algebraic-geometry-foundations/regular-scheme"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

A morphism of schemes \(f:X\to S\) is **smooth** if it is locally of finite
presentation, [[algebraic-geometry-foundations/flat-morphism|flat]], and every
geometric fiber \(X_{\overline s}\) is regular.

If every nonempty geometric fiber has pure dimension \(n\), then \(f\) is
**smooth of relative dimension \(n\)**. Smoothness is preserved by base
change and composition and is local on both source and target for the étale
topology.

## Infinitesimal criterion

For morphisms [[algebraic-geometry-foundations/locally-of-finite-presentation|locally of finite presentation]], smoothness is equivalent to
formal smoothness: maps from a nilpotent closed subscheme lift locally across
the thickening. This is the scheme-theoretic analogue of having no
infinitesimal singularities in the fibers.

## References

1. The Stacks Project Authors, “Smooth morphisms,”
   [Tag 01V4](https://stacks.math.columbia.edu/tag/01V4).
