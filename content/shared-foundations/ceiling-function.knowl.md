+++
id = "shared-foundations/ceiling-function"
title = "Ceiling function"
kind = "definition"
summary = "The least integer not less than a real number."
aliases = ["ceiling", "ceil"]
domains = ["shared-foundations"]
section_mode = "progressive"
prerequisites = ["shared-foundations/floor-function"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For a real number \(x\), its **ceiling** \(\lceil x\rceil\) is the unique integer satisfying
\[
\lceil x\rceil-1<x\le\lceil x\rceil.
\]
Equivalently, \(\lceil x\rceil=-\lfloor-x\rfloor\), where the brackets on the right denote the [[shared-foundations/floor-function|floor]].

## Scale comparison

For \(x\ge1\),
\[
x\le\lceil x\rceil<x+1\le2x.
\]
Thus replacing a positive real frequency scale by its ceiling gives an integer scale with comparable size. For example, \(\lceil2.3\rceil=3\) and \(\lceil-2.3\rceil=-2\).
