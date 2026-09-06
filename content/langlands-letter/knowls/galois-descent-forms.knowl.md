+++
id = "langlands-letter/knowls/galois-descent-forms"
title = "Galois descent, twisted forms, and inner forms"
kind = "definition"
summary = "Semilinear cocycle data that descend an algebraic group and distinguish general, inner, and pure inner forms."
aliases = ["galois-descent-forms", "Galois Descent, Twisted Forms, and Inner Forms"]
domains = ["langlands-letter"]
prerequisites = ["langlands-letter/knowls/galois-extension-and-group", "algebraic-geometry-foundations/algebraic-group"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 1
legacy_source_path = "langlands-letter/knowls/galois-descent-forms.md"
section_mode = "progressive"
+++

Let \(K/k\) be a finite
[[langlands-letter/knowls/galois-extension-and-group|Galois extension]]
with group \(\Gamma\), and let \(H/K\) be an
[[algebraic-geometry-foundations/algebraic-group|algebraic group]]. A **\(K/k\)-descent datum** is a family of semilinear
isomorphisms

\[
\phi_\sigma:{}^\sigma H\longrightarrow H
\]

satisfying
\(\phi_{\sigma\tau}=\phi_\sigma\circ{}^\sigma\phi_\tau\).
For affine algebraic groups, finite Galois descent is effective.

## Forms

Fix a \(k\)-group \(G_0\). Forms of \(G_0\) split by \(K\), after choosing a
\(K\)-identification with \((G_0)_K\), are classified by

\[
H^1\!\left(\Gamma,\operatorname{Aut}(G_0)(K)\right).
\]

Changing the identification changes the cocycle by
[[langlands-letter/knowls/nonabelian-h1-galois-cohomology|nonabelian
cohomology]].

## Inner and pure inner twists

An **inner form** has class in the image of

\[
H^1(k,G_{0,\mathrm{ad}})
\longrightarrow
H^1(k,\operatorname{Aut}(G_0)).
\]

A **pure inner twist** consists of an inner twisting isomorphism
\(\psi:G_0\to G'\) over \(k_s\) together with a cocycle
\(z\in Z^1(k,G_0)\) satisfying

\[
\psi^{-1}\sigma(\psi)=\operatorname{Int}(z_\sigma).
\]

Thus a cocycle in \(G_0\) is part of the data; it is not merely a name for
the resulting \(k\)-group. Not every inner form admits a pure inner twist.

The [[langlands/refined-local-langlands-correspondence|refined local
Langlands correspondence]] often needs the still more flexible rigid
[[langlands/rigid-inner-twist|rigid inner-twist formalism]].

## Relation to the letter

The letter first descends a split group through outer automorphisms and then
modifies it by an inner class. Its requirement that the inner class become
locally trivial at almost all places is the precursor of the global
organization of local inner forms.

## References

1. Jean-Pierre Serre, *Galois Cohomology*, Springer, 1997.
2. Tasho Kaletha, “Rigid inner forms of real and \(p\)-adic groups,”
   *Annals of Mathematics* 184 (2016), 559–632.
   [DOI](https://doi.org/10.4007/annals.2016.184.2.6).
