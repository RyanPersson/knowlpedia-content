+++
id = "operator-algebras/state-space"
title = "State space of a C*-algebra"
kind = "definition"
summary = "The convex set of all positive norm-one functionals on a C*-algebra."
aliases = ["S(A)", "C*-state space"]
domains = ["operator-algebras"]
section_mode = "progressive"
+++

Let \(A\) be a [[operator-algebras/cstar-algebra|\(C^*\)-algebra]]. Its **state
space**, denoted \(S(A)\), is the set of all
[[operator-algebras/state-cstar-algebra|states]] on \(A\):
\[
S(A)=\{\varphi\in A^*:\varphi\geq 0,\ \|\varphi\|=1\}.
\]
It is a [[convex-analysis/convex-set|convex set]] in the Banach dual \(A^*\),
equipped most often with the
[[functional-analysis/weak-star-topology|weak-star topology]]. If \(A\) is
unital, the norm condition is equivalent to \(\varphi(1_A)=1\), and \(S(A)\)
is weak-star compact. For nonunital \(A\), \(S(A)\) need not be weak-star
compact, although the [[operator-algebras/positive-linear-functional|positive functionals]] of norm at most one form a
weak-star [[topology/compact-set|compact set]].

## Convex structure

A state is [[operator-algebras/pure-state-cstar-algebra|pure]] exactly when it
is an extreme point of \(S(A)\). Thus convex decompositions express mixed
states as combinations of other states. The Krein–Milman theorem implies that,
for unital \(A\), the compact convex set \(S(A)\) is the closed
[[convex-analysis/convex-hull|convex hull]] of its pure states. This convex
viewpoint is developed systematically in
[Alfsen and Shultz, Part I](https://doi.org/10.1007/978-1-4612-0147-2).

## Standard examples

For \(A=C(X)\) with \(X\) compact Hausdorff, \(S(A)\) is the space of Radon
[[probability/probability-measure|probability measures]] on \(X\); its pure
states are the point masses. For \(A=M_n(\mathbb C)\), states correspond to
positive matrices \(\rho\) with \(\operatorname{Tr}(\rho)=1\) through
\(\varphi(a)=\operatorname{Tr}(\rho a)\). The pure states correspond to
rank-one \(\rho\).

## Topological caveat

**Warning.** Weak-star compactness of the state space requires unitality in
this formulation. For example, states on \(C_0(X)\) can converge weak-star to
zero as their mass escapes to infinity. The weak-star compact replacement for
a nonunital algebra is its quasi-state space
\(\{\varphi\in A^*:\varphi\geq0,\ \|\varphi\|\leq1\}\).

## References

1. Gerard J. Murphy, *C*-Algebras and Operator Theory*, Academic Press, 1990. [DOI record](https://doi.org/10.1016/C2009-0-22289-6). Relevant: §3.2 on states, convexity, and weak-star compactness.
2. Erik M. Alfsen and Frederic W. Shultz, *State Spaces of Operator Algebras: Basic Theory, Orientations, and C*-Products*, Birkhäuser, 2001. [DOI record](https://doi.org/10.1007/978-1-4612-0147-2). Relevant: Part I on compact convex state spaces.
