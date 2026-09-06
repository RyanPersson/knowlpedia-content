+++
id = "harmonic-analysis/convolution-involution"
title = "Involution on a group convolution algebra"
kind = "definition"
summary = "The convolution involution reverses a function by group inversion, complex conjugation, and the modular correction."
aliases = ["group-algebra involution", "convolution star operation", "f-star"]
domains = ["harmonic-analysis", "functional-analysis", "operator-algebras"]
prerequisites = ["topology/locally-compact-group", "harmonic-analysis/haar-measure", "harmonic-analysis/modular-function"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(G\) be a [[topology/locally-compact-group|locally compact group]], let
\(\mu\) be a left [[harmonic-analysis/haar-measure|Haar measure]], and let
\(\Delta\) be its [[harmonic-analysis/modular-function|modular function]], with
\(\int_G h(xg)\,d\mu(x)=\Delta(g)^{-1}\int_G h(x)\,d\mu(x)\). For
\(f\in L^1(G,\mu)\), the **convolution involution** is
\[
f^*(x)=\Delta(x^{-1})\,\overline{f(x^{-1})}
\]
for almost every \(x\in G\). Together with
\((f*g)(x)=\int_G f(y)g(y^{-1}x)\,d\mu(y)\), this operation makes
\(L^1(G,\mu)\) a Banach \(*\)-algebra: it is conjugate-linear,
\((f^*)^*=f\), \((f*g)^*=g^* * f^*\), and
\(\lVert f^*\rVert_1=\lVert f\rVert_1\).

## Why the modular factor is present

Group inversion need not preserve a left Haar measure. The factor
\(\Delta(x^{-1})\) is exactly the Radon–Nikodym correction that compensates
for this change of measure. It makes the integrated form of a
[[lie-groups/strongly-continuous-unitary-representation|strongly continuous
unitary representation]]
satisfy
\(\pi(f^*)=\pi(f)^*\), where
\(\pi(f)=\int_G f(x)\pi(x)\,d\mu(x)\). Thus this convention is compatible with
[[harmonic-analysis/integrated-form-unitary-representation|integrated representations]].

## The unimodular case

If \(G\) is [[harmonic-analysis/unimodular-group|unimodular]], then
\(\Delta=1\), so the formula reduces to
\(f^*(x)=\overline{f(x^{-1})}\). Dropping the modular factor on a
nonunimodular group generally destroys both the \(L^1\)-isometry and the
adjoint identity for integrated representations.

## Conventions and scope

**Warning.** Some authors define the modular function by the reciprocal
translation formula. Under that convention the displayed power of
\(\Delta\) is correspondingly reversed. The definition above is tied to the
stated right-translation identity and to left Haar measure.

## References

1. Gerald B. Folland, *A Course in Abstract Harmonic Analysis*, 2nd ed., CRC Press, 2016. [DOI record](https://doi.org/10.1201/B19172). Relevant: §§2.4 and 3.1 on convolution, involution, and integrated representations.
