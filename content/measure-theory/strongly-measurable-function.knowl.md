+++
id = "measure-theory/strongly-measurable-function"
title = "Strongly measurable Banach-valued function"
kind = "definition"
summary = "A Banach-valued function approximable almost everywhere in norm by measurable simple functions."
aliases = ["strong measurability"]
domains = ["measure-theory"]
section_mode = "progressive"
prerequisites = ["linear-algebra/banach-space", "measure-theory/simple-function", "measure-theory/almost-everywhere", "topology/convergent-sequence"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

On a measure space \(X\), a function \(f:X\to B\), with \(B\) a Banach space, is **strongly measurable** if there are measurable simple functions \(s_n:X\to B\) such that \(\|s_n(x)-f(x)\|_B\to0\) outside a measurable null set. A Banach-valued simple function has finite range and is written \(\sum_jb_j\mathbf1_{E_j}\) with measurable \(E_j\).

## Integral norms

Strong measurability makes \(x\mapsto\|f(x)\|_B\) measurable up to null-set modification, as a pointwise limit of the measurable scalar norms of the approximations. If the measure is not complete, work with a measurable representative or its completion. Together with integrability of this norm, it characterizes [[measure-theory/bochner-integral|Bochner integrability]].
