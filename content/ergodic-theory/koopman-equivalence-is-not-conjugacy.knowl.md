+++
id = "ergodic-theory/koopman-equivalence-is-not-conjugacy"
title = "Koopman equivalence need not imply conjugacy"
kind = "example"
summary = "Bernoulli shifts can have equivalent Koopman representations but different measure-theoretic entropies."
aliases = []
domains = ["ergodic-theory"]
section_mode = "progressive"
prerequisites = ["ergodic-theory/measurable-conjugacy", "ergodic-theory/bernoulli-shift", "ergodic-theory/kolmogorov-sinai-generator-theorem", "algebra-representation-theory/regular-representation"]
+++

The fair two-symbol and fair three-symbol two-sided [[ergodic-theory/bernoulli-shift|Bernoulli shifts]] have unitarily equivalent Koopman representations of \(\mathbb Z\), but are not measurably conjugate. Their entropies are \(\log2\) and \(\log3\), respectively, so [[ergodic-theory/measurable-conjugacy|conjugacy]] is impossible.

## Representation calculation

Choose an orthonormal basis in one coordinate consisting of the constant one and mean-zero functions. Finite products of these basis functions over different coordinates form an orthonormal basis of the product \(L^2\). Except for the constant function, each product has nonempty finite support, so its shift orbit is infinite with no repetitions.

Each such orbit spans one copy of the regular representation on \(\ell^2(\mathbb Z)\). In either alphabet size there are countably infinitely many distinct orbits, so each reduced Koopman representation is a countable direct sum of the regular representation. Adding the constant line gives equivalent full representations.

## What is lost

A unitary intertwiner need not respect products of bounded functions or positivity. The function-algebra structure in the classical operator-algebra dictionary retains information that the Hilbert-space representation alone can lose.
