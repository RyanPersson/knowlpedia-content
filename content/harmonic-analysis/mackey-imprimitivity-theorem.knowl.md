+++
id = "harmonic-analysis/mackey-imprimitivity-theorem"
title = "Mackey imprimitivity theorem"
kind = "theorem"
summary = "Transitive systems of imprimitivity are exactly those obtained by inducing representations from stabilizer subgroups."
aliases = ["imprimitivity theorem", "imprimitivity classification"]
domains = ["harmonic-analysis", "representation-theory"]
section_mode = "progressive"
+++

Let \(G\) be a second-countable
[[topology/locally-compact-group|locally compact Hausdorff group]], let \(H\)
be a closed subgroup, and let \(X=G/H\). The **Mackey imprimitivity theorem**
states that every [[harmonic-analysis/system-of-imprimitivity|system of imprimitivity]] \((U,P)\) for the [[algebra-groups/transitive-action|transitive action]] of \(G\) on \(X\) is
unitarily equivalent to one obtained from a
[[lie-groups/strongly-continuous-unitary-representation|strongly continuous unitary representation]] \(\sigma\) of \(H\): the representation \(U\) is
\(\operatorname{Ind}_H^G\sigma\), and \(P(E)\) acts on its section model by
multiplication by \(1_E\). The representation \(\sigma\) is determined up to
unitary equivalence by \((U,P)\).

## From a stabilizer to a system

Starting with \(\sigma\), form the
[[harmonic-analysis/unitary-induced-representation|induced representation]]
on \(L^2\)-sections of \(G\times_HV_\sigma\to G/H\). Multiplication by bounded
functions on \(G/H\), or equivalently by the projections \(1_E\), supplies a
[[functional-analysis/projection-valued-measure|projection-valued measure]]. Translation of sections transports multiplication
operators according to
\[
U(g)P(E)U(g)^{-1}=P(gE),
\]
so the pair is a system of imprimitivity.

## Recovering the stabilizer representation

The converse is the substantive direction. Covariance forces the spectral
data represented by \(P\) to be spread transitively over \(G/H\). A measurable
decomposition over the base isolates a fiber over the identity coset, and the
stabilizer \(H\) acts unitarily on that fiber. Re-inducing this \(H\)-action
reconstructs the original pair, including both the representation and its
projection-valued measure
[Mackey, pp. 537–545](https://doi.org/10.1073/pnas.35.9.537).

## Why the projection data matters

The theorem does not say that every unitary representation of \(G\) is
induced from \(H\). It classifies representations equipped with a compatible
system based on the specified transitive \(G\)-space. The same representation
\(U\) can admit inequivalent systems of imprimitivity, while a representation
without such a system need not arise from that stabilizer.

## Example

For the translation action of \(G\) on \(G/H\), the system attached to the
trivial representation of \(H\) has \(U\) equal to the
[[harmonic-analysis/quasi-regular-representation|quasi-regular representation]] and \(P(E)\) equal to multiplication by \(1_E\). The theorem
identifies the fiber representation at \(eH\) as the trivial \(H\)-action.

## References

1. George W. Mackey, “Imprimitivity for Representations of Locally Compact Groups I,” *Proceedings of the National Academy of Sciences* 35 (1949), 537–545. [DOI record](https://doi.org/10.1073/pnas.35.9.537). Relevant: the transitive imprimitivity classification.
2. Gerald B. Folland, *A Course in Abstract Harmonic Analysis*, 2nd ed., CRC Press, 2016. [DOI record](https://doi.org/10.1201/B19172). Relevant: Chapter 6, Theorem 6.31 and the surrounding construction.
