+++
id = "ergodic-theory/lyapunov-exponent"
title = "Lyapunov exponent of a linear cocycle"
kind = "definition"
summary = "An asymptotic exponential growth rate of a vector under iterated linear dynamics."
aliases = []
domains = ["ergodic-theory"]
section_mode = "progressive"
prerequisites = ["ergodic-theory/linear-cocycle", "linear-algebra/norm"]
+++

For a [[ergodic-theory/linear-cocycle|linear cocycle]] \(A^{(n)}(x)\) and a nonzero vector \(v\), the **Lyapunov exponent**, when the limit exists, is
\[
\lambda(x,v)=\lim_{n\to\infty}\frac1n\log\|A^{(n)}(x)v\|.
\]
It measures exponential growth or contraction along the orbit. Equivalent fixed norms in finite dimension give the same limit.

## Relation to Koopman frequencies

A positive Lyapunov exponent concerns growth of vectors, for example infinitesimal perturbations of a trajectory. A Koopman eigenvalue of a probability-preserving invertible system has modulus one and describes oscillation of an observable. These quantities answer different questions and can coexist in a mixing system such as the cat map.
