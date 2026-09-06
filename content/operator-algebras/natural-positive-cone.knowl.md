+++
id = "operator-algebras/natural-positive-cone"
title = "Natural positive cone"
kind = "definition"
summary = "The canonical self-dual cone obtained from the modular data of a cyclic separating representation."
aliases = ["self-dual cone of standard form", "P-natural"]
domains = ["operator-algebras"]
prerequisites = ["operator-algebras/von-neumann-algebra", "operator-algebras/cyclic-vector", "operator-algebras/separating-vector", "operator-algebras/tomita-operator", "operator-algebras/modular-operator", "operator-algebras/modular-conjugation"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(M\subseteq B(H)\) be a [[operator-algebras/von-neumann-algebra|von Neumann algebra]] with [[operator-algebras/cyclic-vector|cyclic]] [[operator-algebras/separating-vector|separating vector]] \(\Omega\), and let \(S=J\Delta^{1/2}\) be the polar decomposition of its [[operator-algebras/tomita-operator|Tomita operator]]. The **natural positive cone** is
\[
P_\Omega^\natural
=\overline{\{\Delta^{1/4}x\Omega:x\in M_+\}}\subseteq H,
\]
where the closure is in the Hilbert-space norm, \(\Delta\) is the [[operator-algebras/modular-operator|modular operator]], and \(J\) is the [[operator-algebras/modular-conjugation|modular conjugation]]. Thus \(P_\Omega^\natural\) is a distinguished closed convex cone attached to the represented algebra and its modular data, not the operator-positive cone \(M_+\). It is the cone used to place this representation in standard form.

## Self-duality and invariance

The cone is self-dual:
\[
P_\Omega^\natural
=\{\xi\in H:\langle\xi,\eta\rangle\geq0
\text{ for every }\eta\in P_\Omega^\natural\}.
\]
It is fixed pointwise by \(J\), and \(xJxJ\) maps it into itself for every \(x\in M\). These are structural theorems of modular theory, not extra clauses in the displayed construction.

Every [[operator-algebras/normal-functional|normal positive functional]] on \(M\) is represented by a unique vector \(\xi\in P_\Omega^\natural\) through \(\varphi(x)=\langle x\xi,\xi\rangle\). This uniqueness is one reason the cone is more useful than an arbitrary positive-vector realization.

## Relationship to standard form

The quadruple \((M,H,J,P_\Omega^\natural)\) is a [[operator-algebras/standard-form|standard form]] of \(M\). Different cyclic separating vectors may produce different Tomita operators, but the resulting standard forms are canonically unitarily equivalent. Consequently the natural cone expresses positivity in a representation-independent way once the standard-form identification is made.

## References

1. H. Araki, “Some Properties of Modular Conjugation Operator of von Neumann Algebras and a Non-commutative Radon–Nikodym Theorem with a Chain Rule,” *Pacific Journal of Mathematics* 50 (1974), 309–354. [DOI record](https://doi.org/10.2140/pjm.1974.50.309). Relevant: construction, self-duality, and representation of normal positive functionals by cone vectors.
2. U. Haagerup, “The Standard Form of von Neumann Algebras,” *Mathematica Scandinavica* 37 (1975), 271–283. [DOI record](https://doi.org/10.7146/math.scand.a-11606). Relevant: Theorem 1.6 and Definition 2.1 on the natural cone and standard form.
