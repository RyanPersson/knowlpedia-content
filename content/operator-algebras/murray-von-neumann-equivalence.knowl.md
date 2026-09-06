+++
id = "operator-algebras/murray-von-neumann-equivalence"
title = "Murray–von Neumann equivalence of projections"
kind = "definition"
summary = "The equivalence relation on projections implemented by partial isometries inside an operator algebra."
aliases = ["equivalent projections", "MvN equivalence"]
domains = ["operator-algebras"]
prerequisites = ["operator-algebras/von-neumann-algebra", "operator-algebras/projection-cstar-algebra", "functional-analysis/partial-isometry", "operator-algebras/cstar-algebra"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(M\) be a [[operator-algebras/von-neumann-algebra|von Neumann algebra]]
and let \(p,q\in M\) be
[[operator-algebras/projection-cstar-algebra|projections]]. They are
**Murray–von Neumann equivalent**, written \(p\sim q\), if there is a
[[functional-analysis/partial-isometry|partial isometry]] \(v\in M\) such
that
\[
v^*v=p
\qquad\text{and}\qquad
vv^*=q.
\]
Thus \(v\) restricts to an isometric identification of the initial subspace
of \(p\) with the final subspace of \(q\), but the implementing operator must
belong to \(M\). The same definition applies to projections in any
[[operator-algebras/cstar-algebra|\(C^*\)-algebra]]. Reflexivity, symmetry,
and transitivity follow respectively
from \(p\), \(v^*\), and products of compatible implementing partial
isometries.

## Sub-equivalence and finiteness

One writes \(p\precsim q\) if \(p\sim r\) for some projection \(r\leq q\).
This compares the sizes of projections without assigning a numerical
dimension. A projection \(p\) is finite when \(p\sim r\leq p\) forces
\(r=p\); otherwise it is infinite. These notions are internal to the algebra:
the same concrete projections can have different comparison behavior when
viewed inside different von Neumann algebras.

## Concrete interpretation

In \(B(H)\), two projections are Murray–von Neumann equivalent exactly when
their ranges have the same Hilbert-space dimension. In a matrix algebra this
reduces to equality of ranks. Equivalence need not mean conjugacy by a
unitary in \(M\): extending an implementing partial isometry \(v\) to a
unitary also requires the complementary projections \(1-p\) and \(1-q\) to
be equivalent.

## Role in classification

Murray–von Neumann equivalence is the comparison relation behind the
dimension theory of von Neumann algebras. Passing to [[shared-foundations/equivalence-class|equivalence classes]] and
using orthogonal sums of projections records how pieces of the identity can
be decomposed. The distinction between finite, semifinite, and properly
infinite behavior—and ultimately the type I, II, and III classification—is
formulated through this comparison theory.

## References

- [Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras, Volume II: Advanced Theory*, §6.3 (American Mathematical Society, 1997)](https://bookstore.ams.org/gsm-16/)
- [Masamichi Takesaki, *Theory of Operator Algebras I*, Chapter V (Springer, 1979)](https://doi.org/10.1007/978-1-4612-6188-9)
