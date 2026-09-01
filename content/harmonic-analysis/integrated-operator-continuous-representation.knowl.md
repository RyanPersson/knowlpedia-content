+++
id = "harmonic-analysis/integrated-operator-continuous-representation"
title = "Integrated operator of a continuous representation"
kind = "construction"
summary = "The operator obtained by averaging a strongly continuous Banach- or Fréchet-space representation against a compactly supported function."
aliases = ["integrated operator", "integrated continuous representation", "integrated Banach representation"]
domains = ["harmonic-analysis", "lie-groups", "functional-analysis"]
prerequisites = ["topology/locally-compact-group", "harmonic-analysis/haar-measure", "linear-algebra/banach-space", "functional-analysis/frechet-space"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(G\) be a [[topology/locally-compact-group|locally compact Hausdorff
group]] with left [[harmonic-analysis/haar-measure|Haar measure]], and let
\(\pi:G\to\operatorname{GL}(E)\) be a strongly continuous representation on
a [[linear-algebra/banach-space|Banach space]]. For \(f\in C_c(G)\), its
**integrated operator** is
\[
\pi(f)v=\int_G f(g)\pi(g)v\,dg .
\]
This Bochner integral exists because \(\{\pi(g):g\in\operatorname{supp}f\}\)
is uniformly bounded. It defines a bounded operator on \(E\) and satisfies
\(\pi(f*h)=\pi(f)\pi(h)\). The same construction works on a complete
[[functional-analysis/frechet-space|Fréchet space]] using its
locally-convex vector integral. Without a compatible Hilbert-space unitary
structure, \(f\mapsto\pi(f)\) is not asserted to preserve involution or to be
a \(*\)-representation.

## Banach-space estimate

If \(K=\operatorname{supp}f\) and
\(M_K=\sup_{g\in K}\lVert\pi(g)\rVert\), then
\[
\lVert\pi(f)v\rVert
\leq M_K\lVert f\rVert_{L^1(G)}\lVert v\rVert .
\]
Strong continuity and the [[functional-analysis/uniform-boundedness-principle|uniform boundedness principle]] make \(M_K\) finite.
This estimate is local in \(G\): a continuous representation need not be
uniformly bounded on the whole group, so its integrated action need not
extend continuously from \(C_c(G)\) to all of \(L^1(G)\).

## Fréchet-space interpretation

Suppose \(E\) is Fréchet and the action \(G\times E\to E\) is continuous.
For each compact \(K\subseteq G\), the operators \(\pi(g)\), \(g\in K\), form
an [[real-analysis/equicontinuous-family|equicontinuous family]]. Completeness permits integration of the
compactly-supported [[topology/continuous-map|continuous map]] \(g\mapsto f(g)\pi(g)v\). For every
continuous seminorm \(p\) on \(E\), equicontinuity supplies a continuous
seminorm \(q\) and \(C_K>0\) such that
\[
p(\pi(f)v)\leq C_K\lVert f\rVert_1q(v).
\]
Hence \(\pi(f)\) is a continuous linear endomorphism of \(E\).

## Convolution and smoothing

For \(f,h\in C_c(G)\), [[measure-theory/fubinis-theorem|Fubini's theorem]] and
\(\pi(xy)=\pi(x)\pi(y)\) give
\[
\pi(f*h)=\pi(f)\pi(h).
\]
When \(G\) is a [[fiber-bundles/lie-group|Lie group]] and \(f\in C_c^\infty(G)\), these operators are the
basic smoothing operators used to form the
[[lie-groups/garding-subspace|Gårding subspace]]. Approximate identities
supported near the identity recover vectors in the original topology under
the usual continuity hypotheses.

## Unitary specialization and warning

If \(E\) is a [[linear-algebra/hilbert-space|Hilbert space]] and \(\pi\) is unitary, the construction becomes
the [[harmonic-analysis/integrated-form-unitary-representation|integrated
form of a unitary representation]]. It then extends to \(L^1(G)\), is
contractive, and respects the [[harmonic-analysis/convolution-involution|group-algebra involution]].

For a general nonunitary representation, convolution multiplicativity still
holds on \(C_c(G)\), but
\(\pi(f^*)=\pi(f)^*\) is unavailable or false. In particular, the integrated
operator used for an admissible nonunitary representation must not be cited
as though it were a unitary \(*\)-representation.

## References

1. Lars Gårding, “Note on Continuous Representations of Lie Groups,” *Proceedings of the National Academy of Sciences* 33 (1947), 331–332. [DOI record](https://doi.org/10.1073/pnas.33.11.331). Relevant: integration of continuous representations against compactly supported smooth functions.
2. François Trèves, *Topological Vector Spaces, Distributions and Kernels*, Academic Press, 1967. [Elsevier book record](https://shop.elsevier.com/books/topological-vector-spaces-distributions-and-kernels/treves/978-1-4831-9859-0). Relevant: vector-valued integration and continuous linear maps on complete locally convex spaces.
3. Joseph Bernstein and Bernhard Krötz, “Smooth Fréchet globalizations of Harish-Chandra modules,” *Israel Journal of Mathematics* 199 (2014), 45–111. [DOI record](https://doi.org/10.1007/s11856-013-0056-1). Relevant: §1 on continuous and smooth Fréchet representations.
