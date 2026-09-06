+++
id = "operator-algebras/projection-cstar-algebra"
title = "Projection in a C*-algebra"
kind = "definition"
summary = "A self-adjoint idempotent in a C*-algebra."
aliases = ["self-adjoint idempotent", "C*-projection", "operator-algebra projection"]
domains = ["operator-algebras"]
prerequisites = ["operator-algebras/cstar-algebra", "algebra-rings/idempotent-element"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(A\) be a [[operator-algebras/cstar-algebra|\(C^*\)-algebra]]. A
**projection** in \(A\) is an element \(p\in A\) satisfying
\[
p=p^*=p^2.
\]
Thus a projection is a self-adjoint
[[algebra-rings/idempotent-element|idempotent]]. The definition makes sense
whether or not \(A\) is unital; the zero element is always a projection, while
a multiplicative identity is a projection when it exists. If \(A\) is
represented faithfully on a [[linear-algebra/hilbert-space|Hilbert space]], \(p\) acts as the orthogonal
projection onto its closed range. This abstract definition does not require a
particular representation or a subspace chosen in advance.

## Spectral and geometric properties

The spectrum of a projection lies in \(\{0,1\}\). Every nonzero projection has
norm one, and \(1-p\) is a projection when \(A\) is unital. In a concrete
operator algebra, self-adjointness distinguishes [[linear-algebra/orthogonal-projection|orthogonal projections]] from
general idempotent operators, whose range and kernel need not be orthogonal.
These facts follow directly from the [[operator-algebras/continuous-functional-calculus|continuous functional calculus]].

## Equivalence and stabilization

Projections \(p\) and \(q\) are Murray–von Neumann equivalent when there is a
[[functional-analysis/partial-isometry|partial isometry]] \(v\) with \(v^*v=p\) and \(vv^*=q\). This records isomorphism
of the corresponding [[algebra-modules/projective-module|projective modules]] and is weaker than equality. One also
studies projections in matrix algebras \(M_n(A)\); block sum provides the
stabilization operation used in operator \(K\)-theory.

## Role in K-theory

For a unital \(C^*\)-algebra, the group
[[operator-algebras/k0-cstar-algebra|\(K_0(A)\)]] is built from stable
[[shared-foundations/equivalence-class|equivalence classes]] of projections in the matrix algebras over \(A\). For a
nonunital algebra, one passes to a unitization and retains the kernel of the
map induced by the scalar quotient. Consequently, “a projection defining a
\(K_0\)-class” may live in a matrix algebra or a unitization rather than in
\(A\) itself.

## References

1. Bruce Blackadar, *K-Theory for Operator Algebras*, 2nd ed., Cambridge University Press, 1998. [Publisher record](https://doi.org/10.1017/9781009701907). Relevant: Chapter III, especially §5, on projections and \(K_0\).
2. Gerard J. Murphy, \(C^*\)-Algebras and Operator Theory, Academic Press, 1990. [DOI record](https://doi.org/10.1016/C2009-0-22289-6). Relevant: §§2.2–2.3 on projections and functional calculus.
