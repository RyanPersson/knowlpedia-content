+++
id = "functional-analysis/closed-graph-theorem"
title = "Closed graph theorem"
kind = "theorem"
summary = "An everywhere-defined linear operator between Banach spaces is bounded when its graph is closed."
aliases = ["closed graph theorem for Banach spaces"]
domains = ["functional-analysis"]
section_mode = "progressive"
+++

Let \(X\) and \(Y\) be
[[linear-algebra/banach-space|Banach spaces]] over the same scalar field
\(\mathbb R\) or \(\mathbb C\), and let \(T:X\to Y\) be linear and defined on
all of \(X\). If \(T\) is a
[[functional-analysis/closed-linear-operator|closed linear operator]], then
\(T\) is bounded. Explicitly, closedness means that
\[
x_n\to x\text{ in }X,\quad Tx_n\to y\text{ in }Y
\quad\Longrightarrow\quad Tx=y.
\]
Thus a topological condition on the graph forces continuity, provided both
spaces are complete and the domain of \(T\) is all of \(X\)
[Conway, Chapter VI].

## Relation to the open mapping theorem

Give the graph \(\Gamma(T)\subseteq X\times Y\) the product norm. Closedness
makes \(\Gamma(T)\) a Banach space. The first-coordinate projection
\(\pi_X:\Gamma(T)\to X\) is a bounded linear bijection, so the
[[functional-analysis/open-mapping-theorem|open mapping theorem]] makes its
inverse bounded. Composing that inverse with the second-coordinate projection
shows that \(T\) is bounded.

## Domain-sensitive scope

The full-domain hypothesis is indispensable. On \(\ell^2\), let
\[
D(T)=\{x=(x_n): (nx_n)\in\ell^2\},\qquad Tx=(nx_n).
\]
This operator is closed and unbounded, but \(D(T)\) is a proper dense
subspace of \(\ell^2\). Such examples are the normal setting for unbounded
differential and spectral operators; their domains are part of their
definitions. Conversely, every
[[functional-analysis/bounded-linear-operator|bounded operator between normed spaces]] has a closed graph when the codomain is Hausdorff.

## References

1. John B. Conway, *A Course in Functional Analysis*, 2nd ed., Graduate Texts in Mathematics 96, Springer, 1990. [Springer DOI record](https://doi.org/10.1007/978-1-4757-4383-8). Relevant: Chapter VI, “Linear Operators on a Banach Space.”
2. Walter Rudin, *Functional Analysis*, 2nd ed., McGraw–Hill, 1991. [WorldCat record](https://search.worldcat.org/title/21163277). Relevant: Chapter 2, the closed graph theorem.
