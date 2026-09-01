+++
id = "harmonic-analysis/unitary-induced-representation"
title = "Induced unitary representation"
kind = "definition"
summary = "A unitary representation built from a closed-subgroup representation on square-integrable sections over a homogeneous space."
aliases = ["unitary induction", "Mackey induction"]
domains = ["harmonic-analysis", "representation-theory"]
prerequisites = ["topology/locally-compact-group", "lie-groups/strongly-continuous-unitary-representation", "harmonic-analysis/quasi-invariant-measure", "linear-algebra/hilbert-space", "lie-groups/left-translation"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(G\) be a second-countable [[topology/locally-compact-group|locally compact Hausdorff group]], \(H\subseteq G\) a closed subgroup, and
\((\sigma,V)\) a
[[lie-groups/strongly-continuous-unitary-representation|strongly continuous unitary representation]] of \(H\). Form the Hilbert bundle
\(G\times_HV\to G/H\), where
\((x,v)\sim(xh,\sigma(h)^{-1}v)\). Given a
[[harmonic-analysis/quasi-invariant-measure|quasi-invariant measure]]
\(\mu\) on \(G/H\), the **induced unitary representation**
\(\operatorname{Ind}_H^G\sigma\) acts on the [[linear-algebra/hilbert-space|Hilbert space]] of
square-integrable measurable sections. Its action is [[lie-groups/left-translation|left translation]] of
sections, multiplied by the square root of the appropriate Radon–Nikodym
derivative so that every operator is unitary.

## Explicit action and measure independence

Write \(r_g=d(g_*\mu)/d\mu\), with \(g_*\mu(E)=\mu(g^{-1}E)\). If
\(g\cdot-\) denotes the natural map from the fiber over \(g^{-1}xH\) to the
fiber over \(xH\), then
\[
\bigl(\operatorname{Ind}_H^G\sigma(g)s\bigr)(xH)
=r_g(xH)^{1/2}\,g\cdot s(g^{-1}xH).
\]
The Radon–Nikodym cocycle gives the representation law, and a change to an
equivalent quasi-invariant measure is implemented by multiplication by the
square root of its density. Hence the unitary-equivalence class is independent
of the chosen measure within the canonical measure class.

## Equivariant-function model

After choosing measurable trivializations, vectors can instead be represented
by [[measure-theory/measurable-function|measurable functions]] \(F:G\to V\) satisfying
\[
F(xh)=\sigma(h)^{-1}F(x).
\]
Their norm is an integral over \(G/H\), with a density or modular correction
determined by the chosen quotient-measure convention. This model is useful for
calculations, but omitting that correction is legitimate only in invariant
measure situations. The bundle model packages the same data without making a
choice of coset representatives.

## Basic examples and structure

Induction from the trivial representation of \(H\) gives the
[[harmonic-analysis/quasi-regular-representation|quasi-regular representation]] on \(L^2(G/H)\). Taking \(H=\{e\}\) gives the left
[[harmonic-analysis/regular-representations-locally-compact-group|regular representation]] of \(G\). Induction respects Hilbert direct sums and is
transitive along chains of closed subgroups. It is also characterized by the
[[harmonic-analysis/system-of-imprimitivity|system of imprimitivity]] carried by multiplication operators on the base
\(G/H\).

## Conventions and scope

**Warning.** The notation \(\operatorname{Ind}_H^G\) is also used for
algebraic induction, compact induction, smooth induction, and normalized
parabolic induction. Those constructions live in different categories and
need not have the same underlying space. Here “induced” means Mackey's
Hilbert-space construction, including the measure-class correction that makes
the representation unitary.

## References

1. Gerald B. Folland, *A Course in Abstract Harmonic Analysis*, 2nd ed., CRC Press, 2016. [DOI record](https://doi.org/10.1201/B19172). Relevant: Chapter 6, §6.1 on the inducing construction.
2. George W. Mackey, “Induced Representations of Locally Compact Groups I,” *Annals of Mathematics* 55 (1952), 101–139. [DOI record](https://doi.org/10.2307/1969423). Relevant: the Hilbert-space induction construction and its measure-class invariance.
