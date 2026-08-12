+++
id = "langlands/stable-conjugacy"
title = "Stable conjugacy"
kind = "knowl"
summary = "Conjugacy over an algebraic closure, retaining the Galois descent class of the centralizer."
aliases = ["stably conjugate", "stable conjugacy class"]
domains = ["langlands", "algebraic-geometry-foundations", "number-theory"]
section_mode = "progressive"
+++

Let \(G\) be a connected [[algebraic-geometry-foundations/reductive-algebraic-group|reductive group]] over a field \(F\). Two
[[langlands/strongly-regular-semisimple-element|strongly regular semisimple]]
elements \(\gamma,\gamma'\in G(F)\) are **stably conjugate** if they are
conjugate over an
[[algebra-fields-galois/algebraic-closure|algebraic closure]]: there is
\(g\in G(\overline F)\) such that

\[
\gamma'=g\gamma g^{-1}.
\]

For more general semisimple elements, the standard definition additionally
requires the cocycle \(g^{-1}\sigma(g)\) to lie in the identity component of
the [[algebra-groups/centralizer|centralizer]] \(G_\gamma\) for every
\(\sigma\) in the
[[langlands-letter/knowls/galois-extension-and-group|absolute Galois group]]
\(\operatorname{Gal}(\overline F/F)\).

## Rational classes inside a stable class

Fix strongly regular \(\gamma\) and write \(T=G_\gamma\). The
\(G(F)\)-conjugacy classes in its stable class are parametrized by a kernel in
[[langlands-letter/knowls/nonabelian-h1-galois-cohomology|nonabelian Galois
cohomology]]:

\[
\ker\!\left[
H^1(F,T)\longrightarrow H^1(F,G)
\right].
\]

Thus stable conjugacy is coarser than rational conjugacy. Over a
[[algebra-fields-galois/local-field|local field]],
the displayed kernel is finite.

For \(\operatorname{GL}_n\), two regular semisimple elements that are
conjugate over \(\overline F\) are already conjugate over \(F\), so a stable
class contains one rational class. Other groups can have several.

## Stable invariants

For a split group, the adjoint quotient \(G\to T/W\) records a
characteristic-polynomial-like invariant. On the strongly regular locus,
two elements have the same adjoint-quotient value exactly when they are
stably conjugate.

## Role in endoscopy

Ordinary [[langlands/orbital-integral|orbital integrals]] distinguish
rational [[algebra-groups/conjugacy-class|conjugacy classes]]. Endoscopy reorganizes their combinations into
[[langlands/stable-distribution|stable distributions]], beginning with
[[langlands/stable-orbital-integral|stable orbital integrals]]. Matching
stable classes on an endoscopic group and on \(G\) is a prerequisite for
defining the [[langlands/transfer-factor|transfer factor]].

## References

1. Robert E. Kottwitz, “Stable trace formula: elliptic singular terms,”
   *Mathematische Annalen* 275 (1986), 365–399.
   [DOI](https://doi.org/10.1007/BF01458611).
2. Ngô Bảo Châu, “Survey on the fundamental lemma,” §2.1.
   [PDF](https://math.uchicago.edu/~ngo/survey.pdf).
