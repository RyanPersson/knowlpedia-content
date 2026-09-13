+++
id = "real-analysis/smooth-extension"
title = "Smooth extension of a function"
kind = "definition"
summary = "A smooth function on a larger domain that agrees with the given function on its original domain."
aliases = []
domains = ["real-analysis"]
section_mode = "progressive"
prerequisites = ["real-analysis/class-ck-map", "shared-foundations/restriction-of-a-function"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

Let \(U\subseteq V\subseteq\mathbb R^n\) be open and \(f:U\to\mathbb R^m\) smooth. A **smooth extension of \(f\) to \(V\)** is a [[real-analysis/class-ck-map|smooth function]] \(F:V\to\mathbb R^m\) whose [[shared-foundations/restriction-of-a-function|restriction]] to \(U\) equals \(f\).

## Existence and nonuniqueness

An extension need not exist: \(1/t\) on \((0,1)\) has no continuous extension across zero. When one exists it need not be unique, since smooth functions supported in \(V\setminus\overline U\) may be added without changing the restriction.

The [[real-analysis/smooth-zero-extension|zero-extension criterion]] gives a useful sufficient condition across a flat boundary. [[real-analysis/borel-jet-extension|Borel's extension theorem]] concerns prescribing boundary derivatives; it does not assert that an arbitrary function on an open domain extends smoothly.
