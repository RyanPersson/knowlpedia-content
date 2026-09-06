+++
id = "lie-groups/orbit-method"
title = "Orbit method"
kind = "definition"
summary = "A program relating irreducible unitary representations of a Lie group to symplectic coadjoint orbits."
aliases = ["Kirillov orbit method", "method of coadjoint orbits"]
domains = ["lie-groups", "representation-theory", "differential-geometry"]
prerequisites = ["lie-groups/irreducible-unitary-representation", "fiber-bundles/lie-group", "differential-geometry/coadjoint-orbit", "lie-groups/polarization-of-a-coadjoint-orbit"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

The **orbit method** is the representation-theoretic program that associates irreducible [[lie-groups/irreducible-unitary-representation|unitary representations]] of a [[fiber-bundles/lie-group|Lie group]] \(G\) with its [[differential-geometry/coadjoint-orbit|coadjoint orbits]] in \(\mathfrak g^*\), interpreting each orbit as a classical symplectic phase space and its representation as a quantization. For a connected, simply connected nilpotent Lie group, the precise Kirillov correspondence sends the orbit of \(\ell\) to the equivalence class of the representation induced from the character \(e^{i\ell}\) of a subgroup integrating a [[lie-groups/polarization-of-a-coadjoint-orbit|polarization at \(\ell\)]]. In this setting it is a bijection \(\mathfrak g^*/G\to\widehat G\), independent of the polarization chosen.

## The nilpotent correspondence

For connected simply connected nilpotent \(G\), the [[lie-groups/exponential-map-lie-group|exponential map]] is a diffeomorphism and every \(\ell\in\mathfrak g^*\) admits a polarization. If \(P=\exp(\mathfrak p)\), Kirillov constructs
\[
\pi_\ell=\operatorname{Ind}_P^G\chi_\ell,\qquad
\chi_\ell(\exp X)=e^{i\ell(X)}.
\]
The representation is irreducible; changing \(\ell\) within its coadjoint orbit or changing the polarization does not change its unitary-equivalence class; and every irreducible unitary representation arises this way. With the [[topology/quotient-topology|quotient topology]] on \(\mathfrak g^*/G\) and the [[harmonic-analysis/fell-topology|Fell topology]] on \(\widehat G\), the correspondence is a homeomorphism.

## Geometry encoded by an orbit

Each orbit carries the [[differential-geometry/kirillov-kostant-souriau-form|Kirillov–Kostant–Souriau symplectic form]]. Orbit dimension predicts the number of variables in an induced model, stabilizers control the inducing subgroup, and [[fiber-bundles/invariant-function|invariant functions]] on \(\mathfrak g^*\) reflect central or infinitesimal-character data. For [[algebra-groups/nilpotent-group|nilpotent groups]], the orbit method also yields character and Plancherel formulas.

## Examples and limitations

For an [[lie-groups/abelian-lie-group|abelian Lie group]], every coadjoint orbit is a point and the method reduces to the classification by unitary characters. For the [[lie-groups/heisenberg-group|Heisenberg group]], nonzero central values give the familiar infinite-dimensional Schrödinger representations. For compact or noncompact semisimple groups, however, raw coadjoint orbits do not stand in a simple bijection with the [[harmonic-analysis/unitary-dual|unitary dual]]: integrality, admissible orbit data, coverings, and choices of quantization intervene. Kirillov’s survey explicitly separates the nilpotent success from these later obstacles.

## Conventions and scope

**Warning.** “Orbit method” can mean the exact Kirillov classification for nilpotent groups or the broader coadjoint-orbit philosophy. The core states both and labels their scopes. It should not be read as asserting a universal bijection \(\mathfrak g^*/G\cong\widehat G\) for every Lie group.

## References

1. A. A. Kirillov, *Lectures on the Orbit Method*, Graduate Studies in Mathematics 64, American Mathematical Society, 2004. [AMS record](https://bookstore.ams.org/GSM/64). Relevant: Chapters 1–5, especially Chapter 3.
2. A. A. Kirillov, “Merits and Demerits of the Orbit Method,” *Bulletin of the American Mathematical Society* 36 (1999), 433–488. [DOI record](https://doi.org/10.1090/S0273-0979-99-00849-6). Relevant: §§2–4.
3. Lawrence J. Corwin and Frederick P. Greenleaf, *Representations of Nilpotent Lie Groups and Their Applications, Part I: Basic Theory and Examples*, Cambridge Studies in Advanced Mathematics 18, Cambridge University Press, 1990. [Publisher front matter](https://assets.cambridge.org/97805216/04956/frontmatter/9780521604956_frontmatter.pdf). Relevant: Chapters 1–4.
