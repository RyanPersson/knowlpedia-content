+++
id = "operator-algebras/gns-uniqueness"
title = "GNS uniqueness theorem"
kind = "theorem"
summary = "Any two cyclic representations implementing the same positive functional are canonically unitarily equivalent."
aliases = ["uniqueness of the GNS representation", "GNS representation theorem"]
domains = ["operator-algebras"]
section_mode = "progressive"
prerequisites = ["operator-algebras/positive-linear-functional", "operator-algebras/cstar-algebra", "operator-algebras/gns-construction", "operator-algebras/cyclic-cstar-representation", "operator-algebras/unitary-equivalence-cstar-representations"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(\varphi\) be a
[[operator-algebras/positive-linear-functional|positive linear functional]]
on a [[operator-algebras/cstar-algebra|\(C^*\)-algebra]] \(A\). Suppose
\((\pi_\varphi,H_\varphi,\xi_\varphi)\) is the cyclic triple produced by the
[[operator-algebras/gns-construction|GNS construction]], and
\((\rho,K,\eta)\) is any
[[operator-algebras/cyclic-cstar-representation|cyclic representation]]
satisfying
\[
\varphi(a)=\langle\rho(a)\eta,\eta\rangle
\qquad(a\in A).
\]
Then there is a unique unitary \(U:H_\varphi\to K\) such that
\[
U\xi_\varphi=\eta
\quad\text{and}\quad
U\pi_\varphi(a)=\rho(a)U
\qquad(a\in A).
\]
Thus the pointed cyclic representation implementing \(\varphi\) is unique up
to canonical
[[operator-algebras/unitary-equivalence-cstar-representations|unitary equivalence]].
The uniqueness is pointed: both the representation and its distinguished
cyclic vector are part of the data.

## Construction of the unitary

On the dense cyclic subspace, define
\[
U_0\bigl(\pi_\varphi(a)\xi_\varphi\bigr)=\rho(a)\eta.
\]
The implementing identities show that both sides have the same inner
products:
\[
\langle\pi_\varphi(a)\xi_\varphi,\pi_\varphi(b)\xi_\varphi\rangle
=\varphi(b^*a)
=\langle\rho(a)\eta,\rho(b)\eta\rangle.
\]
Hence \(U_0\) is well defined and isometric. Cyclicity makes its range dense,
so it extends to the asserted unitary. Density also proves uniqueness.

## Why the pointing matters

The theorem is stronger than unpointed unitary equivalence: the implementing
unitary must carry the distinguished cyclic vector to the other distinguished
vector. An unpointed cyclic representation may have many
[[operator-algebras/cyclic-vector|cyclic vectors]] that induce different
positive functionals. Likewise, dropping cyclicity permits extra orthogonal
summands and destroys uniqueness.

## References

1. Gerard J. Murphy, *C*-Algebras and Operator Theory, Academic Press, 1990. [DOI record](https://doi.org/10.1016/C2009-0-22289-6). Relevant: §3.3, especially Theorem 3.3.3 on existence and uniqueness of the cyclic representation.
2. Gert K. Pedersen, *C*-Algebras and Their Automorphism Groups, 2nd ed., Academic Press, 2018. [DOI record](https://doi.org/10.1016/C2016-0-03431-9). Relevant: Chapter 3 on positive functionals and cyclic representations.
