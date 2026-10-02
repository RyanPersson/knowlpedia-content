+++
id = "catalog/arithmetic/base-field-f"
title = "Specified base field F"
kind = "definition"
summary = "Specified base field F with its specified scalar field, operations, and categorical structure."
aliases = []
domains = ["catalog", "algebra-fields-galois"]
section_mode = "progressive"
prerequisites = ["algebra-rings/field"]
dependency_heuristic = "catalog-definition-core-reviewed-v1"
dependency_review_count = 0
+++

A **specified base field \(F\)** is a [[algebra-rings/field|field]] carried as an explicit parameter of a categorical comparison. Its addition, multiplication, zero and unit are fixed; the symbol does not denote a universal field containing all the other catalogue fields.

## Keeping the parameter fixed

An \(F\)-linear map must commute with this specified scalar action. An \(F\)-algebra map must also preserve multiplication, and in a unital algebra category preserve the unit. Changing the parameter changes the category, so diagrams from different choices cannot be composed merely because their labels both say \(F\).
