+++
id = "differential-geometry/isotopy-extension-theorem"
title = "Isotopy extension theorem"
kind = "theorem"
summary = "A smooth isotopy of a compact embedded manifold extends to a smooth ambient isotopy."
aliases = ["ambient isotopy extension theorem"]
domains = ["differential-geometry", "topology"]
prerequisites = ["fiber-bundles/smooth-manifold", "differential-geometry/smooth-isotopy", "differential-geometry/ambient-isotopy", "fiber-bundles/vector-field", "differential-geometry/tubular-neighborhood"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(N\) be a compact [[fiber-bundles/smooth-manifold|smooth manifold]], let \(M\) be a smooth manifold without boundary, and let \(F:N\times[0,1]\to M\) be a [[differential-geometry/smooth-isotopy|smooth isotopy]] of embeddings with \(F_0=i\). The **isotopy extension theorem** states that there is a smooth [[differential-geometry/ambient-isotopy|ambient isotopy]] \(\Phi:M\times[0,1]\to M\) such that \(\Phi_0=\operatorname{id}_M\) and
\[
\Phi_t\circ i=F_t
\]
for every \(t\). Moreover, \(\Phi_t\) can be chosen to have compact support in an arbitrarily prescribed neighborhood of the track \(F(N\times[0,1])\), after that neighborhood is chosen suitably. Thus deforming the embedded copy of \(N\) can be realized by deforming all of \(M\).

## Construction idea

Differentiating \(F_t\) in \(t\) gives a [[fiber-bundles/vector-field|vector field]] along the moving submanifold \(F_t(N)\). A [[differential-geometry/tubular-neighborhood|tubular neighborhood]], extension in the normal directions, and a cutoff function extend it to a compactly supported time-dependent vector field on \(M\). The flow of this ambient field is the required \(\Phi_t\). Compact support ensures that the flow exists for the whole parameter interval.

## Relative and boundary forms

There are relative versions that keep a region fixed when the original isotopy is stationary there. Manifolds with boundary also admit versions when the embeddings and extended vector fields respect the boundary, often after requiring the isotopy to be fixed near it. These additional hypotheses are part of the theorem being applied; the boundaryless statement in the core avoids silently imposing one convention.

## Consequences and limitations

Two compact embeddings joined by a smooth isotopy are therefore ambiently isotopic, so their complements are diffeomorphic. Compactness, properness, or a suitable support condition cannot be discarded indiscriminately: for a noncompact embedded manifold, a moving velocity field may admit no complete ambient extension. A mere [[differential-geometry/smooth-homotopy|smooth homotopy]] is also insufficient because its intermediate maps may fail to remain embeddings.

## References

1. Morris W. Hirsch, *Differential Topology*, Graduate Texts in Mathematics 33, Springer, 1976. [DOI record](https://doi.org/10.1007/978-1-4684-9449-5). Relevant: Chapter 8, §1, isotopy extension and support control.
