+++
id = "algebra-groups/symmetric-group"
title = "Symmetric group"
kind = "definition"
summary = "The group of all bijections of a set under composition."
aliases = []
domains = ["algebra-groups"]
section_mode = "progressive"
prerequisites = ["algebra-groups/group", "shared-foundations/bijective-function", "shared-foundations/finite-permutation"]
+++

The **symmetric group** \(\operatorname{Sym}(X)\) of a set \(X\) consists of all [[shared-foundations/bijective-function|bijections]] \(X\to X\), with composition as multiplication. For \(X=\{1,\ldots,n\}\), it is denoted \(S_n\) and has \(n!\) elements.

## Action and labeling

Evaluation gives the natural action on \(X\). A labeling of an arbitrary \(n\)-element set identifies \(\operatorname{Sym}(X)\) with \(S_n\); the identification depends on the labeling.

## Probability interpretation

With uniform probability on a finite set, its measure-preserving automorphism group is exactly its symmetric group. With nonuniform positive weights, only permutations preserving the weights are allowed.
