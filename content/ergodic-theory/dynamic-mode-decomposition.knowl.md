+++
id = "ergodic-theory/dynamic-mode-decomposition"
title = "Dynamic mode decomposition"
kind = "construction"
summary = "A least-squares linear evolution fitted to paired snapshots, then analyzed through its modes and eigenvalues."
aliases = ["DMD"]
domains = ["ergodic-theory"]
section_mode = "progressive"
prerequisites = ["linear-algebra/linear-map", "linear-algebra/eigenvalue", "ergodic-theory/koopman-operator"]
+++

Given snapshot pairs \(x_j,y_j\in\mathbb C^d\), assemble \(X=[x_1\ \cdots\ x_M]\), \(Y=[y_1\ \cdots\ y_M]\). **Dynamic mode decomposition (DMD)** fits a matrix \(A\) minimizing
\[
\|Y-AX\|_F^2,
\]
using the solution of minimum Frobenius norm when the minimizer is not unique, and studies its [[linear-algebra/eigenvalue|eigenvalues]] and associated modes. The norm \(\|B\|_F^2=\sum_{i,j}|B_{ij}|^2\) is the sum of squared entry magnitudes.

## Koopman connection

If \(y_j=T(x_j)\), this fits future coordinates as linear combinations of present coordinates. These coordinates are a finite dictionary of observables. Their span need not be invariant under the actual [[ergodic-theory/koopman-operator|Koopman operator]]; the fitted finite matrix is therefore an approximation, even when the original dynamics is deterministic.

The broader [[ergodic-theory/extended-dynamic-mode-decomposition|extended DMD]] construction uses nonlinear observables and makes the projected operator interpretation explicit. Finite-data eigenvalues need not be true Koopman eigenvalues.

## References

1. J. H. Tu, C. W. Rowley, D. M. Luchtenburg, S. L. Brunton, and J. N. Kutz, [“On Dynamic Mode Decomposition: Theory and Applications”](https://arxiv.org/pdf/1312.0041), §2.
