+++
id = "algebraic-geometry-foundations/scheme"
title = "Scheme"
kind = "knowl"
summary = "A locally ringed space covered by open subsets that are affine schemes."
aliases = ["scheme"]
domains = ["algebraic-geometry-foundations"]
legacy_source_path = "algebraic-geometry-foundations/scheme.md"
+++

A **scheme** is a [[algebraic-geometry-foundations/locally-ringed-space|locally ringed space]] \((X,\mathcal O_X)\) that has an [[topology/open-cover|open cover]] \(X=\bigcup_iU_i\) for which every restricted locally ringed space \((U_i,\mathcal O_X|_{U_i})\) is an [[algebraic-geometry-foundations/affine-scheme|affine scheme]]. Thus schemes are spaces obtained by gluing prime spectra of commutative rings while also gluing their local algebraic functions.

Every affine scheme is a scheme, using the one-set cover. A field \(k\) gives the one-point scheme \(\operatorname{Spec}k\), and the [[algebraic-geometry-foundations/affine-line|affine line]] is \(\operatorname{Spec}k[x]\). The [[algebraic-geometry-foundations/projective-space|projective space]] \(\mathbb P_k^n\) is generally not affine, but it is a scheme because it is covered by \(n+1\) open subsets, each isomorphic to [[algebraic-geometry-foundations/affine-n-space|affine \(n\)-space]]. Maps between schemes must preserve both the topology and this local ring structure; these are [[algebraic-geometry-foundations/morphism-of-schemes|morphisms of schemes]].
