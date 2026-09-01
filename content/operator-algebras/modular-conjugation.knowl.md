+++
id = "operator-algebras/modular-conjugation"
title = "Modular conjugation"
kind = "definition"
summary = "Modular conjugation is the antiunitary involution in the polar decomposition of a Tomita operator."
aliases = ["Tomita conjugation", "J operator"]
domains = ["operator-algebras"]
prerequisites = ["operator-algebras/von-neumann-algebra", "operator-algebras/cyclic-vector", "operator-algebras/separating-vector", "operator-algebras/tomita-operator", "operator-algebras/modular-operator"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(M\subseteq B(H)\) be a
[[operator-algebras/von-neumann-algebra|von Neumann algebra]] with
[[operator-algebras/cyclic-vector|cyclic]]
[[operator-algebras/separating-vector|separating vector]] \(\Omega\), and let
\(S\) be the associated
[[operator-algebras/tomita-operator|Tomita operator]].
In the polar decomposition
\[
S=J\Delta^{1/2},
\]
the **modular conjugation** is the antiunitary operator \(J:H\to H\). It is
conjugate-linear, satisfies
\(\langle J\xi,J\eta\rangle=\langle\eta,\xi\rangle\), and is an involution:
\(J^2=1\). Moreover \(J\Omega=\Omega\). Both \(J\) and the positive
[[operator-algebras/modular-operator|modular operator]] \(\Delta\) are
determined by the pair \((M,\Omega)\); the notation \(J\) does not denote a
choice of complex structure.

## Relation to the commutant

The [[operator-algebras/tomita-takesaki-theorem|Tomita–Takesaki theorem]]
identifies the conjugated algebra as
\[
JMJ=M',
\]
where \(M'\) is the [[operator-algebras/commutant|commutant]] of \(M\). Thus
\(x\mapsto JxJ\) is a conjugate-linear multiplicative bijection from \(M\)
onto \(M'\); equivalently, \(x\mapsto Jx^*J\) is a linear
\(*\)-anti-isomorphism. This conclusion is a theorem, not merely a consequence
of antiunitarity.

## Interaction with modular time

The polar factors satisfy
\[
J\Delta J=\Delta^{-1}
\quad\text{and}\quad
J\Delta^{it}J=\Delta^{it}.
\]
Consequently \(J\) exchanges the algebra with its commutant while respecting
the unitary modular evolution in the appropriate conjugate-linear sense.
When the [[operator-algebras/vector-state|vector state]] is tracial,
\(\Delta=1\), but \(J\) can still be
nontrivial: it implements passage from left to right multiplication in the
[[operator-algebras/standard-form|standard representation]].

## Example and conventions

For \(M=M_n(\mathbb C)\) acting on its Hilbert–Schmidt space with trace vector,
\(J(x)=x^*\). Left multiplication by \(a\) is carried to right multiplication
by \(a^*\), exhibiting \(JMJ=M'\).

**Warning.** Some inner-product conventions change intermediate adjoint
formulas, but not the defining statement that \(J\) is the antiunitary polar
factor of \(S\). It should not be confused with an arbitrary antiunitary
implementing a symmetry.

## References

1. Masamichi Takesaki, *Theory of Operator Algebras I*, Springer, 1979. [DOI record](https://doi.org/10.1007/978-1-4612-6188-9). Relevant: Chapter VI, §1 on the polar decomposition of the Tomita operator.
