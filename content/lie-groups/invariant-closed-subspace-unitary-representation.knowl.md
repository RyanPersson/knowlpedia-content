+++
id = "lie-groups/invariant-closed-subspace-unitary-representation"
title = "Invariant closed subspace of a unitary representation"
kind = "definition"
summary = "A closed Hilbert subspace preserved by every operator in a unitary group representation."
aliases = ["reducing subspace", "invariant Hilbert subspace"]
domains = ["lie-groups", "harmonic-analysis"]
section_mode = "progressive"
+++

Let \((\pi,\mathcal H)\) be a [[lie-groups/strongly-continuous-unitary-representation|strongly continuous unitary representation]] of a group \(G\). A [[linear-algebra/closed-linear-subspace|closed linear subspace]] \(M\subseteq\mathcal H\) is **invariant** if
\[
\pi(g)M\subseteq M\qquad\text{for every }g\in G.
\]
Because \(g^{-1}\in G\), this inclusion implies \(\pi(g)M=M\). Unitarity then makes the [[linear-algebra/orthogonal-complement|orthogonal complement]] \(M^\perp\) invariant as well, so \(M\) is reducing and
\[
\mathcal H=M\oplus M^\perp
\]
is an orthogonal decomposition into subrepresentations.

## Restricted representations

The restriction \(\pi|_M:G\to U(M)\) is again strongly continuous: each [[fiber-bundles/orbit-map|orbit map]] is the restriction of an orbit map in \(\mathcal H\). The [[linear-algebra/orthogonal-projection|orthogonal projection]] \(P_M\) commutes with every \(\pi(g)\), and conversely a commuting orthogonal projection has invariant range. Thus invariant closed subspaces correspond exactly to orthogonal projections in the commutant of the representation.

## Irreducibility and decomposition

The representation is **irreducible** when its only invariant closed subspaces are \(\{0\}\) and \(\mathcal H\). Closedness matters in infinite dimension: an invariant dense proper [[convex-analysis/linear-subspace|linear subspace]] does not contradict unitary irreducibility. Direct-sum and direct-integral decomposition theory studies representations through families of invariant closed subspaces and their associated projections [Folland, §3.1](https://doi.org/10.1201/B19172).

## Conventions and scope

For a single nonunitary operator or a semigroup representation, invariance of \(M\) need not imply invariance of \(M^\perp\); then “invariant” and “reducing” are distinct. Their coincidence here uses both inverses in \(G\) and the unitarity of every \(\pi(g)\).

## References

1. G. B. Folland, *A Course in Abstract Harmonic Analysis*, 2nd ed., CRC Press, 2016. [DOI record](https://doi.org/10.1201/B19172). Relevant: §3.1 on invariant subspaces and irreducible unitary representations.
