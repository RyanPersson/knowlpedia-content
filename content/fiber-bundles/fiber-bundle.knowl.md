+++
id = "fiber-bundles/fiber-bundle"
title = "Fiber bundle"
kind = "definition"
summary = "A bundle that is locally a product over its base with a fixed model fiber."
aliases = ["fiber bundle", "fibre bundle", "topological fiber bundle", "locally trivial bundle"]
domains = ["fiber-bundles", "topology"]
section_mode = "progressive"
prerequisites = ["fiber-bundles/bundle", "topology/open-cover", "topology/homeomorphism", "topology/product-topology"]
+++

A **fiber bundle** with nonempty model fiber \(F\) is a [[fiber-bundles/bundle|bundle]] \(\pi:E\to B\), with \(F\) a topological space, for which there is an [[topology/open-cover|open cover]] \(\{U_i\}\) of \(B\) and [[topology/homeomorphism|homeomorphisms]]
\[
\Phi_i:\pi^{-1}(U_i)\longrightarrow U_i\times F,
\qquad \operatorname{pr}_1\circ\Phi_i=\pi|_{\pi^{-1}(U_i)}.
\]
Each product carries the [[topology/product-topology|product topology]]. These maps are **local trivializations**: they identify the entire bundle over \(U_i\) with a product while preserving its projection to the base.

## Fibers and smooth bundles

Restricting \(\Phi_i\) over a point \(b\) gives a homeomorphism \(E_b\cong F\). Such an identification depends on a choice of trivialization. Having homeomorphic fibers alone does not supply local trivializations.

For smooth manifolds and diffeomorphic local product charts, the corresponding notion is a [[fiber-bundles/smooth-fiber-bundle|smooth fiber bundle]]. Forgetting smoothness gives a fiber bundle in the topological sense defined here.

## Examples

The projection \(B\times F\to B\) has a single global trivialization. A [[fiber-bundles/vector-bundle|vector bundle]] is locally a product with a vector space and has additional linear compatibility. A [[fiber-bundles/topological-principal-bundle|topological principal bundle]] has a group as its model fiber and an action compatible with its trivializations.

## References

1. Ralph L. Cohen, *The Topology of Fiber Bundles*, Chapter 1, Definition 1.1. [Author-hosted notes](https://math.stanford.edu/~ralph/fiber.pdf). The definition here does not require the base to be connected or pointed.
