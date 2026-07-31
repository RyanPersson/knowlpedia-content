+++
id = "harmonic-analysis/quasi-regular-representation"
title = "Quasi-regular representation"
kind = "definition"
summary = "A quasi-regular representation is the unitary action of a locally compact group on square-integrable functions over a homogeneous space."
aliases = ["representation on L2(G/H)", "homogeneous-space representation"]
domains = ["harmonic-analysis", "representation-theory", "lie-groups"]
section_mode = "progressive"
+++

Let \(G\) be a [[topology/locally-compact-group|locally compact Hausdorff group]], let \(H\) be a closed subgroup, and let \(\mu\) be a [[harmonic-analysis/quasi-invariant-measure|quasi-invariant regular measure]] on the [[harmonic-analysis/locally-compact-homogeneous-space|locally compact homogeneous space]] \(G/H\). Write \(g_*\mu(E)=\mu(g^{-1}E)\) and \(r_g=d(g_*\mu)/d\mu\). The **quasi-regular representation** of \(G\) on [[measure-theory/lp-space|\(L^2(G/H,\mu)\)]] is
\[
(\lambda_{G/H}(g)\xi)(xH)
=r_g(xH)^{1/2}\xi(g^{-1}xH).
\]
Quasi-invariance makes the derivative exist, and the Radon–Nikodym factor makes every \(\lambda_{G/H}(g)\) unitary. The cocycle identity for \(r_g\) gives the representation law.

## Invariant-measure case

If \(G/H\) has a \(G\)-invariant measure, then \(r_g=1\) [[measure-theory/almost-everywhere|almost everywhere]] and the formula reduces to translation:
\[
(\lambda_{G/H}(g)\xi)(xH)=\xi(g^{-1}xH).
\]
By the [[harmonic-analysis/weil-integration-formula|Weil integration formula]], such an invariant measure exists exactly when \(\Delta_G|_H=\Delta_H\). In particular, it exists when \(H\) is compact.

## Relationship to induction

The quasi-regular representation is the
[[harmonic-analysis/unitary-induced-representation|unitary representation
induced]] from the trivial one-dimensional representation of \(H\). This
interpretation explains why it is central to harmonic analysis on quotients:
its [[harmonic-analysis/coefficient-function|matrix coefficients]] and invariant vectors record how \(G\) acts on
\(G/H\), while induction connects those data to representations of the
subgroup.

## Examples and measure-class independence

For \(H=\{e\}\), the construction is the left [[harmonic-analysis/regular-representations-locally-compact-group|regular representation]] on \(L^2(G)\). For \(H=G\), it is the trivial representation on a one-dimensional [[linear-algebra/hilbert-space|Hilbert space]]. Replacing \(\mu\) by an equivalent quasi-invariant measure changes the displayed realization but yields a unitarily equivalent representation through multiplication by the square root of the density.

**Warning.** Omitting the Radon–Nikodym factor is valid only for an invariant quotient measure; with a merely quasi-invariant measure, plain translation need not preserve the \(L^2\) norm.

## References

1. G. B. Folland, *A Course in Abstract Harmonic Analysis*, 2nd ed., CRC Press, 2016. [DOI record](https://doi.org/10.1201/B19172). Relevant: homogeneous spaces, quasi-invariant measures, and induced representations.
2. B. Bekka, P. de la Harpe, and A. Valette, *Kazhdan's Property (T)*, Cambridge University Press, 2008. [DOI record](https://doi.org/10.1017/CBO9780511542749). Relevant: quasi-regular representations and invariant vectors.
