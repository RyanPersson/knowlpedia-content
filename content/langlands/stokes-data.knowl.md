+++
id = "langlands/stokes-data"
title = "Stokes data"
kind = "definition"
summary = "The sectorial transition data that, together with formal type, classify an irregular meromorphic connection analytically."
aliases = ["Stokes matrices", "Stokes local system"]
domains = ["langlands", "algebraic-geometry-foundations"]
prerequisites = ["langlands/irregular-singular-connection"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Near an [[langlands/irregular-singular-connection|irregular singularity]],
choose sectorial fundamental solutions having a fixed formal asymptotic
expansion. On overlaps of adjacent sectors, two such solutions differ by a
locally constant unipotent transformation. The resulting transformations,
indexed by the singular directions and subject to their product and
compatibility relations, are the **Stokes data** of the connection.

Stokes data are invariant under changes of sectorial solutions up to the
appropriate simultaneous gauge equivalence. Formal type, formal monodromy,
and Stokes data together recover the local analytic isomorphism class; formal
type and ordinary monodromy alone generally do not.

## References

1. Philip Boalch, “Geometry and braiding of Stokes data; fission and wild
   character varieties,” *Annals of Mathematics* 179 (2014), 301–365.
   [arXiv](https://arxiv.org/abs/1111.6228).
