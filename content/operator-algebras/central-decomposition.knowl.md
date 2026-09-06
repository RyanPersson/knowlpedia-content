+++
id = "operator-algebras/central-decomposition"
title = "Central decomposition of a von Neumann algebra"
kind = "definition"
summary = "A direct-integral realization of a von Neumann algebra whose fibers are factors and whose center acts by scalar fields."
aliases = ["direct integral decomposition into factors", "factor decomposition"]
domains = ["operator-algebras", "functional-analysis"]
section_mode = "progressive"
prerequisites = ["operator-algebras/von-neumann-algebra", "linear-algebra/hilbert-space", "measure-theory/measure-space", "operator-algebras/von-neumann-factor", "measure-theory/almost-everywhere", "operator-algebras/center-of-von-neumann-algebra", "measure-theory/null-set"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(M\subseteq B(H)\) be a
[[operator-algebras/von-neumann-algebra|von Neumann algebra]] on a separable
[[linear-algebra/hilbert-space|Hilbert space]].
A **central decomposition** of \(M\) is a spatial direct-integral
realization
\[
H\cong\int_X^\oplus H_x\,d\mu(x),\qquad
M\cong\int_X^\oplus M_x\,d\mu(x),
\]
over a standard [[measure-theory/measure-space|measure space]], such that
\(M_x\subseteq B(H_x)\) is a
[[operator-algebras/von-neumann-factor|factor]] for
[[measure-theory/almost-everywhere|almost every \(x\)]], and
the [[operator-algebras/center-of-von-neumann-algebra|center]] \(Z(M)\)
corresponds to the diagonal scalar algebra \(L^\infty(X,\mu)\). Equalities
and fiber properties are understood modulo [[measure-theory/null-set|null sets]]; individual fibers are
not pointwise canonical.

## Existence and uniqueness

For a separably acting von Neumann algebra, the factorial decomposition
theorem produces such a measurable field of factors. Subject to the standard
measurability hypotheses, the base measure class and factor field are unique
up to the appropriate almost-everywhere measurable equivalence. This is a
disintegration theorem, not merely a decomposition by finitely many central
projections.

## How the center controls the fibers

Under the decomposition, a central element \(z\) acts on \(H_x\) as
multiplication by a scalar \(f_z(x)\). Conversely, every essentially bounded
measurable scalar field gives a central
[[functional-analysis/decomposable-operator|decomposable operator]]. The
fiber algebras have trivial centers almost everywhere, so the variation that
remains in \(Z(M)\) has been transferred to the parameter space.

## Examples and scope

A finite direct sum \(M_1\oplus\cdots\oplus M_n\) of factors is the discrete
case, with \(X=\{1,\ldots,n\}\). A
[[operator-algebras/commutative-von-neumann-algebra|commutative von Neumann algebra]] decomposes into one-dimensional factors almost everywhere.
Separability or standardness cannot simply be dropped: more general von
Neumann algebras require
additional measure-theoretic formulations, and “the” decomposition should
not be read as a preferred choice of representatives at every point.

## References

1. Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras, Volume II: Advanced Theory*, American Mathematical Society, 1997. [AMS DOI record](https://doi.org/10.1090/gsm/016). Relevant: §6.5 on central and factorial decomposition.
2. Masamichi Takesaki, *Theory of Operator Algebras I*, Springer, 1979. [Springer DOI record](https://doi.org/10.1007/978-1-4612-6188-9). Relevant: Chapter IV, §8 on direct integrals and decomposable operators.
