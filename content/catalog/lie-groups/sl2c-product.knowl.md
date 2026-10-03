+++
id = "catalog/lie-groups/sl2c-product"
title = "SL(2,C) × SL(2,C)"
kind = "definition"
summary = "SL(2,C) × SL(2,C) as a separately identified complex Lie group, with its defining operations and dimension."
aliases = []
domains = ["catalog", "lie-groups"]
section_mode = "progressive"
prerequisites = ["lie-groups/product-lie-group", "lie-groups/sl2-complex-as-real-and-complex-lie-group"]
dependency_heuristic = "catalog-semantic-core-v1"
dependency_review_count = 1
+++

The [[lie-groups/product-lie-group|product Lie group]] \(\mathrm{SL}(2,\mathbb C)\times\mathrm{SL}(2,\mathbb C)\) has two copies of [[lie-groups/sl2-complex-as-real-and-complex-lie-group|\(\operatorname{SL}(2,\mathbb C)\)]] as factors, with componentwise multiplication.

## Dimensions and structure

This group has real dimension \(12\), complex dimension \(6\). The two factors commute, and the manifold dimension is the sum of their dimensions. It is [[topology/simply-connected-space|simply connected]].

Its [[lie-groups/complex-lie-group|complex Lie group]] structure uses holomorphic multiplication and inversion. Forgetting the complex structure gives the [[lie-groups/underlying-real-lie-group|underlying real Lie group]]; real and holomorphic homomorphisms belong to different categories.

## Direct verification

Products carry componentwise multiplication and inversion and the [[differential-geometry/product-manifold|product manifold]] structure. Dimensions add, and the two projections and the inclusions of each factor are smooth homomorphisms.
