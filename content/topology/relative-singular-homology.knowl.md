+++
id = "topology/relative-singular-homology"
title = "Relative singular homology"
kind = "definition"
summary = "Homology of the quotient singular chain complex of a pair of spaces."
aliases = ["relative homology", "relative singular homology"]
domains = ["topology"]
section_mode = "progressive"
prerequisites = ["topology/singular-chain-complex", "topology/singular-homology-group", "algebra-homological/homology-module"]
dependency_heuristic = "dependency-structure-review-v1"
dependency_review_count = 2
+++

Let \(B\subseteq X\) be a subspace of a topological space \(X\) and let \(A\) be an abelian group. The inclusion induces a subcomplex \(C_\bullet(B;A)\subseteq C_\bullet(X;A)\). The **relative singular chain complex** is
\[
C_\bullet(X,B;A):=C_\bullet(X;A)/C_\bullet(B;A),
\]
and the **relative singular homology group** is
\[
H_n(X,B;A):=H_n(C_\bullet(X,B;A)).
\]
Thus a relative cycle is a chain in \(X\) whose boundary lies in \(B\), modulo chains in \(B\) and relative boundaries.

## Functoriality and exact sequence

A map of pairs \(f:(X,B)\to(Y,D)\) induces maps on relative homology. The short exact sequence of chain complexes
\[
0\to C_\bullet(B;A)\to C_\bullet(X;A)\to C_\bullet(X,B;A)\to0
\]
gives the long exact sequence of the pair, relating \(H_n(B;A)\), \(H_n(X;A)\), and \(H_n(X,B;A)\).

## Reference

See Allen Hatcher, *Algebraic Topology*, Chapter 2, [author-hosted book](https://pi.math.cornell.edu/~hatcher/AT/ATpage.html).
