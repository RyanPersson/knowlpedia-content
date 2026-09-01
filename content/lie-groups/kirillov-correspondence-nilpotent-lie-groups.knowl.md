+++
id = "lie-groups/kirillov-correspondence-nilpotent-lie-groups"
title = "Kirillov correspondence for nilpotent Lie groups"
kind = "theorem"
summary = "The classification of irreducible unitary representations of a connected simply connected nilpotent Lie group by its coadjoint orbits."
aliases = ["orbit-method theorem for nilpotent groups", "Kirillov homeomorphism"]
domains = ["lie-groups", "representation-theory", "harmonic-analysis"]
prerequisites = ["fiber-bundles/lie-group", "lie-groups/lie-algebra", "lie-groups/orbit-method-induced-representation", "differential-geometry/coadjoint-orbit", "harmonic-analysis/unitary-dual", "topology/quotient-topology", "lie-groups/strongly-continuous-unitary-representation"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(G\) be a connected, simply connected nilpotent [[fiber-bundles/lie-group|Lie group]] with [[lie-groups/lie-algebra|Lie algebra]] \(\mathfrak g\). For \(\ell\in\mathfrak g^*\), choose a polarization and form the [[lie-groups/orbit-method-induced-representation|orbit-method induced representation]] \(\pi_\ell\). The **Kirillov correspondence** asserts that
\[
\mathfrak g^*/G\longrightarrow\widehat G,\qquad
G\ell\longmapsto[\pi_\ell],
\]
is a well-defined bijection from [[differential-geometry/coadjoint-orbit|coadjoint orbits]] onto the [[harmonic-analysis/unitary-dual|unitary dual]] of \(G\). With the [[topology/quotient-topology|quotient topology]] on \(\mathfrak g^*/G\) and the Fell topology on \(\widehat G\), this map is a homeomorphism. Thus every irreducible [[lie-groups/strongly-continuous-unitary-representation|strongly continuous unitary representation]] of \(G\) arises from a coadjoint orbit, and two such constructions are equivalent exactly when their functionals lie on the same orbit.

## Content of the theorem

Well-definedness includes independence of the chosen polarization. Injectivity identifies the orbit as the complete invariant of the [[algebra-representation-theory/induced-representation|induced representation]], while surjectivity says that no [[lie-groups/irreducible-unitary-representation|irreducible unitary representations]] are missed. The topological statement is stronger than a set-theoretic classification: convergence in the generally non-Hausdorff [[lie-groups/orbit-space|orbit space]] corresponds to Fell convergence of representations.

Kirillov's original article proves the classification by induction on the dimension of the group.

## Abelian and Heisenberg cases

If \(G\) is abelian, every coadjoint orbit is a point and the correspondence reduces to Pontryagin duality: \(\ell\) gives the character \(x\mapsto e^{i\ell(x)}\). For the [[lie-groups/heisenberg-group|Heisenberg group]], nonzero values of \(\ell\) on the center label the infinite-dimensional Schrödinger representations, while functionals vanishing on the center give one-dimensional characters.

## Hypotheses and limits

Connectedness and simple connectedness allow the Lie-algebraic data to integrate without lattice obstructions. Nilpotence supplies polarizations with the required properties and makes induction exhaustive. For solvable or semisimple groups, coadjoint orbits remain important geometric data, but the displayed map is not in general a bijection with the full unitary dual.

## References

1. A. A. Kirillov, “Unitary Representations of Nilpotent Lie Groups,” *Russian Mathematical Surveys* 17, no. 4 (1962), 53–104. [DOI record](https://doi.org/10.1070/RM1962v017n04ABEH004118). Relevant: §§5–7, construction and classification of irreducible representations.
2. Lawrence J. Corwin and Frederick P. Greenleaf, *Representations of Nilpotent Lie Groups and Their Applications, Part I: Basic Theory and Examples*, Cambridge University Press, 1990. [Publisher front matter](https://assets.cambridge.org/97805216/04956/frontmatter/9780521604956_frontmatter.pdf). Relevant: Chapter 2, the Kirillov map and its topology.
