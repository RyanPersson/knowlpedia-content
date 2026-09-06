+++
id = "operator-algebras/pure-state-cstar-algebra"
title = "Pure state of a C*-algebra"
kind = "definition"
summary = "A state that is an extreme point of the C*-algebra's state space."
aliases = ["extreme state", "C*-pure state"]
domains = ["operator-algebras"]
section_mode = "progressive"
prerequisites = ["operator-algebras/cstar-algebra", "operator-algebras/state-cstar-algebra", "operator-algebras/state-space"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(A\) be a [[operator-algebras/cstar-algebra|\(C^*\)-algebra]]. A
[[operator-algebras/state-cstar-algebra|state]] \(\varphi\in S(A)\) is
**pure** if it is an extreme point of the
[[operator-algebras/state-space|state space]]: whenever
\[
\varphi=t\psi+(1-t)\chi
\]
for states \(\psi,\chi\in S(A)\) and \(0<t<1\), one must have
\(\psi=\chi=\varphi\). Thus purity means that \(\varphi\) admits no nontrivial
convex decomposition into other states. It is a convex-geometric condition,
not a continuity or nondegeneracy condition; in particular, purity does not
mean normality or faithfulness.

## GNS characterization

A state is pure if and only if its
[[operator-algebras/gns-construction|GNS representation]] is irreducible. This
connects extreme points of \(S(A)\) with
[[operator-algebras/irreducible-cstar-representation|irreducible
representations]] of \(A\). The equivalence is a theorem, not an alternative
convention for the definition.

## Standard examples

For \(A=C_0(X)\), pure states are evaluations \(f\mapsto f(x)\) at points
\(x\in X\); equivalently, they are the [[operator-algebras/character-cstar-algebra|multiplicative states]]. On
\(M_n(\mathbb C)\), pure states are
[[operator-algebras/vector-state|vector states]]
\(\varphi(a)=\langle a\xi,\xi\rangle\) for unit vectors \(\xi\), or
[[quantum-foundations/density-operator|density matrices]] of rank one. A
density matrix of rank greater than one gives a mixed, not pure, state.

## Distinctions

**Warning.** A pure state on a noncommutative \(C^*\)-algebra need not be
multiplicative. Nor need it be faithful: for \(n>1\), every pure state on
\(M_n(\mathbb C)\) vanishes on some nonzero positive matrix, even though its
GNS representation is irreducible and faithful. Normality is a separate
property defined only after a [[operator-algebras/von-neumann-algebra|von
Neumann algebra]] structure is specified.

## References

1. Gerard J. Murphy, *C*-Algebras and Operator Theory*, Academic Press, 1990. [DOI record](https://doi.org/10.1016/C2009-0-22289-6). Relevant: §3.3 on pure states and irreducible GNS representations.
2. Gert K. Pedersen, *C*-Algebras and Their Automorphism Groups*, 2nd ed., Academic Press, 2018. [DOI record](https://doi.org/10.1016/C2016-0-03431-9). Relevant: §3.3 on states and purity.
