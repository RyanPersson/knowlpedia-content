+++
id = "algebra-groups/finite-group"
title = "Finite group"
kind = "definition"
summary = "A group whose underlying set has finitely many elements."
aliases = ["finite group"]
domains = ["algebra-groups"]
section_mode = "progressive"
prerequisites = ["algebra-groups/group", "shared-foundations/finite-set"]
dependency_heuristic = "finite-groups-semantic-review-v1"
dependency_review_count = 1
+++

A **finite group** is a [[algebra-groups/group|group]] \(G\) whose underlying set is a [[shared-foundations/finite-set|finite set]]. Its **order**, denoted \(|G|\), is the number of its elements. In particular, the trivial group has order \(1\).

## Examples and classification

The additive group \(\mathbb Z/n\mathbb Z\) has order \(n\), for every integer \(n\geq1\). The [[algebra-groups/symmetric-group|symmetric group]] \(S_n\) has order \(n!\).

The [[algebra-groups/classification-finite-simple-groups|classification of finite simple groups]] applies to the finite groups having no proper nontrivial [[algebra-groups/normal-subgroup|normal subgroup]] and having order greater than one. General finite groups need not be simple; the [finite-group table](/catalog/finite-groups/table/) includes both kinds.

## References

- P. J. Cameron, [Group Theory revision notes](https://maths.qmul.ac.uk/~pjc/MTHM024/gtrev.pdf), §1.1, p. 2: finite groups and their orders.
