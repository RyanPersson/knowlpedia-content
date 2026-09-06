+++
id = "algebra-groups/p-group-nontrivial-center-corollary"
title = "Finite p-Group Has Nontrivial Center"
kind = "knowl"
summary = "The center of a nontrivial finite p-group has order divisible by p."
aliases = ["p-group-nontrivial-center-corollary", "Finite p-Group Has Nontrivial Center"]
domains = ["algebra-groups"]
legacy_source_path = "algebra-groups/p-group-nontrivial-center-corollary.md"
prerequisites = ["algebra-groups/p-group", "algebra-groups/center-of-group"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(p\) be a prime and let \(G\) be a finite [[algebra-groups/p-group|\(p\)-group]] of order \(p^n\), where \(n\ge 1\). Then the [[algebra-groups/center-of-group|center]] \(Z(G)\) is nontrivial. More precisely,
\[
p\mid |Z(G)|.
\]

## Examples

- If \(G\) is abelian, then \(Z(G)=G\).
- For \(D_8=\langle r,s\mid r^4=s^2=e,\ srs=r^{-1}\rangle\), one has \(Z(D_8)=\{e,r^2\}\).

## Remarks

This follows from the [[algebra-groups/class-equation|class equation]]: every noncentral [[algebra-groups/conjugacy-class|conjugacy class]] has cardinality divisible by \(p\), so \(|Z(G)|\equiv |G|\equiv 0\pmod p\).
