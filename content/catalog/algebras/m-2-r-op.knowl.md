+++
id = "catalog/algebras/m-2-r-op"
title = "Opposite ring of M_2(R)"
kind = "definition"
summary = "Opposite ring of M_2(R)."
aliases = []
domains = ["catalog", "algebra-rings"]
prerequisites = ["catalog/algebras/m-2-r"]
+++

The **opposite ring \(A^{\mathrm{op}}\)** of [[catalog/algebras/m-2-r|\(A=M_2(\mathbb R)\)]] has the same matrices, addition, and unit as \(A\), and product \(a\star b=ba\), where the right-hand side uses the original matrix multiplication.

Associativity follows from associativity in \(A\); distributivity and the unit identities are unchanged. Scalar multiplication by real numbers makes this a unital real associative algebra of dimension four.

## Transpose and identity

Transpose \(T:A^{\mathrm{op}}\to A\), \(T(a)=a^{\mathsf T}\), is a unital real algebra isomorphism since \((ba)^{\mathsf T}=a^{\mathsf T}b^{\mathsf T}\). The identity on matrices is not a ring homomorphism from \(A^{\mathrm{op}}\) to \(A\): for the matrix units \(a=E_{12}\), \(b=E_{21}\), we have \(ab=E_{11}\ne E_{22}=ba\).
