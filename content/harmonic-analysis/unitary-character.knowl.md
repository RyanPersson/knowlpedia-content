+++
id = "harmonic-analysis/unitary-character"
title = "Continuous unitary character"
kind = "definition"
summary = "A continuous homomorphism from a topological group to the circle group."
aliases = ["unitary character", "circle-valued character"]
domains = ["harmonic-analysis", "representation-theory"]
prerequisites = ["topology/topological-group", "algebra-groups/group-homomorphism", "lie-groups/strongly-continuous-unitary-representation"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(G\) be a [[topology/topological-group|topological group]] and let
\(\mathbb T=\{z\in\mathbb C:|z|=1\}\) be the circle group. A **continuous
unitary character** of \(G\) is a continuous
[[algebra-groups/group-homomorphism|group homomorphism]]
\[
\chi:G\longrightarrow\mathbb T.
\]
Equivalently, it is a one-dimensional
[[lie-groups/strongly-continuous-unitary-representation|strongly continuous unitary representation]] of \(G\) on \(\mathbb C\), with
\(\pi(g)z=\chi(g)z\). No commutativity hypothesis on \(G\) is needed, although
every such character is trivial on commutators and therefore factors through
the abelianization of \(G\).

## Relation to Pontryagin duality

When \(G\) is locally compact and abelian, all continuous unitary characters
form the [[harmonic-analysis/pontryagin-dual|Pontryagin dual]]
\(\widehat G\), equipped with pointwise multiplication and the compact-open
topology. For a nonabelian group, unitary characters still form an abelian
group, but they see only the abelianized quotient and do not describe the full
[[harmonic-analysis/unitary-dual|unitary dual]].

## Examples

Every continuous unitary character of \((\mathbb R,+)\) has the form
\[
\chi_t(x)=e^{2\pi i tx}
\]
for a unique \(t\in\mathbb R\). The characters of \(\mathbb Z\) are
\(n\mapsto z^n\), parametrized by \(z\in\mathbb T\). The determinant
\(\det:U(n)\to\mathbb T\) is a unitary character of the finite-dimensional
[[lie-groups/unitary-group|unitary group]].

## Terminology warning

**Warning.** This notion is not the
[[algebra-representation-theory/character|trace character of a finite-dimensional group representation]], which is generally not
multiplicative. It is also not a
[[operator-algebras/character-cstar-algebra|character of a \(C^*\)-algebra]], whose multiplication law is imposed on an algebra rather
than on a group.

## References

1. Gerald B. Folland, *A Course in Abstract Harmonic Analysis*, 2nd ed., CRC Press, 2016. [DOI record](https://doi.org/10.1201/B19172). Relevant: Chapter 4, §4.1 on dual groups and continuous characters.
2. Walter Rudin, *Fourier Analysis on Groups*, Wiley-Interscience, 1962. [Wiley DOI record](https://doi.org/10.1002/9781118165621). Relevant: Chapter 1, §1.2 on character groups.
