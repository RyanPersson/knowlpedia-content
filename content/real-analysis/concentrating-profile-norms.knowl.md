+++
id = "real-analysis/concentrating-profile-norms"
title = "Norms of an anisotropically concentrating profile"
kind = "lemma"
summary = "The amplitude and volume factors in the Lp norm of a rescaled fixed profile."
aliases = []
domains = ["real-analysis"]
section_mode = "progressive"
prerequisites = ["real-analysis/anisotropic-dilation", "measure-theory/lp-space", "real-analysis/change-of-variables-formula", "measure-theory/essential-supremum"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

Let \(V\in L^p(\mathbb R^d)\), \(1\le p\le\infty\), and set \(u_\tau(x)=\tau^{-a}V(D_\tau^{-1}x)\), where \(D_\tau\) has exponents \(b_i\). Then
\[
\|u_\tau\|_{L^p}=\tau^{-a+(b_1+\cdots+b_d)/p}\|V\|_{L^p},
\]
with \(1/\infty=0\). The [[measure-theory/lp-space|norm]] is finite under the stated hypothesis on \(V\).

## Proof

For finite \(p\), substitute \(x=D_\tau y\) in \(\int|u_\tau|^p\,dx\); the volume factor is \(\tau^{\sum b_i}\). For \(p=\infty\), an invertible linear change of variables preserves null sets and the essential supremum of the profile.

## Energy and peak size

The squared \(L^2\) norm scales as \(\tau^{-2a+\sum b_i}\), whereas \(\|u_\tau\|_\infty=\tau^{-a}\|V\|_\infty\). Thus if \(0<2a<\sum b_i\), a nonzero bounded profile has growing peak size but vanishing squared \(L^2\) norm. This scaling observation alone proves no PDE solution exists.
