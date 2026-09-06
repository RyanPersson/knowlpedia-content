+++
id = "lie-groups/gelfand-pair"
title = "Gelfand pair"
kind = "definition"
summary = "A locally compact group and compact subgroup whose bi-invariant convolution algebra is commutative."
aliases = ["commutative homogeneous pair", "spherical pair"]
domains = ["lie-groups", "harmonic-analysis"]
section_mode = "progressive"
prerequisites = ["topology/locally-compact-group", "harmonic-analysis/haar-measure", "lie-groups/homogeneous-space"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(G\) be a [[topology/locally-compact-group|locally compact group]] and
\(K\leq G\) a compact subgroup. The pair \((G,K)\) is a **Gelfand pair** if the
convolution algebra
\[
C_c(K\backslash G/K)
=\{f\in C_c(G):f(k_1gk_2)=f(g)\}
\]
is commutative, where convolution is formed using a
[[harmonic-analysis/haar-measure|left Haar measure]] on \(G\). Equivalently,
the \(K\)-bi-invariant part of \(L^1(G)\) is commutative.
The definition depends on the pair, not on \(G\) alone, and equips the
[[lie-groups/homogeneous-space|homogeneous space]] \(G/K\) with a commutative
spherical harmonic analysis.

## Representation-theoretic characterization

When \(G\) is second countable and
[[lie-groups/type-i-locally-compact-group|type I]], \((G,K)\) is a Gelfand
pair exactly when the
[[harmonic-analysis/quasi-regular-representation|quasi-regular representation]] of \(G\) on \(L^2(G/K)\) is multiplicity-free. Equivalently,
every [[lie-groups/irreducible-unitary-representation|irreducible unitary representation]] of \(G\) has at most one \(K\)-fixed vector. These
equivalences connect
commutativity of convolution with the one-dimensional spherical eigenspaces
that underlie spherical functions.

## Examples and non-examples

For \(n\geq 2\), the Euclidean motion pair
\((\mathbb R^n\rtimes \mathrm{SO}(n),\mathrm{SO}(n))\) is a Gelfand pair; its
spherical analysis reduces to radial Fourier analysis. Compact symmetric
pairs, such as
\((\mathrm{SO}(n+1),\mathrm{SO}(n))\), give another basic family.

If \(G\) is a nonabelian discrete group and \(K=\{e\}\), then
\(C_c(K\backslash G/K)=C_c(G)\) is the noncommutative group convolution
algebra. Thus \((G,\{e\})\) is not a Gelfand pair, although \(G/\{e\}\) is
still a homogeneous space.

## Conventions and scope

Some authors use a dense test-function algebra, the \(K\)-bi-invariant part of
\(L^1(G)\), or the convolution algebra of compactly supported
\(K\)-bi-invariant measures. For compact \(K\) these standard formulations
agree. “Commutative homogeneous space” is shorthand for the pair \((G,K)\);
it does not assert that the space \(G/K\) itself carries a group law.

## References

1. Gerald B. Folland, *A Course in Abstract Harmonic Analysis*, 2nd ed., CRC Press, 2016. [DOI record](https://doi.org/10.1201/B19172). Relevant: §9.5 on Gelfand pairs, spherical functions, and multiplicity.
2. Jacques Faraut, *Analysis on Lie Groups: An Introduction*, Cambridge University Press, 2008. [Publisher record](https://doi.org/10.1017/CBO9780511755170). Relevant: Chapter 9 on spherical analysis of the sphere and Euclidean space.
