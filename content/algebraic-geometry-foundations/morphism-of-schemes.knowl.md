+++
id = "algebraic-geometry-foundations/morphism-of-schemes"
title = "Morphism of schemes"
kind = "knowl"
summary = "A continuous map of schemes equipped with a compatible local map of structure sheaves."
aliases = ["morphism-of-schemes", "Morphism of schemes", "scheme morphism"]
domains = ["algebraic-geometry-foundations"]
prerequisites = ["algebraic-geometry-foundations/morphism-of-locally-ringed-spaces", "topology/continuous-map", "algebraic-geometry-foundations/morphism-of-sheaves", "algebraic-geometry-foundations/structure-sheaf", "algebraic-geometry-foundations/direct-image-sheaf", "algebraic-geometry-foundations/stalk", "algebra-rings/ring-homomorphism", "algebraic-geometry-foundations/affine-scheme"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
legacy_source_path = "algebraic-geometry-foundations/morphism-of-schemes.md"
+++

A **morphism of schemes** \(f:X\to Y\) is a [[algebraic-geometry-foundations/morphism-of-locally-ringed-spaces|morphism of locally ringed spaces]]. It consists of a [[topology/continuous-map|continuous map]] of underlying spaces and a compatible [[algebraic-geometry-foundations/morphism-of-sheaves|morphism]] of [[algebraic-geometry-foundations/structure-sheaf|structure sheaves]] into a [[algebraic-geometry-foundations/direct-image-sheaf|direct image sheaf]]:
\[
f^\#:\mathcal O_Y\longrightarrow f_*\mathcal O_X.
\]
For every \(x\in X\), the induced map on [[algebraic-geometry-foundations/stalk|stalks]]
\[
f_x^\#:\mathcal O_{Y,f(x)}\longrightarrow\mathcal O_{X,x}
\]
must be a **local** ring homomorphism: the inverse image of the target's maximal ideal is the source's maximal ideal.

The basic example comes from a [[algebra-rings/ring-homomorphism|ring homomorphism]] \(\varphi:A\to B\). It induces a morphism of [[algebraic-geometry-foundations/affine-scheme|affine schemes]]
\[
\operatorname{Spec}B\longrightarrow\operatorname{Spec}A,
\qquad \mathfrak q\longmapsto\varphi^{-1}(\mathfrak q).
\]
The reversed direction is fundamental: \(\operatorname{Spec}\) is contravariant. In particular, a field inclusion \(F\hookrightarrow K\) gives \(\operatorname{Spec}K\to\operatorname{Spec}F\).
