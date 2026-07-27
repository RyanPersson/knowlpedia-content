+++
id = "quantum-foundations/positive-semidefinite-operator"
title = "Positive semidefinite operator"
kind = "knowl"
summary = "A self-adjoint operator whose quadratic form is nonnegative on every vector."
aliases = ["positive semidefinite operator", "positive operator", "positive semidefinite"]
domains = ["quantum-foundations", "linear-algebra"]
+++

Let $H$ be a complex [[linear-algebra/hilbert-space|Hilbert space]]. A bounded linear operator $A:H\to H$ is **positive semidefinite**, written $A\ge0$, if
$$
\langle x,Ax\rangle\ge0
$$
for every $x\in H$. This condition implies that $A$ is self-adjoint and is equivalent to the existence of a bounded operator $B$ with $A=B^*B$. In finite dimension it is also equivalent to every eigenvalue of $A$ being nonnegative.

## Quantum interpretation

Positive operators bounded above by the identity are the effects in a [[quantum-foundations/positive-operator-valued-measure|POVM]]. Positive trace-class operators of trace $1$ are [[quantum-foundations/density-operator|density operators]].
