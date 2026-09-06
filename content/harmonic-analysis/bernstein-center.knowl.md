+++
id = "harmonic-analysis/bernstein-center"
title = "Bernstein center"
kind = "definition"
summary = "The algebra of natural endomorphisms of the identity functor on smooth representations of a reductive p-adic group."
aliases = ["Bernstein centre", "categorical Bernstein center", "center of the category of smooth representations"]
domains = ["harmonic-analysis", "langlands", "algebra-representation-theory"]
prerequisites = ["algebraic-geometry-foundations/reductive-algebraic-group", "harmonic-analysis/smooth-representation-totally-disconnected-group", "algebra-representation-theory/irreducible-representation", "algebra-representation-theory/schurs-lemma"]
dependency_review_count = 1
section_mode = "progressive"
+++

For a
[[algebraic-geometry-foundations/reductive-algebraic-group|reductive]]
\(p\)-adic group \(G(F)\), the **Bernstein center** is the
commutative algebra

\[
\mathfrak Z(G)=
\operatorname{End}(\operatorname{Id}_{\operatorname{Rep}(G(F))})
\]

of natural endomorphisms of the identity functor on the category of
[[harmonic-analysis/smooth-representation-totally-disconnected-group|smooth]]
complex representations.  Thus an element \(z\) assigns to every smooth
representation \(V\) an endomorphism \(z_V\), functorially in \(V\).

On an
[[algebra-representation-theory/irreducible-representation|irreducible
representation]],
[[algebra-representation-theory/schurs-lemma|Schur's lemma]] makes \(z_V\) a
scalar. The
scalar varies algebraically in unramified families.

## Bernstein variety

Under the [[harmonic-analysis/bernstein-decomposition|Bernstein
decomposition]], the center is the product of the centers of the individual
blocks.  It identifies with the ring of regular functions on the Bernstein
variety, whose components are quotients of unramified-character tori attached
to inertial supercuspidal data.

## Spectral comparison

The ordinary Bernstein center acts on representations. The
[[langlands/spectral-bernstein-center|spectral Bernstein center]] is instead
the ring of functions on the
[[langlands/stack-of-l-parameters|stack of \(L\)-parameters]].
Fargues–Scholze construct a map from the spectral center to this ordinary
center; the two terms should not be treated as synonyms. The action of
[[algebraic-geometry-foundations/perfect-complex|perfect complexes]] is the
stronger categorical [[langlands/spectral-action|spectral action]], not the
definition of the spectral center itself.

## References

1. Joseph Bernstein, “Le ‘centre’ de Bernstein,” in *Représentations des
   groupes réductifs sur un corps local*, Travaux en Cours, Hermann, 1984,
   1–32.
2. David Helm, “The Bernstein center of the category of smooth
   \(W(k)[\mathrm{GL}_n(F)]\)-modules,” *Forum of Mathematics, Sigma* 4 (2016),
   e11. [DOI](https://doi.org/10.1017/fms.2016.10).
