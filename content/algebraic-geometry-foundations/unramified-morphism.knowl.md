+++
id = "algebraic-geometry-foundations/unramified-morphism"
title = "Unramified morphism"
kind = "knowl"
summary = "A locally finite type scheme morphism whose relative differentials vanish."
aliases = ["unramified-morphism", "Unramified morphism"]
domains = ["algebraic-geometry-foundations"]
+++

A morphism \(f:Y\to X\) of [[algebraic-geometry-foundations/scheme|schemes]] is **unramified** if it is [[algebraic-geometry-foundations/locally-of-finite-type|locally of finite type]] and its [[algebraic-geometry-foundations/relative-kahler-differentials|sheaf of relative Kähler differentials]] vanishes:
\[
\Omega_{Y/X}=0.
\]
Equivalently, for a locally finite type morphism, the [[algebraic-geometry-foundations/diagonal-morphism|diagonal]]
\[
\Delta_f:Y\longrightarrow Y\times_XY
\]
is an open immersion.

Affine-locally, \(\operatorname{Spec}B\to\operatorname{Spec}A\) is unramified when \(B\) is a finitely generated \(A\)-algebra and \(\Omega_{B/A}=0\). This condition is local on source and target.

For a finite field extension \(K/F\), the morphism \(\operatorname{Spec}K\to\operatorname{Spec}F\) is unramified exactly when \(K/F\) is [[algebra-fields-galois/separable-extension|separable]].
