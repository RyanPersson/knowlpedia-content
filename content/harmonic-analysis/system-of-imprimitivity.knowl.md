+++
id = "harmonic-analysis/system-of-imprimitivity"
title = "System of imprimitivity"
kind = "definition"
summary = "A system of imprimitivity is a unitary representation together with a projection-valued measure covariant for a group action."
aliases = ["covariant projection-valued measure", "imprimitivity system"]
domains = ["harmonic-analysis", "representation-theory"]
section_mode = "progressive"
prerequisites = ["topology/locally-compact-group", "linear-algebra/hilbert-space", "lie-groups/strongly-continuous-unitary-representation", "functional-analysis/projection-valued-measure"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let a [[topology/locally-compact-group|locally compact group]] \(G\) act measurably on a standard Borel space \(X\). A **system of imprimitivity** for this action on a complex [[linear-algebra/hilbert-space|Hilbert space]] \(\mathcal H\) is a pair \((U,P)\), where \(U\) is a [[lie-groups/strongly-continuous-unitary-representation|strongly continuous unitary representation]] of \(G\) on \(\mathcal H\) and \(P\) is a [[functional-analysis/projection-valued-measure|projection-valued measure]] on \(X\), such that
\[
U(g)P(E)U(g)^{-1}=P(gE)
\]
for every \(g\in G\) and every Borel set \(E\subseteq X\). The equation is the covariance axiom linking the representation to the action on measurable subsets.

## Function-algebra formulation

Integrating bounded [[measure-theory/measurable-function|measurable functions]] against \(P\) gives a representation \(M_P\) by operators on \(\mathcal H\). Covariance becomes
\[
U(g)M_P(f)U(g)^{-1}=M_P(f\circ g^{-1}).
\]
Thus a system of imprimitivity can equivalently be viewed as a covariant representation of the action on functions. The projection-valued and function-algebra formulations contain the same information.

## Transitive actions and induction

When \(X=G/H\) is a
[[harmonic-analysis/locally-compact-homogeneous-space|locally compact
homogeneous space]] for a closed subgroup \(H\), Mackey's [[harmonic-analysis/mackey-imprimitivity-theorem|imprimitivity
theorem]] classifies systems based on \(G/H\) by unitary representations of
\(H\). The associated representation of \(G\) is induced from \(H\), and
\(P(E)\) acts by multiplication by the indicator of \(E\). This equivalence
is the main bridge between induction and spectral localization.

## Examples and non-examples

For the translation action of \(G\) on itself, let \(\mathcal H=L^2(G)\), let \(U\) be the [[harmonic-analysis/regular-representations-locally-compact-group|left regular representation]], and let \(P(E)\) multiply by \(1_E\). This is a system of imprimitivity. Pairing the same \(P\) with a representation that does not transport supports according to the action fails the covariance axiom.

**Warning.** A projection-valued measure alone is only spectral data. A unitary representation alone is only dynamical data. The term “system of imprimitivity” applies to the covariant pair.

## References

1. George W. Mackey, “Imprimitivity for Representations of Locally Compact Groups I,” *Proceedings of the National Academy of Sciences* 35 (1949), 537–545. [DOI record](https://doi.org/10.1073/pnas.35.9.537). Relevant: the transitive imprimitivity theorem.
2. Gerald B. Folland, *A Course in Abstract Harmonic Analysis*, 2nd ed., CRC Press, 2016. [DOI record](https://doi.org/10.1201/B19172). Relevant: §6.3, systems of imprimitivity and induced representations.
