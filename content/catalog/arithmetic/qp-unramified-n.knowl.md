+++
id = "catalog/arithmetic/qp-unramified-n"
title = "Unramified degree n extension of Q_p"
kind = "definition"
summary = "Unramified degree n extension of Q_p with its specified scalar field, operations, and categorical structure."
aliases = []
domains = ["catalog", "algebra-fields-galois"]
section_mode = "progressive"
prerequisites = ["algebra-fields-galois/unramified-extension-local", "algebra-commutative/residue-field"]
dependency_heuristic = "catalog-definition-core-reviewed-v1"
dependency_review_count = 0
+++

For a prime \(p\) and \(n\ge1\), **\(\mathbb Q_p^{(n),\mathrm{ur}}\)** denotes an [[algebra-fields-galois/unramified-extension-local|unramified extension]] of \(\mathbb Q_p\) of degree \(n\), equipped with the extended \(p\)-adic topology. Its ramification index is one and its [[algebra-commutative/residue-field|residue field]] is \(\mathbb F_{p^n}\).

## Choice and notation

Within a chosen [[algebra-fields-galois/algebraic-closure|algebraic closure]] of \(\mathbb Q_p\), there is a unique such subextension of each positive degree. The displayed notation is local catalogue notation; the algebraic closure and embedding are parameters when needed. Its valuation ring has uniformizer \(p\).

## Degree-one boundary

Degree one recovers [[catalog/arithmetic/qp|\(\mathbb Q_p\)]]. Higher-degree examples give characteristic-zero [[algebra-fields-galois/local-field|local fields]] with the same residue-field sizes as the equal-characteristic Laurent-series examples; these fields are not isomorphic because their characteristics differ.

## References

1. [J. S. Milne, Algebraic Number Theory](https://www.jmilne.org/math/CourseNotes/ANT.pdf), Chapter 7, Proposition 7.50, unramified extensions, pp. 127–128.
