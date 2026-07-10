+++
id = "algebraic-geometry-foundations/finite-morphism"
title = "Finite morphism"
kind = "knowl"
summary = "A scheme morphism that is affine and is locally induced by a ring map making the target a finite module over the source."
aliases = ["finite-morphism", "Finite morphism"]
domains = ["algebraic-geometry-foundations"]
+++

A morphism \(f:Y\to X\) of [[algebraic-geometry-foundations/scheme|schemes]] is **finite** if every affine open \(U=\operatorname{Spec}A\subseteq X\) has affine inverse image
\[
f^{-1}(U)=\operatorname{Spec}B
\]
and \(B\) is a finitely generated \(A\)-module through the induced [[algebra-rings/ring-homomorphism|ring homomorphism]] \(A\to B\).

It is enough to verify this condition on an affine open cover of \(X\). Thus finiteness is affine-local on the target, whereas the definition of a finite morphism is global.

For a field extension \(K/F\), the morphism \(\operatorname{Spec}K\to\operatorname{Spec}F\) is finite exactly when \(K\) is finite-dimensional over \(F\), that is, when \(K/F\) is a finite [[algebra-fields-galois/field-extension|field extension]].
