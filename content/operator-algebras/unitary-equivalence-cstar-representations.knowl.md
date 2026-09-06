+++
id = "operator-algebras/unitary-equivalence-cstar-representations"
title = "Unitary equivalence of C*-representations"
kind = "definition"
summary = "The equivalence relation on Hilbert-space representations implemented by a unitary intertwining operator."
aliases = ["equivalent *-representations"]
domains = ["operator-algebras", "representation-theory"]
section_mode = "progressive"
prerequisites = ["operator-algebras/cstar-representation", "functional-analysis/unitary-operator", "linear-algebra/inner-product", "shared-foundations/equivalence-relation"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(\pi:A\to\mathcal B(H_\pi)\) and
\(\rho:A\to\mathcal B(H_\rho)\) be
[[operator-algebras/cstar-representation|\(C^*\)-representations]] of the same
algebra. They are **unitarily equivalent** if there is a [[functional-analysis/unitary-operator|unitary operator]]
\(U:H_\pi\to H_\rho\) such that
\[
U\pi(a)=\rho(a)U\qquad(a\in A).
\]
Equivalently, \(\rho(a)=U\pi(a)U^*\) for every \(a\). The unitary \(U\) is an
intertwiner, and it identifies the representations together with their
Hilbert-space [[linear-algebra/inner-product|inner products]]. Similarity by a merely bounded invertible
operator is not the [[shared-foundations/equivalence-relation|equivalence relation]] defined here.

## Equivalence relation

Unitary equivalence is reflexive, symmetric, and transitive: use the identity,
\(U^*\), and composition of implementing unitaries, respectively. It is
therefore meaningful to classify representations by unitary-equivalence
classes rather than by chosen Hilbert-space realizations.

## Preserved structure

The intertwining relation carries invariant and cyclic subspaces from one
representation to the other. It also preserves kernels, faithfulness,
nondegeneracy, irreducibility, and multiplicities in direct-sum
decompositions. Moreover, their
[[operator-algebras/commutant|commutants]] satisfy
\[
U\pi(A)'U^*=\rho(A)',
\]
so they are spatially isomorphic.

## Pointed cyclic representations

For [[operator-algebras/cyclic-cstar-representation|cyclic representations]]
with pointed triples \((\pi,H,\xi)\) and \((\rho,K,\eta)\), equivalence of the
pointed triples additionally requires \(U\xi=\eta\). The uniqueness statement
in the [[operator-algebras/gns-construction|GNS construction]] is of this
stronger pointed form. Two unpointed representations can be unitarily
equivalent even when a chosen
[[operator-algebras/cyclic-vector|cyclic vector]] is not carried to another
chosen vector.

## References

1. Gerard J. Murphy, *C*-Algebras and Operator Theory*, Academic Press, 1990. [DOI record](https://doi.org/10.1016/C2009-0-22289-6). Relevant: Chapter 3 on representations and intertwiners.
2. Gert K. Pedersen, *C*-Algebras and Their Automorphism Groups, 2nd ed., Academic Press, 2018. [DOI record](https://doi.org/10.1016/C2016-0-03431-9). Relevant: Chapter 3 on unitary equivalence and cyclic representations.
