+++
id = "ergodic-theory/ergodic-transformation"
title = "Ergodic transformation"
kind = "definition"
summary = "A probability-preserving transformation with no invariant event of intermediate probability."
aliases = ["ergodicity", "ergodic probability-preserving system"]
domains = ["ergodic-theory"]
section_mode = "progressive"
prerequisites = ["ergodic-theory/measure-preserving-system", "ergodic-theory/invariant-sigma-algebra"]
+++

A [[ergodic-theory/measure-preserving-system|probability-preserving transformation]] \(T\) is **ergodic** if
\[
\mu(T^{-1}E\triangle E)=0\quad\Longrightarrow\quad\mu(E)\in\{0,1\}
\qquad(E\in\Sigma).
\]
Equivalently, its [[ergodic-theory/invariant-sigma-algebra|invariant sigma-algebra]] is trivial modulo null sets.

## Meaning

There is no decomposition into two measurable invariant pieces of positive probability. Ergodicity does not assert a single orbit, nor does it require all orbits to be dense. On an atomless space, every orbit of a single invertible transformation is countable and has measure zero.

## Examples

The [[ergodic-theory/finite-uniform-system|finite uniform systems]] that are ergodic are exactly single cycles. An [[ergodic-theory/torus-translation-ergodicity|irrational circle rotation]] is ergodic, while an orthogonal map of a finite-dimensional Gaussian space is not.
