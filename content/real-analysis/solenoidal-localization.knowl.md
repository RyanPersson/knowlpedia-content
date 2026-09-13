+++
id = "real-analysis/solenoidal-localization"
title = "Localization through a vector potential"
kind = "construction"
summary = "Taking the curl after inserting a cutoff preserves divergence freedom and produces an explicit cutoff correction."
aliases = ["solenoidal cutoff", "divergence-free localization"]
domains = ["real-analysis"]
section_mode = "progressive"
prerequisites = ["real-analysis/vector-potential", "real-analysis/cutoff-function", "real-analysis/curl", "real-analysis/gradient", "linear-algebra/cross-product", "real-analysis/divergence-free-field"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

Let \(A\) be a smooth [[real-analysis/vector-potential|vector potential]] on \(U\subseteq\mathbb R^3\), with \(u=\nabla\times A\), and let \(\chi\) be a smooth cutoff with compact support in \(U\). Define
\[
v=\nabla\times(\chi A)
=\chi u+\nabla\chi\times A,
\]
extending \(\chi A\) by zero outside \(U\). Then \(v\) is smooth, compactly supported, and [[real-analysis/divergence-free-field|divergence free]] on \(\mathbb R^3\).

## Plateau and correction

Where \(\chi=1\) on a neighborhood, \(v=u\). The term \(\nabla\chi\times A\) is the cutoff correction and is supported where the cutoff varies. The identity follows by the componentwise product rule for curl, while \(\nabla\cdot v=0\) follows from the divergence-of-curl identity.

## Why the potential is needed

Multiplication alone gives \(\nabla\cdot(\chi u)=\nabla\chi\cdot u\), which is not usually zero. The construction assumes a potential on the region being localized; existence of a global potential can depend on the domain.
