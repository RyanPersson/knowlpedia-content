+++
id = "lie-groups/heisenberg-derived-representation"
title = "Derived Heisenberg representation on Schwartz space"
kind = "example"
summary = "Differentiation, multiplication by ix, and iI realize the Heisenberg Lie algebra on one common smooth domain."
aliases = ["infinitesimal Schrödinger representation"]
domains = ["lie-groups"]
section_mode = "progressive"
prerequisites = ["lie-groups/heisenberg-group", "mathematical-physics/schrodinger-representation", "lie-groups/schrodinger-smooth-vectors", "lie-groups/derived-representation-on-smooth-vectors"]
+++

In symmetric coordinates \((a,b,z)\) on the [[lie-groups/heisenberg-group|Heisenberg group]], the [[mathematical-physics/schrodinger-representation|Schrödinger action]] is
\[
(\pi(a,b,z)f)(x)=e^{i(z+bx+ab/2)}f(x+a).
\]
On its [[lie-groups/schrodinger-smooth-vectors|smooth domain]] \(\mathcal S(\mathbb R)\), the [[lie-groups/derived-representation-on-smooth-vectors|derived representation]] for the coordinate Lie-algebra basis \(A,B,C\) is
\[
d\pi(A)f=f',\qquad d\pi(B)f=ixf,\qquad d\pi(C)f=if.
\]
It realizes \([A,B]=C\) and \([A,C]=[B,C]=0\).

## Bracket calculation

All three operators preserve Schwartz space, and
\[
[d\pi(A),d\pi(B)]f=(ixf)'-ixf'=if=d\pi(C)f.
\]
Thus the commutator is an identity on a specified common domain. These operators are continuous for the Schwartz topology but the first two are unbounded in the \(L^2\) norm.

## Unsymmetrized coordinates

Putting \(c=z+ab/2\) changes the group law to
\[
(a,b,c)(a',b',c')=(a+a',b+b',c+c'+ab')
\]
and the action to \(\pi(a,b,c)f(x)=e^{i(c+bx)}f(x+a)\). This is the same representation in different coordinates, not a change of central sign. In terms of the existing Weyl convention, \(\pi(a,b,z)=e^{iz}V(b,a)\).

## Unitary versus algebraic irreducibility

The representation on \(L^2\) is [[lie-groups/irreducible-unitary-representation|unitarily irreducible]], but its derived action on Schwartz space is not [[lie-groups/irreducible-representation-lie-algebra|algebraically irreducible]]. The nonzero proper subspace \(C_c^\infty(\mathbb R)\) is preserved by differentiation and multiplication by \(x\). It is dense in \(L^2\), so it does not contradict the absence of proper closed invariant Hilbert subspaces.

## References

1. Rahul Garg and Sundaram Thangavelu, [*On the structure of analytic vectors for the Schrödinger representation*](https://arxiv.org/abs/1006.3265). §2, group law and Schrödinger formula; the coordinate conversion and operator identities are calculated directly above.
