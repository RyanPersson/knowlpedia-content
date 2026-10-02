+++
id = "catalog/arithmetic/f3-polynomials"
title = "Polynomial ring F_3[t]"
kind = "definition"
summary = "Polynomial ring F_3[t] with its specified scalar field, operations, and categorical structure."
aliases = []
domains = ["catalog", "algebra-rings"]
section_mode = "progressive"
prerequisites = ["catalog/arithmetic/f3"]
dependency_heuristic = "catalog-definition-core-reviewed-v1"
dependency_review_count = 0
+++

The **polynomial ring \(\mathbb F_3[t]\)** is the set of finite sums \(\sum_{j=0}^m a_jt^j\) over the [[catalog/arithmetic/f3|finite field \(\mathbb F_3\)]], with coefficientwise addition and multiplication determined by \(t^it^j=t^{i+j}\).

## Ring and maps

Its units are the nonzero constants. A unital \(\mathbb F_3\)-algebra map from this ring to another commutative unital \(\mathbb F_3\)-algebra is determined by the chosen image of \(t\). Its fraction field is [[catalog/arithmetic/f3-rational-functions|\(\mathbb F_3(t)\)]].

## Completion is extra structure

The formal power-series ring [[catalog/arithmetic/f3-power-series|\(\mathbb F_3[\![t]\!]\)]] arises by \(t\)-adic completion, not by merely allowing a larger finite polynomial degree. This record is algebraic and does not impose a topology.
