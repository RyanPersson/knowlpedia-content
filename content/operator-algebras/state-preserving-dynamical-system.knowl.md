+++
id = "operator-algebras/state-preserving-dynamical-system"
title = "State-preserving operator-algebra dynamical system"
kind = "definition"
summary = "An operator algebra, a state, and a unital star endomorphism preserving that state."
aliases = ["W*-probability dynamical system"]
domains = ["operator-algebras"]
section_mode = "progressive"
prerequisites = ["operator-algebras/noncommutative-probability-space", "operator-algebras/unital-star-homomorphism", "operator-algebras/star-automorphism"]
+++

A **state-preserving dynamical system** is a triple \((A,\varphi,\alpha)\), where \((A,\varphi)\) is a unital \(C^*\)-algebraic [[operator-algebras/noncommutative-probability-space|probability space]] and \(\alpha:A\to A\) is a unital \(*\)-endomorphism satisfying
\[
\varphi\circ\alpha=\varphi.
\]
The system is invertible when \(\alpha\) is a \(*\)-automorphism. In the von Neumann setting, require \(\alpha\) and \(\varphi\) to be normal. For a group action, each \(\alpha_g\) is an [[operator-algebras/star-automorphism|automorphism]] and \(\alpha_{gh}=\alpha_g\alpha_h\).

## Preservation of events and probabilities

A \(*\)-homomorphism preserves multiplication, involution, and hence projections. State preservation keeps their probabilities unchanged. More general quantum channels need not be multiplicative; they belong to a broader setting than this definition.

## Classical convention

For invertible \(T\), use \(\alpha(f)=f\circ T^{-1}\). For noninvertible \(T\), use \(\beta(f)=f\circ T\), an injective state-preserving endomorphism of \(L^\infty\). If \(T\) is invertible, \(\beta=\alpha^{-1}\).
