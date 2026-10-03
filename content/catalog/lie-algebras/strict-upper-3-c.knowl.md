+++
id = "catalog/lie-algebras/strict-upper-3-c"
title = "Strictly upper triangular Lie algebra n3(C)"
kind = "definition"
summary = "Strictly upper triangular Lie algebra n3(C)."
aliases = ["Strictly upper triangular Lie algebra n3(C)"]
domains = ["catalog", "lie-groups"]
section_mode = "progressive"
prerequisites = ["lie-groups/lie-algebra", "linear-algebra/matrix"]
dependency_heuristic = "semantic-catalog-review-v1"
dependency_review_count = 1
+++

The **strictly upper triangular complex matrix [[lie-groups/lie-algebra|Lie algebra]]** \(\mathfrak n_{3}(\mathbb C)\) consists of matrices \(X=(x_{ij})\in M_{3}(\mathbb C)\) with \(x_{ij}=0\text{ whenever }i\geq j\), using the commutator bracket.

## Basis and nilpotency

The basis \(E_{ij}\ (i<j)\) has brackets \([E_{ij},E_{kl}]=\delta_{jk}E_{il}-\delta_{li}E_{kj}\). Each additional commutator moves entries farther above the diagonal. In size three the only nonzero basic bracket is \([E_{12},E_{23}]=E_{13}\), giving the three-dimensional Heisenberg algebra.
