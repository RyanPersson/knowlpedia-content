+++
id = "quantum-foundations/positive-semidefinite-operator"
title = "Positive semidefinite operator"
kind = "knowl"
summary = "A self-adjoint operator whose quadratic form is nonnegative on every vector."
aliases = ["positive semidefinite operator", "positive operator", "positive semidefinite"]
domains = ["quantum-foundations", "linear-algebra"]
+++

An operator \(A\) on a complex Hilbert space is **positive semidefinite**, written \(A\ge0\), if
\[
\langle x,Ax\rangle\ge0
\]
for every vector \(x\). Positivity implies that \(A\) is self-adjoint. In finite dimension it is equivalent to all eigenvalues of \(A\) being real and nonnegative, and also equivalent to a factorization \(A=B^*B\).

Positive operators are the effects in a [[quantum-foundations/positive-operator-valued-measure|POVM]] and, after trace normalization, the [[quantum-foundations/density-operator|density operators]] of quantum theory.
