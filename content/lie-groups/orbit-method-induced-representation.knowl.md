+++
id = "lie-groups/orbit-method-induced-representation"
title = "Induced representation attached to a polarization"
kind = "construction"
summary = "The unitary representation obtained by inducing the character defined by a coadjoint functional from a polarizing subgroup."
aliases = ["orbit representation", "Kirillov induced representation"]
domains = ["lie-groups", "representation-theory", "harmonic-analysis"]
section_mode = "progressive"
+++

Let \(G\) be a connected, simply connected nilpotent Lie group with [[lie-groups/lie-algebra|Lie algebra]] \(\mathfrak g\), let \(\ell\in\mathfrak g^*\), and choose a real [[lie-groups/polarization-of-a-coadjoint-orbit|polarization]] \(\mathfrak p\) at \(\ell\). Since the exponential map is a diffeomorphism, \(P=\exp(\mathfrak p)\) is a closed connected subgroup. Subordination gives a unitary character
\[
\chi_\ell(\exp X)=e^{i\ell(X)},\qquad X\in\mathfrak p.
\]
The **induced representation attached to \((\ell,\mathfrak p)\)** is
\[
\pi_{\ell,\mathfrak p}=\operatorname{Ind}_P^G\chi_\ell,
\]
formed by [[harmonic-analysis/unitary-induced-representation|unitary induction]]. It is a [[lie-groups/strongly-continuous-unitary-representation|strongly continuous unitary representation]] of \(G\); in the nilpotent setting it is irreducible and its equivalence class depends only on the [[differential-geometry/coadjoint-orbit|coadjoint orbit]] of \(\ell\).

## Why subordination produces a character

The condition \(\ell([\mathfrak p,\mathfrak p])=0\) makes \(i\ell|_{\mathfrak p}\) a one-dimensional representation of the Lie algebra \(\mathfrak p\). Because \(P\) is connected and simply connected, it integrates uniquely to \(\chi_\ell\). The Baker–Campbell–Hausdorff formula gives the same conclusion directly: every commutator term is annihilated by \(\ell\).

The convention \(e^{2\pi i\ell(X)}\) is also common. It amounts to rescaling the parameter \(\ell\) and must be coordinated with the chosen Fourier-transform convention.

## Independence and orbit invariance

Different polarizations at the same \(\ell\) yield unitarily equivalent representations. If \(\ell'=\operatorname{Ad}^*(g)\ell\), conjugation carries a polarization at \(\ell\) to one at \(\ell'\), and the resulting induced representations are again equivalent. Conversely, for connected simply connected nilpotent \(G\), equivalence of these representations implies that \(\ell\) and \(\ell'\) lie on the same orbit [Kirillov, §§5–6](https://doi.org/10.1070/RM1962v017n04ABEH004118).

## Heisenberg example

For the three-dimensional Heisenberg group, take \(\ell(Z)=\lambda\ne0\) on the central generator and choose \(\mathfrak p=\operatorname{span}\{Y,Z\}\). The construction induces the character \(e^{i(\eta y+\lambda z)}\) of \(P\) to the Schrödinger representation with central character \(e^{i\lambda z}\). Changing the polarization to \(\operatorname{span}\{X,Z\}\) gives its Fourier-equivalent model.

## Scope

The construction can be written for more general Lie groups, but irreducibility, independence of polarization, and exhaustion of the unitary dual can fail without the connected, simply connected, nilpotent hypotheses. Positivity or Pukánszky conditions are often imposed in broader orbit-method settings.

## References

1. A. A. Kirillov, “Unitary Representations of Nilpotent Lie Groups,” *Russian Mathematical Surveys* 17, no. 4 (1962), 53–104. [DOI record](https://doi.org/10.1070/RM1962v017n04ABEH004118). Relevant: §§5–6, polarizations, induced representations, and orbit invariance.
2. Lawrence J. Corwin and Frederick P. Greenleaf, *Representations of Nilpotent Lie Groups and Their Applications, Part I: Basic Theory and Examples*, Cambridge University Press, 1990. [Publisher front matter](https://assets.cambridge.org/97805216/04956/frontmatter/9780521604956_frontmatter.pdf). Relevant: Chapter 2, the inducing construction and polarization independence.
