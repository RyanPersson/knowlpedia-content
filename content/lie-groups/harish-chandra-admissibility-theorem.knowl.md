+++
id = "lie-groups/harish-chandra-admissibility-theorem"
title = "Harish–Chandra admissibility theorem"
kind = "theorem"
summary = "Every irreducible unitary representation of a real reductive group has finite multiplicity for each irreducible maximal-compact-subgroup type."
aliases = ["admissibility theorem for irreducible unitary representations"]
domains = ["lie-groups", "representation-theory"]
section_mode = "progressive"
+++

Let \(G\) be a [[lie-groups/real-reductive-lie-group|real reductive group]] in the Harish–Chandra class, and let \(K\) be a [[lie-groups/maximal-compact-subgroup-real-reductive-group|maximal compact subgroup]]. The **Harish–Chandra admissibility theorem** states that every [[lie-groups/irreducible-unitary-representation|irreducible unitary representation]] \((\pi,\mathcal H)\) of \(G\) is admissible: for each irreducible finite-dimensional representation \(\tau\) of \(K\),
\[
\dim\operatorname{Hom}_K(E_\tau,\mathcal H)<\infty .
\]
Equivalently, every [[lie-groups/k-type|\(K\)-type]] occurs in \(\pi|_K\) with finite multiplicity. The theorem bounds each multiplicity separately; it does not say that only finitely many \(K\)-types occur.

## Why the conclusion is substantial

Compact-group theory decomposes the restriction \(\pi|_K\) into \(K\)-isotypic Hilbert subspaces, but compactness alone does not force their multiplicities to be finite. For example, an infinite Hilbert direct sum of the trivial representation of \(K\) has infinite trivial-type multiplicity. The theorem uses irreducibility for the noncompact group \(G\), together with the structure of real reductive groups, to rule out this behavior. This is the finiteness theorem stated in [Knapp, Chapter VIII, Theorem 8.1](https://www.math.stonybrook.edu/~aknapp/books/repthy1.html).

## Algebraic consequence

The [[lie-groups/k-finite-vector|\(K\)-finite vectors]] \(\mathcal H_K\) are dense in \(\mathcal H\) and carry compatible actions of the complexified [[lie-groups/lie-algebra|Lie algebra]] \(\mathfrak g\) and \(K\). Admissibility supplies finite \(K\)-multiplicities, while irreducibility supplies finite generation over \(U(\mathfrak g)\); consequently \(\mathcal H_K\) is an irreducible [[lie-groups/harish-chandra-module|Harish–Chandra module]]. This passage replaces the Hilbert-space representation by a tractable algebraic core without discarding its infinitesimal and compact-subgroup data [Wallach, Chapter 3, §§3.3–3.5](https://shop.elsevier.com/books/real-reductive-groups-i/wallach/978-0-12-732960-4).

## Hypotheses and scope

**Warning.** The statement is not a theorem about arbitrary Banach representations. Irreducible Banach representations of real reductive groups can fail to be admissible. Nor does the theorem claim that every reducible unitary representation is admissible: infinite multiplicities already arise from infinite direct sums. Formulations for groups outside the Harish–Chandra class require their own hypotheses, especially concerning the center and component group.

## References

1. Anthony W. Knapp, *Representation Theory of Semisimple Groups: An Overview Based on Examples*, Princeton University Press, 1986. [Author-maintained record](https://www.math.stonybrook.edu/~aknapp/books/repthy1.html). Relevant: Chapter VIII, especially Theorem 8.1.
2. Nolan R. Wallach, *Real Reductive Groups I*, Academic Press, 1988. [Publisher record](https://shop.elsevier.com/books/real-reductive-groups-i/wallach/978-0-12-732960-4). Relevant: Chapter 3, §§3.3–3.5.
