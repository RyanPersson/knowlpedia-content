+++
id = "measure-theory/reference-subtracted-integral"
title = "Reference-subtracted integral"
kind = "definition"
summary = "An integral of a difference that may converge even when neither term is separately integrable."
aliases = ["subtracted radial moment", "renormalized moment relative to a reference"]
domains = ["measure-theory"]
section_mode = "progressive"
prerequisites = ["measure-theory/lebesgue-integrable-function", "measure-theory/lebesgue-integral", "measure-theory/measurable-function", "real-analysis/weighted-radial-moment"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 2
+++

If measurable functions \(f,g\) satisfy \(f-g\in L^1(\mu)\), the **reference-subtracted integral** is
\[
\int(f-g)\,d\mu.
\]
The reference \(g\) is part of its definition. This [[measure-theory/lebesgue-integral|integral]] can exist even if \(f\) and \(g\) are not separately integrable.

## Weighted moments and comparisons

A reference-subtracted radial moment has the form \(\int_0^\infty r^e(f-f_{\rm ref})\,dr\), with absolute integrability of the weighted difference required. It is not the undefined subtraction of two divergent integrals. Changing the reference by an integrable function changes the result by its integral. Such a prescribed subtraction is also distinct from choosing a regularization procedure without an explicit reference.
