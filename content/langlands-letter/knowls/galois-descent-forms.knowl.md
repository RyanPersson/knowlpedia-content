+++
id = "langlands-letter/knowls/galois-descent-forms"
title = "Galois Descent, Twisted Forms, and Inner Forms"
kind = "knowl"
summary = "Constructing forms of algebraic groups by Galois descent and nonabelian 1-cocycles."
aliases = ["galois-descent-forms", "Galois Descent, Twisted Forms, and Inner Forms"]
domains = ["langlands-letter"]
legacy_source_path = "langlands-letter/knowls/galois-descent-forms.md"
+++

Let $K/k$ be a finite Galois extension with group $\Gamma=\operatorname{Gal}(K/k)$, and let $G$ be a split algebraic group over $k$.

A homomorphism $\delta:\Gamma\to \operatorname{Aut}(G_K)$ whose values are compatible with the natural Galois action defines descent data on $G_K$. When this data is effective, its descent is a **twisted form** $G_\delta$ over $k$.

An **inner twist** is specified by a nonabelian $1$-cocycle $a:\Gamma\to G(K)$ satisfying
$$
a_{\sigma\tau}=a_\sigma\,{}^\sigma a_\tau.
$$
The Galois action in this identity is the action appropriate to the form being twisted. Cocycles modulo the usual coboundary equivalence form the pointed set $H^1(\Gamma,G)$.

## Remarks

In the letter, $G$ is built as a $\delta$-twist followed by an inner twist; at almost all primes, the inner cocycle becomes trivial locally.
