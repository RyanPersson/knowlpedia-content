+++
id = "catalog/lie-algebras/strict-upper-2-r"
title = "Strictly upper triangular Lie algebra n2(R)"
kind = "definition"
summary = "Strictly upper triangular Lie algebra n2(R)."
aliases = ["Strictly upper triangular Lie algebra n2(R)"]
domains = ["catalog", "lie-groups"]
section_mode = "progressive"
prerequisites = ["lie-groups/lie-algebra", "linear-algebra/matrix"]
dependency_heuristic = "semantic-catalog-review-v1"
dependency_review_count = 1
+++

The **strictly upper triangular real matrix [[lie-groups/lie-algebra|Lie algebra]]** \(\mathfrak n_{2}(\mathbb R)\) consists of matrices \(X=(x_{ij})\in M_{2}(\mathbb R)\) with \(x_{ij}=0\text{ whenever }i\geq j\), using the commutator bracket.

## Basis and nilpotency

The basis \(E_{ij}\ (i<j)\) has brackets \([E_{ij},E_{kl}]=\delta_{jk}E_{il}-\delta_{li}E_{kj}\). Each additional commutator moves entries farther above the diagonal. In size two this is the one-dimensional abelian algebra spanned by \(E_{12}\).
