+++
id = "lie-groups/centralizer-of-a-lie-subalgebra"
title = "Centralizer of a Lie subalgebra"
kind = "definition"
summary = "The Lie subalgebra of elements commuting with every element of a given Lie subalgebra."
aliases = ["centralizer of a Lie subalgebra", "Lie-algebra centralizer", "commutant in a Lie algebra"]
domains = ["lie-groups"]
prerequisites = ["lie-groups/lie-subalgebra"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(\mathfrak k\subseteq\mathfrak g\) be a [[lie-groups/lie-subalgebra|Lie subalgebra]]. The **centralizer of \(\mathfrak k\) in \(\mathfrak g\)** is
\[
C_{\mathfrak g}(\mathfrak k)
=\{x\in\mathfrak g:[x,y]=0\text{ for every }y\in\mathfrak k\}.
\]
It is a Lie subalgebra of \(\mathfrak g\).

## Basic properties

For subalgebras \(\mathfrak a\subseteq\mathfrak b\subseteq\mathfrak g\), centralizers reverse inclusion:
\[
C_{\mathfrak g}(\mathfrak b)\subseteq C_{\mathfrak g}(\mathfrak a).
\]
Moreover,
\[
Z(\mathfrak g)\subseteq C_{\mathfrak g}(\mathfrak k),
\qquad
Z(\mathfrak k)=\mathfrak k\cap C_{\mathfrak g}(\mathfrak k),
\qquad
\mathfrak k\subseteq C_{\mathfrak g}\!\left(C_{\mathfrak g}(\mathfrak k)\right).
\]
The last containment need not be equality; equality is a double-centralizer property.

## Centralizer versus normalizer

The centralizer requires \([x,\mathfrak k]=0\). The normalizer
\[
N_{\mathfrak g}(\mathfrak k)
=\{x\in\mathfrak g:[x,\mathfrak k]\subseteq\mathfrak k\}
\]
only requires \(x\) to preserve \(\mathfrak k\) under the adjoint action. Hence
\[
C_{\mathfrak g}(\mathfrak k)\subseteq N_{\mathfrak g}(\mathfrak k).
\]

## Matrix interpretation

If \(\mathfrak g\) is a matrix [[lie-groups/lie-algebra|Lie algebra]], then \(C_{\mathfrak g}(\mathfrak k)\) consists of the matrices in \(\mathfrak g\) commuting, in the ordinary matrix sense, with every element of \(\mathfrak k\). For [[lie-groups/regular-lie-subalgebra|regular reductive subalgebras]] of a semisimple algebra, the centralizer can often be read directly from roots.

## References

1. Anthony W. Knapp, *Lie Groups Beyond an Introduction*, 2nd ed., Birkhäuser, 2002, Chapters I–II. [Publisher record](https://doi.org/10.1007/978-1-4757-2453-0).
2. Arkady L. Onishchik and Ernest B. Vinberg, eds., *Lie Groups and Lie Algebras III: Structure of Lie Groups and Lie Algebras*, Springer, 1994, Chapter 3. [Publisher record](https://link.springer.com/book/9783540546832).
