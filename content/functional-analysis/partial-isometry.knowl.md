+++
id = "functional-analysis/partial-isometry"
title = "Partial isometry"
kind = "definition"
summary = "A bounded Hilbert-space operator that is isometric on the orthogonal complement of its kernel."
aliases = ["partial-isometric operator"]
domains = ["functional-analysis"]
section_mode = "progressive"
+++

Let \(H\) and \(K\) be [[linear-algebra/hilbert-space|Hilbert spaces]]. A
[[functional-analysis/bounded-linear-operator|bounded operator]] \(V:H\to K\)
is a **partial isometry** if its restriction to
[[linear-algebra/orthogonal-complement|\((\ker V)^\perp\)]] preserves norms.
The [[linear-algebra/closed-linear-subspace|closed subspace]]
\((\ker V)^\perp\) is the **initial space**, and
\(\operatorname{Ran}V\) is the **final space**; the final space is closed
because this restriction is an isometry. Equivalently, using the
[[functional-analysis/adjoint-bounded-operator|adjoint]], \(V^*V\) is the
[[linear-algebra/orthogonal-projection|orthogonal projection]] onto the
initial space. Then \(VV^*\) is the orthogonal projection onto the final
space.

## Polar decomposition

Every bounded operator \(T:H\to K\) has a polar decomposition
\[
T=V|T|,\qquad |T|=(T^*T)^{1/2},
\]
where \(V\) is a partial isometry with initial space
\(\overline{\operatorname{Ran}|T|}
=\overline{\operatorname{Ran}T^*}\) and final space
\(\overline{\operatorname{Ran}T}\). Requiring \(\ker V=\ker T\) makes this
partial isometry unique. Thus partial isometries are the correct polar factors
even when \(T\) is neither injective nor surjective
[Conway, Chapter II](https://doi.org/10.1007/978-1-4757-4383-8).

## Operator-algebra formulation

An element \(v\) of a \(C^*\)-algebra is called a partial isometry when
\(v^*v\) is a [[operator-algebras/projection-cstar-algebra|projection]]; this
implies that \(vv^*\) is also a projection. In a concrete operator algebra the
two projections record the initial and final spaces. Partial isometries
therefore implement
[[operator-algebras/murray-von-neumann-equivalence|Murray–von Neumann
equivalence]] between projections.

## Examples and non-examples

Every orthogonal projection,
[[functional-analysis/unitary-operator|unitary operator]], and isometric
embedding is a partial isometry. The unilateral shift is a partial isometry whose initial
space is all of \(\ell^2(\mathbb N)\) and whose final space has codimension
one. The zero operator also qualifies, with zero initial and final spaces. By
contrast, \(2I\) on a nonzero Hilbert space is not a partial isometry because
it does not preserve norms on the orthogonal complement of its kernel.

## References

1. John B. Conway, *A Course in Functional Analysis*, 2nd ed., Graduate Texts in Mathematics 96, Springer, 1990. [DOI record](https://doi.org/10.1007/978-1-4757-4383-8). Relevant: Chapter II on adjoints and polar decomposition.
2. Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras, Volume I: Elementary Theory*, American Mathematical Society, 1997. [DOI record](https://doi.org/10.1090/gsm/015). Relevant: §2.5 on partial isometries and projections.
