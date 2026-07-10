+++
id = "algebraic-geometry-foundations/flat-morphism"
title = "Flat morphism"
kind = "knowl"
summary = "A scheme morphism whose induced homomorphisms on local rings are flat."
aliases = ["flat-morphism", "Flat morphism"]
domains = ["algebraic-geometry-foundations"]
+++

A morphism \(f:Y\to X\) of [[algebraic-geometry-foundations/scheme|schemes]] is **flat at** \(y\in Y\) if the induced homomorphism of local rings
\[
\mathcal O_{X,f(y)}\longrightarrow \mathcal O_{Y,y}
\]
makes \(\mathcal O_{Y,y}\) a [[algebra-modules/flat-module|flat module]] over \(\mathcal O_{X,f(y)}\). The morphism is **flat** if it is flat at every point of \(Y\).

Affine-locally, a morphism \(\operatorname{Spec}B\to\operatorname{Spec}A\) is flat exactly when \(B\) is a flat \(A\)-module. Flatness is local on both source and target.

Every field extension \(K/F\) is a vector space over \(F\), hence a flat \(F\)-module. Therefore \(\operatorname{Spec}K\to\operatorname{Spec}F\) is flat.
