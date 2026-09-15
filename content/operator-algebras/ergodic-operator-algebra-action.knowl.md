+++
id = "operator-algebras/ergodic-operator-algebra-action"
title = "Ergodic action on an operator algebra"
kind = "definition"
summary = "An action whose common fixed-point algebra consists only of scalar multiples of the identity."
aliases = ["fixed-algebra ergodicity"]
domains = ["operator-algebras"]
section_mode = "progressive"
prerequisites = ["operator-algebras/state-preserving-dynamical-system", "operator-algebras/fixed-point-algebra"]
+++

A [[operator-algebras/state-preserving-dynamical-system|state-preserving action]] \(\alpha:G\to\operatorname{Aut}(A)\) on a unital operator algebra is **ergodic in the fixed-algebra sense** if its [[operator-algebras/fixed-point-algebra|fixed-point algebra]] is
\[
A^G=\{a\in A:\alpha_g(a)=a\text{ for every }g\in G\}=\mathbb C1.
\]
For one automorphism, take the action of \(\mathbb Z\) that it generates.

## Classical comparison

For \(A=L^\infty(X,\mu)\), this is precisely measurable ergodicity. For \(A=C(X)\), it concerns only continuous invariant functions; by itself it neither determines a unique invariant probability measure nor implies ergodicity for every invariant measure. The algebra and the notion of invariance must therefore be specified.

## Noncommutative example

The full unitary group acts ergodically on matrices by [[operator-algebras/unitary-conjugation-ergodicity|unitary conjugation]], preserving normalized trace.
