+++
id = "harmonic-analysis/harish-chandra-xi-function"
title = "Harish-Chandra Xi-function"
kind = "definition"
summary = "The normalized positive spherical matrix coefficient that controls decay on a real semisimple Lie group."
aliases = ["Xi function", "elementary spherical function Xi"]
domains = ["harmonic-analysis", "lie-groups"]
section_mode = "progressive"
+++

Let \(G\) be a connected
[[lie-groups/real-reductive-lie-group|real semisimple Lie group]] with finite
center, let \(K\) be a
[[lie-groups/maximal-compact-subgroup-real-reductive-group|maximal compact
subgroup]], and choose a
[[lie-groups/minimal-parabolic-subgroup|minimal parabolic subgroup]]
\(P=MAN\). In the compact realization of the unitary
[[lie-groups/spherical-principal-series|spherical principal-series
representation]] induced from the trivial representation of \(P\), let
\(v_0\) be the normalized \(K\)-fixed vector. The **Harish-Chandra
Xi-function** is the [[harmonic-analysis/coefficient-function|matrix
coefficient]]
\[
\Xi(g)=\langle \pi_0(g)v_0,v_0\rangle,\qquad g\in G.
\]
Equivalently, for the
[[lie-groups/iwasawa-decomposition|Iwasawa projection]]
\(H:G\to\mathfrak a\) and the half-sum \(\rho\) of positive
[[lie-groups/restricted-root-system|restricted roots]],
\[
\Xi(g)=\int_K e^{-\rho(H(gk))}\,dk,
\]
with Haar [[probability/probability-measure|probability measure]] on \(K\).

## Basic properties

The function \(\Xi\) is continuous, real-valued, positive, [[harmonic-analysis/positive-definite-function|positive definite]], and bi-\(K\)-invariant, with \(\Xi(e)=1\) and \(\Xi(g^{-1})=\Xi(g)\). It is the [[harmonic-analysis/spherical-function|elementary spherical function]] with spectral parameter zero. Its decay along a positive Weyl chamber is exponential up to a polynomial factor; that estimate supplies the natural weight in the [[harmonic-analysis/harish-chandra-schwartz-space|Harish-Chandra Schwartz space]].

## Example

For a compact semisimple group one may take \(K=G\). The relevant [[algebra-representation-theory/induced-representation|induced representation]] has only the constant normalized \(K\)-fixed vector, and \(\Xi(g)=1\) for every \(g\). For a noncompact semisimple group, \(\Xi\) instead decays at infinity and records the large-scale behavior of spherical [[harmonic-analysis/coefficient-function|matrix coefficients]].

## Conventions and scope

The letter \(\Xi\) is also used for variants on reductive groups and for estimates comparable to the normalized spherical coefficient. The definition above fixes the standard connected semisimple, finite-center setting. Signs in the integral formula vary with the convention for the Iwasawa projection and [[lie-groups/positive-root|positive roots]]; the matrix-coefficient definition is invariant under that bookkeeping.

## References

1. Anthony W. Knapp, *Representation Theory of Semisimple Groups: An Overview Based on Examples*, Princeton University Press, 1986. [Author-maintained record](https://www.math.stonybrook.edu/~aknapp/books/repthy1.html). Relevant: Chapter VII on principal series and elementary spherical functions.
