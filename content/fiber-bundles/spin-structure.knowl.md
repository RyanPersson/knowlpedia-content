+++
id = "fiber-bundles/spin-structure"
title = "Spin structure"
kind = "definition"
summary = "A lift of the oriented orthonormal frame bundle through the double covering Spin(n) to SO(n)."
aliases = ["spin lift of the frame bundle", "principal Spin bundle"]
domains = ["fiber-bundles", "differential-geometry", "topology"]
prerequisites = ["fiber-bundles/special-orthonormal-frame-bundle-reduction", "fiber-bundles/bundle-map", "lie-groups/spin-group", "algebra-groups/group-action"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \((M,g)\) be an oriented Riemannian \(n\)-manifold, let \(P_{\mathrm{SO}}(M)\) be its [[fiber-bundles/special-orthonormal-frame-bundle-reduction|oriented orthonormal frame bundle]], and let \(\lambda:\mathrm{Spin}(n)\to\mathrm{SO}(n)\) be the double covering. A **spin structure** on \(M\) is a principal \(\mathrm{Spin}(n)\)-bundle \(P_{\mathrm{Spin}}(M)\to M\) together with a [[fiber-bundles/bundle-map|bundle map]]
\[
\Phi:P_{\mathrm{Spin}}(M)\longrightarrow P_{\mathrm{SO}}(M)
\]
over \(M\) satisfying \(\Phi(pg)=\Phi(p)\lambda(g)\). Thus \(\Phi\) lifts each oriented orthonormal frame through the [[lie-groups/spin-group|spin group]] in a way compatible with the [[algebra-groups/group-action|group actions]].

## Existence and classification

An oriented manifold admits a spin structure exactly when the second [[fiber-bundles/stiefel-whitney-class|Stiefel–Whitney class]] of its [[fiber-bundles/tangent-bundle|tangent bundle]] vanishes:
\[
w_2(TM)=0.
\]
When spin structures exist, their isomorphism classes form a torsor for \(H^1(M;\mathbb Z/2)\); there is generally no preferred origin in this torsor.

The Riemannian definition uses orthonormal frames, but existence and equivalence do not depend on the chosen metric: changing the metric canonically transports the lifting problem to another [[fiber-bundles/oriented-frame|oriented frame]] reduction.

## Associated geometry

A spin structure lifts the Levi-Civita connection to \(P_{\mathrm{Spin}}(M)\). Associating a spin representation produces the [[differential-geometry/spinor-bundle|spinor bundle]], and composing its covariant derivative with Clifford multiplication gives the [[noncommutative-geometry/dirac-operator|Dirac operator]]. The spin structure is additional global data: an orientation and Riemannian metric do not by themselves choose one.

## Examples and non-examples

The standard oriented \(\mathbb R^n\) has a spin structure obtained from its trivial oriented orthonormal frame bundle. Every oriented surface is spin; its spin structures form a torsor for \(H^1(M;\mathbb Z/2)\). Complex [[algebraic-geometry-foundations/projective-space|projective space]] \(\mathbb{CP}^2\) is oriented but not spin because \(w_2(T\mathbb{CP}^2)\neq0\). The latter computation follows from the relation between Chern and Stiefel–Whitney classes.

## References

1. H. Blaine Lawson Jr. and Marie-Louise Michelsohn, *Spin Geometry*, Princeton University Press, 1989. [Publisher record](https://doi.org/10.1515/9781400883912). Relevant: Chapter II, especially §2, spin structures and their obstruction.
2. John W. Milnor and James D. Stasheff, *Characteristic Classes*, Princeton University Press, 1974. [Publisher record](https://doi.org/10.1515/9781400881826). Relevant: Chapter 14, spin characteristic classes and examples.
