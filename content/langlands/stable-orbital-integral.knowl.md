+++
id = "langlands/stable-orbital-integral"
title = "Stable orbital integral"
kind = "knowl"
summary = "The sum of orbital integrals over rational conjugacy classes in one stable conjugacy class."
aliases = ["stable orbital integrals", "stable orbital distribution"]
domains = ["langlands", "harmonic-analysis", "representation-theory"]
prerequisites = ["algebra-fields-galois/local-field", "langlands/strongly-regular-semisimple-element", "langlands/stable-conjugacy", "langlands/orbital-integral", "harmonic-analysis/haar-measure"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(F\) be a
[[algebra-fields-galois/local-field|local field]] and
let \(\gamma\in G(F)\) be
[[langlands/strongly-regular-semisimple-element|strongly regular
semisimple]]. The **stable orbital integral** of
\(f\in C_c^\infty(G(F))\) is

\[
SO_\gamma(f)
=
\sum_{\gamma'}
O_{\gamma'}(f),
\]

where \(\gamma'\) ranges over representatives of the \(G(F)\)-conjugacy
classes in the [[langlands/stable-conjugacy|stable conjugacy class]] of
\(\gamma\), and the [[langlands/orbital-integral|orbital integrals]] use
compatibly transported [[harmonic-analysis/haar-measure|Haar measures]] on their centralizer tori.

## Stability

Unlike an individual orbital integral, \(SO_\gamma\) depends only on the
stable conjugacy class. A
[[langlands/stable-distribution|stable distribution]] assembled from such
expressions vanishes on
[[harmonic-analysis/test-function-space-local-group|test functions]] whose
stable orbital
integrals all vanish.

The displayed unweighted sum is the basic strongly regular definition.
Extensions to singular elements and global trace formulas can involve
Kottwitz signs, measures, or limiting procedures; those conventions must be
stated.

## Kappa refinements

The rational classes inside the stable class are parametrized by a finite
[[langlands-letter/knowls/nonabelian-h1-galois-cohomology|cohomological
kernel]] \(A_\gamma\). For a
[[algebra-representation-theory/character|character]]
\(\kappa:A_\gamma\to\mathbb C^\times\), the associated
[[langlands/kappa-orbital-integral|\(\kappa\)-orbital integral]] weights the
summands by \(\kappa\). The stable orbital integral is the case of the
trivial character.

## Endoscopic role

For an [[langlands/endoscopic-datum|endoscopic group]] \(H\), transfer seeks
a function \(f^H\) such that stable orbital integrals on \(H\) equal
transfer-factor-weighted \(\kappa\)-orbital integrals on \(G\). The
[[langlands/fundamental-lemma|fundamental lemma]] proves this matching for
the unramified unit elements, and general transfer provides matching test
functions.

## References

1. Robert P. Langlands and Diana Shelstad, “On the definition of transfer
   factors,” *Mathematische Annalen* 278 (1987), 219–271.
   [DOI](https://doi.org/10.1007/BF01458070).
2. Ngô Bảo Châu, “Survey on the fundamental lemma,” §2.2.
   [PDF](https://math.uchicago.edu/~ngo/survey.pdf).
