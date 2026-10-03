+++
id = "catalog/lie-algebras/strict-upper-n-r"
title = "Strictly upper triangular Lie algebra nn(R)"
kind = "definition"
summary = "Strictly upper triangular Lie algebra nn(R)."
aliases = ["Strictly upper triangular Lie algebra nn(R)"]
domains = ["catalog", "lie-groups"]
section_mode = "progressive"
prerequisites = ["lie-groups/lie-algebra", "linear-algebra/matrix"]
dependency_heuristic = "semantic-catalog-review-v1"
dependency_review_count = 1
+++

For an integer \(n\geq1\), the **strictly upper triangular real matrix [[lie-groups/lie-algebra|Lie algebra]]** \(\mathfrak n_{n}(\mathbb R)\) consists of matrices \(X=(x_{ij})\in M_{n}(\mathbb R)\) with \(x_{ij}=0\text{ whenever }i\geq j\), using the commutator bracket.

## Basis and nilpotency

The basis \(E_{ij}\ (i<j)\) has brackets \([E_{ij},E_{kl}]=\delta_{jk}E_{il}-\delta_{li}E_{kj}\). Each additional commutator moves entries farther above the diagonal. For \(n\geq2\) the nilpotency class is exactly \(n-1\): successive commutators of \(E_{12},E_{23},\ldots,E_{n-1,n}\) reach \(E_{1n}\).
