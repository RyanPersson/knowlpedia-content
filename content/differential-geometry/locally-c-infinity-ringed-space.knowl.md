+++
id = "differential-geometry/locally-c-infinity-ringed-space"
title = "Locally C-infinity-ringed space"
kind = "definition"
summary = "A space with a sheaf of C-infinity rings whose stalks are local, with morphisms preserving all smooth operations."
aliases = ["locally C∞-ringed space", "local C-infinity ringed space", "C-infinity locally ringed space"]
domains = ["differential-geometry", "algebraic-geometry-foundations"]
section_mode = "progressive"
+++

A **locally \(C^\infty\)-ringed space** is a pair
\((X,\mathcal O_X)\) in which \(X\) is a topological space and
\(\mathcal O_X\) is a sheaf of
[[differential-geometry/c-infinity-ring|\(C^\infty\)-rings]] whose stalks
are local rings after forgetting the extra smooth operations. A morphism
\[
(f,f^\#):(X,\mathcal O_X)\longrightarrow(Y,\mathcal O_Y)
\]
consists of a continuous map \(f:X\to Y\) and a morphism
\[
f^\#:\mathcal O_Y\longrightarrow f_*\mathcal O_X
\]
of sheaves of \(C^\infty\)-rings that induces local homomorphisms on stalks.

Forgetting the operations \(\Phi_g\) but retaining addition and
multiplication produces an
[[algebraic-geometry-foundations/locally-ringed-space|ordinary locally
ringed space]]. The converse is false: a sheaf of real algebras need not
carry, or determine, operations for every smooth
\(g:\mathbb R^n\to\mathbb R\).

## Smooth manifolds as structured spaces

Every smooth manifold \(M\) determines
\[
(M,C^\infty_M).
\]
Here \(C^\infty_M\) is its
[[differential-geometry/sheaf-of-smooth-functions|sheaf of smooth
functions]].
Each point has a neighborhood for which this pair is isomorphic to
\((U,C^\infty_U)\) for an open subset \(U\subseteq\mathbb R^n\).
Conversely, a Hausdorff second-countable locally \(C^\infty\)-ringed space
locally modeled in this way recovers a smooth manifold. Morphisms between
these manifold models correspond exactly to smooth maps.

## Broader smooth spaces

General locally \(C^\infty\)-ringed spaces need not be manifolds. Allowing
quotient \(C^\infty\)-rings and more general local models admits singular and
infinitesimal smooth spaces. Accordingly, “locally \(C^\infty\)-ringed” is
the ambient structured-space notion; “locally modeled on open subsets of
Euclidean space” is the additional manifold condition.

## References

1. Dominic Joyce, “Algebraic Geometry over \(C^\infty\)-rings,” *Memoirs of the AMS* 260 (2019). [arXiv version](https://arxiv.org/abs/1001.0023). Relevant: §§2–3, local \(C^\infty\)-rings and \(C^\infty\)-ringed spaces.
2. Ieke Moerdijk and Gonzalo E. Reyes, *Models for Smooth Infinitesimal Analysis*, Springer, 1991. [DOI record](https://doi.org/10.1007/978-1-4757-4148-6). Relevant: Chapter I, smooth algebras and loci.
