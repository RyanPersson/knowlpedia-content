+++
id = "algebraic-geometry-foundations/finite-etale-algebra"
title = "Finite étale algebra"
kind = "definition"
summary = "A finite algebra whose spectrum is étale over the spectrum of the base ring."
aliases = ["finite étale algebra", "finite etale algebra"]
domains = ["algebraic-geometry-foundations"]
+++

Over a field \(F\), the first examples are finite separable field extensions \(K/F\). Allowing products, such as \(K_1\times\cdots\times K_r\), is essential: finite étale geometry naturally permits several connected components.

Let \(R\) be a [[algebra-rings/commutative-ring|commutative ring]]. A commutative \(R\)-algebra \(A\) is a **finite étale \(R\)-algebra** if the induced morphism

\[
\operatorname{Spec}A\longrightarrow\operatorname{Spec}R
\]

is finite and [[algebraic-geometry-foundations/etale-morphism|étale]]. Equivalently, \(A\) is a finitely generated projective \(R\)-module and is unramified over \(R\); the latter can be expressed as

\[
\Omega^1_{A/R}=0.
\]

When \(R=F\) is a field, every finite étale algebra has the form

\[
A\cong K_1\times\cdots\times K_r
\]

for finite separable extensions \(K_i/F\). It is a field exactly when its spectrum is [[algebraic-geometry-foundations/connected-scheme|connected]].

**Warning.** Étale is the algebraic analogue of a [[algebraic-geometry-foundations/local-diffeomorphism|local diffeomorphism]], not the same notion. No classical smooth manifold underlies a general scheme, and in positive characteristic separability is indispensable.
