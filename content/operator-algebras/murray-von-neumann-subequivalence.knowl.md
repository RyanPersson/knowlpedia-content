+++
id = "operator-algebras/murray-von-neumann-subequivalence"
title = "Murray–von Neumann subequivalence of projections"
kind = "definition"
summary = "The comparison relation saying that one projection is equivalent to a subprojection of another."
aliases = ["subordinate equivalence", "p preccurlyeq q"]
domains = ["operator-algebras"]
section_mode = "progressive"
+++

Let \(p\) and \(q\) be projections in a \(C^*\)-algebra \(A\). The projection
\(p\) is **Murray–von Neumann subequivalent** to \(q\), written
\(p\precsim q\), if \(p\) is
[[operator-algebras/murray-von-neumann-equivalence|Murray–von Neumann
equivalent]] to a subprojection of \(q\). Equivalently, there is a
[[functional-analysis/partial-isometry|partial isometry]] \(v\in A\) such
that
\[
v^*v=p,\qquad vv^*\leq q.
\]
Thus \(v\) identifies the range represented by \(p\) with a part of the range
represented by \(q\). The relation depends on the ambient algebra: enlarging
\(A\) can introduce additional partial isometries and hence additional
subequivalences.

## Order properties

Subequivalence is reflexive and transitive. Murray–von Neumann equivalence
implies subequivalence in both directions, and for projections in a von
Neumann algebra the converse also holds. Passing to equivalence classes
therefore turns \(\precsim\) into a partial order. Orthogonal sums respect the
relation: if \(p_i\precsim q_i\) with mutually orthogonal families, then the
corresponding sums are subequivalent whenever they exist.

## Central obstruction

In a von Neumann algebra, \(p\precsim q\) implies
\(c_M(p)\leq c_M(q)\), where \(c_M\) denotes
[[operator-algebras/central-support|central support]]. This condition alone
does not compare the sizes of \(p\) and \(q\) inside each central summand.
The comparison theorem supplies the central decomposition on which one or
the other subequivalence holds.

## Dimension-theoretic role

For finite-dimensional matrix algebras, \(p\precsim q\) exactly when
\(\operatorname{rank}(p)\leq\operatorname{rank}(q)\). In general von Neumann
algebras, subequivalence replaces rank comparison. It is used to define
finite, infinite, and properly infinite projections and underlies the
Murray–von Neumann classification of factors.

## References

1. Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras, Volume II: Advanced Theory*, American Mathematical Society, 1997. [Publisher record](https://bookstore.ams.org/GSM/16/). Relevant: §6.3 on equivalence and comparison of projections.
2. Masamichi Takesaki, *Theory of Operator Algebras I*, Springer, 2002. [Publisher record](https://doi.org/10.1007/978-1-4612-6188-9). Relevant: Chapter V on projection comparison.
