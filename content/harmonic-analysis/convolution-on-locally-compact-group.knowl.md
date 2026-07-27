+++
id = "harmonic-analysis/convolution-on-locally-compact-group"
title = "Convolution on a locally compact group"
kind = "definition"
summary = "The product of functions obtained by integrating one function against left translates of another."
aliases = ["group convolution", "convolution of functions on a group", "f star g"]
domains = ["harmonic-analysis", "functional-analysis", "algebra-groups"]
section_mode = "progressive"
+++

Let \(G\) be a [[topology/locally-compact-group|locally compact group]] with a fixed left [[harmonic-analysis/haar-measure|Haar measure]] \(\mu\). For functions \(f,g:G\to\mathbb C\) for which the [[measure-theory/lebesgue-integral|integral]] exists, their **convolution** is
\[
(f*g)(x)
=
\int_G f(y)g(y^{-1}x)\,d\mu(y).
\]
In particular, this formula defines \(f*g\) for compactly supported continuous functions and, up to [[measure-theory/ae-equality|almost-everywhere equality]], for \(f,g\in L^1(G)\). The order of the factors matters: unless \(G\) is abelian, \(f*g\) need not equal \(g*f\). Fixing left rather than right Haar measure also fixes the displayed convention.

## Algebraic and analytic properties

Convolution is bilinear and associative whenever the relevant integrals are defined. On \(L^1(G)\), it satisfies
\[
\lVert f*g\rVert_1\leq \lVert f\rVert_1\lVert g\rVert_1.
\]
Consequently \(L^1(G)\) becomes a [[functional-analysis/banach-algebra|Banach algebra]] under convolution. Compactly supported continuous functions are also closed under convolution. The proofs combine left invariance of Haar measure with Tonelli’s theorem and a change of variables.

## Translation interpretation

Writing \(L_y g(x)=g(y^{-1}x)\), the value \((f*g)(x)\) averages the left translates \(L_y g\), weighted by \(f(y)\). This viewpoint explains why convolution converts group representations into operators: a representation can integrate the operators assigned to group elements against \(f\).

## Involution and modular correction

For non-unimodular groups, inversion does not preserve a left Haar measure. The natural star operation on the convolution algebra must therefore include the [[harmonic-analysis/modular-function|modular function]]. The precise correction is recorded in the [[harmonic-analysis/convolution-involution|involution on a group convolution algebra]]; omitting it generally breaks the identity \((f*g)^*=g^{*}*f^{*}\).

The construction and its measure-theoretic normalization are developed in [Folland, Chapter 2](https://www.routledge.com/A-Course-in-Abstract-Harmonic-Analysis/Folland/p/book/9781032922218).

## References

1. Gerald B. Folland, *A Course in Abstract Harmonic Analysis*, 2nd ed., CRC Press, 2016. [Routledge publisher record](https://www.routledge.com/A-Course-in-Abstract-Harmonic-Analysis/Folland/p/book/9781032922218). Relevant: Chapter 2, “Convolutions.”
2. Edwin Hewitt and Kenneth A. Ross, *Abstract Harmonic Analysis*, Volume I, Springer, 1963. [Springer DOI record](https://doi.org/10.1007/978-3-662-40409-6). Relevant: “Convolutions and Group Representations.”
