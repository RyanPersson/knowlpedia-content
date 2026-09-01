+++
id = "langlands-letter/knowls/characters-separate-semisimple-classes"
title = "Characters separate semisimple conjugacy classes"
kind = "knowl"
summary = "Semisimple conjugacy classes in a connected complex reductive group are determined by all algebraic character values."
aliases = ["characters-separate-semisimple-classes", "Characters Separate Semisimple Conjugacy Classes"]
domains = ["langlands-letter"]
prerequisites = ["algebraic-geometry-foundations/reductive-algebraic-group", "langlands-letter/knowls/semisimple-element-and-class", "algebra-representation-theory/irreducible-representation"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
legacy_source_path = "langlands-letter/knowls/characters-separate-semisimple-classes.md"
section_mode = "progressive"
+++

Let \(H\) be a connected complex [[algebraic-geometry-foundations/reductive-algebraic-group|reductive group]]. If \(h,h'\in H\) are
[[langlands-letter/knowls/semisimple-element-and-class|semisimple]], then

\[
h\sim_H h'
\quad\Longleftrightarrow\quad
\operatorname{tr}(\rho(h))
=
\operatorname{tr}(\rho(h'))
\]

for every finite-dimensional algebraic representation \(\rho\) of \(H\).
It suffices to range over [[algebra-representation-theory/irreducible-representation|irreducible representations]].

## Invariant-theory explanation

Choose a
[[langlands-letter/knowls/maximal-torus-weight-lattice|maximal torus]] \(T\)
with [[lie-groups/weyl-group|Weyl group]] \(W\). Semisimple conjugacy
classes are identified with \(W\)-orbits in \(T\), and restriction gives

\[
\mathcal O(H)^H\simeq\mathcal O(T)^W.
\]

The characters of irreducible algebraic representations span the
[[algebra-representation-theory/representation-ring|representation ring]]
and generate enough Weyl-invariant regular functions
to distinguish the closed, hence semisimple, [[algebra-groups/conjugacy-class|conjugacy classes]].

## Closed-orbit qualification

Invariant regular functions separate closed orbits in the affine quotient.
For a general element they recover the semisimple part of its Jordan
[[langlands-letter/knowls/semisimple-element-and-class|decomposition]], not
its full conjugacy class. This is why
[[langlands/excursion-operator|excursion-operator]]
reconstruction naturally produces semisimple parameters.

## Disconnected and twisted scope

A [[langlands-letter/knowls/frobenius-unramified|Frobenius]] fiber in an
[[langlands/l-group|\(L\)-group]] is a coset of the
[[langlands-letter/knowls/langlands-dual-group|dual group]] \(\widehat G\),
not a connected group. Its conjugacy is
[[langlands/twisted-conjugacy|twisted]] by the
[[langlands/weil-group|Weil-group]] action. The analogous
separation statement uses invariant functions on the twisted quotient;
the connected theorem should not be applied to that coset without this
modification.

## Relation to the letter

Values of all dual-group characters on the Satake class determine that
semisimple class. This is the invariant-theoretic reason that the collection
of unramified Euler factors can record a [[langlands/satake-parameter|Satake parameter]].

## References

1. T. A. Springer, *Linear Algebraic Groups*, second edition, Birkhäuser,
   1998.
2. Claudio Procesi, *Lie Groups: An Approach through Invariants and
   Representations*, Springer, 2007.
