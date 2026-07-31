+++
id = "harmonic-analysis/quasi-invariant-measure"
title = "Quasi-invariant measure under a locally compact group action"
kind = "definition"
summary = "A quasi-invariant measure has the same null sets as each of its translates under the group action."
aliases = ["invariant measure class", "G-quasi-invariant measure"]
domains = ["harmonic-analysis", "measure-theory"]
section_mode = "progressive"
+++

Let a [[topology/locally-compact-group|locally compact group]] \(G\) act measurably on a [[measure-theory/measurable-space|measurable space]] \(X\), and let \(\mu\) be a \(\sigma\)-finite measure on \(X\). The measure \(\mu\) is **quasi-invariant** under the action if, for every \(g\in G\), the pushforward \(g_*\mu\), defined by \(g_*\mu(E)=\mu(g^{-1}E)\), is mutually absolutely continuous with \(\mu\). Equivalently,
\[
\mu(E)=0\quad\Longleftrightarrow\quad\mu(gE)=0
\]
for every measurable \(E\subseteq X\) and \(g\in G\). Thus the action preserves the measure class of \(\mu\), though not necessarily its values. Invariance, meaning \(g_*\mu=\mu\) for every \(g\), is a stronger condition.

## Radon–Nikodym cocycle

By the [[probability/radon-nikodym-theorem|Radon–Nikodym theorem]], quasi-invariance yields derivatives
\[
j(g,x)=\frac{d(g_*\mu)}{d\mu}(x)
\]
defined [[measure-theory/almost-everywhere|almost everywhere]]. With consistent representatives they satisfy a cocycle identity, with the order depending on whether the action and pushforward conventions are written on the left or right. These square-root derivatives correct pullback operators so that actions on \(L^2(X,\mu)\) become unitary [Folland, §2.6](https://doi.org/10.1201/B19172).

## Homogeneous spaces

For a closed subgroup \(H\leq G\), the
[[harmonic-analysis/locally-compact-homogeneous-space|locally compact
homogeneous space]] \(G/H\) always carries a natural quasi-invariant measure
class under standard locally compact hypotheses, even when it has no
\(G\)-invariant measure. This measure class is sufficient for quasi-regular
and induced-representation constructions
[Folland, §2.6](https://doi.org/10.1201/B19172).

## Conventions and near misses

**Warning.** A relatively invariant measure is stronger: it satisfies \(g_*\mu=c(g)\mu\) for a scalar depending only on \(g\). Every relatively invariant measure is quasi-invariant, but a general Radon–Nikodym derivative may depend on both \(g\) and \(x\).

A measure for which \(g_*\mu\ll\mu\) but \(\mu\not\ll g_*\mu\) is not quasi-invariant; one-sided [[analysis/absolute-continuity|absolute continuity]] does not preserve the null-set class.

## References

1. Gerald B. Folland, *A Course in Abstract Harmonic Analysis*, 2nd ed., CRC Press, 2016. [DOI record](https://doi.org/10.1201/B19172). Relevant: §2.6, quasi-invariant measures on homogeneous spaces.
