+++
id = "lie-groups/real-reductive-lie-group"
title = "Real reductive Lie group"
kind = "definition"
summary = "A real Lie group satisfying the reductivity and finiteness hypotheses used in Harish–Chandra theory."
aliases = ["reductive group over the real numbers", "Harish-Chandra class group"]
domains = ["lie-groups"]
section_mode = "progressive"
+++

A **real reductive Lie group in the Harish–Chandra class** is a
[[fiber-bundles/lie-group|real Lie group]] \(G\) such that its [[lie-groups/lie-algebra|Lie algebra]]
\(\mathfrak g\) is [[lie-groups/reductive-lie-algebra|reductive]],
\(\operatorname{Ad}(G)\) lies in the group of [[algebra-groups/inner-automorphism|inner automorphisms]] of
\(\mathfrak g_{\mathbb C}\), \(G\) has finitely many [[topology/connected-component|connected components]], and
the connected analytic subgroup with Lie algebra
\([\mathfrak g,\mathfrak g]\) has finite center. These global conditions are
part of the definition: reductivity of \(\mathfrak g\) alone does not control
the component group or the kernel of the adjoint action. This is the standard
setting for Harish–Chandra’s representation theory.

## Why the global hypotheses matter

The Lie algebra determines local structure but not the topology of the group.
The finite-component condition prevents unrelated discrete phenomena, while
the finite-center condition on the derived subgroup gives the semisimple part
the global finiteness needed for admissibility and harmonic analysis. A
noncompact central vector group is still allowed. Thus groups such as
\(\mathrm{GL}_n(\mathbb R)\) fit the convention even though their centers need
not be compact [Knapp, Chapter VII].

## Cartan structure

Such a group admits a global Cartan involution. Its fixed-point subgroup is a
[[lie-groups/maximal-compact-subgroup-real-reductive-group|maximal compact
subgroup]] \(K\), and its Lie algebra has a
[[lie-groups/cartan-decomposition-real-reductive-lie-algebra|Cartan
decomposition]] \(\mathfrak g=\mathfrak k\oplus\mathfrak p\). These data lead
to both the [[lie-groups/global-cartan-decomposition|global Cartan
decomposition]] and the
[[lie-groups/iwasawa-decomposition|Iwasawa decomposition]].

## Conventions and examples

Terminology varies: some authors use “real reductive group” for linear
algebraic groups over \(\mathbb R\), for closed transpose-stable matrix groups,
or for Lie groups with slightly different covering hypotheses. The
Harish–Chandra-class qualifier therefore records substantive assumptions.
Connected real semisimple Lie groups with finite center, their finite
extensions satisfying the adjoint condition, and \(\mathrm{GL}_n(\mathbb R)\)
are basic examples.

## References

1. A. W. Knapp, *Representation Theory of Semisimple Groups: An Overview Based on Examples*, Princeton University Press, 1986. [DOI record](https://doi.org/10.1515/9781400883974). Relevant: Chapter VII, especially the standing hypotheses for real reductive groups.
2. N. R. Wallach, *Real Reductive Groups I*, Academic Press, 1988. [Publisher record](https://shop.elsevier.com/books/real-reductive-groups-i/wallach/978-0-12-732960-4). Relevant: Chapter 2 on the structure of real reductive groups.
