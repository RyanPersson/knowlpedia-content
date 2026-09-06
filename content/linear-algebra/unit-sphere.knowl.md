+++
id = "linear-algebra/unit-sphere"
title = "Unit sphere of a normed space"
kind = "knowl"
summary = "The set of vectors having norm exactly one."
aliases = ["unit sphere", "unit sphere of a normed space"]
domains = ["linear-algebra", "topology"]
prerequisites = ["linear-algebra/normed-vector-space", "linear-algebra/inner-product"]
dependency_review_count = 1
+++

For a [[linear-algebra/normed-vector-space|normed vector space]] \(E\), its **unit sphere** is
\[
S_E=\{x\in E:\lVert x\rVert=1\}.
\]
It is the boundary of the closed unit ball \(\{x:\lVert x\rVert\le1\}\). The term “sphere” refers to the given norm: unless the norm comes from an [[linear-algebra/inner-product|inner product]], \(S_E\) need not be round in Euclidean coordinates.

Every nonzero vector is a positive scalar multiple of a unique point of \(S_E\), namely \(x/\lVert x\rVert\).
