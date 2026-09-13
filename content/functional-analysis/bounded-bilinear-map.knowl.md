+++
id = "functional-analysis/bounded-bilinear-map"
title = "Bounded bilinear map between normed spaces"
kind = "definition"
summary = "A bilinear map satisfying a uniform product bound on its output norm."
aliases = ["bounded multiplication", "bilinear norm estimate"]
domains = ["functional-analysis"]
section_mode = "progressive"
prerequisites = ["algebra-modules/bilinear-map", "linear-algebra/normed-vector-space"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

A [[algebra-modules/bilinear-map|bilinear map]] \(B:X\times Y\to Z\) between normed spaces is **bounded** if
\[
\|B(x,y)\|_Z\le C\|x\|_X\|y\|_Y
\]
for a fixed finite \(C\). This is equivalent to joint continuity. The least such constant is its bilinear operator norm.

## Difference estimate

Bilinearity gives
\[
B(x,y)-B(\widetilde x,\widetilde y)
=B(x-\widetilde x,y)+B(\widetilde x,y-\widetilde y).
\]
Thus the quadratic map \(Q(x)=B(x,x)\) satisfies
\(\|Q(x)-Q(y)\|\le C(\|x\|+\|y\|)\|x-y\|\).
It is Lipschitz on every norm ball. When \(B\) is an algebra multiplication, this is a bounded-multiplication estimate; associativity and completeness are separate requirements for a Banach algebra.
