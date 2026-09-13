+++
id = "topology/flat-torus"
title = "Flat torus"
kind = "definition"
summary = "A Euclidean space modulo a full-rank lattice, with its quotient distance and local Euclidean coordinates."
aliases = ["unit flat torus", "Euclidean quotient torus"]
domains = ["topology"]
section_mode = "progressive"
prerequisites = ["linear-algebra/euclidean-lattice", "shared-foundations/quotient-set", "topology/metric-space", "linear-algebra/euclidean-norm"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For a [[linear-algebra/euclidean-lattice|full-rank lattice]] \(\Lambda\subset\mathbb R^n\), the **flat torus** \(\mathbb R^n/\Lambda\) consists of classes \([x]=x+\Lambda\) with distance
\[
d([x],[y])=\min_{\lambda\in\Lambda}|x-y-\lambda|.
\]
Discreteness makes the minimum well-defined, and the expression is independent of representatives. It is a metric: zero distance means equal classes, symmetry follows from \(-\Lambda=\Lambda\), and the Euclidean triangle inequality descends to the quotient.

## Local coordinates and normalization

Balls smaller than half the shortest nonzero lattice length have injective Euclidean lifts; still smaller balls preserve all pairwise Euclidean distances. These charts specify smooth functions and the local Euclidean geometry. A compact fundamental parallelepiped maps onto the torus. The **unit torus** is \(\mathbb T^n=\mathbb R^n/\mathbb Z^n\); an angular convention uses \(\mathbb R^n/(2\pi\mathbb Z)^n\). The related [[lie-groups/example-torus|torus as a Lie group]] emphasizes its group structure instead of this metric.
