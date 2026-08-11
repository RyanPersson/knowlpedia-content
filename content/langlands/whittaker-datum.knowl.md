+++
id = "langlands/whittaker-datum"
title = "Whittaker datum"
kind = "definition"
summary = "A conjugacy class of a rational Borel subgroup together with a nondegenerate character of its unipotent radical."
aliases = ["Whittaker data", "generic datum"]
domains = ["langlands", "harmonic-analysis"]
section_mode = "progressive"
+++

Let \(G\) be a
[[algebraic-geometry-foundations/quasi-split-reductive-group|quasi-split
connected reductive group]] over a
[[algebra-fields-galois/local-field|local field]] \(F\).
A **Whittaker datum** for \(G\) is a \(G(F)\)-conjugacy class of pairs
\(\mathfrak w=(B,\psi)\), where \(B=TU\) is an \(F\)-rational
[[algebraic-geometry-foundations/borel-subgroup|Borel subgroup]] with
[[algebraic-geometry-foundations/unipotent-radical|unipotent radical]] \(U\)
and

\[
\psi:U(F)\longrightarrow\mathbb C^\times
\]

is a nondegenerate [[harmonic-analysis/unitary-character|unitary character]]. Nondegeneracy means that the induced
character on every simple-root quotient of \(U\) is nontrivial.

## Representations generic for a datum

A representation is \(\mathfrak w\)-generic if it has a
[[harmonic-analysis/whittaker-model|Whittaker model]] for a representative
\((B,\psi)\). This property is independent of the representative within the
[[algebra-groups/conjugacy-class|conjugacy class]].

## Normalizing packet parametrizations

A Whittaker datum chooses an origin for the internal parametrization of a
[[harmonic-analysis/tempered-representation-p-adic-group|tempered]]
[[langlands/l-packet|\(L\)-packet]] on a quasi-split \(p\)-adic group: the
conjecturally unique
\(\mathfrak w\)-generic member corresponds to the trivial representation of
the appropriate
[[langlands/component-group-of-l-parameter|component group]]. Changing the
datum twists that
parametrization by a character; it does not change the underlying packet.

## Existence and multiplicity

A Whittaker datum exists precisely in the quasi-split setting. It need not be
unique up to \(G(F)\)-conjugacy, even though the underlying rational Borel
subgroups are conjugate in the appropriate sense.

## References

1. Tasho Kaletha, “Representations of reductive groups over local fields,”
   §§2.2 and 2.3.1, 2022. [arXiv](https://arxiv.org/abs/2201.07741).
2. Robert Kottwitz and Diana Shelstad, *Foundations of Twisted Endoscopy*,
   Astérisque 255, 1999. [Numdam](https://www.numdam.org/item/AST_1999__255__R1_0/).
