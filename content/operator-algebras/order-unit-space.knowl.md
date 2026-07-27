+++
id = "operator-algebras/order-unit-space"
title = "Order-unit space"
kind = "definition"
summary = "A real ordered vector space with an Archimedean positive element that bounds every vector."
aliases = ["Archimedean order-unit space", "AOU space"]
domains = ["operator-algebras", "functional-analysis", "convex-analysis"]
section_mode = "progressive"
+++

An **Archimedean order-unit space** is a real [[linear-algebra/vector-space|vector space]] \(A\) with a
proper convex cone \(A_+\) and an element \(e\in A_+\) such that:

1. for every \(a\in A\), some \(r>0\) satisfies
   \(-re\leq a\leq re\); and
2. if \(a+\varepsilon e\in A_+\) for every \(\varepsilon>0\), then
   \(a\in A_+\).

The cone defines \(a\leq b\) by \(b-a\in A_+\). The element \(e\) is the
**order unit**, and the second condition is Archimedeanness. The associated
order-unit norm is
\[
\|a\|_e=\inf\{r>0:-re\leq a\leq re\}.
\]

## States and the order

A **state** on \((A,e)\) is a positive real linear functional
\(\mu:A\to\mathbb R\) satisfying \(\mu(e)=1\). States have norm one for the
order-unit norm and detect its order:
\[
a\in A_+\quad\Longleftrightarrow\quad
\mu(a)\geq0\ \text{for every state }\mu.
\]
The state space is convex and carries the [[functional-analysis/weak-star-topology|weak-star topology]] inherited from
the dual of the normed space \(A\).

## C*-algebra example

If \(B\) is a unital
[[operator-algebras/cstar-algebra|\(C^*\)-algebra]], its self-adjoint part
\(B_{\mathrm{sa}}\), with the
[[operator-algebras/positive-cone|positive cone]] and order unit \(1_B\), is
an Archimedean order-unit space. Its order-unit norm is the restricted
\(C^*\)-norm. Complex
[[operator-algebras/state-cstar-algebra|\(C^*\)-algebra states]] correspond
exactly to the real order-unit states on \(B_{\mathrm{sa}}\).

## Conventions and scope

Some authors say “order-unit space” without requiring Archimedeanness and then
pass to an Archimedeanization. This knowl includes that axiom. Completeness in
\(\|\cdot\|_e\) is not part of the definition. An operator system has
additional compatible matrix-level cones, so it is more than an order-unit
space.

## References

1. Marc A. Rieffel, *Metrics on State Spaces*, Memoirs of the American Mathematical Society 168, no. 796, 2004. [AMS DOI record](https://doi.org/10.1090/memo/0796). Relevant: §2 on order-unit spaces, states, and order-unit norms.
2. Erik M. Alfsen, *Compact Convex Sets and Boundary Integrals*, Springer, 1971. [Publisher DOI record](https://doi.org/10.1007/978-3-642-65009-3). Relevant: Chapters I–II on ordered vector spaces, order units, and state spaces.
