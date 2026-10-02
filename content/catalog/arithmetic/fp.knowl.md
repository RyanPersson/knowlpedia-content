+++
id = "catalog/arithmetic/fp"
title = "Field F_p"
kind = "definition"
summary = "Field F_p with its specified scalar field, operations, and categorical structure."
aliases = []
domains = ["catalog", "algebra-fields-galois"]
section_mode = "progressive"
prerequisites = ["algebra-rings/field"]
dependency_heuristic = "catalog-definition-core-reviewed-v1"
dependency_review_count = 0
+++

For a prime \(p\), the **field \(\mathbb F_p\)** is the quotient [[algebra-rings/field|field]] \(\mathbb Z/p\mathbb Z\), with residue-class addition and multiplication.

## Operations and maps

Every nonzero residue has an inverse because p is prime. A unit-preserving field endomorphism fixes \(1\), hence every sum of copies of \(1\), and is therefore the identity. The zero map is allowed as a nonunital ring map, but never as a field map.

## Underlying groups

Its additive group is cyclic of order \(p\); its nonzero elements form a separate multiplicative group of order \(p-1\). These group structures must be selected explicitly before taking group Hom-sets.
