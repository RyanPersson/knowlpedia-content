+++
id = "partial-differential-equations/nonuniqueness"
title = "Nonuniqueness for an initial-value problem"
kind = "definition"
summary = "Two distinct solutions in the same stated class satisfy the same equation, data, and prescribed force."
aliases = []
domains = ["partial-differential-equations"]
section_mode = "progressive"
prerequisites = ["partial-differential-equations/initial-datum", "shared-foundations/function", "measure-theory/ae-equality"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

An initial-value problem is **nonunique in a specified solution class** if two distinct members of that class satisfy the same equation, [[partial-differential-equations/initial-datum|initial data]], boundary conditions, and prescribed force. Distinctness uses the class's equality convention: for measurable solutions it usually means failure of [[measure-theory/ae-equality|almost-everywhere equality]], whereas continuous [[shared-foundations/function|functions]] are compared pointwise.

## Quantifiers

Existence of a nonunique datum does not assert nonuniqueness for every datum. Two solutions with different forces do not prove nonuniqueness for a fixed forced problem. Enlarging the solution class can destroy uniqueness even when uniqueness holds in a smaller class.
