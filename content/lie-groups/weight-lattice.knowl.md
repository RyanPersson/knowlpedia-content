+++
id = "lie-groups/weight-lattice"
title = "Weight lattice"
kind = "definition"
summary = "The lattice of vectors pairing integrally with every coroot."
aliases = ["integral weight lattice", "weight lattice P", "lattice of integral weights"]
domains = ["lie-groups", "representation-theory"]
section_mode = "progressive"
+++

Let \(\Phi\subset E\) be a crystallographic [[lie-groups/root-system|root system]], with coroots \(\alpha^\vee=2\alpha/(\alpha,\alpha)\). Its **weight lattice** is
\[
P=P(\Phi):=
\{\lambda\in E:\langle\lambda,\alpha^\vee\rangle\in\mathbb Z
\text{ for every }\alpha\in\Phi\}.
\]
Equivalently, if \(\alpha_1,\ldots,\alpha_r\) are the [[lie-groups/simple-root|simple roots]] and \(\omega_1,\ldots,\omega_r\) are the fundamental weights defined by
\[
\langle\omega_i,\alpha_j^\vee\rangle=\delta_{ij},
\]
then
\[
P=\mathbb Z\omega_1\oplus\cdots\oplus\mathbb Z\omega_r.
\]

## Dominant weights and representations

A weight \(\lambda\in P\) is **dominant** when
\[
\langle\lambda,\alpha_i^\vee\rangle\geq0
\quad\text{for every simple root }\alpha_i.
\]
The [[lie-groups/highest-weight-theorem|highest-weight theorem]] identifies dominant elements of \(P\) with finite-dimensional [[algebra-representation-theory/irreducible-representation|irreducible representations]] of the complex [[lie-groups/semisimple-lie-algebra|semisimple Lie algebra]], and with irreducible representations of its [[lie-groups/simply-connected-lie-group|simply connected]] group.

The [[lie-groups/root-lattice|root lattice]] satisfies \(Q\subseteq P\), and \(P/Q\) is finite. This quotient governs the possible central isogeny forms; choosing which intermediate lattice occurs is additional group-level data not specified by the Lie algebra alone.

## Which weights belong to a Lie group?

The abstract weight lattice \(P\) is the largest lattice allowed by the root datum. For a particular connected semisimple group \(G\) with maximal torus \(T\), the actual character lattice satisfies
\[
Q\subseteq X^*(T)\subseteq P.
\]
An integral Lie-algebra [[lie-groups/highest-weight|highest weight]] exponentiates to a representation of \(G\) precisely when it lies in \(X^*(T)\). Hence all of \(P\) occurs for the simply connected form, while only \(Q\) occurs for the adjoint form.

For example, type \(A_1\) has \(P=\mathbb Z\omega\) and \(Q=2\mathbb Z\omega\). Every nonnegative multiple of \(\omega\) defines an \(SU(2)\)-representation, whereas only the even multiples descend to \(SO(3)\).

## Terminology caution

“A [[lie-groups/weight-of-a-representation|weight of a representation]]” is an element that actually occurs as a simultaneous eigenvalue. The weight lattice is the ambient lattice of all integral candidates; most of its elements need not occur in a fixed representation.

## References

1. James E. Humphreys, *Introduction to Lie Algebras and Representation Theory*, Springer, 1972, §§13 and 21. [Publisher record](https://doi.org/10.1007/978-1-4684-9444-2).
2. Brian C. Hall, *Lie Groups, Lie Algebras, and Representations*, 2nd ed., Springer, 2015, Chapters 8 and 12. [Publisher record](https://doi.org/10.1007/978-3-319-13467-3).
