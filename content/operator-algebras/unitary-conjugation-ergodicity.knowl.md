+++
id = "operator-algebras/unitary-conjugation-ergodicity"
title = "Ergodicity of unitary conjugation on matrices"
kind = "example"
summary = "Conjugation by the full unitary group has only scalar fixed matrices and preserves normalized trace."
aliases = []
domains = ["operator-algebras"]
section_mode = "progressive"
prerequisites = ["operator-algebras/state-preserving-dynamical-system", "operator-algebras/fixed-point-algebra", "operator-algebras/ergodic-operator-algebra-action", "operator-algebras/ergodic-operator-algebra-action", "operator-algebras/ergodic-operator-algebra-action", "operator-algebras/ergodic-operator-algebra-action", "lie-groups/unitary-group", "operator-algebras/tracial-state"]
+++

For \(d\geq2\), the [[lie-groups/unitary-group|unitary group]] \(U(d)\) acts on \(M_d(\mathbb C)\) by
\[
\alpha_g(a)=gag^*,\qquad \varphi(a)=d^{-1}\operatorname{Tr}(a).
\]
This is a [[operator-algebras/state-preserving-dynamical-system|state-preserving]] action, and its [[operator-algebras/fixed-point-algebra|fixed-point algebra]] is \(\mathbb CI_d\). It is therefore an [[operator-algebras/ergodic-operator-algebra-action|algebraically ergodic action]] on a noncommutative probability space.

## Verification

The identity \((gh)^*=h^*g^*\) gives \(\alpha_{gh}=\alpha_g\alpha_h\), and cyclicity of the matrix trace gives \(\varphi\circ\alpha_g=\varphi\). A matrix fixed by all diagonal unitaries must be diagonal; being fixed also by all permutation matrices forces every diagonal entry to be equal.

## A group action versus one automorphism

Conjugation by a single unitary \(u\) has the commutant of \(u\) as its fixed algebra. For \(d\geq2\), that algebra contains nontrivial projections onto eigenspaces or subspaces of an eigenspace, so a single such conjugation is not ergodic. Joint invariance under the whole group is the stronger constraint.
