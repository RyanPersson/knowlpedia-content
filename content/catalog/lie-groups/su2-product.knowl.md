+++
id = "catalog/lie-groups/su2-product"
title = "SU(2) × SU(2)"
kind = "definition"
summary = "SU(2) × SU(2) as a separately identified real Lie group, with its defining operations and dimension."
aliases = []
domains = ["catalog", "lie-groups"]
section_mode = "progressive"
prerequisites = ["lie-groups/example-su2", "lie-groups/product-lie-group"]
dependency_heuristic = "catalog-semantic-core-v1"
dependency_review_count = 1
+++

The [[lie-groups/product-lie-group|product Lie group]] \(\mathrm{SU}(2)\times\mathrm{SU}(2)\) has two copies of [[lie-groups/example-su2|\(\operatorname{SU}(2)\)]] as factors, with componentwise multiplication.

## Dimensions and structure

This group has real dimension \(6\). The two factors commute, and the manifold dimension is the sum of their dimensions. It is [[topology/simply-connected-space|simply connected]].

## Direct verification

Products carry componentwise multiplication and inversion and the [[differential-geometry/product-manifold|product manifold]] structure. Dimensions add, and the two projections and the inclusions of each factor are smooth homomorphisms.
