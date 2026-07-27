+++
id = "operator-algebras/finite-projection"
title = "Finite projection"
kind = "definition"
summary = "A projection not Murray-von Neumann equivalent to any proper subprojection of itself."
aliases = ["Murray–von Neumann finite projection"]
domains = ["operator-algebras"]
section_mode = "progressive"
+++

Let \(p\) be a projection in a
[[operator-algebras/von-neumann-algebra|von Neumann algebra]] \(M\). It is a
**finite projection** if, whenever \(q\leq p\) and \(q\) is
[[operator-algebras/murray-von-neumann-equivalence|Murray–von Neumann equivalent]]
to \(p\), one has \(q=p\). Equivalently, there is no
[[functional-analysis/partial-isometry|partial isometry]] \(v\in M\) satisfying
\[
v^*v=p,\qquad vv^*<p.
\]
A projection that is not finite is called infinite. The zero projection is
finite. Finiteness is intrinsic to the ambient von Neumann algebra and its
partial isometries; it is not the same as finite-dimensionality of the
projection's range in a particular representation.

## Corners and equivalence

Finiteness is invariant under Murray–von Neumann equivalence and passes to
subprojections. The projection \(p\) is finite exactly when the corner
\(pMp\), whose identity is \(p\), is a finite von Neumann algebra. A von
Neumann algebra is called finite when its identity projection is finite.

## Examples

In \(B(H)\), a projection is finite exactly when its range is
finite-dimensional. In a type \(II_1\) factor, every projection is finite,
including projections with infinite-dimensional Hilbert-space range. The
identity of \(B(H)\) for infinite-dimensional \(H\) is infinite, as a
unilateral shift implements equivalence with a proper subprojection.

## Finite versus properly infinite

An [[operator-algebras/infinite-projection|infinite projection]] \(p\) is
properly infinite when it contains two orthogonal subprojections, each
equivalent to \(p\). Not every infinite projection is properly infinite in an
arbitrary von Neumann algebra, because
finite and properly infinite behavior can coexist on different central
summands. In a factor, the type classification sharply constrains these
possibilities.

## References

1. Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras, Volume II*, American Mathematical Society, 1997. [Publisher record](https://doi.org/10.1090/gsm/016). Relevant: §6.3 on Murray–von Neumann equivalence and finite projections.
2. F. J. Murray and J. von Neumann, “On Rings of Operators,” *Annals of Mathematics* 37 (1936), 116–229. [JSTOR record](https://doi.org/10.2307/1968693). Relevant: comparison of projections and the finite/infinite distinction.
