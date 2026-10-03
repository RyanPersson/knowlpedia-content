+++
id = "catalog/arithmetic/qsqrt2"
title = "Real quadratic field Q(sqrt(2))"
kind = "definition"
summary = "A specific quadratic extension of the rational field."
aliases = []
domains = ["catalog", "algebra-fields-galois"]
section_mode = "progressive"
prerequisites = ["algebra-fields-galois/field-extension"]
dependency_heuristic = "catalog-definition-core-reviewed-v1"
dependency_review_count = 0
+++

The **Real quadratic field Q(sqrt(2))** is the [[algebra-fields-galois/field-extension|field extension]]
\[
\mathbb Q(\sqrt2)=\mathbb Q[x]/(x^2-2)=\{a+b\sqrt2:a,b\in\mathbb Q\},
\]
with addition and multiplication induced by the displayed quadratic relation.

## Scalar structure

The two real embeddings send \(\sqrt2\) to \(\sqrt2\) and \(-\sqrt2\). This is a field of rational dimension two; its chosen real embedding does not make it a real vector space.

## Maps and coordinates

A rational-linear endomorphism is any two-by-two rational matrix in the basis \(1,\alpha\), where \(\alpha\) is the displayed quadratic generator. A unit-preserving rational-algebra map must send \(\alpha\) to a root of its defining polynomial, so there are precisely the identity and conjugation. The invertible linear maps form \(\mathrm{GL}_2(\mathbb Q)\), a much larger group.
