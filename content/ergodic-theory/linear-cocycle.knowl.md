+++
id = "ergodic-theory/linear-cocycle"
title = "Linear cocycle over a dynamical system"
kind = "definition"
summary = "A measurable family of linear maps multiplied along an orbit."
aliases = ["matrix cocycle"]
domains = ["ergodic-theory"]
section_mode = "progressive"
prerequisites = ["ergodic-theory/measure-preserving-system", "linear-algebra/linear-map"]
+++

For a [[ergodic-theory/measure-preserving-system|probability-preserving transformation]] \(T\), a measurable map \(A:X\to GL_d(\mathbb R)\) generates the **linear cocycle**
\[
A^{(0)}(x)=I,\qquad A^{(n)}(x)=A(T^{n-1}x)\cdots A(x)\quad(n\geq1).
\]
It satisfies \(A^{(n+m)}(x)=A^{(m)}(T^nx)A^{(n)}(x)\). If \(T\) is invertible, negative times are defined by \(A^{(-n)}(x)=A^{(n)}(T^{-n}x)^{-1}\).

## Tangent dynamics

For a differentiable map, the chain rule makes its derivative iterates a cocycle on the tangent bundle. In a measurable trivialization this has the matrix form above. It describes growth of tangent vectors, whereas Koopman operators describe functions of the state.
