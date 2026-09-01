+++
id = "langlands/local-shimura-variety"
title = "Local Shimura variety"
kind = "definition"
summary = "A tower of p-adic moduli spaces attached to local Shimura data and parametrizing bounded modifications of G-bundles."
aliases = ["local Shimura space", "local Shimura datum", "local Shimura tower"]
domains = ["langlands", "algebraic-geometry-foundations", "number-theory"]
prerequisites = ["algebraic-geometry-foundations/reductive-algebraic-group", "langlands-letter/knowls/p-adic-field", "langlands/kottwitz-set-b-g", "algebra-groups/conjugacy-class", "langlands/dominant-coweight", "algebraic-geometry-foundations/adic-space", "algebraic-geometry-foundations/v-stack", "langlands/local-shtuka", "langlands/g-bundle-on-fargues-fontaine-curve", "algebraic-geometry-foundations/tilt-and-untilt"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

A **local Shimura datum** is, in the standard unramified form, a triple

\[
(G,[b],\{\mu\}),
\]

where \(G\) is a connected
[[algebraic-geometry-foundations/reductive-algebraic-group|reductive group]]
over a [[langlands-letter/knowls/p-adic-field|\(p\)-adic field]] \(F\),
\([b]\in B(G)\) is a [[langlands/kottwitz-set-b-g|sigma-conjugacy class]], and
\(\{\mu\}\) is a [[algebra-groups/conjugacy-class|conjugacy class]] of
[[langlands/dominant-coweight|cocharacters]] satisfying the usual
acceptability condition \([b]\in B(G,\mu)\).

The associated **local Shimura variety** is a tower, indexed by compact open
level subgroups \(K\subset G(F)\), of
[[algebraic-geometry-foundations/adic-space|rigid-analytic spaces]] or
[[algebraic-geometry-foundations/v-stack|diamonds]]
\(\mathcal M_{(G,b,\mu),K}\). In the
[[langlands/local-shtuka|local-shtuka]] formulation it parametrizes
modifications of the
[[langlands/g-bundle-on-fargues-fontaine-curve|\(G\)-bundle]] determined by
\(b\) at an [[algebraic-geometry-foundations/tilt-and-untilt|untilt]], bounded
by \(\mu\), together with level structure.

## Why it is a tower

Changing \(K\) changes the amount of trivialization retained by the moduli
problem.  The inverse limit at infinite level is often a
[[algebraic-geometry-foundations/perfectoid-space|perfectoid space]] or a
diamond with commuting actions of \(G(F)\), the self-quasi-isogeny group
\(J_b(F)\), and the [[langlands/weil-group|local Weil group]] \(W_F\).

## Examples and scope

Lubin–Tate and Drinfeld towers are basic examples.  Classical
[[langlands/rapoport-zink-space|Rapoport–Zink spaces]] give many local Shimura
varieties of EL or PEL type.  The term is also used for the more general
local-shtuka spaces constructed in diamond form; not every datum has a
classical formal-scheme model.

Their
[[algebraic-geometry-foundations/compactly-supported-etale-cohomology|compactly
supported cohomology]] is expected to realize
[[langlands/local-langlands-correspondence|local Langlands]] and
Jacquet–Langlands correspondences.

## References

1. Michael Rapoport and Eva Viehmann, “Towards a theory of local Shimura
   varieties,” *Münster Journal of Mathematics* 7 (2014), 273–326.
   [arXiv](https://arxiv.org/abs/1401.2849).
2. Laurent Fargues and Peter Scholze, “Geometrization of the local Langlands
   correspondence,” 2021, Chapter IV.
   [arXiv](https://arxiv.org/abs/2102.13459).
