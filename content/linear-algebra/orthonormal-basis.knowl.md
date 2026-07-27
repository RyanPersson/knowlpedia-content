+++
id = "linear-algebra/orthonormal-basis"
title = "Orthonormal basis"
kind = "knowl"
summary = "A basis whose vectors have unit length and are pairwise orthogonal."
aliases = ["orthonormal basis", "orthonormal bases"]
domains = ["linear-algebra", "quantum-foundations"]
+++

An **orthonormal basis** of a [[linear-algebra/hilbert-space|Hilbert space]] \(H\) is a family \((e_i)_{i\in I}\) whose closed linear span is \(H\) and which satisfies
\[
\langle e_i,e_j\rangle=\delta_{ij}.
\]
Thus each basis vector has norm one, distinct basis vectors are orthogonal, and every vector in \(H\) can be approximated in norm by finite linear combinations of the \(e_i\). In finite dimensions, “closed linear span” may be replaced by “linear span.”

Every \(x\in H\) has the norm-convergent expansion
\[
x=\sum_{i\in I}\langle e_i,x\rangle e_i.
\]
In a finite-dimensional complex space, placing the basis vectors as columns gives a unitary matrix.
