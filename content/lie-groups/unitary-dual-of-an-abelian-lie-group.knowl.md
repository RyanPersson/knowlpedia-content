+++
id = "lie-groups/unitary-dual-of-an-abelian-lie-group"
title = "Unitary dual of an abelian Lie group"
kind = "definition"
summary = "For a connected abelian Lie group, every irreducible unitary representation is a character and the dual is Euclidean-discrete."
aliases = ["characters of abelian Lie groups", "Pontryagin dual of Euclidean spaces and tori"]
domains = ["lie-groups", "harmonic-analysis"]
section_mode = "progressive"
+++

Let \(G\) be a connected [[lie-groups/abelian-lie-group|abelian Lie group]].
Every irreducible
[[lie-groups/strongly-continuous-unitary-representation|strongly continuous unitary representation]] of \(G\) on a complex
[[linear-algebra/hilbert-space|Hilbert space]] is one-dimensional, hence is a
[[harmonic-analysis/unitary-character|continuous unitary character]]. Using
\[
G\cong\mathbb R^n\times\mathbb T^m
\]
from the [[lie-groups/connected-abelian-lie-group-structure|structure theorem for connected abelian Lie groups]], its
[[harmonic-analysis/unitary-dual|unitary dual]] is
\[
\widehat G\cong\mathbb R^n\times\mathbb Z^m.
\]
The point \((\xi,k)\) corresponds to
\(\chi_{\xi,k}(x,z)=e^{i\langle\xi,x\rangle}z_1^{k_1}\cdots z_m^{k_m}\).
This identification carries the usual Euclidean topology on the first factor
and the discrete topology on the second.

## Why irreducibles are characters

All operators in a unitary representation of an [[algebra-groups/abelian-group|abelian group]] commute. For an
[[algebra-representation-theory/irreducible-representation|irreducible representation]], the commutant consists only of scalars, so every
group element acts by a scalar of modulus one. Strong continuity makes the
resulting scalar map \(G\to\mathbb T\) continuous. Thus the unitary dual agrees
with the [[harmonic-analysis/pontryagin-dual|Pontryagin dual]], not merely as
a set but with its natural topology.

## Basic factors

The characters of \(\mathbb R^n\) are
\(x\mapsto e^{i\langle\xi,x\rangle}\), parametrized by
\(\xi\in\mathbb R^n\). The characters of \(\mathbb T^m\) are the monomials
\(z\mapsto z^k\), parametrized by \(k\in\mathbb Z^m\). Consequently,
\(\widehat{\mathbb R^n}\cong\mathbb R^n\) and
\(\widehat{\mathbb T^m}\cong\mathbb Z^m\), while the dual of a product is the
product of the duals.

## Scope and Plancherel theory

Disconnected abelian Lie groups may have additional discrete components; the
general statement remains that their
[[lie-groups/irreducible-unitary-representation|irreducible unitary representations]] are characters, but their dual is obtained from the full
locally compact abelian group rather than the displayed connected
classification.
[[harmonic-analysis/haar-measure|Haar measure]] on \(\widehat G\) combines
[[measure-theory/lebesgue-measure|Lebesgue measure]] on \(\mathbb R^n\) with
counting measure on \(\mathbb Z^m\), up to reciprocal normalization, and is
the measure used in abelian Plancherel theory.

## References

1. Gerald B. Folland, *A Course in Abstract Harmonic Analysis*, 2nd ed., CRC Press, 2016. [DOI record](https://doi.org/10.1201/B19172). Relevant: Chapter 4 on characters, Pontryagin duality, and Fourier analysis of locally compact abelian groups.
2. Walter Rudin, *Fourier Analysis on Groups*, Wiley-Interscience, 1962. [Wiley DOI record](https://doi.org/10.1002/9781118165621). Relevant: Chapter 1 on locally compact abelian groups and their character groups.
