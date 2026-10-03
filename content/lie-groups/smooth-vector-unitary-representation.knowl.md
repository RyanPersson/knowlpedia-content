+++
id = "lie-groups/smooth-vector-unitary-representation"
title = "Smooth vector of a Lie-group representation"
kind = "definition"
summary = "A Hilbert-space vector whose orbit map under a Lie-group representation is infinitely differentiable in norm."
aliases = ["C-infinity vector"]
domains = ["lie-groups", "harmonic-analysis"]
section_mode = "progressive"
prerequisites = ["fiber-bundles/lie-group", "lie-groups/strongly-continuous-unitary-representation", "fiber-bundles/orbit-map", "fiber-bundles/smooth-manifold", "linear-algebra/hilbert-space", "convex-analysis/linear-subspace"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(G\) be a finite-dimensional [[fiber-bundles/lie-group|Lie group]] and let \((\pi,\mathcal H)\) be a [[lie-groups/strongly-continuous-unitary-representation|strongly continuous unitary representation]]. A vector \(\xi\in\mathcal H\) is a **smooth vector** if its [[fiber-bundles/orbit-map|orbit map]]
\[
G\longrightarrow\mathcal H,\qquad g\longmapsto\pi(g)\xi,
\]
is \(C^\infty\) as a map from the [[fiber-bundles/smooth-manifold|smooth manifold]] \(G\) to the [[linear-algebra/hilbert-space|Hilbert space]] \(\mathcal H\), with differentiability taken in the norm topology. The space of all smooth vectors is denoted \(\mathcal H^\infty\). It is a \(\pi(G)\)-invariant [[convex-analysis/linear-subspace|linear subspace]] and is dense in \(\mathcal H\).

## Finite differentiability and topology

A [[lie-groups/ck-vector-unitary-representation|differentiable vector]] only requires a \(C^1\) orbit map; a smooth vector requires all orders. The [[lie-groups/smooth-vector-frechet-topology|smooth-vector Fréchet topology]] records convergence of every representation derivative and is generally stronger than the inherited Hilbert norm. Equivalently, smooth vectors form the [[lie-groups/smooth-vectors-iterated-generator-domains|intersection of all ordered generator domains]].

Some authors call a representation smooth when its smooth vectors are dense. In the finite-dimensional Lie-group setting, Gårding's theorem guarantees that property; it does not say that every Hilbert vector is smooth. For the Schrödinger representation the smooth vectors are [[lie-groups/schrodinger-smooth-vectors|exactly Schwartz functions]].

## Differentiation

For \(X\) in the [[lie-groups/lie-algebra|Lie algebra]] \(\mathfrak g\) and \(\xi\in\mathcal H^\infty\), the norm derivative
\[
d\pi(X)\xi=\left.\frac{d}{dt}\right|_{t=0}\pi(\exp(tX))\xi
\]
exists. These operators share the invariant dense domain \(\mathcal H^\infty\) and assemble into the [[lie-groups/derived-representation-on-smooth-vectors|derived representation]]. They are generally unbounded as operators on \(\mathcal H\), so their common domain is essential data.

## Density and regularization

For \(f\in C_c^\infty(G)\), the integrated vector
\[
\pi(f)\xi=\int_G f(g)\pi(g)\xi\,dg
\]
is smooth. Approximate identities of such functions converge strongly to the identity, proving the density of \(\mathcal H^\infty\); this is commonly called Gårding's argument.

## Relation to generators

For each \(X\in\mathfrak g\), [[lie-groups/stone-theorem-one-parameter-unitary-groups|Stone's theorem]] gives a self-adjoint operator \(A_X\) with \(\pi(\exp(tX))=e^{itA_X}\). On smooth vectors,
\[
d\pi(X)\xi=iA_X\xi.
\]
Thus \(d\pi(X)\) is the skew-symmetric infinitesimal action, while \(A_X\) is the self-adjoint [[lie-groups/infinitesimal-generator-unitary-representation|Stone generator]]. Neither operator should be described without its domain.

## References

1. G. Warner, *Harmonic Analysis on Semi-Simple Lie Groups I*, Springer, 1972. [DOI record](https://doi.org/10.1007/978-3-642-50275-0). Relevant: §4.4 on differentiable and smooth vectors.
