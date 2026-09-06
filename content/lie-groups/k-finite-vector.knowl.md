+++
id = "lie-groups/k-finite-vector"
title = "K-finite vector"
kind = "definition"
summary = "A vector whose orbit under a compact subgroup spans a finite-dimensional subspace."
aliases = ["finite vector for a compact subgroup", "K-finite part"]
domains = ["lie-groups", "representation-theory"]
prerequisites = ["linear-algebra/vector-space", "lie-groups/strongly-continuous-unitary-representation"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(\pi\) be a representation of a group \(G\) on a complex [[linear-algebra/vector-space|vector space]] \(V\), and let \(K\subseteq G\) be compact. A vector \(v\in V\) is **\(K\)-finite** when
\[
\operatorname{span}_{\mathbb C}\{\pi(k)v:k\in K\}
\]
is finite-dimensional. The \(K\)-finite vectors form a \(K\)-stable linear
subspace \(V_K\), called the \(K\)-finite part. For a
[[lie-groups/strongly-continuous-unitary-representation|strongly continuous
unitary representation]], the finite-dimensional orbit span is a finite
direct sum of irreducible \(K\)-representations; equivalently, a
\(K\)-finite vector has nonzero components in only finitely many irreducible
summands.

## Density and algebraic role

If \(K\) is compact and \(\pi|_K\) is continuous and unitary, then \(V_K\) is dense in the [[linear-algebra/hilbert-space|Hilbert space]]. This follows by applying the [[lie-groups/peter-weyl-theorem|Peter–Weyl theorem]] to the [[algebra-representation-theory/restricted-representation|restricted representation]]. When \(G\) is a [[lie-groups/real-reductive-lie-group|real reductive group]] and \(K\) a [[lie-groups/maximal-compact-subgroup-real-reductive-group|maximal compact subgroup]], the \(K\)-finite part is the algebraic carrier on which the differentiated Lie-algebra action and the \(K\)-action combine into a \((\mathfrak g,K)\)-module.
Its decomposition is organized by the
[[lie-groups/k-type|\(K\)-types]] occurring in the restricted
representation.

## Example

Let \(K=S^1\) act on \(L^2(S^1)\) by rotations. The characters \(z\mapsto z^m\) are \(K\)-finite, and every trigonometric polynomial is \(K\)-finite because it involves finitely many characters. A function with infinitely many nonzero Fourier coefficients is not \(K\)-finite, although such functions are limits of \(K\)-finite vectors.

## Conventions and scope

The letter \(K\) usually denotes a maximal compact subgroup in real-reductive representation theory, but the definition makes sense for any compact subgroup. It concerns the algebraic span of an orbit, not whether the orbit is a finite set. Thus a one-dimensional character has \(K\)-finite vectors even when its image is infinite.

## References

1. Nolan R. Wallach, *Real Reductive Groups I*, Academic Press, 1988. [Publisher record](https://shop.elsevier.com/books/real-reductive-groups-i/wallach/978-0-12-732960-4). Relevant: Chapter 3, §3.3 on \((\mathfrak g,K)\)-modules and \(K\)-finite vectors.
2. Anthony W. Knapp, *Representation Theory of Semisimple Groups: An Overview Based on Examples*, Princeton University Press, 1986. [DOI record](https://doi.org/10.1515/9781400883974). Relevant: Chapter VIII on admissible representations and \(K\)-finite vectors.
