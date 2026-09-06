+++
id = "langlands/hecke-eigensheaf"
title = "Hecke eigensheaf"
kind = "definition"
summary = "An automorphic sheaf on Bun_G whose geometric Hecke transforms are governed by a dual-group local system."
aliases = ["Hecke eigen-D-module", "automorphic eigensheaf"]
domains = ["langlands"]
section_mode = "progressive"
prerequisites = ["langlands/g-local-system", "langlands/hecke-functor", "fiber-bundles/local-system"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(E\) be a \(\widehat G\)-[[langlands/g-local-system|local system]] on
\(X\). A **Hecke eigensheaf with eigenvalue \(E\)** is an automorphic
\(D\)-module \(\mathcal F\) on \(\operatorname{Bun}_G(X)\), together with
compatible isomorphisms
\[
H_V(\mathcal F)\simeq \mathcal F\boxtimes E_V
\]
for every finite-dimensional representation \(V\) of \(\widehat G\). Here
[[langlands/hecke-functor|\(H_V\)]] is the geometric Hecke functor and
\(E_V\) is the vector [[fiber-bundles/local-system|local system]] associated to \(E\) through \(V\).

The isomorphisms must be tensor-compatible in \(V\) and compatible with
fusion at several points. A single eigen-isomorphism for one representation
is generally not enough.

## Pointwise and categorical forms

Constructing \(\mathcal F_E\) for an individual \(E\) is the eigensheaf form
of geometric Langlands. The categorical form organizes all spectral
parameters at once as an equivalence of sheaf categories.

## Scope

For reducible or otherwise singular spectral parameters, eigensheaves can
have derived multiplicities and automorphisms. The modern formulation is
therefore not a naive bijection between isomorphism classes.

## References

1. Alexander Beilinson and Vladimir Drinfeld, *Quantization of Hitchin’s
   Integrable System and Hecke Eigensheaves*, preprint.
   [author manuscript](https://math.uchicago.edu/~drinfeld/langlands/QuantizationHitchin.pdf).
2. Edward Frenkel, Dennis Gaitsgory, and Kari Vilonen, “On the geometric
   Langlands conjecture,” *Journal of the American Mathematical Society* 15
   (2002), 367–417. [arXiv](https://arxiv.org/abs/math/0012255).
