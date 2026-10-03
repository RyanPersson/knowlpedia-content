+++
id = "catalog/arithmetic/f2-power-series"
title = "Formal power series over F_2"
kind = "definition"
summary = "Formal power series over F_2 with its specified scalar field, operations, and categorical structure."
aliases = []
domains = ["catalog", "algebra-rings"]
section_mode = "progressive"
prerequisites = ["catalog/arithmetic/f2"]
dependency_heuristic = "catalog-definition-core-reviewed-v1"
dependency_review_count = 0
+++

The **formal power-series ring \(\mathbb F_2[\![t]\!]\)** consists of all series \(\sum_{j\ge0}a_jt^j\) over the [[catalog/arithmetic/f2|finite field \(\mathbb F_2\)]], with coefficientwise addition and convolution multiplication. It carries the \(t\)-adic topology, whose neighborhoods of zero are the ideals \(t^m\mathbb F_2[\![t]\!]\).

## Units, residue and completion

A series is invertible exactly when its constant coefficient is nonzero. This compact complete ring has [[algebra-rings/maximal-ideal|maximal ideal]] \((t)\) and [[algebra-commutative/residue-field|residue field]] \(\mathbb F_2\). It is the inverse limit of \(\mathbb F_2[t]/(t^m)\); inversion of \(t\) gives [[catalog/arithmetic/f2-laurent|\(\mathbb F_2((t))\)]].

## Polynomial comparison

The [[catalog/arithmetic/f2-polynomials|polynomial ring \(\mathbb F_2[t]\)]] is dense here, but it contains only finite sums. Infinite positive tails belong to the power-series ring and generally are not rational functions.

## References

1. [J. S. Milne, Algebraic Number Theory](https://www.jmilne.org/math/CourseNotes/ANT.pdf), Chapter 7, Theorem 7.23; Propositions 7.26, 7.46; Remark 7.49, pp. 115–127.
