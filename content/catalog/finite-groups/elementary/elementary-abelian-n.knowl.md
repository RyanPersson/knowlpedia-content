+++
id = "catalog/finite-groups/elementary/elementary-abelian-n"
title = "Elementary abelian group C_p^n"
kind = "definition"
summary = "Additive group of a finite vector space over the prime field."
aliases = []
domains = ["catalog", "algebra-groups"]
prerequisites = ["algebra-groups/group", "algebra-groups/direct-product-groups", "catalog/finite-groups/elementary/cyclic-p"]
dependency_heuristic = "finite-elementary-semantic-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(p\) be prime and let \(n\geq1\) be an integer. The **elementary abelian group \(C_p^{n}\)** is the additive [[algebra-groups/group|group]] of \(\mathbb F_p^{n}\), with coordinatewise addition. Equivalently it is the [[algebra-groups/direct-product-groups|direct product]] of \(n\) copies of the [[catalog/finite-groups/elementary/cyclic-p|cyclic group of order \(p\)]].

## Order and simplicity

Its order is \(p^{n}\), and every nonzero element has order \(p\). The case \(n=1\) is cyclic of prime order and simple. For \(n>1\), a one-dimensional subspace is proper nontrivial normal, so simplicity fails.

## Structure being selected

This record selects the additive group structure. [[linear-algebra/linear-map|Linear maps]] over \(\mathbb F_p\) and [[algebra-groups/group-homomorphism|group homomorphisms]] between elementary abelian \(p\)-groups agree, because repeated addition supplies scalar multiplication by every element of the prime field.
