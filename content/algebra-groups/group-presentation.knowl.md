+++
id = "algebra-groups/group-presentation"
title = "Group Presentation"
kind = "knowl"
summary = "A group specified as a quotient of a free group by the normal closure of a set of relations."
aliases = ["group-presentation", "Group Presentation"]
domains = ["algebra-groups"]
legacy_source_path = "algebra-groups/group-presentation.md"
+++

A **group presentation** consists of a set $S$ of generators and a set $R\subseteq F(S)$ of relators. The notation
$$
\langle S \mid R\rangle
$$
denotes the quotient of the [[algebra-groups/free-group|free group]] $F(S)$ by the [[algebra-groups/normal-closure|normal closure]] of $R$:
$$
\langle S \mid R\rangle \;:=\; F(S)\big/\!\langle\!\langle R\rangle\!\rangle,
$$
a [[algebra-groups/quotient-group|quotient group]] in which every relator is equal to the identity.

## Remarks

A presentation is **finite** when both $S$ and $R$ are finite. Different presentations can define isomorphic groups.

## Examples

- The cyclic group of order $n$ has presentation $\langle a\mid a^n=e\rangle$.
- The free abelian group of rank $2$ has presentation $\langle a,b\mid aba^{-1}b^{-1}=e\rangle$.
- The dihedral group $D_{2n}$ has presentation $\langle r,s\mid r^n=e,\ s^2=e,\ srs^{-1}=r^{-1}\rangle$.
