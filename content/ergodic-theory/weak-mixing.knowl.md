+++
id = "ergodic-theory/weak-mixing"
title = "Weak mixing"
kind = "definition"
summary = "Ergodicity of the Cartesian square of a probability-preserving system."
aliases = ["weakly mixing system"]
domains = ["ergodic-theory"]
section_mode = "progressive"
prerequisites = ["ergodic-theory/product-system", "ergodic-theory/ergodic-transformation"]
+++

A probability-preserving transformation \(T\) is **weakly mixing** if its [[ergodic-theory/product-system|Cartesian square]] \(T\times T\) is [[ergodic-theory/ergodic-transformation|ergodic]] on \((X\times X,\mu\otimes\mu)\). A probability-preserving group action is weakly mixing if its diagonal action on the square is ergodic.

## Correlation criterion for a transformation

Equivalently, for every \(f,h\in L^2_0(X,\mu)\),
\[
\frac1N\sum_{n=0}^{N-1}|\langle U_T^nf,h\rangle|^2\longrightarrow0.
\]
Persistent oscillation cannot disappear merely by cancellation in this average. The [[ergodic-theory/weak-mixing-spectral-criterion|spectral characterization]] identifies the obstruction as nonconstant eigenfunctions in the invertible case.

## Comparison

Strong mixing implies weak mixing, which implies ergodicity. An irrational circle rotation is ergodic but not weakly mixing.

## References

1. Jesse Peterson, [*Lecture notes on ergodic theory*](https://www.math.vanderbilt.edu/~peters10/teaching/Spring2011/ErgodicTheoryNotes.pdf), 2011. §2.2.2.
