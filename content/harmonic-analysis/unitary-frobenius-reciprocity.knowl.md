+++
id = "harmonic-analysis/unitary-frobenius-reciprocity"
title = "Unitary Frobenius reciprocity"
kind = "theorem"
summary = "For a compact group, bounded intertwiners into an induced representation correspond to subgroup intertwiners."
aliases = ["Frobenius reciprocity for compact groups", "compact unitary reciprocity"]
domains = ["harmonic-analysis", "representation-theory"]
prerequisites = ["lie-groups/strongly-continuous-unitary-representation", "lie-groups/intertwining-operator-unitary-representations", "harmonic-analysis/haar-measure"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(G\) be a compact group, \(H\subseteq G\) a closed subgroup,
\(\pi\) a [[lie-groups/strongly-continuous-unitary-representation|unitary representation]] of \(G\), and \(\sigma\) a unitary representation of \(H\).
**Unitary Frobenius reciprocity** is the natural linear isomorphism
\[
\operatorname{Hom}_G\!\left(\pi,\operatorname{Ind}_H^G\sigma\right)
\cong
\operatorname{Hom}_H\!\left(\pi|_H,\sigma\right),
\]
where both sides consist of bounded
[[lie-groups/intertwining-operator-unitary-representations|intertwining operators]] and \(\operatorname{Ind}_H^G\sigma\) is unitary induction. With
normalized [[harmonic-analysis/haar-measure|Haar measure]], the correspondence can be chosen compatibly with
Hilbert adjoints. In particular, for irreducible finite-dimensional
representations it equates the relevant multiplicities.

## The intertwiner correspondence

In the equivariant-function model of
[[harmonic-analysis/unitary-induced-representation|unitary induction]], an
intertwiner \(T:\pi\to\operatorname{Ind}_H^G\sigma\) is evaluated at the
identity to obtain an \(H\)-intertwiner \(E(T):\pi|_H\to\sigma\). Conversely,
an \(H\)-intertwiner \(S\) determines
\[
(T_Sv)(x)=S\bigl(\pi(x^{-1})v\bigr).
\]
Compactness ensures that this function is square-integrable and that the
construction is bounded. The two operations are inverse.

## Multiplicity form

If \(\pi\) and \(\sigma\) are irreducible, compact-group complete
reducibility turns the isomorphism into
\[
\operatorname{mult}\!\left(\pi,\operatorname{Ind}_H^G\sigma\right)
=
\operatorname{mult}\!\left(\sigma,\pi|_H\right).
\]
For \(H=\{e\}\), this recovers that an irreducible \(\pi\) occurs in the
[[algebra-representation-theory/regular-representation|regular representation]] of \(G\) with multiplicity \(\dim\pi\).

## Noncompact warning

**Warning.** The displayed bounded-Hom formula is not a theorem for arbitrary
noncompact \(G\). If \(H=\{e\}\) and \(G\) is noncompact, the trivial
\(H\)-representation has nonzero maps from the restriction of the trivial
\(G\)-representation, whereas the left regular representation
\(\operatorname{Ind}_{\{e\}}^G1\) generally has no trivial subrepresentation.
General reciprocity results therefore use extra square-integrability or
admissibility hypotheses, different topological categories, or modified
intertwiner spaces. Mackey's analytic theory makes these domain and
boundedness issues explicit.

## References

1. Gerald B. Folland, *A Course in Abstract Harmonic Analysis*, 2nd ed., CRC Press, 2016. [DOI record](https://doi.org/10.1201/B19172). Relevant: Chapter 6, section “The Frobenius Reciprocity Theorem,” for the compact-group Hilbert-space statement.
2. George W. Mackey, “Induced Representations of Locally Compact Groups II: The Frobenius Reciprocity Theorem,” *Annals of Mathematics* 58 (1953), 193–221. [DOI record](https://doi.org/10.2307/1969786). Relevant: analytic reciprocity and the hypotheses needed beyond the finite-group setting.
