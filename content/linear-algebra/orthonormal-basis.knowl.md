+++
id = "linear-algebra/orthonormal-basis"
title = "Orthonormal basis"
kind = "knowl"
summary = "A basis whose vectors have unit length and are pairwise orthogonal."
aliases = ["orthonormal basis", "orthonormal bases"]
domains = ["linear-algebra", "quantum-foundations"]
+++

An **orthonormal basis** of an [[linear-algebra/inner-product-space|inner-product space]] \(H\) is a basis \((e_i)\) satisfying
\[
\langle e_i,e_j\rangle=\delta_{ij}.
\]
Thus each basis vector has norm one and distinct basis vectors are orthogonal. In a finite-dimensional complex space, placing the vectors as columns of a matrix gives an orthonormal basis exactly when the matrix is unitary.

Every vector has coordinates \(x=\sum_i\langle e_i,x\rangle e_i\); in a [[linear-algebra/hilbert-space|Hilbert space]] the corresponding infinite sum converges in norm.
