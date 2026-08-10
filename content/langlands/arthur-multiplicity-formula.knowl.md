+++
id = "langlands/arthur-multiplicity-formula"
title = "Arthur multiplicity formula"
kind = "knowl"
summary = "The component-group character formula selecting representations and multiplicities in a global Arthur packet."
aliases = ["Arthur's multiplicity formula", "automorphic multiplicity formula", "A-packet multiplicity formula"]
domains = ["langlands", "representation-theory", "number-theory"]
section_mode = "progressive"
+++

Let \(\psi\) be a discrete global [[langlands/arthur-parameter|Arthur
parameter]], let \(\mathcal S_\psi\) be its finite component group, and let
\(\epsilon_\psi:\mathcal S_\psi\to\{\pm1\}\) be Arthur's canonical global
character. For a member

\[
\pi=\bigotimes_v'\pi_v
\]

of the global [[langlands/a-packet|\(A\)-packet]], the local packet pairings
give a global character

\[
\langle s,\pi\rangle
=
\prod_v \langle s_v,\pi_v\rangle .
\]

The **Arthur multiplicity formula** selects the representations for which
this character matches \(\epsilon_\psi\). In a standard multiplicity-free
form,

\[
m_\psi(\pi)
=
\frac{1}{|\mathcal S_\psi|}
\sum_{s\in\mathcal S_\psi}
\epsilon_\psi(s)\,
\langle s,\pi\rangle .
\]

By [[algebra-representation-theory/character-orthogonality|character orthogonality]] this is \(1\) when the two characters agree and
\(0\) otherwise.

## Meaning

Local packets supply many possible restricted tensor products. The formula
is a global reciprocity constraint: local component-group labels must
multiply to the distinguished global sign. It therefore explains why a
global packet is not simply the Cartesian product of its local packets.

## Source of the sign

The character \(\epsilon_\psi\) is built from global root numbers of pairs of
the cuspidal general-linear-group constituents of \(\psi\). It is not an
arbitrary choice and can force a representation out of the discrete
spectrum even when all of its local components lie in the prescribed
packets.

## Scope and variants

The displayed formula is the clean form for the quasisplit classical
settings of Arthur's classification. Central quotients, even orthogonal
outer automorphisms, non-quasisplit inner forms, and parameters with
multiplicity require refinements of the packet and coefficient conventions.

The formula is a theorem for the symplectic and [[lie-groups/orthogonal-group|orthogonal groups]] treated by
Arthur and in corresponding established extensions, such as quasisplit
unitary groups. It remains part of the conjectural general theory for
arbitrary [[algebraic-geometry-foundations/reductive-algebraic-group|reductive groups]].

## References

1. James Arthur, *The Endoscopic Classification of Representations:
   Orthogonal and Symplectic Groups*, Theorem 1.5.2 and Chapter 8, AMS,
   2013. [AMS](https://bookstore.ams.org/COLL/61).
2. Chung Pang Mok, “Endoscopic classification of representations of
   quasi-split unitary groups,” *Memoirs of the AMS* 235 (2015).
   [AMS](https://bookstore.ams.org/memo-235-1108).
