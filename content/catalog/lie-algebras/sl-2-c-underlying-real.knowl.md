+++
id = "catalog/lie-algebras/sl-2-c-underlying-real"
title = "sl(2,C) with scalars restricted to R"
kind = "definition"
summary = "sl(2,C) with scalars restricted to R."
aliases = ["sl(2,C) with scalars restricted to R"]
domains = ["catalog", "lie-groups"]
section_mode = "progressive"
prerequisites = ["lie-groups/underlying-real-lie-algebra", "lie-groups/lie-algebra", "lie-groups/example-sl2c"]
dependency_heuristic = "semantic-catalog-review-v1"
dependency_review_count = 1
+++

The **underlying real [[lie-groups/lie-algebra|Lie algebra]]** \(\mathfrak{sl}(2,\mathbb C)_{\mathbb R}\) has the same trace-zero complex matrices and commutator bracket as [[lie-groups/example-sl2c|\(\mathfrak{sl}(2,\mathbb C)\)]], but only real scalar multiplication is part of its structure.

## Retained and forgotten structure

Its real dimension is 6. Multiplication by \(i\) is an additional real-linear operator \(J\) with \(J^2=-1\) and \([JX,Y]=J[X,Y]=[X,JY]\). A real-linear homomorphism is complex-linear precisely when it commutes with \(J\).

This operation differs from taking a real form: \(\mathfrak{sl}(2,\mathbb R)\) has only 3 real dimensions.
