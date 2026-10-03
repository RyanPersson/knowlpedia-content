+++
id = "algebra-modules/polynomial-module-from-operator"
title = "Polynomial module associated with a linear operator"
kind = "definition"
summary = "A linear operator T makes its vector space an F[X]-module by letting X act as T."
aliases = ["polynomial module from an operator", "F[X]-module of a linear operator", "operator module"]
domains = ["algebra-modules"]
section_mode = "progressive"
prerequisites = ["linear-algebra/vector-space", "linear-algebra/linear-map", "algebra-rings/polynomial-ring", "algebra-modules/module"]
dependency_heuristic = "semantic-transcript-review-v1"
dependency_review_count = 1
+++

Let \(V\) be an \(F\)-[[linear-algebra/vector-space|vector space]] and \(T:V\to V\) an \(F\)-[[linear-algebra/linear-map|linear map]]. The **polynomial module associated with \(T\)** is the \(F[X]\)-[[algebra-modules/module|module]] on \(V\) whose action is
\[
\left(\sum_{j=0}^m a_jX^j\right)\cdot v
=\sum_{j=0}^m a_jT^j(v),\qquad T^0=\operatorname{id}_V.
\]

This is the unique action of the [[algebra-rings/polynomial-ring|polynomial ring]] \(F[X]\) for which constants act by the original scalar multiplication and \(X\cdot v=T(v)\). Finite dimensionality is not required.

## Why this satisfies the module axioms

Polynomial evaluation gives \((f+g)(T)=f(T)+g(T)\), \((fg)(T)=f(T)g(T)\), and \(1(T)=\operatorname{id}_V\). The multiplicative identity follows by expanding products and using \(T^iT^j=T^{i+j}\). Each \(f(T)\) is linear, so the two distributive [[algebra-modules/module-axioms|module axioms]] follow as well.

The ring of all linear endomorphisms of \(V\) may be noncommutative; the scalar operators and the powers of this single \(T\) commute, which is all the construction needs.

## Morphisms and invariant subspaces

For operators \(T\) on \(V\) and \(S\) on \(W\), a linear map \(u:V\to W\) is an \(F[X]\)-module homomorphism exactly when \(uT=Su\). A subspace is an \(F[X]\)-submodule exactly when it is \(T\)-invariant.

For finite-dimensional \(V\), the [[linear-algebra/minimal-polynomial|minimal polynomial]] generates the annihilator of this module. The construction is the bridge to [[algebra-modules/rcf-from-structure-theorem|rational canonical form from the module structure theorem]].

## References

1. The polynomial identities above verify existence directly; the images of constants and \(X\) prove uniqueness. The intertwining condition extends from \(X\) to every polynomial by induction and linearity.
