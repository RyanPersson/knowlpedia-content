+++
id = "partial-differential-equations/harmonic-distribution"
title = "Harmonic distribution"
kind = "definition"
summary = "A distribution annihilated by the distributional Laplacian."
aliases = ["distributional harmonicity"]
domains = ["partial-differential-equations"]
section_mode = "progressive"
prerequisites = ["functional-analysis/distribution", "functional-analysis/distributional-derivative", "real-analysis/laplacian"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

A distribution \(h\) on an open set \(\Omega\subset\mathbb R^n\) is **harmonic in distributions** if \(\Delta h=0\), meaning
\[
\langle h,\Delta\varphi\rangle=0\qquad(\varphi\in C_c^\infty(\Omega)).
\]
The Laplacian is formed using [[functional-analysis/distributional-derivative|distributional derivatives]].

## Ambiguity of Poisson solutions

If \(-\Delta u=f=-\Delta v\), then \(u-v\) is harmonic in distributions. A nonzero constant is harmonic, so harmonicity alone does not force the difference to vanish. A global norm condition can remove this ambiguity. Every classical harmonic function gives an example of a harmonic distribution.
