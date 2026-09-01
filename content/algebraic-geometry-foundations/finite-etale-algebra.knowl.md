+++
id = "algebraic-geometry-foundations/finite-etale-algebra"
title = "Finite étale algebra"
kind = "definition"
summary = "A finite algebra whose spectrum is étale over the spectrum of the base ring."
aliases = ["finite étale algebra", "finite etale algebra"]
domains = ["algebraic-geometry-foundations"]
prerequisites = ["algebra-rings/commutative-ring", "algebraic-geometry-foundations/etale-morphism"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
+++

Let \(R\) be a [[algebra-rings/commutative-ring|commutative ring]]. A commutative \(R\)-algebra \(A\) is a **finite étale \(R\)-algebra** if the induced morphism

\[
\operatorname{Spec}A\longrightarrow\operatorname{Spec}R
\]

is finite and [[algebraic-geometry-foundations/etale-morphism|étale]]. Equivalently, \(A\) is a finitely generated projective \(R\)-module and is unramified over \(R\); the latter can be expressed as

\[
\Omega^1_{A/R}=0.
\]

## Classification over a field

When \(R=F\) is a field, every finite étale algebra has the form

\[
A\cong K_1\times\cdots\times K_r
\]

for finite separable extensions \(K_i/F\). It is a field exactly when its spectrum is [[algebraic-geometry-foundations/connected-scheme|connected]].

## Remarks

Étale morphisms are algebraic analogues of [[algebraic-geometry-foundations/local-diffeomorphism|local diffeomorphisms]], but the notions are not identical. A general scheme has no underlying classical smooth manifold, and in positive characteristic separability is indispensable.
