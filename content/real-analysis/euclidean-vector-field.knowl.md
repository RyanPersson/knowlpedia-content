+++
id = "real-analysis/euclidean-vector-field"
title = "Vector field on a Euclidean open set"
kind = "definition"
summary = "A vector-valued function assigning an ambient vector to each point of a Euclidean open set."
aliases = ["Euclidean vector field", "vector-valued field"]
domains = ["real-analysis"]
section_mode = "progressive"
prerequisites = ["shared-foundations/function", "linear-algebra/euclidean-space", "topology/open-set"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

A **vector field** on an [[topology/open-set|open set]] \(U\subseteq\mathbb R^n\) is a map \(u:U\to\mathbb R^n\). In Cartesian coordinates it is written \(u=(u_1,\ldots,u_n)\). The word “field” alone imposes no regularity: continuity, differentiability, measurability or integrability must be specified.

## Time and regularity

A time-dependent field is a map \((t,x)\mapsto u(t,x)\). A [[real-analysis/class-ck-map|smooth field]] has smooth Cartesian components. In a moving orthonormal basis, its scalar components can satisfy different derivative formulas because the basis itself varies.

## Geometric interpretation

Identifying every tangent space of \(U\) with \(\mathbb R^n\) identifies a smooth Euclidean field with a [[fiber-bundles/vector-field|smooth tangent vector field]]. The elementary definition here does not require a choice of manifold charts.
