+++
id = "algebraic-geometry-foundations/scheme"
title = "Scheme"
kind = "definition"
summary = "A locally ringed space covered by open subsets that are affine schemes."
aliases = ["scheme"]
domains = ["algebraic-geometry-foundations"]
legacy_source_path = "algebraic-geometry-foundations/scheme.md"
+++

A **scheme** is a [[algebraic-geometry-foundations/locally-ringed-space|locally ringed space]] $(X,\mathcal O_X)$ that has an [[topology/open-cover|open cover]] $X=\bigcup_iU_i$ for which every restricted locally ringed space $(U_i,\mathcal O_X|_{U_i})$ is an [[algebraic-geometry-foundations/affine-scheme|affine scheme]].

In other words, a scheme is assembled by gluing prime spectra of commutative rings, while simultaneously gluing the algebraic functions carried by their [[algebraic-geometry-foundations/structure-sheaf|structure sheaves]].

## How to read the definition

The topological space $X$ records how algebraic loci specialize and intersect. The sheaf $\mathcal O_X$ records which functions are available on each open set, and its [[algebraic-geometry-foundations/stalk|stalk]] at a point records functions defined near that point. The affine-cover condition says that all of this data is locally controlled by commutative rings.

Maps between schemes must preserve both layers of information. These are [[algebraic-geometry-foundations/morphism-of-schemes|morphisms of schemes]], not merely continuous maps of the underlying spaces.

## Examples

Every affine scheme is a scheme, using the one-set cover. A field $k$ gives the one-point scheme $\operatorname{Spec}k$, and the [[algebraic-geometry-foundations/affine-line|affine line]] is $\operatorname{Spec}k[x]$.

The [[algebraic-geometry-foundations/projective-space|projective space]] $\mathbb P_k^n$ is generally not affine, but it is a scheme because it is covered by $n+1$ open subsets, each isomorphic to [[algebraic-geometry-foundations/affine-n-space|affine $n$-space]].
