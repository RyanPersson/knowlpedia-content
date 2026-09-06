+++
id = "harmonic-analysis/haar-integral"
title = "Haar integral"
kind = "definition"
summary = "A nonzero positive linear functional on compactly supported continuous functions that is invariant under left translation."
aliases = ["invariant integral", "left invariant integral"]
domains = ["harmonic-analysis", "measure-theory", "topology"]
section_mode = "progressive"
prerequisites = ["topology/locally-compact-group", "operator-algebras/positive-linear-functional", "harmonic-analysis/haar-measure"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(G\) be a Hausdorff [[topology/locally-compact-group|locally compact group]], and let \(C_c(G)\) denote the complex-valued continuous functions on \(G\) with compact support. A **left Haar integral** is a nonzero [[operator-algebras/positive-linear-functional|positive linear functional]]
\[
I:C_c(G)\longrightarrow\mathbb C
\]
such that \(I(L_gf)=I(f)\) for every \(g\in G\), where \(L_gf(x)=f(g^{-1}x)\). Haar’s theorem asserts that such a functional exists and is unique up to multiplication by a positive scalar. By measure representation, it has the form
\[
I(f)=\int_G f\,d\mu
\]
for a left [[harmonic-analysis/haar-measure|Haar measure]] \(\mu\), so the functional and measure formulations are equivalent.

## Positivity and normalization

Positivity means \(I(f)\geq 0\) whenever \(f\) is real-valued and nonnegative. It forces compatibility with monotone approximation and makes \(I\) an actual [[measure-theory/lebesgue-integral|integral]], rather than merely an invariant linear functional. The uniqueness statement leaves one scale factor: choosing a normalization amounts to choosing that factor.

If \(G\) is compact, one usually normalizes \(I(1)=1\). If \(G\) is discrete, counting measure gives
\[
I(f)=\sum_{x\in G}f(x)
\]
for finitely supported \(f\). On \(\mathbb R^n\) under addition, Lebesgue integration is a Haar integral.

## Left and right invariance

Replacing [[lie-groups/left-translation|left translations]] by \(R_gf(x)=f(xg)\) defines a right Haar integral. Every locally compact group has both kinds. They coincide up to scale exactly in the [[harmonic-analysis/unimodular-group|unimodular]] case; in general, the [[harmonic-analysis/modular-function|modular function]] records how a left Haar integral changes under [[lie-groups/right-translation|right translation]].

## References

1. Gerald B. Folland, *A Course in Abstract Harmonic Analysis*, 2nd ed., CRC Press, 2016. [Routledge publisher record](https://www.routledge.com/A-Course-in-Abstract-Harmonic-Analysis/Folland/p/book/9781032922218). Relevant: Chapter 2, “Haar Measure.”
2. Edwin Hewitt and Kenneth A. Ross, *Abstract Harmonic Analysis*, Volume I, Springer, 1963. [Springer DOI record](https://doi.org/10.1007/978-3-662-40409-6). Relevant: “Invariant Functionals.”
