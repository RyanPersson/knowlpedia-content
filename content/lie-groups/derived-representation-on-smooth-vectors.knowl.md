+++
id = "lie-groups/derived-representation-on-smooth-vectors"
title = "Derived representation on smooth vectors"
kind = "definition"
summary = "The Lie-algebra representation obtained by differentiating a strongly continuous unitary representation on its smooth vectors."
aliases = ["infinitesimal representation", "differential of a unitary representation"]
domains = ["lie-groups", "functional-analysis"]
section_mode = "progressive"
+++

Let \(G\) be a finite-dimensional [[fiber-bundles/lie-group|Lie group]] with
[[lie-groups/lie-algebra|Lie algebra]] \(\mathfrak g\), and let \(\pi\) be a
[[lie-groups/strongly-continuous-unitary-representation|strongly continuous
unitary representation]] on a [[linear-algebra/hilbert-space|Hilbert space]]
\(\mathcal H\). On the common dense invariant subspace \(\mathcal H^\infty\)
of [[lie-groups/smooth-vector-unitary-representation|smooth vectors]], its
**derived representation** is
\[
d\pi(X)v=\left.\frac{d}{dt}\right|_{t=0}\pi(\exp(tX))v,
\qquad X\in\mathfrak g,\quad v\in\mathcal H^\infty.
\]
The map \(X\mapsto d\pi(X)\) is a [[lie-groups/representation-of-a-lie-algebra|Lie-algebra representation]] by generally unbounded operators sharing the domain \(\mathcal H^\infty\).

## Domain and invariance

The smooth-vector space is preserved both by \(\pi(G)\) and by every
\(d\pi(X)\). Thus iterated expressions such as
\(d\pi(X_1)\cdots d\pi(X_k)v\) are defined on one canonical domain, rather
than on an intersection chosen separately for each product. With its standard
Fréchet topology, \(\mathcal H^\infty\) is a continuous
[[algebra-modules/module|module]] over the
[[lie-groups/universal-enveloping-algebra|universal enveloping algebra]]
\(U(\mathfrak g_{\mathbb C})\). The density and invariance of this space are
basic smooth-vector results [Warner, §4.4].

## Relation to one-parameter generators

For fixed \(X\), the curve \(t\mapsto\pi(\exp(tX))\) is a strongly continuous
one-parameter unitary group. By
[[lie-groups/stone-theorem-one-parameter-unitary-groups|Stone's theorem]], the
operator \(d\pi(X)\) on \(\mathcal H^\infty\) is skew-symmetric, is
essentially skew-adjoint, and its closure is the infinitesimal generator of
that group. Equivalently, if the
self-adjoint-generator convention writes
\(\pi(\exp(tX))=e^{itA_X}\), then \(d\pi(X)=iA_X\) on smooth vectors. This
factor of \(i\) explains an important convention difference between Lie
representation theory and spectral theory.

## Algebraic identities and equivariance

For \(X,Y\in\mathfrak g\) and \(v\in\mathcal H^\infty\),
\[
d\pi([X,Y])v
=\bigl(d\pi(X)d\pi(Y)-d\pi(Y)d\pi(X)\bigr)v.
\]
The group and infinitesimal actions are compatible through
\[
\pi(g)d\pi(X)\pi(g)^{-1}v=d\pi(\operatorname{Ad}(g)X)v.
\]
These identities hold on the smooth domain; treating the operators as
everywhere-defined bounded operators is generally incorrect. If the original
representation is finite-dimensional and smooth, this construction reduces to
the ordinary differential of a Lie-group representation.

## References

1. Garth Warner, *Harmonic Analysis on Semi-Simple Lie Groups I*, Springer, 1972. [Springer DOI record](https://doi.org/10.1007/978-3-642-50275-0). Relevant: §4.4 on differentiable and smooth vectors.
2. V. S. Varadarajan, *Lie Groups, Lie Algebras, and Their Representations*, Springer, 1984. [Springer DOI record](https://doi.org/10.1007/978-1-4612-1126-6). Relevant: Chapter 4 on differentiating representations.
