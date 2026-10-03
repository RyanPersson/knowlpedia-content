+++
id = "ergodic-theory/ergodic-decomposition-theorem"
title = "Ergodic decomposition theorem"
kind = "theorem"
summary = "An invariant probability on a standard Borel system is a mixture of ergodic invariant probabilities."
aliases = []
domains = ["ergodic-theory"]
section_mode = "progressive"
prerequisites = ["ergodic-theory/measure-preserving-system", "ergodic-theory/ergodic-transformation", "measure-theory/standard-borel-space", "measure-theory/disintegration-theorem", "ergodic-theory/invariant-sigma-algebra"]
+++

For a Borel [[ergodic-theory/measure-preserving-system|probability-preserving transformation]] \(T\) on a [[measure-theory/standard-borel-space|standard Borel space]], there is a measurable family \(y\mapsto\mu_y\) of invariant [[ergodic-theory/ergodic-transformation|ergodic]] Borel probability measures, with a probability \(\nu\) on an indexing space, such that
\[
\mu(E)=\int\mu_y(E)\,d\nu(y)
\qquad(E\text{ Borel}).
\]
The family is the disintegration over the invariant factor, unique modulo null sets and equivalence of indexing. It is the **ergodic decomposition** of the system.

## Time averages within components

The component average of \(f\) supplies \(\mathbb E[f\mid\mathcal I_T]\). Different components can therefore give different long-time statistics even though the overall measure is preserved.

## Finite example

For a permutation with cycles \(C_j\), let \(\mu_j\) be uniform on \(C_j\). The uniform measure on all \(n\) points decomposes as \(\sum_j(|C_j|/n)\mu_j\). Each cycle system is ergodic. On an atomless system the components can each have total \(\mu\)-measure zero, so this is a measure mixture, not necessarily a countable partition into positive-measure pieces.

## References

1. Terence Tao, [“254A, Lecture 9: Ergodicity”](https://terrytao.wordpress.com/2008/02/04/254a-lecture-9-ergodicity/), Proposition 4 (Ergodic decomposition).
