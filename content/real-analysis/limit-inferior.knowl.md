+++
id = "real-analysis/limit-inferior"
title = "Limit inferior"
kind = "knowl"
summary = "The supremum of the infima of the tails of an extended-real sequence."
aliases = ["limit-inferior", "Limit inferior"]
domains = ["real-analysis"]
prerequisites = []
dependency_review_count = 1
legacy_source_path = "real-analysis/limit-inferior.md"
+++

The **limit inferior** of a sequence \((a_n)_{n\ge1}\) of extended real numbers is
\[
\liminf_{n\to\infty} a_n \;=\; \sup_{n\ge 1}\,\inf_{k\ge n} a_k,
\]
where the supremum and infima are taken in \([-\infty,+\infty]\).

## Remarks

The tail infima form a nondecreasing sequence, so their extended-real supremum is always defined. Together with the [[real-analysis/limit-superior|limit superior]], the limit inferior describes asymptotic subsequential behavior.
