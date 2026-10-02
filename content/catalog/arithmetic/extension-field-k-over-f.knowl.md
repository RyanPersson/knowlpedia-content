+++
id = "catalog/arithmetic/extension-field-k-over-f"
title = "Specified extension field K/F"
kind = "definition"
summary = "Specified extension field K/F with its specified scalar field, operations, and categorical structure."
aliases = []
domains = ["catalog", "algebra-fields-galois"]
section_mode = "progressive"
prerequisites = ["algebra-fields-galois/field-extension"]
dependency_heuristic = "catalog-definition-core-reviewed-v1"
dependency_review_count = 0
+++

A **specified extension field \(K/F\)** is a [[algebra-fields-galois/field-extension|field extension]] with a fixed injective unital homomorphism \(\iota:F\hookrightarrow K\). The catalogue object is the field \(K\), together with this scalar inclusion; its \(F\)-action is \(a\cdot x=\iota(a)x\).

## Two vector-space views

The field is one-dimensional over itself. Its dimension over \(F\) is \([K:F]\), possibly infinite. The \(K\)-linear endomorphisms are multiplications by elements of \(K\); \(F\)-linear maps have fewer scalar constraints and may form a much larger ring.

## Two algebra views

The only unital \(K\)-algebra endomorphism of \(K\) is the identity, since every element is a scalar. Its unital \(F\)-algebra automorphisms are precisely [[algebra-fields-galois/field-automorphism|field automorphisms]] fixing \(\iota(F)\) pointwise. This distinction depends on the specified inclusion, not on the carrier set alone.
