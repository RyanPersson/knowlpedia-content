+++
id = "quantum-foundations/positive-operator-valued-measure"
title = "Positive operator-valued measure"
kind = "knowl"
summary = "A family of positive operators summing to the identity and representing a generalized quantum measurement."
aliases = ["positive operator-valued measure", "POVM", "positive operator valued measure"]
domains = ["quantum-foundations"]
+++

On a [[quantum-foundations/complex-hilbert-space-finite|finite-dimensional complex Hilbert space]] \(H\), a **positive operator-valued measure** or **POVM** with finite outcome set \(I\) is a family of [[quantum-foundations/positive-semidefinite-operator|positive semidefinite operators]] \((E_i)_{i\in I}\) satisfying
\[
\sum_{i\in I}E_i=I_H.
\]
For a [[quantum-foundations/density-operator|density operator]] \(\rho\), outcome \(i\) has probability \(\operatorname{Tr}(\rho E_i)\). Positivity makes these probabilities nonnegative, and the normalization makes them sum to one.

Orthogonal projective measurements are a special case; general POVM effects need not be projections or mutually orthogonal.
