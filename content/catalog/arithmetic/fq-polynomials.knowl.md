+++
id = "catalog/arithmetic/fq-polynomials"
title = "Polynomial ring F_q[t]"
kind = "definition"
summary = "Polynomial ring F_q[t] with its specified scalar field, operations, and categorical structure."
aliases = []
domains = ["catalog", "algebra-rings"]
section_mode = "progressive"
prerequisites = ["catalog/arithmetic/fpk"]
dependency_heuristic = "catalog-definition-core-reviewed-v1"
dependency_review_count = 0
+++

The **polynomial ring \(\mathbb F_q[t]\)** is the set of finite sums \(\sum_{j=0}^m a_jt^j\) over the [[catalog/arithmetic/fpk|finite field \(\mathbb F_q\)]], with coefficientwise addition and multiplication determined by \(t^it^j=t^{i+j}\).

## Ring and maps

Its units are the nonzero constants. A unital \(\mathbb F_q\)-algebra map from this ring to another commutative unital \(\mathbb F_q\)-algebra is determined by the chosen image of \(t\). Its fraction field is [[catalog/arithmetic/fq-rational-functions|\(\mathbb F_q(t)\)]].

## Completion is extra structure

The formal power-series ring [[catalog/arithmetic/fq-power-series|\(\mathbb F_q[\![t]\!]\)]] arises by \(t\)-adic completion, not by merely allowing a larger finite polynomial degree. This record is algebraic and does not impose a topology.
