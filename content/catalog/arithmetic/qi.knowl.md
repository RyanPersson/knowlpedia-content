+++
id = "catalog/arithmetic/qi"
title = "Gaussian rational field"
kind = "definition"
summary = "A specific quadratic extension of the rational field."
aliases = []
domains = ["catalog", "algebra-fields-galois"]
section_mode = "progressive"
prerequisites = ["algebra-fields-galois/field-extension"]
dependency_heuristic = "catalog-definition-core-reviewed-v1"
dependency_review_count = 0
+++

The **Gaussian rational field** is the [[algebra-fields-galois/field-extension|field extension]]
\[
\mathbb Q(i)=\mathbb Q[x]/(x^2+1)=\{a+bi:a,b\in\mathbb Q\},
\]
with addition and multiplication induced by the displayed quadratic relation.

## Scalar structure

Here \(i^2=-1\), and conjugation sends \(a+bi\) to \(a-bi\). The subring with integral coordinates is the [[catalog/arithmetic/gaussian-integers|Gaussian integer ring]].

## Maps and coordinates

A rational-linear endomorphism is any two-by-two rational matrix in the basis \(1,\alpha\), where \(\alpha\) is the displayed quadratic generator. A unit-preserving rational-algebra map must send \(\alpha\) to a root of its defining polynomial, so there are precisely the identity and conjugation. The invertible linear maps form \(\mathrm{GL}_2(\mathbb Q)\), a much larger group.
