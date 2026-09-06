+++
id = "discrete-structures/nearest-neighbor-zd"
title = "Nearest-neighbor adjacency on Z^d"
kind = "knowl"
summary = "The standard notion of adjacency on the integer lattice where points differ by 1 in one coordinate."
aliases = ["nearest-neighbor-zd", "Nearest-neighbor adjacency on Z^d"]
domains = ["discrete-structures"]
prerequisites = ["discrete-structures/lattice-zd"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
legacy_source_path = "discrete-structures/nearest-neighbor-zd.md"
+++

On the [[discrete-structures/lattice-zd|integer lattice]] \(\mathbb Z^d\), two sites \(x,y\) are **nearest neighbors**, written \(x\sim y\), if they differ by \(1\) in exactly one coordinate and agree in all others.

Equivalently, using the \(\ell^1\) norm,
\[
x\sim y \quad\Longleftrightarrow\quad \|x-y\|_1 = 1,
\]
where \(\|z\|_1 := \sum_{i=1}^d |z_i|\).

A convenient characterization is:
\[
y = x \pm e_i \text{ for some } i\in\{1,\dots,d\},
\]
where \(e_i\) is the \(i\)-th standard basis vector.

## Remarks

**Degree.** Each site in \(\mathbb{Z}^d\) has exactly \(2d\) nearest neighbors.

This adjacency relation turns \(\mathbb{Z}^d\) into an infinite graph, sometimes called the **nearest-neighbor lattice graph**.
