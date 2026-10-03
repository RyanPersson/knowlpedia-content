+++
id = "catalog/finite-groups/elementary/elementary-abelian-2"
title = "Elementary abelian group C_p^2"
kind = "definition"
summary = "Additive group of a finite vector space over the prime field."
aliases = []
domains = ["catalog", "algebra-groups"]
prerequisites = ["algebra-groups/group", "algebra-groups/direct-product-groups", "catalog/finite-groups/elementary/cyclic-p"]
dependency_heuristic = "finite-elementary-semantic-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(p\) be prime. The **elementary abelian group \(C_p^{2}\)** is the additive [[algebra-groups/group|group]] of \(\mathbb F_p^{2}\), with coordinatewise addition. Equivalently it is the [[algebra-groups/direct-product-groups|direct product]] of \(2\) copies of the [[catalog/finite-groups/elementary/cyclic-p|cyclic group of order \(p\)]].

## Order and simplicity

Its order is \(p^{2}\), and every nonzero element has order \(p\). Any one-coordinate subspace is a proper nontrivial subgroup. Because the group is abelian, that subgroup is normal, so the group is not simple.

## Structure being selected

This record selects the additive group structure. [[linear-algebra/linear-map|Linear maps]] over \(\mathbb F_p\) and [[algebra-groups/group-homomorphism|group homomorphisms]] between elementary abelian \(p\)-groups agree, because repeated addition supplies scalar multiplication by every element of the prime field.
