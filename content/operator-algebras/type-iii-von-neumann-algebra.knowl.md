+++
id = "operator-algebras/type-iii-von-neumann-algebra"
title = "Type III von Neumann algebra"
kind = "definition"
summary = "A von Neumann algebra with no nonzero finite projections."
aliases = ["type III W*-algebra"]
domains = ["operator-algebras"]
section_mode = "progressive"
+++

A [[operator-algebras/von-neumann-algebra|von Neumann algebra]] \(M\) is
**type III** if it has no nonzero
[[operator-algebras/finite-projection|finite projection]]. Equivalently, every
nonzero projection of \(M\) is [[operator-algebras/infinite-projection|infinite]].
This condition applies to the whole algebra, not only to its center. A general
von Neumann algebra has a unique largest type III central summand, while
saying that \(M\) is type III means that this summand has central support
\(1\). If \(M\) is also a
[[operator-algebras/von-neumann-factor|factor]], it is called a type III
factor.

## Consequences

A nonzero type III von Neumann algebra admits no nonzero normal semifinite
trace, because any positive finite-trace spectral cut would yield a nonzero
finite projection. In particular, it has no tracial state. This does not mean
that it has no normal states or no faithful normal semifinite weights:
normality, semifiniteness of a weight, and the tracial identity are separate
conditions. The absence of finite projections is the defining type III
feature.

## Factor subtypes

The modular-spectrum refinement divides type III factors into
\(\mathrm{III}_0\), \(\mathrm{III}_\lambda\) for \(0<\lambda<1\), and
\(\mathrm{III}_1\), using modular-theoretic invariants. These labels refine
type III; they do not arise by assigning a “dimension” to projections as in
types I and II. The subtype definitions apply through these invariants, while
deeper structure and uniqueness theorems may require hypotheses such as a
separable predual; such hypotheses must accompany the theorem that uses them.

## Classification convention

The Roman numeral III refers to Murray–von Neumann type. An algebra with both
a semifinite central summand and a type III central summand is not itself type
III under the convention used here; only its latter central summand is.
The projection criterion and the central type decomposition are given in
[Kadison–Ringrose, §6.5](https://bookstore.ams.org/GSM/16).

## References

1. Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras, Volume II: Advanced Theory*, American Mathematical Society, 1997. [AMS record](https://bookstore.ams.org/GSM/16). Relevant: §6.5 on type III algebras and the central type decomposition.
2. Masamichi Takesaki, *Theory of Operator Algebras I*, Springer, 1979. [DOI record](https://doi.org/10.1007/978-1-4612-6188-9). Relevant: Chapter V on factor types and traces.
