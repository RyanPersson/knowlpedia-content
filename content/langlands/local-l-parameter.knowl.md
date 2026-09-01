+++
id = "langlands/local-l-parameter"
title = "Local Langlands parameter"
kind = "definition"
summary = "An admissible homomorphism from the local Langlands group to the L-group of a reductive group."
aliases = ["local L-parameter", "Langlands parameter", "admissible L-parameter"]
domains = ["langlands", "harmonic-analysis"]
prerequisites = ["algebra-fields-galois/local-field", "langlands/weil-group", "algebraic-geometry-foundations/reductive-algebraic-group", "langlands/l-group", "langlands-letter/knowls/semisimple-element-and-class", "langlands-letter/knowls/langlands-dual-group"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(F\) be a
[[algebra-fields-galois/local-field|local field]], let
\(W_F\) denote its [[langlands/weil-group|Weil group]], and let \(G\) be a
connected [[algebraic-geometry-foundations/reductive-algebraic-group|reductive
\(F\)-group]].  The local Langlands group used here is

\[
L_F=
\begin{cases}
W_F, & F\text{ archimedean},\\
W_F\times\operatorname{SL}_2(\mathbb C), & F\text{ nonarchimedean}.
\end{cases}
\]

A **local Langlands parameter**, or **local \(L\)-parameter**, is an admissible
continuous homomorphism

\[
\varphi:L_F\longrightarrow{}^LG
\]

to the [[langlands/l-group|\(L\)-group]] whose composite with
\({}^LG\to W_F\) is the natural projection, whose
restriction to \(\operatorname{SL}_2(\mathbb C)\) is algebraic when that factor
is present, and whose Weil-group elements have
[[langlands-letter/knowls/semisimple-element-and-class|semisimple]]
[[langlands-letter/knowls/langlands-dual-group|dual-group]] part.
Parameters are considered up to conjugation by \(\widehat G\).

## Relevance

For a non-[[algebraic-geometry-foundations/quasi-split-reductive-group|quasi-split]]
[[langlands-letter/knowls/galois-descent-forms|inner form]], not every parameter for the common
\(L\)-group corresponds to a representation of that particular form. A
parameter is **relevant** to \(G\) when every [[algebraic-geometry-foundations/parabolic-subgroup|parabolic subgroup]] of
\({}^LG\) containing its image corresponds to a parabolic subgroup defined
for \(G\). Basic local Langlands uses relevant parameters.

## Tempered and discrete parameters

A parameter is **tempered** when the image of \(W_F\) in \(\widehat G\) is
bounded after the standard projection, and **discrete** when its image is not
contained in any proper
[[algebraic-geometry-foundations/levi-subgroup|Levi subgroup]] of
\({}^LG\). These conditions parallel
[[harmonic-analysis/tempered-representation-p-adic-group|tempered]] and
[[lie-groups/square-integrable-modulo-center-representation|essentially
square-integrable]] representations.

A parameter trivial on the Deligne \(\operatorname{SL}_2\) has zero
[[langlands/weil-deligne-group|monodromy]]. An unramified parameter is
additionally trivial on the
[[algebra-fields-galois/inertia-subgroup|inertia subgroup]] and is determined
by a [[langlands/satake-parameter|Satake parameter]].

## Weil–Deligne form for \(\mathrm{GL}_n\)

For \(G=\operatorname{GL}_n\), a parameter is equivalently an
\(n\)-dimensional Frobenius-semisimple
[[langlands/weil-deligne-representation|Weil–Deligne representation]].

## References

1. Armand Borel, “Automorphic \(L\)-functions,” in *Automorphic Forms,
   Representations and \(L\)-Functions*, Proceedings of Symposia in Pure
   Mathematics 33, part 2, 1979, §§8–10.
2. Tasho Kaletha, “Representations of reductive groups over local fields,”
   §2.1, 2022. [arXiv](https://arxiv.org/abs/2201.07741).
