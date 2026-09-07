+++
id = "topology/singular-homology-group"
title = "Singular homology group"
kind = "definition"
summary = "The homology of the singular chain complex of a topological space."
aliases = ["singular homology", "singular homology group"]
domains = ["topology"]
section_mode = "progressive"
prerequisites = ["topology/singular-chain-complex", "algebra-groups/abelian-group", "algebra-homological/homology-module"]
dependency_heuristic = "dependency-structure-review-v1"
dependency_review_count = 2
+++

Let \(X\) be a [[topology/topological-space|topological space]] and \(A\) an abelian group. The **\(n\)-th singular homology group** of \(X\) with coefficients in \(A\) is
\[
H_n(X;A):=H_n(C_\bullet(X;A))
=\ker(\partial_n)/\operatorname{im}(\partial_{n+1}),
\]
where \(C_\bullet(X;A)\) is the [[topology/singular-chain-complex|singular chain complex]]. Its elements are cycles modulo boundaries.

## Functoriality

A continuous map \(f:X\to Y\) induces \(f_*:H_n(X;A)\to H_n(Y;A)\), and homotopic maps induce the same map. Thus singular homology is a covariant homotopy invariant.

## Reduced and relative forms

The reduced group \(\widetilde H_n(X;A)\) modifies degree zero using the augmentation to \(A\). For a pair \(B\subseteq X\), the relative group is defined from the quotient chain complex and is recorded separately as [[topology/relative-singular-homology|relative singular homology]].

## Reference

See Allen Hatcher, *Algebraic Topology*, Chapter 2, [author-hosted book](https://pi.math.cornell.edu/~hatcher/AT/ATpage.html).
