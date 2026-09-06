+++
id = "algebra-representation-theory/representation-ring"
title = "Representation ring"
kind = "definition"
summary = "The Grothendieck ring of finite-dimensional representations, with direct sum as addition and tensor product as multiplication."
aliases = ["Grothendieck ring of representations", "representation ring R(G)", "character ring"]
domains = ["algebra-representation-theory", "algebra-groups", "langlands"]
prerequisites = ["algebra-groups/group", "topology/topological-group", "algebraic-geometry-foundations/group-scheme", "algebra-rings/field", "algebra-representation-theory/group-representation", "algebra-modules/short-exact-sequence"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(G\) be a [[algebra-groups/group|group]],
[[topology/topological-group|topological group]], or affine
[[algebraic-geometry-foundations/group-scheme|group scheme]], and fix a
coefficient [[algebra-rings/field|field]] \(k\). The **representation ring**
\(R_k(G)\) is the
Grothendieck group of the exact category of finite-dimensional
[[algebra-representation-theory/group-representation|\(k\)-representations]]
of \(G\), with multiplication induced by tensor product:

\[
[V]+[W]=[V\oplus W],
\qquad
[V][W]=[V\otimes_k W].
\]

Equivalently, the additive relations are
\([V]=[V']+[V'']\) for every
[[algebra-modules/short-exact-sequence|short exact sequence]]
\(0\to V'\to V\to V''\to0\).

## Semisimple case

If the representation category is semisimple, \(R_k(G)\) is the free abelian
group on the
[[algebra-representation-theory/irreducible-representation|irreducible
representations]]. Dual representations define an
involution \([V]\mapsto[V^\vee]\), and exterior powers give it a
\(\lambda\)-ring structure.

## Characters

Taking [[linear-algebra/trace|traces]] defines a
[[algebra-rings/ring-homomorphism|ring homomorphism]] from \(R_k(G)\) to
[[algebra-groups/class-function|class functions]].
For finite groups in characteristic \(0\), or for complex
[[algebraic-geometry-foundations/reductive-algebraic-group|reductive groups]] in
the appropriate regular-character setting, this character map is injective.
The statement that [[algebra-representation-theory/character|characters]]
separate semisimple [[algebra-groups/conjugacy-class|conjugacy classes]] concerns
the resulting functions on the semisimple quotient, not arbitrary elements in
all characteristics.

## References

1. Jean-Pierre Serre, *Linear Representations of Finite Groups*, Graduate
   Texts in Mathematics 42, Springer, 1977, Chapters 2 and 9.
2. Alexander Grothendieck, “La théorie des classes de Chern,” *Bulletin de la
   Société Mathématique de France* 86 (1958), 137–154.
   [Numdam](https://www.numdam.org/item/BSMF_1958__86__137_0/).
