+++
id = "operator-algebras/noncommutative-probability-space"
title = "Noncommutative probability space"
kind = "definition"
summary = "A unital operator algebra with a state serving as expectation."
aliases = ["C*-probability space", "von Neumann probability space"]
domains = ["operator-algebras"]
section_mode = "progressive"
prerequisites = ["operator-algebras/unital-cstar-algebra", "operator-algebras/state-cstar-algebra"]
+++

A **\(C^*\)-algebraic probability space** is a pair \((A,\varphi)\), where \(A\) is a [[operator-algebras/unital-cstar-algebra|unital \(C^*\)-algebra]] and \(\varphi:A\to\mathbb C\) is a [[operator-algebras/state-cstar-algebra|state]]:
\[
\varphi(1)=1,\qquad\varphi(a^*a)\geq0\quad(a\in A).
\]
It is called a **noncommutative probability space** when no commutativity assumption is imposed on \(A\). A von Neumann probability space uses a von Neumann algebra and a [[operator-algebras/normal-state|normal state]]; faithfulness or traciality is an additional hypothesis, stated when needed.

## Classical model

For a probability space, \(A=L^\infty(X,\mu)\) and \(\varphi(f)=\int f\,d\mu\). Projections are indicator functions modulo null sets and have state equal to the event's probability. In a matrix algebra, a density matrix \(\rho\) supplies \(\varphi(a)=\operatorname{Tr}(\rho a)\).

## Measurable and topological information

The classical \(L^\infty\) algebra remembers events modulo null sets. The algebra \(C(Y)\) of continuous functions on a compact Hausdorff space instead encodes topology through [[operator-algebras/gelfand-duality|Gelfand duality]]. These models express different kinds of structure.
