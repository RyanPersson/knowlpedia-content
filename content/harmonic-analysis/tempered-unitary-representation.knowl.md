+++
id = "harmonic-analysis/tempered-unitary-representation"
title = "Tempered unitary representation"
kind = "definition"
summary = "A unitary representation weakly contained in the regular representation of its locally compact group."
aliases = ["representation weakly contained in the regular representation", "tempered representation"]
domains = ["harmonic-analysis", "lie-groups", "operator-algebras"]
section_mode = "progressive"
+++

Let \(G\) be a [[topology/locally-compact-group|locally compact group]] and
\(\pi\) a [[lie-groups/strongly-continuous-unitary-representation|strongly continuous unitary representation]] of \(G\). The representation \(\pi\) is
**tempered** if it is
[[harmonic-analysis/weak-containment-unitary-representations|weakly contained]] in the
[[harmonic-analysis/regular-representations-locally-compact-group|left regular representation]] \(\lambda_G\):
\[
\pi\prec\lambda_G.
\]
Equivalently, the integrated form of \(\pi\) factors through the
[[operator-algebras/reduced-group-cstar-algebra|reduced group \(C^*\)-algebra]] \(C_r^*(G)\). Some authors reserve “tempered” for
[[algebra-representation-theory/irreducible-representation|irreducible representations]]; under that convention, \(\pi\) is additionally
assumed irreducible. Temperedness depends only on the unitary-equivalence
class of \(\pi\), not on a chosen realization of its
[[linear-algebra/hilbert-space|Hilbert space]].

## Almost-square-integrable coefficients

For a connected semisimple [[fiber-bundles/lie-group|Lie group]] with finite center, an irreducible
unitary representation is tempered exactly when all its \(K\)-finite matrix
coefficients lie in \(L^{2+\varepsilon}(G)\) for every
\(\varepsilon>0\). This “almost \(L^2\)” criterion is a major practical test
for temperedness
[Cowling–Haagerup–Howe, Theorem 1].

## Examples and boundary cases

The [[algebra-representation-theory/regular-representation|regular representation]] is tempered, as are its subrepresentations and
weakly contained representations. Discrete-series representations of a semisimple
group are tempered. The trivial representation is tempered exactly when
\(G\) is
[[harmonic-analysis/amenable-locally-compact-group|amenable]]; therefore it
is a decisive non-example for nonamenable groups.

## Role in harmonic analysis

Tempered irreducibles form the natural support of Plancherel theory: the
regular representation decomposes over them, with measure described by
[[harmonic-analysis/plancherel-measure-nonabelian|nonabelian Plancherel measure]]. They also constitute the part of the
[[harmonic-analysis/unitary-dual|unitary dual]] detected by \(C_r^*(G)\),
explaining why temperedness connects representation theory
with reduced group \(C^*\)-algebras
[Knapp, Chapter VIII].

## References

1. Michael Cowling, Uffe Haagerup, and Roger Howe, “Almost \(L^2\) Matrix Coefficients,” *Journal für die reine und angewandte Mathematik* 387 (1988), 97–110. [DOI record](https://doi.org/10.1515/crll.1988.387.97). Relevant: Theorem 1 and the \(L^{2+\varepsilon}\) criterion.
2. Anthony W. Knapp, *Representation Theory of Semisimple Groups: An Overview Based on Examples*, Princeton University Press, 1986. [Author record](https://www.math.stonybrook.edu/~aknapp/books/repthy1.html). Relevant: Chapter VIII on tempered representations and Plancherel theory.
