+++
id = "operator-algebras/separating-vector"
title = "Separating vector"
kind = "definition"
summary = "A vector on which no nonzero operator from the represented algebra vanishes."
aliases = ["separating vector for an operator algebra"]
domains = ["operator-algebras", "algebra-representation-theory"]
prerequisites = ["operator-algebras/von-neumann-algebra", "linear-algebra/hilbert-space", "linear-algebra/linear-map"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(M\subseteq B(H)\) be a
[[operator-algebras/von-neumann-algebra|von Neumann algebra]] on a
[[linear-algebra/hilbert-space|Hilbert space]]. A vector \(\xi\in H\) is
**separating for \(M\)** if
\[
x\xi=0\text{ for }x\in M\quad\Longrightarrow\quad x=0.
\]
Equivalently, the [[linear-algebra/linear-map|linear map]] \(M\to H\), \(x\mapsto x\xi\), is injective.
For a representation \(\pi:A\to B(H)\), “separating for \(\pi(A)\)” has the
same meaning; it is stronger than faithfulness of \(\pi\), since faithfulness
only requires each nonzero algebra element to act nontrivially on at least
one vector.

## Duality with cyclicity

A vector \(\xi\) is separating for \(M\) exactly when it is
[[operator-algebras/cyclic-vector|cyclic]] for the commutant \(M'\). Dually,
\(\xi\) is cyclic for \(M\) exactly when it is separating for \(M'\). The
proof uses the [[linear-algebra/orthogonal-projection|orthogonal projection]] onto \(\overline{M'\xi}\): this
projection belongs to \(M''\), and for a
[[operator-algebras/von-neumann-algebra|von Neumann algebra]] the identity
\(M''=M\) turns separation into density.

## Examples and failure

For \(M=B(H)\) with \(\dim H>1\), no vector is separating: a nonzero
projection onto \(\xi^\perp\) annihilates \(\xi\). In the standard
representation of \(L^\infty(X,\mu)\) on \(L^2(X,\mu)\), a vector is
separating precisely when it is nonzero [[measure-theory/almost-everywhere|almost everywhere]]. A faithful normal
state represented by the [[operator-algebras/gns-construction|GNS construction]] has a cyclic vector, but that
vector becomes separating for the represented von Neumann algebra only under
the appropriate faithfulness hypothesis.

## Role in modular theory

A von Neumann algebra with a vector that is both cyclic and separating is in
standard position for Tomita–Takesaki theory. On the dense domain \(M\xi\),
one defines the antilinear operator \(S_0(x\xi)=x^*\xi\). Separation makes
this definition unambiguous, while cyclicity makes its domain dense. The
closure and polar decomposition of \(S_0\) then produce the [[operator-algebras/modular-operator|modular operator]]
and [[operator-algebras/modular-conjugation|modular conjugation]].

## References

1. Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras, Volume I: Elementary Theory*, American Mathematical Society, 1997. [AMS DOI record](https://doi.org/10.1090/gsm/015). Relevant: §5.5 on cyclic and separating vectors.
2. Masamichi Takesaki, *Theory of Operator Algebras I*, Springer, 1979. [DOI record](https://doi.org/10.1007/978-1-4612-6188-9). Relevant: Chapter VI on cyclic and separating vectors and modular theory.
