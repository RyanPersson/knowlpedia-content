+++
id = "functional-analysis/adjoint-bounded-operator"
title = "Adjoint of a bounded operator"
kind = "definition"
summary = "The unique bounded operator obtained by transferring a Hilbert-space operator across the inner product."
aliases = ["bounded-operator adjoint", "Hilbert-space adjoint"]
domains = ["functional-analysis"]
prerequisites = ["linear-algebra/hilbert-space", "linear-algebra/inner-product", "functional-analysis/bounded-linear-operator", "functional-analysis/riesz-representation-hilbert-space"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(H\) and \(K\) be complex [[linear-algebra/hilbert-space|Hilbert
spaces]] whose [[linear-algebra/inner-product|inner products]] are linear in the first variable, and let
\(T:H\to K\) be a
[[functional-analysis/bounded-linear-operator|bounded linear operator]]. The
**adjoint** of \(T\) is the unique bounded operator \(T^*:K\to H\) satisfying
\[
\langle Tx,y\rangle_K=\langle x,T^*y\rangle_H
\qquad (x\in H,\ y\in K).
\]
Existence and uniqueness follow from the
[[functional-analysis/riesz-representation-hilbert-space|Riesz representation
theorem]] applied to \(x\mapsto\langle Tx,y\rangle_K\). The adjoint reverses the direction of
the map, so self-adjointness is defined only when source and target agree.

## Norm and algebraic identities

The adjoint has the same [[linear-algebra/operator-norm|operator norm]] as the
original operator and satisfies
\[
\lVert T^*\rVert=\lVert T\rVert,\qquad
T^{**}=T,\qquad
(ST)^*=T^*S^*.
\]
It is conjugate-linear in the operator:
\[
(\alpha S+\beta T)^*
=\overline{\alpha}S^*+\overline{\beta}T^*.
\]
When \(T\in B(H)\), the identity
\(\lVert T^*T\rVert=\lVert T\rVert^2\) makes the adjoint the involution in
the \(C^*\)-algebra \(B(H)\).

## Kernels, ranges, and matrices

The orthogonality relations
\[
\ker T^*=(\operatorname{Ran}T)^\perp,\qquad
\ker T=(\operatorname{Ran}T^*)^\perp
\]
connect algebraic failure of injectivity with density of the opposite range.
For finite-dimensional [[linear-algebra/hilbert-space|Hilbert spaces]] with
[[linear-algebra/orthonormal-basis|orthonormal bases]], \(T^*\) is
represented by the conjugate-transpose matrix. For the unilateral shift on
\(\ell^2(\mathbb N)\), the adjoint is the backward shift
\((x_0,x_1,\ldots)\mapsto(x_1,x_2,\ldots)\).

## Relation to unbounded adjoints

The [[functional-analysis/adjoint-unbounded-operator|adjoint of a densely
defined operator]] is defined by the same inner-product identity, but its
domain may be a proper dense subspace. For bounded \(T\) defined on all of
\(H\), that construction yields an everywhere-defined bounded \(T^*\).
Conflating the two settings can hide the domain questions responsible for
symmetry, self-adjointness, and extension theory.

## References

1. John B. Conway, *A Course in Functional Analysis*, 2nd ed., Graduate Texts in Mathematics 96, Springer, 1990. [DOI record](https://doi.org/10.1007/978-1-4757-4383-8). Relevant: Chapter II on Hilbert-space operators and adjoints.
2. Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras, Volume I: Elementary Theory*, American Mathematical Society, 1997. [DOI record](https://doi.org/10.1090/gsm/015). Relevant: §2.5 on operators on Hilbert space.
