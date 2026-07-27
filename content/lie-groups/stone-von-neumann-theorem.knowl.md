+++
id = "lie-groups/stone-von-neumann-theorem"
title = "Stone–von Neumann theorem"
kind = "theorem"
summary = "Irreducible unitary representations of the real Heisenberg group with a fixed nontrivial central character are unitarily equivalent."
aliases = ["uniqueness of the Schrödinger representation", "Heisenberg representation theorem"]
domains = ["lie-groups", "harmonic-analysis", "functional-analysis"]
section_mode = "progressive"
+++

Let \(H_n\) be the real [[lie-groups/heisenberg-group|Heisenberg group]] with
center \(Z=\{(0,0,z):z\in\mathbb R\}\), and fix
\(\lambda\in\mathbb R\setminus\{0\}\). The **Stone–von Neumann theorem**
states that every [[lie-groups/irreducible-unitary-representation|irreducible]]
[[lie-groups/strongly-continuous-unitary-representation|continuous unitary representation]]
\(\pi\) of \(H_n\) satisfying
\[
\pi(0,0,z)=e^{i\lambda z}I
\]
is unitarily equivalent to the Schrödinger representation on
\(L^2(\mathbb R^n)\). Thus fixing a nontrivial character of the center fixes
the [[algebra-representation-theory/irreducible-representation|irreducible representation]] up to unitary equivalence; among representations
with nontrivial central action, varying the character gives the family indexed
by \(\lambda\ne0\).

## Schrödinger model

For the convention
\[
(x,y,z)(x',y',z')=(x+x',y+y',
z+z'+\tfrac12(x\cdot y'-y\cdot x')),
\]
one Schrödinger model is
\[
[\pi_\lambda(x,y,z)f](u)
=e^{i\lambda(z+y\cdot u+\frac12x\cdot y)}f(u+x).
\]
Translations and modulations therefore fail to commute by exactly the central
phase encoded by the Heisenberg group law. The uniqueness theorem and this
model are developed in
[Folland, §1.5](https://doi.org/10.1515/9781400882427).

## Why the hypotheses matter

Irreducibility is essential: arbitrary representations with the same central
character can be direct sums or direct integrals of copies of the Schrödinger
model. Nontriviality of the central character is also essential. When
\(\lambda=0\), the representation factors through the abelian quotient
\(H_n/Z\), which has many one-dimensional characters rather than one
distinguished irreducible representation.

## Weyl-relations formulation

An equivalent formulation starts with strongly continuous one-parameter
unitary groups satisfying the Weyl commutation relations and an irreducibility
condition. The theorem says that such a finite-dimensional system of canonical
commutation relations is unitarily equivalent to the standard position and
momentum model. This exponentiated formulation avoids the domain ambiguities
of writing commutators of unbounded operators
[Hall, Chapter 14](https://doi.org/10.1007/978-1-4614-7116-5).

## References

1. Gerald B. Folland, *Harmonic Analysis in Phase Space*, Annals of Mathematics Studies 122, Princeton University Press, 1989. [DOI record for the electronic edition](https://doi.org/10.1515/9781400882427). Relevant: §1.5 on the Stone–von Neumann theorem.
2. Brian C. Hall, *Quantum Theory for Mathematicians*, Graduate Texts in Mathematics 267, Springer, 2013. [DOI record](https://doi.org/10.1007/978-1-4614-7116-5). Relevant: Chapter 14 on the canonical commutation relations and Stone–von Neumann theorem.
