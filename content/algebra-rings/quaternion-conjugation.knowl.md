+++
id = "algebra-rings/quaternion-conjugation"
title = "Standard conjugation of a quaternion algebra"
kind = "definition"
summary = "The canonical linear involution that reverses the order of multiplication."
aliases = []
domains = ["algebra-rings"]
section_mode = "progressive"
prerequisites = ["algebra-rings/quaternion-algebra"]
+++

In a [[algebra-rings/quaternion-algebra|quaternion algebra]] \(B=(a,b)_F\), **standard conjugation** is the \(F\)-linear map
\[
\overline{x_0+x_1i+x_2j+x_3ij}=x_0-x_1i-x_2j-x_3ij.
\]
It fixes \(F\), satisfies \(\overline{\bar x}=x\), and reverses multiplication: \(\overline{xy}=\bar y\bar x\). This is the intrinsic standard involution, independent of the chosen quaternion presentation.

## Scalar coefficients stay fixed

Even when \(F\subseteq\mathbb C\), the coefficients \(x_i\) are not complex-conjugated. Standard quaternion conjugation is a different operation from complex conjugation of the coefficient field.

## Matrix example

In the split algebra \(M_2(F)\), it is
\[
\begin{pmatrix}a&b\\c&d\end{pmatrix}
\longmapsto\begin{pmatrix}d&-b\\-c&a\end{pmatrix}.
\]
Multiplying a matrix by this conjugate gives its determinant times the identity.
