+++
id = "lie-groups/strongly-continuous-unitary-representation"
title = "Strongly continuous unitary representation"
kind = "definition"
summary = "A unitary group representation whose orbit map at every vector is norm-continuous."
aliases = ["continuous unitary representation"]
domains = ["lie-groups", "functional-analysis"]
section_mode = "progressive"
+++

Let \(G\) be a [[topology/topological-group|topological group]] and \(\mathcal H\) a complex [[linear-algebra/hilbert-space|Hilbert space]]. A **strongly continuous unitary representation** of \(G\) on \(\mathcal H\) is a [[algebra-groups/group-homomorphism|group homomorphism]]
\[
\pi:G\longrightarrow \mathcal U(\mathcal H)
\]
such that, for every \(\xi\in\mathcal H\), the [[fiber-bundles/orbit-map|orbit map]] \(g\mapsto\pi(g)\xi\) is continuous in the norm of \(\mathcal H\). Thus “strongly” refers to pointwise norm continuity of the operators, not norm continuity of \(g\mapsto\pi(g)\) in the [[linear-algebra/operator-norm|operator norm]]. The representation is unitary because every \(\pi(g)\) preserves the Hilbert-space [[linear-algebra/inner-product|inner product]].

## Equivalent continuity tests

Strong continuity is equivalent to continuity of the action map \(G\times\mathcal H\to\mathcal H\), \((g,\xi)\mapsto\pi(g)\xi\). The [[lie-groups/weak-strong-continuity-equivalence-unitary-representations|weak–strong continuity theorem]] says it is also equivalent to continuity of every matrix coefficient \(g\mapsto\langle\pi(g)\xi,\eta\rangle\): weak continuity implies strong continuity by applying the coefficient identity to \(\|\pi(g)\xi-\pi(g_0)\xi\|^2\) [Folland, opening of §3.1]. These equivalences require unitarity, which supplies uniform norm control.

## Examples and consequences

Every norm-continuous homomorphism \(G\to\mathcal U(\mathcal H)\) is strongly continuous, but the converse can fail in infinite dimension. For a [[topology/locally-compact-group|locally compact group]], the left [[algebra-representation-theory/regular-representation|regular representation]] on \(L^2(G)\), given by \((\lambda(g)f)(x)=f(g^{-1}x)\), is strongly continuous. Strong continuity is precisely the regularity needed to obtain [[lie-groups/infinitesimal-generator-unitary-representation|infinitesimal generators]] from [[lie-groups/one-parameter-subgroup|one-parameter subgroups]].

## Conventions and scope

Some authors say simply “unitary representation” and include strong continuity in the term. For a discrete group the condition is automatic. A finite-dimensional [[lie-groups/representation-of-a-lie-group|representation of a Lie group]] is often formulated using smoothness; the present notion is designed to include infinite-dimensional Hilbert spaces and does not assert operator-norm continuity.

## References

1. Gerald B. Folland, *A Course in Abstract Harmonic Analysis*, 2nd ed., CRC Press, 2016. [DOI record](https://doi.org/10.1201/B19172). Relevant: §3.1 on unitary representations and continuity.
2. Bachir Bekka, Pierre de la Harpe, and Alain Valette, *Kazhdan's Property (T)*, Cambridge University Press, 2008. [Author record](https://www.math.univ-toulouse.fr/~bekka/KazhdanTotal.pdf). Relevant: Appendix A on unitary representations.
