+++
id = "lie-groups/schrodinger-smooth-vectors"
title = "Smooth vectors of the Schrödinger representation"
kind = "theorem"
summary = "The smooth-vector space of the Heisenberg Schrödinger representation is Schwartz space, with the same topology."
aliases = ["Heisenberg smooth vectors", "Schwartz vectors for the Schrödinger representation"]
domains = ["lie-groups"]
section_mode = "progressive"
prerequisites = ["mathematical-physics/schrodinger-representation", "lie-groups/heisenberg-group", "lie-groups/smooth-vector-unitary-representation", "lie-groups/smooth-vector-frechet-topology", "functional-analysis/schwartz-space"]
+++

For the [[mathematical-physics/schrodinger-representation|Schrödinger representation]] of the [[lie-groups/heisenberg-group|real Heisenberg group]] on \(H=L^2(\mathbb R)\), the [[lie-groups/smooth-vector-unitary-representation|smooth vectors]] are precisely
\[
H^\infty=\mathcal S(\mathbb R),
\]
where \(L^2\) classes are identified with their smooth representatives. The [[lie-groups/smooth-vector-frechet-topology|smooth-vector Fréchet topology]] equals the usual [[functional-analysis/schwartz-space|Schwartz topology]].

## Why both regularity and decay appear

The infinitesimal translation and modulation operators are \(d/dx\) and \(ix\). Their ordered products require all weighted weak derivatives \(x^a f^{(b)}\) to belong to \(L^2\). The [[lie-groups/smooth-vectors-iterated-generator-domains|iterated-domain characterization]] therefore tests both spatial differentiability and decay.

Schwartz bounds imply these \(L^2\) bounds by adding a sufficiently high polynomial weight. Conversely, applying one-dimensional [[functional-analysis/sobolev-embedding-bounded-derivatives|Sobolev bounds]] to each \(x^a f^{(b)}\) makes it bounded, since it and its derivative lie in \(L^2\). These estimates in both directions identify both the space and its topology. The same statement holds on \(\mathbb R^n\), with multi-indices and sufficiently high Sobolev order.

## Pointwise smoothness is not enough

The function
\[
f(x)=(1+x^2)^{-1/2}
\]
is smooth and square-integrable, but \(xf\notin L^2\). It is not in the domain of the [[lie-groups/modulation-unitary-group|modulation generator]], so it is not a smooth vector for the Heisenberg representation. Smoothness of a representative function and smoothness of its Hilbert-valued orbit map are different requirements.

## The resulting rigging

The space of [[lie-groups/distribution-vectors-of-a-representation|distribution vectors]] is the continuous anti-dual \(\mathcal S(\mathbb R)^\times\). Thus
\[
\mathcal S(\mathbb R)\hookrightarrow L^2(\mathbb R)
\hookrightarrow\mathcal S(\mathbb R)^\times.
\]
It is the anti-linear version of the familiar tempered-distribution rigging. Unlike an arbitrary smooth-vector space, Schwartz space is nuclear.

## References

1. Rahul Garg and Sundaram Thangavelu, [*On the structure of analytic vectors for the Schrödinger representation*](https://arxiv.org/abs/1006.3265). §2, opening identification of smooth vectors with Schwartz space, and Theorem 2.2. The equivalence of topologies follows from the weighted Sobolev estimates above.
