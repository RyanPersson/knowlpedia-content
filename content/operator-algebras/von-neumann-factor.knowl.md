+++
id = "operator-algebras/von-neumann-factor"
title = "Von Neumann factor"
kind = "definition"
summary = "A von Neumann algebra whose center consists only of scalar multiples of its identity."
aliases = ["primary von Neumann algebra"]
domains = ["operator-algebras"]
section_mode = "progressive"
prerequisites = ["operator-algebras/von-neumann-algebra", "operator-algebras/center-of-von-neumann-algebra"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

A **von Neumann factor**, or simply a **factor**, is a
[[operator-algebras/von-neumann-algebra|von Neumann algebra]] \(M\) whose
[[operator-algebras/center-of-von-neumann-algebra|center]] is
\[
Z(M)=\mathbb C1_M.
\]
Equivalently, \(0\) and \(1_M\) are the only central projections in \(M\).
This condition means that \(M\) cannot be decomposed as a nontrivial direct
sum along central projections.

## Example and warning

Being a factor does not mean having no proper norm-closed ideals as a \(C^*\)-algebra. For example, \(B(H)\) on an infinite-dimensional [[linear-algebra/hilbert-space|Hilbert space]] is a factor but contains the [[linear-algebra/compact-operator|compact operators]] as a proper norm-closed ideal.

## Closed ideals and central decomposition

Ultraweakly closed [[algebra-rings/two-sided-ideal|two-sided ideals]] in a von Neumann algebra have the form
\(Mz\) for central projections \(z\). Hence a factor has no nonzero proper
ultraweakly closed two-sided ideals. General von Neumann algebras can often be
analyzed as direct integrals of factors, with their centers supplying the
measurable parameter algebra.

## Type classification

Factors divide into types \(I_n\), \(I_\infty\), \(II_1\),
\(II_\infty\), and \(III\), according to the comparison and finiteness
behavior of their projections.
[[operator-algebras/type-i-von-neumann-algebra|Type I]] factors are precisely
the algebras \(B(H)\). Type II factors have
[[operator-algebras/finite-projection|finite projections]] but no nonzero
[[operator-algebras/abelian-projection|abelian projections]], while type III
factors have no nonzero finite
projections.

## Representations and factorial states

If a representation \(\pi\) generates the von Neumann algebra
\(\pi(A)''\), the representation is called factorial when this
[[operator-algebras/bicommutant|bicommutant]] is a factor. A state is
factorial when its GNS representation is factorial.
Irreducibility is stronger: it forces \(\pi(A)'=\mathbb C1\), whereas
factoriality only forces the center of \(\pi(A)''\) to be scalar.

## References

1. F. J. Murray and J. von Neumann, “On Rings of Operators,” *Annals of Mathematics* 37 (1936), 116–229. [JSTOR record](https://doi.org/10.2307/1968693). Relevant: the introduction of factors and the projection-based type classification.
2. Masamichi Takesaki, *Theory of Operator Algebras I*, Springer, 2002. [Publisher record](https://doi.org/10.1007/978-1-4612-6188-9). Relevant: Chapter V on factors and their types.
