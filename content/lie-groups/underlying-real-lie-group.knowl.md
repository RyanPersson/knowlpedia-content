+++
id = "lie-groups/underlying-real-lie-group"
title = "Underlying real Lie group"
kind = "construction"
summary = "The real Lie group obtained from a complex Lie group by forgetting its complex structure."
aliases = ["realification of a complex Lie group", "restriction of scalars of a complex Lie group"]
domains = ["lie-groups"]
prerequisites = ["lie-groups/complex-lie-group", "differential-geometry/complex-manifold", "algebra-groups/group-homomorphism"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

If \(G\) is a [[lie-groups/complex-lie-group|complex Lie group]], its **underlying real Lie group**, denoted \(G_{\mathbb R}\), has the same points, multiplication, and inversion as \(G\), but its [[differential-geometry/complex-manifold|complex manifold]] is regarded as a smooth real manifold. If \(\dim_{\mathbb C}G=n\), then
\[
\dim_{\mathbb R}G_{\mathbb R}=2n.
\]
This construction is functorial on holomorphic [[algebra-groups/group-homomorphism|group homomorphisms]].

## What is and is not forgotten

Only the scalar field of the manifold charts is forgotten. The topology and abstract group are unchanged. The original complex structure can be retained as an additional left-invariant endomorphism \(J\) of the real [[fiber-bundles/tangent-bundle|tangent bundle]] satisfying \(J^2=-1\), but \(J\) is not part of \(G_{\mathbb R}\) and is not generally determined by the underlying real Lie group.

The construction differs from choosing a **real form** \(H\) of \(G\), for which \(\operatorname{Lie}(H)\otimes_{\mathbb R}\mathbb C\cong\operatorname{Lie}_{\mathbb C}(G)\). It also differs from [[algebraic-geometry-foundations/weil-restriction|Weil restriction]], although analytification of \(\operatorname{Res}_{\mathbb C/\mathbb R}X\) recovers an underlying real Lie group in standard algebraic examples.

## References

1. Anthony W. Knapp, *Lie Groups Beyond an Introduction*, 2nd ed., Birkhäuser, 2002, Chapter I. [Publisher record](https://doi.org/10.1007/978-1-4757-2453-0).
2. Sigurdur Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces*, AMS, 2001, Chapter II. [Publisher record](https://doi.org/10.1090/gsm/034).
