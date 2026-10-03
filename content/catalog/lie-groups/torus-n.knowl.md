+++
id = "catalog/lie-groups/torus-n"
title = "Torus T^n"
kind = "definition"
summary = "Torus T^n as a separately identified real Lie group, with its defining operations and dimension."
aliases = []
domains = ["catalog", "lie-groups"]
section_mode = "progressive"
prerequisites = ["fiber-bundles/lie-group"]
dependency_heuristic = "catalog-semantic-core-v1"
dependency_review_count = 1
+++

For every integer \(n\ge1\), the real [[fiber-bundles/lie-group|Lie group]] \(\mathbb T^{n}\) is \(U(1)^{n}\) with coordinatewise multiplication; equivalently it is \(\mathbb R^{n}/(2\pi\mathbb Z)^{n}\) with addition.

## Dimensions and structure

This group has real dimension \(n\). It is compact, connected and abelian. Its [[lie-groups/universal-covering-group|universal covering group]] is additive \(\mathbb R^{n}\). The complex multiplicative group has a different real dimension and is noncompact.

## Direct verification

Coordinatewise multiplication and conjugation preserve the unit-circle equations. Each circle contributes one real dimension; the exponential map from Rⁿ has kernel 2πZⁿ.
