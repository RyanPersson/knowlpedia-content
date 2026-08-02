+++
id = "lie-groups/spherical-representation"
title = "Spherical representation"
kind = "definition"
summary = "An irreducible unitary representation of a reductive group containing a nonzero vector fixed by a maximal compact subgroup."
aliases = ["class-one representation", "K-spherical representation"]
domains = ["lie-groups", "harmonic-analysis"]
section_mode = "progressive"
+++

Let \(G\) be a
[[lie-groups/real-reductive-lie-group|real reductive Lie group]] and let
\(K\) be a
[[lie-groups/maximal-compact-subgroup-real-reductive-group|maximal compact subgroup]]. An
[[lie-groups/irreducible-unitary-representation|irreducible unitary representation]] \((\pi,H)\) of \(G\) is **\(K\)-spherical**, or **of class
one**, if
\[
H^K=\{v\in H:\pi(k)v=v\text{ for every }k\in K\}
\]
is nonzero. A nonzero member of \(H^K\) is a spherical vector. Because
\((G,K)\) is a [[lie-groups/gelfand-pair|Gelfand pair]] in the standard reductive setting,
\(\dim H^K=1\), so a unit spherical vector is unique up to a scalar of
[[real-analysis/absolute-value|absolute value]] one.

## Spherical matrix coefficient

If \(v\) is a unit spherical vector, then
\[
\varphi_\pi(g)=\langle\pi(g)v,v\rangle
\]
is \(K\)-bi-invariant, positive definite, and normalized by
\(\varphi_\pi(e)=1\). This
[[harmonic-analysis/coefficient-function|coefficient function]] is the
spherical function attached to \(\pi\).
Conversely, normalized positive-definite elementary spherical functions
recover spherical unitary representations through the
[[harmonic-analysis/gns-construction-positive-definite-function|GNS
construction for a positive-definite function]].

## Examples and representation theory

The trivial representation is spherical. Spherical [[lie-groups/principal-series-representation|principal series]] provide
the basic nontrivial family and are treated separately as
[[lie-groups/spherical-principal-series|spherical principal series]].
Spherical representations are precisely the irreducible constituents
relevant to harmonic analysis of \(K\)-bi-invariant functions and of the
[[lie-groups/riemannian-symmetric-space-noncompact-type|symmetric space]]
\(G/K\).

## Conventions and scope

Some literature defines a spherical representation for a general pair
\((G,K)\), or does not require unitarity. In that broader usage, the
one-dimensionality of \(H^K\) requires the Gelfand-pair hypothesis and is
not automatic. The present definition fixes the unitary real-reductive
setting and should not be confused with a representation of a sphere.

## References

1. Sigurdur Helgason, *Groups and Geometric Analysis: Integral Geometry, Invariant Differential Operators, and Spherical Functions*, American Mathematical Society, 2000. [AMS record](https://doi.org/10.1090/surv/039). Relevant: Chapter IV, §§2–3 on class-one representations and spherical functions.
2. Anthony W. Knapp, *Representation Theory of Semisimple Groups: An Overview Based on Examples*, Princeton University Press, 1986. [Author record](https://www.math.stonybrook.edu/~aknapp/books/repthy1.html). Relevant: Chapter VII on spherical representations and principal series.
