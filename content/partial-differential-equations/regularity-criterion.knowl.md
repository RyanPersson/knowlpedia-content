+++
id = "partial-differential-equations/regularity-criterion"
title = "Regularity criterion"
kind = "definition"
summary = "A specified additional condition that implies a stated regularity or continuation conclusion for a solution class."
aliases = []
domains = ["partial-differential-equations"]
section_mode = "progressive"
prerequisites = ["partial-differential-equations/partial-differential-equation", "partial-differential-equations/classical-solution", "partial-differential-equations/maximal-existence-time"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

A **regularity criterion** for a [[partial-differential-equations/partial-differential-equation|PDE]] is a theorem of the form: every solution in a specified class that satisfies an additional condition has a stated regularity property, such as being a [[partial-differential-equations/classical-solution|classical solution]] on a region or admitting [[partial-differential-equations/maximal-existence-time|continuation]] beyond an endpoint. The criterion includes the equation, dimension, domain, force, solution class, and exact norm or geometric condition.

## Contrapositive

If a finite norm guarantees continuation, failure of that continuation forces failure of the norm condition, provided all other hypotheses still hold. Different norms or different solution classes cannot be substituted without a theorem.
