+++
id = "differential-geometry/ambient-isotopy"
title = "Ambient isotopy"
kind = "definition"
summary = "An ambient isotopy is a smooth family of diffeomorphisms of a manifold beginning at the identity."
aliases = ["isotopy by diffeomorphisms"]
domains = ["differential-geometry"]
prerequisites = ["fiber-bundles/smooth-manifold", "differential-geometry/smooth-map-of-manifolds-with-boundary", "fiber-bundles/diffeomorphism", "differential-geometry/embedded-submanifold"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(N\) be a [[fiber-bundles/smooth-manifold|smooth manifold]]. An
**ambient isotopy** of \(N\) is a [[differential-geometry/smooth-map-of-manifolds-with-boundary|smooth map in the manifold-with-boundary sense]]
\(\Phi:N\times[0,1]\to N\) such that every time slice
\(\Phi_t(x)=\Phi(x,t)\) is a
[[fiber-bundles/diffeomorphism|diffeomorphism]] and
\(\Phi_0=\operatorname{id}_N\). Two subsets or
[[differential-geometry/embedded-submanifold|embedded submanifolds]]
\(A_0,A_1\subseteq N\) are ambiently isotopic if some ambient isotopy
satisfies \(\Phi_1(A_0)=A_1\). For parametrized embeddings
\(f_0,f_1:M\to N\), one instead requires
\(f_1=\Phi_1\circ f_0\). Thus ambient isotopy deforms the whole surrounding
manifold, not only the object lying inside it, and records equivalence through
motions of that ambient space.

## Relation to smooth isotopy

An ambient isotopy produces a
[[differential-geometry/smooth-isotopy|smooth isotopy]] of every embedding by
\(f_t=\Phi_t\circ f_0\). The converse is the content of an isotopy-extension
theorem and requires hypotheses, typically including properness or compact
support conditions.

## Examples and invariants

Rotating \(\mathbb R^2\) continuously about the origin is an ambient isotopy.
A compactly supported time-dependent
[[fiber-bundles/vector-field|vector field]] integrates, on its time interval,
to an ambient isotopy through its flow. Ambiently isotopic embedded
submanifolds have diffeomorphic complements, so embeddings whose complements
have different topological invariants cannot be ambiently isotopic.

## Conventions and scope

**Warning.** Some authors call any path in the
[[differential-geometry/diffeomorphism-group|diffeomorphism group]] an
ambient isotopy without requiring the initial map to be the identity. Such a
path can be normalized by composing with \(\Phi_0^{-1}\). In noncompact
manifolds, “ambient isotopy” does not by itself mean compactly supported or
proper; those conditions must be stated separately.

## References

1. Morris W. Hirsch, *Differential Topology*, Graduate Texts in Mathematics 33, Springer, 1976. [DOI record](https://doi.org/10.1007/978-1-4684-9449-5). Relevant: Chapter 8, isotopies and isotopy extension.
2. Victor Guillemin and Alan Pollack, *Differential Topology*, AMS Chelsea Publishing, 2010 reprint. [DOI record](https://doi.org/10.1090/chel/370). Relevant: isotopy and ambient deformation of submanifolds.
