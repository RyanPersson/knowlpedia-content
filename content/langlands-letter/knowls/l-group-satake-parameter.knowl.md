+++
id = "langlands-letter/knowls/l-group-satake-parameter"
title = "Historical L-group and Satake-parameter bridge"
kind = "knowl"
summary = "The letter's bundled passage from the L-group to the semisimple conjugacy class encoding unramified local data."
aliases = ["l-group-satake-parameter", "\\(L\\)-Group and Satake Parameter"]
domains = ["langlands-letter"]
legacy_source_path = "langlands-letter/knowls/l-group-satake-parameter.md"
section_mode = "progressive"
prerequisites = ["langlands/l-group", "langlands-letter/knowls/pinned-automorphisms", "langlands/weil-group", "langlands-letter/knowls/langlands-dual-group", "langlands/satake-parameter", "langlands-letter/knowls/semisimple-element-and-class", "langlands-letter/knowls/frobenius-unramified"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

The letter packages two now-separate notions. For a connected reductive
group \(G\), the [[langlands/l-group|\(L\)-group]] is an extension

\[
{}^LG=\widehat G\rtimes W_F
\]

after a [[langlands-letter/knowls/pinned-automorphisms|pinning]] and a
[[langlands/weil-group|Weil-group]] action on the
[[langlands-letter/knowls/langlands-dual-group|dual group]] through a finite
quotient have been chosen. At an unramified local place, a spherical
irreducible
representation determines a [[langlands/satake-parameter|Satake parameter]],
a [[langlands-letter/knowls/semisimple-element-and-class|semisimple]]
\(\widehat G\)-conjugacy class in the
[[langlands-letter/knowls/frobenius-unramified|Frobenius]] fiber of
\({}^LG\).

## Unramified class

Let \(F_v\) be a
[[algebra-fields-galois/nonarchimedean-local-field|nonarchimedean local field]], let \(G/F_v\) be
[[algebraic-geometry-foundations/unramified-reductive-group|unramified]],
and choose a
[[langlands-letter/knowls/maximal-compact-hyperspecial|hyperspecial
subgroup]] \(K_v\). If \(\pi_v^{K_v}\neq0\), the
[[langlands-letter/knowls/spherical-hecke-algebra-satake|normalized Satake
isomorphism]] sends the Hecke character on this one-dimensional space
to a class

\[
[c(\pi_v)]\subset \widehat G\rtimes\operatorname{Frob}_v.
\]

For [[langlands-letter/knowls/split-reductive-group|split]] \(G\), the Weil
action is trivial, so this is commonly recorded as
a semisimple [[algebra-groups/conjugacy-class|conjugacy class]] \(s(\pi_v)\subset\widehat G\). Arithmetic and
[[langlands-letter/knowls/frobenius-unramified|geometric Frobenius]]
conventions invert the Weil element and must be
coordinated with the Satake normalization.

## Local factor

For an algebraic representation
\(r:{}^LG\to\operatorname{GL}(V_r)\), the unramified factor is

\[
L_v(s,\pi_v,r)
=
\det\!\left(
1-r(c(\pi_v))q_v^{-s}\mid V_r
\right)^{-1}.
\]

A unitary versus arithmetic normalization can shift \(s\) by a
half-integer; the definition is complete only after that convention is
stated.

## Modern placement

The \(L\)-group exists independently of a representation. The Satake
parameter is the unramified case of a
[[langlands/local-l-parameter|local \(L\)-parameter]]. Ramified parameters
require [[langlands/weil-group|Weil]] or
[[langlands/weil-deligne-representation|Weil–Deligne data]] and cannot be
recovered from the
[[harmonic-analysis/hecke-algebra-locally-compact-group-pair|spherical Hecke algebra]].

## References

1. A. Borel, “Automorphic \(L\)-functions,” Proc. Sympos. Pure Math. 33,
   part 2, 1979, §§2–6.
2. Kevin Buzzard and Toby Gee, “The conjectural connections between
   automorphic representations and Galois representations,” §2.
   [arXiv](https://arxiv.org/abs/1009.0785).
