+++
id = "fiber-bundles/nowhere-vanishing-section"
title = "Nowhere-vanishing section"
kind = "definition"
summary = "A vector bundle section whose value is nonzero in every fiber."
aliases = ["nonvanishing section", "nowhere-zero section"]
domains = ["fiber-bundles"]
section_mode = "progressive"
+++

Let \(\pi:E\to M\) be a real or complex [[fiber-bundles/vector-bundle|vector bundle]] and let \(s:M\to E\) be a [[fiber-bundles/section-of-a-vector-bundle|section]]. The section \(s\) is **nowhere vanishing** if
\[
s(x)\neq 0_x
\]
for every \(x\in M\), where \(0_x\) is the value of the [[fiber-bundles/zero-section|zero section]] in \(E_x\). Equivalently, the image \(s(M)\) is disjoint from the image of the zero section. In the smooth category, \(s\) is required to be smooth; in the topological category, it is required to be continuous. No choice of norm is needed because nonzeroness is intrinsic to each [[linear-algebra/vector-space|vector space]] \(E_x\).

## Trivial line summand

A nowhere-vanishing section spans a rank-one subbundle
\[
L_s=\{(x,\lambda s(x))\mid x\in M,\ \lambda\in\mathbb F\}\subseteq E,
\]
canonically trivialized by \(s\). After choosing a [[fiber-bundles/bundle-metric|bundle metric]], the [[linear-algebra/orthogonal-complement|orthogonal complement]] gives a splitting
\[
E\cong \underline{\mathbb F}\oplus L_s^\perp.
\]
Conversely, a trivial line subbundle of \(E\) supplies a nowhere-vanishing section. Thus existence of such a section is equivalent to splitting off a trivial line summand, although the complementary summand is not canonical.

## Obstructions

For an oriented real rank-\(n\) vector bundle, the [[fiber-bundles/euler-class|Euler class]] is the primary obstruction to a nowhere-vanishing section. A nowhere-vanishing section forces the Euler class to vanish. The converse requires additional hypotheses and is not true as an unrestricted statement: higher obstruction classes can remain when the base has dimension greater than the rank [Milnor–Stasheff, §12](https://doi.org/10.1515/9781400881826).

## Examples and non-examples

Every [[fiber-bundles/trivial-vector-bundle-mvm|trivial vector bundle]] of positive rank has a constant nowhere-vanishing section. The [[fiber-bundles/tangent-bundle|tangent bundle]] of \(S^1\) has one, while the tangent bundle of \(S^2\) has none by the hairy-ball theorem. A section that vanishes at even one point is a decisive non-example, regardless of whether its zero is isolated.

## References

1. Dale Husemoller, *Fibre Bundles*, 3rd ed., Springer, 1994. [DOI record](https://doi.org/10.1007/978-1-4757-2261-1). Relevant: Chapter 3, sections and trivial summands of vector bundles.
2. John W. Milnor and James D. Stasheff, *Characteristic Classes*, Princeton University Press, 1974. [Publisher record](https://doi.org/10.1515/9781400881826). Relevant: §12, the Euler class as an obstruction to a nonzero section.
