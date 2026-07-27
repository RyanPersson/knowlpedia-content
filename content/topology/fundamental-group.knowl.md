+++
id = "topology/fundamental-group"
title = "Fundamental group"
kind = "definition"
summary = "The group of based loops in a space modulo endpoint-preserving homotopy."
aliases = ["pi_1", "homotopy group in degree one"]
domains = ["topology"]
section_mode = "progressive"
+++

Let \(X\) be a [[topology/topological-space|topological space]] with basepoint \(x_0\). A based loop is a [[topology/path|path]] \(\gamma:[0,1]\to X\) with \(\gamma(0)=\gamma(1)=x_0\). Two based loops are equivalent when they are joined by a continuous homotopy through based loops, keeping both endpoints fixed throughout. The **fundamental group**
\[
\pi_1(X,x_0)
\]
is the set of these [[shared-foundations/equivalence-class|equivalence classes]], with multiplication induced by concatenating loops. The constant loop is the identity, and reversing a loop gives its inverse. These operations are well defined on homotopy classes and make \(\pi_1(X,x_0)\) a [[algebra-groups/group|group]].

## Basepoint dependence

If \(x_0\) and \(x_1\) lie in the same path component, a path from \(x_0\) to \(x_1\) induces an isomorphism
\[
\pi_1(X,x_0)\cong\pi_1(X,x_1).
\]
Different choices of path can change this isomorphism by an [[algebra-groups/inner-automorphism|inner automorphism]]. Hence a path-connected space has a fundamental group well defined up to noncanonical isomorphism, while a specific basepoint and connecting paths matter for functorial constructions.

## Functoriality

A [[topology/continuous-map|continuous map]] \(f:X\to Y\) satisfying \(f(x_0)=y_0\) induces a [[algebra-groups/group-homomorphism|group homomorphism]]
\[
f_*:\pi_1(X,x_0)\to\pi_1(Y,y_0),
\qquad
[\gamma]\longmapsto[f\circ\gamma].
\]
Homotopic pointed maps induce the same homomorphism. In particular, a [[topology/homotopy-equivalence|homotopy equivalence]] induces an isomorphism of fundamental groups, subject to the usual basepoint choices.

## Examples

- Every nonempty convex subset of \(\mathbb R^n\) has trivial fundamental group.
- The circle satisfies \(\pi_1(S^1,1)\cong\mathbb Z\); the integer records winding number.
- The \(n\)-sphere has trivial fundamental group for \(n\ge2\).
- A bouquet of \(r\) circles has free fundamental group on \(r\) generators.

## Interpretation

The fundamental group measures the obstruction to continuously contracting based loops. It also governs connected covering spaces: under standard local hypotheses, connected coverings of \(X\) correspond to [[algebra-groups/conjugacy-class|conjugacy classes]] of subgroups of \(\pi_1(X,x_0)\). Because it can be nonabelian, it retains information that first homology discards.

## References

1. Allen Hatcher, *Algebraic Topology*, Cambridge University Press, 2002. [Author-hosted chapter record](https://pi.math.cornell.edu/~hatcher/AT/ATchapters.html). Relevant: Chapter 1, the fundamental group and covering spaces.
2. Edwin H. Spanier, *Algebraic Topology*, Springer, 1966. [DOI record](https://doi.org/10.1007/978-1-4684-9322-1). Relevant: fundamental groups and covering-space theory.
