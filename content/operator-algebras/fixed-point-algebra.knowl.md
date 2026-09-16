+++
id = "operator-algebras/fixed-point-algebra"
title = "Fixed-point algebra of an action"
kind = "definition"
summary = "The subalgebra consisting of all elements fixed by the dynamics."
aliases = ["invariant subalgebra of dynamics"]
domains = ["operator-algebras"]
section_mode = "progressive"
prerequisites = ["operator-algebras/state-preserving-dynamical-system"]
+++

For an [[operator-algebras/star-automorphism|automorphism]] \(\alpha\) of a unital operator algebra \(A\), its **fixed-point algebra** is
\[
A^\alpha=\{a\in A:\alpha(a)=a\}.
\]
For a group action use \(A^G=\{a:\alpha_g(a)=a\text{ for every }g\in G\}\). These are unital \(*\)-subalgebras, norm closed in a \(C^*\)-algebra and ultraweakly closed for normal actions on a von Neumann algebra.

## Ergodicity

A scalar fixed algebra is the defining condition for an [[operator-algebras/ergodic-operator-algebra-action|ergodic operator-algebra action]].
