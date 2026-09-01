+++
id = "harmonic-analysis/pontryagin-duality-theorem"
title = "Pontryagin duality theorem"
kind = "theorem"
summary = "Every locally compact abelian group is canonically isomorphic as a topological group to the Pontryagin dual of its dual."
aliases = ["double-dual theorem for LCA groups", "Pontryagin-van Kampen duality"]
domains = ["harmonic-analysis", "topology", "algebra-groups"]
prerequisites = ["topology/locally-compact-group", "algebra-groups/abelian-group", "harmonic-analysis/pontryagin-dual", "algebra-groups/group-isomorphism", "topology/homeomorphism"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(G\) be a [[topology/locally-compact-group|locally compact Hausdorff group]] that is [[algebra-groups/abelian-group|abelian]], and let \(\widehat G\) be its [[harmonic-analysis/pontryagin-dual|Pontryagin dual]], both duals carrying the compact-open topology. The **Pontryagin duality theorem** states that the evaluation homomorphism
\[
\eta_G:G\longrightarrow\widehat{\widehat G},
\qquad
\eta_G(x)(\gamma)=\gamma(x),
\]
is an [[algebra-groups/group-isomorphism|isomorphism of groups]] and a [[topology/homeomorphism|homeomorphism]]. Hence the characters of \(G\) separate its points, every continuous character of \(\widehat G\) is evaluation at a unique point of \(G\), and the topology of \(G\) is recovered by the bidual.

## Hypotheses and naturality

Local compactness and the compact-open topology are essential parts of the theorem. The maps \(\eta_G\) are natural: for a continuous homomorphism \(u:G\to H\), dualization gives \(\widehat u:\widehat H\to\widehat G\) by precomposition, and the resulting bidual map satisfies
\[
\widehat{\widehat u}\circ\eta_G=\eta_H\circ u.
\]
Thus Pontryagin duality is a contravariant equivalence on the category of locally compact abelian groups.

## Compact-discrete correspondence

Duality exchanges compact and discrete groups. If \(G\) is compact, \(\widehat G\) is discrete; if \(G\) is discrete, \(\widehat G\) is compact. It also exchanges closed subgroups with annihilator quotients, turning exact sequences into reversed exact sequences under the standard closedness hypotheses.

## Examples and limitations

The canonical evaluation maps identify
\[
\widehat{\widehat{\mathbb R}}\cong\mathbb R,\qquad
\widehat{\widehat{\mathbb Z}}\cong\mathbb Z,\qquad
\widehat{\widehat{\mathbb T}}\cong\mathbb T.
\]
Finite abelian groups are abstractly isomorphic to their duals, but such a self-duality need not be canonical; the canonical statement is the bidual isomorphism.

**Warning.** For a nonabelian group, the set of [[lie-groups/irreducible-unitary-representation|irreducible unitary representations]] is not generally a group and Pontryagin biduality does not apply to it.

## References

1. W. Rudin, *Fourier Analysis on Groups*, Wiley-Interscience, 1962. [DOI record](https://doi.org/10.1002/9781118165621). Relevant: Chapter 1, the Pontryagin duality theorem.
2. E. Hewitt and K. A. Ross, *Abstract Harmonic Analysis*, Volume I, Springer, 1963. [DOI record](https://doi.org/10.1007/978-3-662-40409-6). Relevant: character groups and duality for locally compact abelian groups.
