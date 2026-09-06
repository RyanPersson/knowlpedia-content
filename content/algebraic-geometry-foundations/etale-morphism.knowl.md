+++
id = "algebraic-geometry-foundations/etale-morphism"
title = "Étale morphism"
kind = "knowl"
summary = "A scheme morphism that is flat, unramified, and locally of finite presentation."
aliases = ["etale-morphism", "Etale morphism", "Étale morphism"]
domains = ["algebraic-geometry-foundations"]
prerequisites = ["algebraic-geometry-foundations/scheme", "algebraic-geometry-foundations/flat-morphism", "algebraic-geometry-foundations/unramified-morphism", "algebraic-geometry-foundations/locally-of-finite-presentation", "algebraic-geometry-foundations/relative-kahler-differentials", "algebraic-geometry-foundations/local-diffeomorphism"]
dependency_review_count = 1
+++

A morphism \(f:Y\to X\) of [[algebraic-geometry-foundations/scheme|schemes]] is **étale** if it is simultaneously

- [[algebraic-geometry-foundations/flat-morphism|flat]],
- [[algebraic-geometry-foundations/unramified-morphism|unramified]], and
- [[algebraic-geometry-foundations/locally-of-finite-presentation|locally of finite presentation]].

These conditions are local on both source and target, so étaleness may be checked on affine open covers. For an affine morphism \(\operatorname{Spec}B\to\operatorname{Spec}A\), this says that \(B\) is a flat, finitely presented \(A\)-algebra with [[algebraic-geometry-foundations/relative-kahler-differentials|\(\Omega_{B/A}=0\)]].

For a finite field extension \(K/F\), the morphism \(\operatorname{Spec}K\to\operatorname{Spec}F\) is étale exactly when \(K/F\) is separable. Étale morphisms are therefore the algebraic-geometric analogue of [[algebraic-geometry-foundations/local-diffeomorphism|local diffeomorphisms]].
