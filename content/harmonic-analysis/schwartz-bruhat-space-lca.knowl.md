+++
id = "harmonic-analysis/schwartz-bruhat-space-lca"
title = "Schwartz–Bruhat space on a locally compact abelian group"
kind = "definition"
summary = "The canonical test-function space on a locally compact abelian group, assembled from Schwartz functions on elementary quotients."
aliases = ["Bruhat space", "Schwartz-Bruhat space", "Bruhat test functions"]
domains = ["harmonic-analysis", "functional-analysis"]
section_mode = "progressive"
prerequisites = ["topology/locally-compact-group", "algebra-groups/generated-subgroup", "functional-analysis/schwartz-space"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(G\) be a [[topology/locally-compact-group|locally compact abelian
group]]. Its **Schwartz–Bruhat space** \(\mathcal S(G)\) consists of
functions obtained as follows: choose an open, compactly [[algebra-groups/generated-subgroup|generated subgroup]]
\(H\subseteq G\) and a compact subgroup \(K\subseteq H\) such that \(H/K\)
is an elementary group, pull a Schwartz function on \(H/K\) back along the
quotient map, and extend it by zero outside \(H\). Here an elementary group
has the form
\(\mathbb R^n\times\mathbb Z^m\times\mathbb T^r\times F\), with \(F\)
finite. Its Euclidean factor uses the
[[functional-analysis/schwartz-space|ordinary Schwartz space]], while the
discrete directions are rapidly decreasing and the torus directions are
smooth. The locally convex topology is the corresponding inductive-limit
topology.

## Structural role

The construction is independent of the auxiliary pair \((H,K)\): enlarging \(H\) or shrinking \(K\) gives compatible transition maps. Translation, reflection, multiplication by characters, and [[harmonic-analysis/convolution-on-locally-compact-group|convolution]] preserve \(\mathcal S(G)\). After compatible [[harmonic-analysis/haar-measure|Haar measures]] are chosen, the [[harmonic-analysis/fourier-transform-lca|Fourier transform]] is a topological isomorphism
\[
\mathcal S(G)\longrightarrow \mathcal S(\widehat G),
\]
where \(\widehat G\) is the [[harmonic-analysis/pontryagin-dual|Pontryagin dual]]. This Fourier-invariant construction is the principal reason to use the Schwartz–Bruhat space rather than compactly supported continuous functions.

## Standard cases

For \(G=\mathbb R^n\), one recovers the ordinary Schwartz space. If \(G\) is discrete, the space consists of rapidly decreasing functions on each finitely generated subgroup, extended by zero. If \(G\) is compact, every test function factors through a compact Lie quotient; thus \(\mathcal S(G)\) is generally larger than the locally constant functions unless \(G\) is totally disconnected.

## Conventions and scope

The notations \(\mathcal S(G)\), \(\mathcal D(G)\), and “Bruhat space” vary across sources. The quotient-based definition is essential: a general locally compact [[algebra-groups/abelian-group|abelian group]] need not itself be a [[fiber-bundles/lie-group|Lie group]] or admit coordinates in which derivatives and polynomial weights can be written directly.

## References

1. François Bruhat, “Distributions sur un groupe localement compact et applications à l’étude des représentations des groupes \(p\)-adiques,” *Bulletin de la Société Mathématique de France* 89 (1961), 43–75. [DOI record](https://doi.org/10.24033/bsmf.1559). Relevant: pp. 60–61 on rapidly decreasing test functions and Fourier transformation.
