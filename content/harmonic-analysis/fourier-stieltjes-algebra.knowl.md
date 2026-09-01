+++
id = "harmonic-analysis/fourier-stieltjes-algebra"
title = "Fourier–Stieltjes algebra"
kind = "definition"
summary = "The Banach algebra of coefficient functions of continuous unitary representations of a locally compact group."
aliases = ["Fourier-Stieltjes algebra", "B(G)", "algebra of unitary representation coefficients"]
domains = ["harmonic-analysis", "operator-algebras"]
prerequisites = ["topology/locally-compact-group", "harmonic-analysis/coefficient-function", "lie-groups/strongly-continuous-unitary-representation", "linear-algebra/hilbert-space", "linear-algebra/vector-space"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(G\) be a [[topology/locally-compact-group|locally compact group]]. Its
**Fourier–Stieltjes algebra** \(B(G)\) is the set of all
[[harmonic-analysis/coefficient-function|coefficient functions]]
\[
u(x)=\langle \pi(x)\xi,\eta\rangle
\]
arising from [[lie-groups/strongly-continuous-unitary-representation|strongly continuous unitary representations]] \(\pi\) of \(G\) on
complex [[linear-algebra/hilbert-space|Hilbert spaces]] and vectors \(\xi,\eta\). Direct sums show that these
coefficients form a [[linear-algebra/vector-space|vector space]], while tensor products show that they are
closed under pointwise multiplication. With the norm transported from the
dual of the full group \(C^*\)-algebra, \(B(G)\) is a commutative unital Banach
algebra.

## Dual realization and norm

Every coefficient \(u\) determines a unique bounded functional
\(\omega_u\) on the full group \(C^*\)-algebra \(C^*(G)\), characterized on
integrable functions by
\[
\omega_u(f)=\int_G f(x)u(x)\,dx.
\]
The norm is \(\lVert u\rVert_{B(G)}=\lVert\omega_u\rVert\). Equivalently, it is
the infimum of \(\lVert\xi\rVert\lVert\eta\rVert\) over all coefficient
realizations of \(u\). This identification is isometric and is central to
Eymard's treatment.

## Positive-definite functions and examples

The algebra \(B(G)\) is the linear span of the continuous
[[harmonic-analysis/positive-definite-function|positive-definite functions]]
on \(G\). The constant function \(1\) is the coefficient of the trivial
representation. If \(G\) is locally compact abelian, Fourier–Stieltjes
transforms identify \(B(G)\) with the measure algebra on the [[harmonic-analysis/pontryagin-dual|Pontryagin dual]].
For a nonabelian group, \(B(G)\) remains commutative because its multiplication
is pointwise, even though the full group \(C^*\)-algebra is generally
noncommutative.

## Relation to the Fourier algebra

The [[harmonic-analysis/fourier-algebra|Fourier algebra]] \(A(G)\) consists of coefficients of the left regular
representation and is a closed ideal in \(B(G)\). Thus \(B(G)\) uses all
unitary representations, whereas \(A(G)\) records the [[algebra-representation-theory/regular-representation|regular representation]].
The distinction can be substantial for noncompact groups and should not be
suppressed by calling both spaces simply “Fourier transforms.”

## References

1. Pierre Eymard, “L'algèbre de Fourier d'un groupe localement compact,” *Bulletin de la Société Mathématique de France* 92 (1964), 181–236. [DOI record](https://doi.org/10.24033/bsmf.1607). Relevant: §§2.1–2.3 on \(B(G)\), its norm, and \(A(G)\).
2. Gerald B. Folland, *A Course in Abstract Harmonic Analysis*, 2nd ed., CRC Press, 2016. [DOI record](https://doi.org/10.1201/B19172). Relevant: chapters on unitary representations and Fourier–Stieltjes transforms.
