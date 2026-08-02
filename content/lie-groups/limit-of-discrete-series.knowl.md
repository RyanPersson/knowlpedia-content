+++
id = "lie-groups/limit-of-discrete-series"
title = "Limit of discrete series representation"
kind = "definition"
summary = "A nonzero irreducible representation obtained by extending the discrete-series parameter construction to a singular dominant Harish-Chandra parameter."
aliases = ["limit discrete-series representation"]
domains = ["lie-groups", "harmonic-analysis"]
section_mode = "progressive"
+++

Let \(G\) be a linear connected semisimple real [[fiber-bundles/lie-group|Lie group]] with compact [[lie-groups/cartan-subalgebra|Cartan subalgebra]] \(\mathfrak t\), and choose a Weyl chamber \(C\) in the [[lie-groups/root-system|root system]] of \((\mathfrak g_{\mathbb C},\mathfrak t_{\mathbb C})\). Let \(\rho_C\) be half the sum of the \(C\)-positive roots, and let \(\lambda\) be dominant on the closure of \(C\), with \(\lambda-\rho_C\) exponentiating to a character of the corresponding compact Cartan subgroup. The Harish-Chandra construction extends from regular \(\lambda\), which gives [[lie-groups/discrete-series-representation|discrete series]], to singular \(\lambda\). A **limit of discrete series representation** is a nonzero [[lie-groups/irreducible-unitary-representation|irreducible unitary representation]] \(\pi(\lambda,C)\) obtained from such a singular parameter.

## Nonvanishing and temperedness

The continued character \(\pi(\lambda,C)\) is zero exactly when \(\lambda\) is orthogonal to a compact \(C\)-simple root. Every nonzero limit is irreducible and tempered. These criteria, and equivalence under the [[lie-groups/weyl-group|Weyl group]] of the compact roots, are part of the Knapp–Zuckerman classification.

## Example

For \(SU(1,1)\), the compact Cartan has no compact roots. Moving a regular Harish-Chandra parameter to the singular value \(0\) from either of the two Weyl chambers produces two distinct nonzero limits of discrete series. They are tempered but not square-integrable, and provide the archimedean representations associated with weight-one phenomena.

## Conventions and scope

**Warning.** “Limit” refers to coherent continuation of the Harish-Chandra parameter and character formula to a chamber wall; it does not mean an arbitrary topological limit in the [[harmonic-analysis/fell-topology|Fell topology]]. Some sources include regular discrete series among “limits of discrete series.” This knowl reserves the term for singular parameters, matching Knapp–Zuckerman. For reductive groups with noncompact center, the construction is formulated using relative discrete-series data and a compatible central character.

## References

1. Anthony W. Knapp and Gregg J. Zuckerman, *Classification of irreducible tempered representations of semisimple groups*, Annals of Mathematics 116 (1982), 389–455, with appendix 493–501. [Journal record](https://annals.math.princeton.edu/1982/116-2/p05). Relevant: Theorem 1.1 and the limit-of-discrete-series parameters.
2. Henri Carayol and Anthony W. Knapp, *Limits of discrete series with infinitesimal character zero*, Transactions of the American Mathematical Society 359 (2007), 5611–5651. [DOI record](https://doi.org/10.1090/S0002-9947-07-04306-1). Relevant: introduction and §2 for the chamber construction, nonvanishing criterion, and examples.
