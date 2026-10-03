+++
id = "catalog/arithmetic/quadratic-number-field"
title = "Quadratic number field Q(sqrt(d))"
kind = "definition"
summary = "Quadratic number field Q(sqrt(d)) with its specified scalar field, operations, and categorical structure."
aliases = []
domains = ["catalog", "algebra-fields-galois"]
section_mode = "progressive"
prerequisites = ["shared-foundations/square-free-integer", "algebra-fields-galois/field-extension"]
dependency_heuristic = "catalog-definition-core-reviewed-v1"
dependency_review_count = 0
+++

For a [[shared-foundations/square-free-integer|squarefree integer]] \(d\ne0,1\), the **quadratic number field** \(\mathbb Q(\sqrt d)\) is the quotient [[algebra-fields-galois/field-extension|field extension]] \(\mathbb Q[x]/(x^2-d)\). Its elements have unique expressions \(a+b\sqrt d\) with \(a,b\in\mathbb Q\).

## Real and imaginary cases

For \(d>0\) the field has two real embeddings; for \(d<0\) it has a pair of conjugate complex embeddings and no real embedding. In both cases the nonidentity rational-field automorphism negates \(\sqrt d\).

## Catalogue scope

This is a parameterized family, not a single chosen field. A specific value of \(d\) and an embedding must be supplied when a relationship depends on that choice. The case \(d=1\) is excluded because the quotient by \(x^2-1\) is not a field.
