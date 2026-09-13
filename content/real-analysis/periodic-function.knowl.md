+++
id = "real-analysis/periodic-function"
title = "Periodic function"
kind = "definition"
summary = "A function unchanged by a specified nonzero translation."
aliases = []
domains = ["real-analysis"]
section_mode = "progressive"
prerequisites = ["shared-foundations/function", "linear-algebra/euclidean-space"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

A [[shared-foundations/function|function]] \(f:\mathbb R^d\to Y\) has **period** \(p\in\mathbb R^d\setminus\{0\}\) if \(f(x+p)=f(x)\) for every \(x\). In one dimension a positive period \(L\) gives an \(L\)-periodic function. The least positive period, when one exists, is called the fundamental period.

## Several coordinates

A function is \(\mathbb Z^d\)-periodic if every standard basis vector is a period, equivalently \(f(x+m)=f(x)\) for all \(m\in\mathbb Z^d\). It is determined by one unit cell, with compatible boundary values. For measurable functions, periodicity may instead be imposed almost everywhere; that convention must be stated.

Different variables of \(f(\theta,H)\) may have different periods. Periodicity in an auxiliary coordinate \(H\) does not imply periodicity of a physical field until the map used to evaluate \(H\) is specified. A constant function has every nonzero period and no least positive one.
