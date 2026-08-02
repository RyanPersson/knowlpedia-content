+++
id = "langlands-letter/knowls/galois-descent-forms"
title = "Galois Descent, Twisted Forms, and Inner Forms"
kind = "definition"
summary = "Semilinear cocycle data that descend an algebraic group and classify its forms."
aliases = ["galois-descent-forms", "Galois Descent, Twisted Forms, and Inner Forms"]
domains = ["langlands-letter"]
legacy_source_path = "langlands-letter/knowls/galois-descent-forms.md"
+++

Let \(K/k\) be a finite Galois extension with group
\(\Gamma=\operatorname{Gal}(K/k)\), and let \(H\) be an algebraic group over \(K\). A **\(K/k\)-descent datum** on \(H\) is a family of semilinear isomorphisms
\[
\phi_\sigma:{}^\sigma H\longrightarrow H
\qquad(\sigma\in\Gamma)
\]
satisfying the cocycle condition
\[
\phi_{\sigma\tau}
=
\phi_\sigma\circ{}^\sigma\!\phi_\tau.
\]
For affine algebraic groups, finite Galois descent is effective: such data determine an algebraic group over \(k\), uniquely up to isomorphism, whose base change to \(K\) is \(H\).

## Classification of forms

Let \(G_0\) be an algebraic group over \(k\). After choosing a \(K\)-isomorphism between a \(K/k\)-form and \((G_0)_K\), the descent datum becomes a nonabelian \(1\)-cocycle in
\(\operatorname{Aut}((G_0)_K)\). Forms split by \(K\) are therefore classified by
\[
H^1\!\left(\Gamma,\operatorname{Aut}(G_0)(K)\right).
\]
Changing the chosen \(K\)-isomorphism changes the cocycle by the usual cohomology relation.

## Inner and pure inner forms

An **inner form** is represented by a class in the image of
\[
H^1(\Gamma,G_{0,\mathrm{ad}}(K))
\longrightarrow
H^1(\Gamma,\operatorname{Aut}(G_0)(K)),
\]
where \(G_{0,\mathrm{ad}}\) acts by inner automorphisms. A cocycle
\(a:\Gamma\to G_0(K)\) satisfying
\[
a_{\sigma\tau}=a_\sigma\,{}^\sigma a_\tau.
\]
defines a **pure inner form**. These notions coincide only under additional hypotheses, so the coefficient group should not be suppressed.

## Role in the letter

In the letter, a group is first obtained from an outer descent datum and then modified by an inner class. At almost all primes, the inner class is required to become trivial after restriction to the local Galois group.
