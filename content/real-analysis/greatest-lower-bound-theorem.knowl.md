+++
id = "real-analysis/greatest-lower-bound-theorem"
title = "Greatest Lower Bound Theorem"
kind = "knowl"
summary = "Every nonempty subset of the real numbers that is bounded below has a real infimum."
aliases = ["greatest-lower-bound-theorem", "Greatest Lower Bound Theorem"]
domains = ["real-analysis"]
prerequisites = ["real-analysis/bounded-below"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
legacy_source_path = "real-analysis/greatest-lower-bound-theorem.md"
+++

If \(E\subseteq\mathbb R\) is nonempty and [[real-analysis/bounded-below|bounded below]], then its greatest lower bound \(\inf E\) exists in \(\mathbb R\).

## Remarks

This is the "lower" counterpart to the [[real-analysis/least-upper-bound-theorem|least upper bound theorem]] and follows immediately by applying the [[real-analysis/supremum|supremum]] property to \(-E=\{-x:x\in E\}\).
