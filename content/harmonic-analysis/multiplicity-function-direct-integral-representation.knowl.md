+++
id = "harmonic-analysis/multiplicity-function-direct-integral-representation"
title = "Multiplicity function of a representation"
kind = "definition"
summary = "A multiplicity function records the dimension of the multiplicity space attached to almost every irreducible fiber in a direct-integral decomposition."
aliases = ["spectral multiplicity", "representation multiplicity function"]
domains = ["harmonic-analysis", "representation-theory"]
section_mode = "progressive"
+++

Let \(G\) be a second-countable type I [[topology/locally-compact-group|locally compact group]] and \(U\) a unitary representation on a separable complex [[linear-algebra/hilbert-space|Hilbert space]]. Suppose \(U\) has the [[harmonic-analysis/direct-integral-unitary-representations|direct-integral disintegration]]
\[
U\cong\int_{\widehat G}^{\oplus}
\bigl(\pi\otimes I_{\mathcal M_\pi}\bigr)\,d\mu(\pi)
\]
over the [[harmonic-analysis/unitary-dual|unitary dual]]. The **multiplicity function** is the [[measure-theory/measurable-function|measurable function]]
\[
m:\widehat G\longrightarrow\{0,1,2,\ldots,\infty\}
\]
where \((\mathcal M_\pi)\) is a measurable field of multiplicity Hilbert
spaces and \(m(\pi)=\dim\mathcal M_\pi\). It is defined only
[[measure-theory/almost-everywhere|\(\mu\)-almost everywhere]] relative to
the chosen measure; normally \(m(\pi)\geq1\) on the chosen carrier of
\(\mu\). In the separable setting, \(m(\pi)=\infty\) means
\(\mathcal M_\pi\cong\ell^2(\mathbb N)\), not an algebraic space
\(\mathbb C^\infty\).

## What it classifies

Under the stated type I and separability hypotheses, the measure class of \(\mu\) and the almost-everywhere [[shared-foundations/equivalence-class|equivalence class]] of \(m\) determine \(U\) up to unitary equivalence. Conversely, equivalent representations have the same spectral measure class and multiplicity function after identifying [[measure-theory/null-set|null sets]]. This uniqueness is the central classification feature of type I disintegration.

The value \(m(\pi)=n\) means that the fiber contains \(n\) copies of \(\pi\); \(m(\pi)=\infty\) means countably infinite multiplicity in the separable setting. Multiplicity is therefore fiberwise, rather than the measure of the set on which \(\pi\) occurs.

## Examples

For a finite Hilbert direct sum \(U=\pi_1\oplus\pi_1\oplus\pi_2\) of pairwise inequivalent irreducibles, take counting measure on \(\{\pi_1,\pi_2\}\); then \(m(\pi_1)=2\) and \(m(\pi_2)=1\). For a multiplicity-free representation, \(m=1\) almost everywhere. An [[algebra-representation-theory/irreducible-representation|irreducible representation]] has spectral measure concentrated at one point with multiplicity one.

## Conventions and scope

**Warning.** Changing \(\mu\) within its measure class does not change the representation or its multiplicity class. Assigning values of \(m\) on a \(\mu\)-null subset has no meaning. Outside the type I setting, decomposition into irreducibles need not furnish a standard measurable classification, so a multiplicity function on \(\widehat G\) may not be a complete invariant.

The underlying Hilbert space is the [[functional-analysis/direct-integral-hilbert-spaces|direct integral of Hilbert spaces]], and the representation acts fiberwise as specified by the [[harmonic-analysis/direct-integral-unitary-representations|direct-integral decomposition]].

## References

1. Gerald B. Folland, *A Course in Abstract Harmonic Analysis*, 2nd ed., CRC Press, 2016. [DOI record](https://doi.org/10.1201/B19172). Relevant: §7.4, multiplicity theory for type I direct integrals.
2. Jacques Dixmier, *\(C^*\)-Algebras*, North-Holland, 1977. [Publisher record](https://www.sciencedirect.com/bookseries/north-holland-mathematical-library/vol/15/suppl/C). Relevant: §18.8, disintegration and multiplicities.
