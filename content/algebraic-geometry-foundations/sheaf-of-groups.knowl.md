+++
id = "algebraic-geometry-foundations/sheaf-of-groups"
title = "Sheaf of groups"
kind = "definition"
summary = "A sheaf whose sections form groups compatibly with restriction."
aliases = ["sheaf of groups", "group sheaf", "group object in sheaves"]
domains = ["algebraic-geometry-foundations"]
+++

Let \(\mathcal C\) be a [[algebraic-geometry-foundations/site|site]]. A **sheaf of groups** on \(\mathcal C\) is a [[algebraic-geometry-foundations/sheaf|sheaf]] \(G\) such that every set of sections \(G(U)\) is a [[algebra-groups/group|group]] and every restriction map associated to a morphism \(V\to U\),

\[
G(U)\longrightarrow G(V)
\]

is a group homomorphism. Equivalently, \(G\) is a group object in the category of sheaves on \(\mathcal C\): multiplication, identity, and inverse are morphisms of sheaves satisfying the group axioms.

A right [[algebra-groups/group-action|action]] of \(G\) on a sheaf \(P\) is a [[algebraic-geometry-foundations/morphism-of-sheaves|morphism of sheaves]]

\[
P\times G\longrightarrow P
\]

whose maps on sections are right group actions and commute with restriction. This is the type of action used in a [[algebraic-geometry-foundations/g-torsor-on-a-site|\(G\)-torsor on a site]].

**Warning.** A sheaf of groups is more than a sheaf together with unrelated group structures on its sets of sections: all restriction maps must preserve multiplication, identity, and inverse.
