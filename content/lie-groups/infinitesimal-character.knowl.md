+++
id = "lie-groups/infinitesimal-character"
title = "Infinitesimal character"
kind = "definition"
summary = "An algebra character through which the center of an enveloping algebra acts on a representation."
aliases = ["central character of U(g)", "Harish-Chandra infinitesimal character"]
domains = ["lie-groups", "algebra-representation-theory"]
section_mode = "progressive"
prerequisites = ["lie-groups/lie-algebra", "lie-groups/universal-enveloping-algebra", "algebra-modules/algebra-homomorphism", "lie-groups/center-of-universal-enveloping-algebra", "lie-groups/harish-chandra-module"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(\mathfrak g\) be a complex [[lie-groups/lie-algebra|Lie algebra]] and let \(V\) be a module over its [[lie-groups/universal-enveloping-algebra|universal enveloping algebra]]. An **infinitesimal character** of \(V\) is a unital [[algebra-modules/algebra-homomorphism|algebra homomorphism]] from [[lie-groups/center-of-universal-enveloping-algebra|the center of \(U(\mathfrak g)\)]] to \(\mathbb C\),
\[
\chi:Z(U(\mathfrak g))\longrightarrow\mathbb C,
\]
such that
\[
zv=\chi(z)v
\]
for every \(z\in Z(U(\mathfrak g))\) and \(v\in V\). A Lie-group representation or [[lie-groups/harish-chandra-module|Harish–Chandra module]] **has infinitesimal character \(\chi\)** when the center acts this way on its differentiated \(\mathfrak g\)-module. For a real Lie algebra one uses its complexification.

## Harish–Chandra parameters

When \(\mathfrak g\) is semisimple and \(\mathfrak h\) is a [[lie-groups/cartan-subalgebra|Cartan subalgebra]], the [[lie-groups/harish-chandra-isomorphism|Harish–Chandra isomorphism]] identifies infinitesimal characters with \(W\)-orbits in \(\mathfrak h^*\). With the shifted convention, a highest-weight module of [[lie-groups/highest-weight|highest weight]] \(\lambda\) has the character obtained by evaluating Weyl-invariant polynomials at \(\lambda+\rho\). Consequently, distinct representations can have the same infinitesimal character.

## Existence and generalized characters

An arbitrary module need not have an infinitesimal character: central elements may act non-scalarly. Irreducible modules in the usual complex semisimple settings do have one under the relevant form of [[algebra-representation-theory/schurs-lemma|Schur's lemma]]. Finite-length modules are sometimes allowed a **generalized infinitesimal character**, meaning that a power of each \(z-\chi(z)\) acts as zero; this is weaker than scalar central action.

## Relation to global characters

If an [[lie-groups/admissible-representation-real-reductive-group|admissible representation]] has infinitesimal character \(\chi\), its [[lie-groups/global-character-of-an-admissible-representation|global character]] is a joint eigendistribution for the invariant differential operators corresponding to the center, with eigenvalues prescribed by \(\chi\). Infinitesimal and global characters are therefore related but are not the same kind of object.

## References

1. Anthony W. Knapp, *Representation Theory of Semisimple Groups: An Overview Based on Examples*, Princeton University Press, 1986; reprint 2001. [Author-maintained record](https://www.math.stonybrook.edu/~aknapp/books/repthy1.html). Relevant: Chapter VIII on infinitesimal characters.
2. Jacques Dixmier, *Enveloping Algebras*, Graduate Studies in Mathematics 11, American Mathematical Society, 1996. [DOI record](https://doi.org/10.1090/gsm/011). Relevant: Chapter 7 on central characters.
