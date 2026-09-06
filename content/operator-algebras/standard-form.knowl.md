+++
id = "operator-algebras/standard-form"
title = "Standard form of a von Neumann algebra"
kind = "definition"
summary = "A faithful representation of a von Neumann algebra equipped with its canonical conjugation and self-dual positive cone."
aliases = ["Haagerup standard form", "standard representation"]
domains = ["operator-algebras"]
prerequisites = ["operator-algebras/von-neumann-algebra", "operator-algebras/natural-positive-cone", "operator-algebras/modular-conjugation", "linear-algebra/hilbert-space"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

A **standard form** of a [[operator-algebras/von-neumann-algebra|von Neumann algebra]] \(M\) is a quadruple \((M,H,J,P)\), with \(M\subseteq B(H)\) faithful and nondegenerate, \(J\) a conjugate-linear isometric involution, and \(P\subseteq H\) a closed self-dual cone, such that
\[
JMJ=M',\qquad J\xi=\xi\quad(\xi\in P),
\]
\[
xJxJ(P)\subseteq P\quad(x\in M),
\qquad JzJ=z^*\quad(z\in Z(M)).
\]
The cone \(P\) is the [[operator-algebras/natural-positive-cone|natural positive cone]], and \(J\) plays the role of [[operator-algebras/modular-conjugation|modular conjugation]]. All four compatibility conditions belong to the standard-form package; merely realizing \(M\) faithfully on a [[linear-algebra/hilbert-space|Hilbert space]] does not give a standard form.

## Existence and uniqueness

Every von Neumann algebra has a standard form. Moreover, if \((M,H,J,P)\) and \((N,K,J_N,P_N)\) are standard forms and \(\alpha\colon M\to N\) is a normal \(*\)-isomorphism, there is a unique unitary \(U\colon H\to K\) implementing \(\alpha\) and satisfying
\[
UJ=J_NU,\qquad U(P)=P_N.
\]
This is Haagerup's standard-form uniqueness theorem.

## Positive functionals as vectors

For every [[operator-algebras/normal-functional|normal positive functional]] \(\varphi\) on \(M\), there is a unique vector \(\xi_\varphi\in P\) such that
\[
\varphi(x)=\langle x\xi_\varphi,\xi_\varphi\rangle
\qquad(x\in M).
\]
Thus the cone removes the nonuniqueness that normally occurs when a [[operator-algebras/positive-linear-functional|positive functional]] is represented by a vector in an arbitrary representation.

## Conventions and scope

Some authors call a representation “standard” when only a conjugation \(J_0\) with \(J_0MJ_0=M'\) is specified. That weaker usage omits the canonical cone and does not, by itself, specify Haagerup's standard form. Here “standard form” always means the full quadruple and the displayed axioms.

## References

1. U. Haagerup, “The Standard Form of von Neumann Algebras,” *Mathematica Scandinavica* 37 (1975), 271–283. [DOI record](https://doi.org/10.7146/math.scand.a-11606). Relevant: Definition 2.1 and Theorem 2.3 on the standard-form axioms and uniqueness.
2. H. Araki, “Some Properties of Modular Conjugation Operator of von Neumann Algebras and a Non-commutative Radon–Nikodym Theorem with a Chain Rule,” *Pacific Journal of Mathematics* 50 (1974), 309–354. [DOI record](https://doi.org/10.2140/pjm.1974.50.309). Relevant: the natural cone and its representation of normal positive functionals.
