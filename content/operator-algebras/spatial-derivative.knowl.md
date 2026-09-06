+++
id = "operator-algebras/spatial-derivative"
title = "Spatial derivative"
kind = "definition"
summary = "Connes's positive self-adjoint Radon-Nikodym operator for a normal semifinite weight relative to a weight on the commutant."
aliases = ["Connes spatial derivative", "spatial Radon-Nikodym derivative"]
domains = ["operator-algebras", "noncommutative-geometry"]
prerequisites = ["operator-algebras/von-neumann-algebra", "operator-algebras/semifinite-weight", "operator-algebras/normal-semifinite-faithful-weight", "operator-algebras/commutant", "functional-analysis/closed-quadratic-form"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(M\subseteq B(H)\) be a
[[operator-algebras/von-neumann-algebra|von Neumann algebra]], let \(\phi\)
be a normal [[operator-algebras/semifinite-weight|semifinite weight]] on
\(M\), and let \(\Psi\) be a
[[operator-algebras/normal-semifinite-faithful-weight|faithful normal semifinite weight]] on the [[operator-algebras/commutant|commutant]] \(M'\).
Put \(\mathfrak n_\Psi=\{y\in M':\Psi(y^*y)<\infty\}\). A vector \(\xi\) is
\(\Psi\)-bounded when \(y\mapsto y\xi\) is bounded for the GNS norm on
\(\mathfrak n_\Psi\); then define
\(R^\Psi(\xi)\Lambda_\Psi(y)=y\xi\) for \(y\in\mathfrak n_\Psi\), where
\(\Lambda_\Psi\) is the GNS map, and
\(q(\xi)=\phi(R^\Psi(\xi)R^\Psi(\xi)^*)\); put \(q(\xi)=+\infty\) otherwise.
The **spatial derivative** \(d\phi/d\Psi\) is the unique positive
self-adjoint operator on \(H\) whose
[[functional-analysis/closed-quadratic-form|closed quadratic form]] is the
closure of \(q\):
\[
q(\xi)=\left\|\left(d\phi/d\Psi\right)^{1/2}\xi\right\|^2.
\]

## Why the commutant appears

The map \(R^\Psi(\xi)\) intertwines the GNS representation of \(M'\) with its
given action on \(H\), so
\(R^\Psi(\xi)R^\Psi(\xi)^*\in M\) and \(\phi\) can evaluate it. The weight
\(\Psi\) supplies a reference measure on the commuting algebra rather than on
\(M\) itself. This makes \(d\phi/d\Psi\) available in any faithful concrete
representation, which explains the adjective “spatial”.

## Relation to modular theory

The operator \(d\phi/d\Psi\) is generally unbounded and need not belong to
\(M\). Its imaginary powers encode relative modular data and transform
covariantly under changes of the reference weight. In the
[[operator-algebras/standard-form|standard form]] of \(M\), with the
commutant weight obtained from a second weight by
[[operator-algebras/modular-conjugation|modular conjugation]], the spatial
derivative becomes the corresponding relative
[[operator-algebras/modular-operator|modular operator]]. Connes introduced
this construction as a noncommutative Radon–Nikodym derivative.

## Commutative model and scope

In the commutative standard representation, the construction reduces to
multiplication by an ordinary Radon–Nikodym density. In finite dimensions,
with \(M=B(K)\) acting in standard form, spatial derivatives are represented
by the familiar left-right density-operator expression for relative modular
operators.

**Warning.** The spatial derivative is not the [[operator-algebras/connes-cocycle-derivative|Connes cocycle derivative]]
\((D\phi:D\omega)_t\). The former is a positive self-adjoint operator formed
relative to a weight on \(M'\); the latter is a one-parameter family of
[[functional-analysis/partial-isometry|partial isometries]] or unitaries in \(M\).

## References

1. Alain Connes, “Sur la théorie non commutative de l'intégration,” in *Algèbres d'Opérateurs*, Lecture Notes in Mathematics 725, Springer, 1979, 19–143. [DOI record](https://doi.org/10.1007/BFb0062614). Relevant: spatial Radon–Nikodym derivatives and noncommutative integration.
2. Fumio Hiai, *Concise Lectures on Selected Topics of von Neumann Algebras*, 2020. [arXiv record](https://arxiv.org/abs/2004.02383). Relevant: §13, especially Definition 13.4 and formula (13.2), for the quadratic-form construction.
