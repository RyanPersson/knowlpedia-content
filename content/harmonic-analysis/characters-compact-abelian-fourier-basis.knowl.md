+++
id = "harmonic-analysis/characters-compact-abelian-fourier-basis"
title = "Fourier basis on a compact abelian group"
kind = "theorem"
summary = "Continuous unitary characters form an orthonormal basis for Haar L2 on a compact abelian group."
aliases = []
domains = ["harmonic-analysis"]
section_mode = "progressive"
prerequisites = ["harmonic-analysis/pontryagin-dual", "harmonic-analysis/haar-measure", "measure-theory/l2-hilbert-space", "linear-algebra/orthonormal-basis"]
+++

Let \(K\) be a compact metrizable abelian group with normalized [[harmonic-analysis/haar-measure|Haar measure]] \(m\). Its continuous unitary characters \(\widehat K\) form an orthonormal basis of \(L^2(K,m)\).

## Orthogonality

If \(\chi\) is nontrivial, choose \(a\) with \(\chi(a)\ne1\). Translation invariance gives \(\int\chi\,dm=\chi(a)\int\chi\,dm\), so the integral is zero. Apply this to \(\chi\overline\psi\) to get orthogonality; each character has norm one.

## Completeness and torus coordinates

Characters separate points; their finite linear combinations form a conjugation-stable algebra containing constants. The Stone–Weierstrass theorem gives density in continuous functions, hence in \(L^2\). For \(K=\mathbb R^d/\mathbb Z^d\), the characters are \(e_k(x)=e^{2\pi i k\cdot x}\), \(k\in\mathbb Z^d\).

This is the compact-group form of [[harmonic-analysis/plancherel-theorem-lca|Plancherel theory]]. It permits fixed functions to be tested one Fourier coefficient at a time.
