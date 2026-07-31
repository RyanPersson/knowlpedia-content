+++
id = "quantum-foundations/positive-operator-valued-measure"
title = "Positive operator-valued measure"
kind = "definition"
summary = "A normalized, weakly countably additive measure taking measurable sets to positive operators."
aliases = ["positive operator-valued measure", "POVM", "positive operator valued measure"]
domains = ["quantum-foundations"]
+++

Let \((\Omega,\Sigma)\) be a measurable space and \(H\) a complex [[linear-algebra/hilbert-space|Hilbert space]]. A **positive operator-valued measure** or **POVM** is a map
\[
E:\Sigma\longrightarrow B(H)
\]
such that:

1. \(E(A)\) is a [[quantum-foundations/positive-semidefinite-operator|positive operator]] for every \(A\in\Sigma\);
2. \(E(\Omega)=I_H\);
3. for every pairwise disjoint sequence \((A_n)\) in \(\Sigma\),
   \[
   \left\langle x,E\!\left(\bigcup_nA_n\right)y\right\rangle
   =
   \sum_n\langle x,E(A_n)y\rangle
   \qquad(x,y\in H).
   \]

The third condition is countable additivity in the weak operator topology.

## Born rule

For a [[quantum-foundations/density-operator|density operator]] \(\rho\), the scalar measure
\[
\mathbb P_\rho(A)=\operatorname{Tr}(\rho E(A))
\]
is the probability distribution of the measurement outcome.

## Discrete outcomes

For a finite or countable outcome set \(I\), a POVM is equivalently a family of positive operators \((E_i)_{i\in I}\) satisfying
\[
\sum_{i\in I}E_i=I_H
\]
in the weak operator topology. Then
\(\mathbb P_\rho(\{i\})=\operatorname{Tr}(\rho E_i)\).

## Projection-valued measures

A POVM is a **projection-valued measure** when every \(E(A)\) is an orthogonal projection; equivalently,
\[
E(A\cap B)=E(A)E(B).
\]
General POVM effects need not be projections or mutually orthogonal.
