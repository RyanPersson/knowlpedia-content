+++
id = "harmonic-analysis/plancherel-measure-nonabelian"
title = "Plancherel measure for a type I locally compact group"
kind = "definition"
summary = "The spectral measure on the unitary dual that makes the nonabelian Fourier transform an L2 isometry."
aliases = ["nonabelian Plancherel measure", "Plancherel measure of a locally compact group"]
domains = ["harmonic-analysis", "lie-groups", "functional-analysis"]
section_mode = "progressive"
+++

Let \(G\) be a second-countable, unimodular, type I
[[topology/locally-compact-group|locally compact group]], fix a left
[[harmonic-analysis/haar-measure|Haar measure]] \(dg\), and let
\(\widehat G\) be its [[harmonic-analysis/unitary-dual|unitary dual]]. For
\(f\in L^1(G)\cap L^2(G)\), set
\(\pi(f)=\int_G f(g)\pi(g)\,dg\). The **Plancherel measure**
\(\mu_{\mathrm{Pl}}\) is the unique positive Borel measure on \(\widehat G\)
for which
\[
\lVert f\rVert_2^2
=\int_{\widehat G}\lVert\pi(f)\rVert_{\mathrm{HS}}^2\,
d\mu_{\mathrm{Pl}}(\pi).
\]
The transform extends to a unitary map from \(L^2(G)\) onto the direct
integral of the [[functional-analysis/hilbert-schmidt-operator|Hilbert–Schmidt operator]] spaces.

## Regular-representation decomposition

Under the Plancherel transform, the
[[harmonic-analysis/regular-representations-locally-compact-group|left regular representation]] acts fiberwise by left multiplication with
\(\pi(g)\). Consequently, the measure class of
\(\mu_{\mathrm{Pl}}\) is the spectral measure class of the regular
representation in its
[[functional-analysis/direct-integral-hilbert-spaces|direct-integral decomposition]]. The type I hypothesis supplies the standard measurable
irreducible decomposition and its essential uniqueness
[Folland, Chapter 7, “The Plancherel Theorem”](https://doi.org/10.1201/B19172).

## Examples and support

For an abelian \(G\), every [[algebra-representation-theory/irreducible-representation|irreducible representation]] is a character and
\(\mu_{\mathrm{Pl}}\) is the Haar measure on the
[[harmonic-analysis/pontryagin-dual|Pontryagin dual]] normalized dually to
\(dg\). For compact \(G\) with Haar [[probability/probability-measure|probability measure]], it is discrete and
assigns mass \(\dim\pi\) to each irreducible class. In general, its support in
the [[harmonic-analysis/fell-topology|Fell topology]] is the tempered part of
\(\widehat G\), which may be smaller than the full unitary dual.

## Conventions and nonunimodular groups

Rescaling \(dg\) rescales the representative Plancherel measure, although its
[[measure-theory/null-set|null sets]] and hence its measure class are unchanged. For a nonunimodular
group, the displayed Hilbert–Schmidt formula must be modified by a measurable
field of positive, generally unbounded Duflo–Moore operators; the bare
formula in the core is therefore not valid unchanged
[Duflo--Moore, abstract and main construction](https://doi.org/10.1016/0022-1236%2876%2990079-3).

## References

1. Gerald B. Folland, *A Course in Abstract Harmonic Analysis*, 2nd ed., CRC Press, 2016. [Publisher record](https://doi.org/10.1201/B19172). Relevant: Chapter 7, sections “Direct Integral Decompositions” and “The Plancherel Theorem.”
2. Michel Duflo and Calvin C. Moore, “On the Regular Representation of a Nonunimodular Locally Compact Group,” *Journal of Functional Analysis* 21 (1976), 209–243. [DOI record](https://doi.org/10.1016/0022-1236%2876%2990079-3). Relevant: the operator-valued correction to the nonunimodular Plancherel formula.
