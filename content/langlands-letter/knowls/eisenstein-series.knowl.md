+++
id = "langlands-letter/knowls/eisenstein-series"
title = "Eisenstein series on a reductive group"
kind = "knowl"
summary = "An automorphic series formed from parabolically induced cuspidal data, with meromorphic continuation and intertwining-operator functional equations."
aliases = ["eisenstein-series", "Eisenstein Series on a Reductive Group"]
domains = ["langlands-letter"]
prerequisites = ["algebraic-geometry-foundations/reductive-algebraic-group", "langlands-letter/knowls/global-local-fields-completions", "algebraic-geometry-foundations/parabolic-subgroup", "algebraic-geometry-foundations/levi-subgroup", "algebraic-geometry-foundations/unipotent-radical", "lie-groups/k-finite-vector", "langlands/cuspidal-automorphic-representation"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
legacy_source_path = "langlands-letter/knowls/eisenstein-series.md"
section_mode = "progressive"
+++

Let \(G\) be a connected [[algebraic-geometry-foundations/reductive-algebraic-group|reductive group]] over a
[[langlands-letter/knowls/global-local-fields-completions|global field]]
\(F\), let \(P=MN\) be a
[[algebraic-geometry-foundations/parabolic-subgroup|parabolic subgroup]]
with [[algebraic-geometry-foundations/levi-subgroup|Levi subgroup]] \(M\)
and [[algebraic-geometry-foundations/unipotent-radical|unipotent radical]]
\(N\), and let \(\phi_\lambda\) be a suitable
[[lie-groups/k-finite-vector|\(K\)-finite]] section of a normalized
representation induced from
[[langlands/cuspidal-automorphic-representation|cuspidal automorphic data]]
on \(M(\mathbb A_F)\). The associated **Eisenstein series** is

\[
E(g,\phi,\lambda)
=
\sum_{\gamma\in P(F)\backslash G(F)}
\phi_\lambda(\gamma g),
\]

initially for \(\operatorname{Re}(\lambda)\) in a sufficiently positive
chamber.

## Analytic continuation and functional equations

Langlands proved that \(E(g,\phi,\lambda)\) has meromorphic continuation in
the complex spectral parameter \(\lambda\). Its
[[langlands/automorphic-constant-term|constant terms]] are finite
sums of global intertwining operators. Relations among normalized
intertwining operators give the Weyl-group functional equations.

In rank one, \(\lambda\) is often written as a single complex variable
\(s\); for a higher-rank Levi it belongs to the complex dual of the real
split-center space of \(M\).

## Spectral role

Values of Eisenstein series generate the
[[langlands/continuous-automorphic-spectrum|continuous automorphic
spectrum]].
Residues at suitable poles can be square-integrable and generate the
[[langlands/residual-automorphic-spectrum|residual automorphic spectrum]].
Thus Eisenstein series organize the noncuspidal part of the automorphic
spectral decomposition recursively from cuspidal data on Levi subgroups.

## L-functions

Normalizing factors of global intertwining operators are built from ratios
of automorphic
[[langlands-letter/knowls/euler-product-and-local-factor|\(L\)-functions]]
in many settings. Their analytic behavior can
therefore imply meromorphic continuation and functional equations for those
\(L\)-functions. This is a method with hypotheses, not a universal
consequence for every representation of every \(L\)-group.

## Relation to the letter

The letter recognizes Eisenstein series as a route from functorial
representation data to analytic properties of Euler products. Modern
theory separates the induced representation, the meromorphic family, its
constant terms, and the resulting spectral constituents.

## References

1. Robert P. Langlands, *On the Functional Equations Satisfied by
   Eisenstein Series*, Lecture Notes in Mathematics 544, Springer, 1976.
   [DOI](https://doi.org/10.1007/BFb0075618).
2. C. Mœglin and J.-L. Waldspurger, *Spectral Decomposition and Eisenstein
   Series*, Cambridge University Press, 1995.
   [DOI](https://doi.org/10.1017/CBO9780511629358).
