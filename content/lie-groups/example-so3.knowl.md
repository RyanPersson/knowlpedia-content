+++
id = "lie-groups/example-so3"
title = "Example: SO(3) and rotations"
kind = "knowl"
summary = "The Lie algebra of SO(3) consists of real skew-symmetric matrices, whose exponentials are rotations."
aliases = ["example-so3", "Example: SO(3) and rotations"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/example-so3.md"
+++

The [[lie-groups/special-orthogonal-group|\(SO(3)\)]] rotation group has Lie algebra [[lie-groups/orthogonal-lie-algebra|\(\mathfrak{so}(3)\)]], the real skew-symmetric \(3\times3\) matrices with bracket \([A,B]=AB-BA\).

## A concrete basis and bracket computation
Set
\[
A_1=\begin{pmatrix}0&0&0\\0&0&-1\\0&1&0\end{pmatrix},\quad
A_2=\begin{pmatrix}0&0&1\\0&0&0\\-1&0&0\end{pmatrix},\quad
A_3=\begin{pmatrix}0&-1&0\\1&0&0\\0&0&0\end{pmatrix}.
\]
Direct multiplication gives the familiar relations
\[
[A_1,A_2]=A_3,\qquad [A_2,A_3]=A_1,\qquad [A_3,A_1]=A_2.
\]
Thus \(\mathfrak{so}(3)\) is three-dimensional and simple as a real Lie algebra.

Identifying \((a_1,a_2,a_3)\in\mathbb R^3\) with \(a_1A_1+a_2A_2+a_3A_3\) turns the Lie bracket into the cross product on \(\mathbb R^3\).

## Exponential = rotations (explicit)
For \(\theta\in\mathbb R\), the matrix \(\theta A_3\) generates infinitesimal rotation in the \((x,y)\)-plane, and the [[lie-groups/exponential-map-lie-group|exponential map]] gives
\[
\exp(\theta A_3)=
\begin{pmatrix}
\cos\theta & -\sin\theta & 0\\
\sin\theta & \cos\theta & 0\\
0&0&1
\end{pmatrix},
\]
the rotation about the \(z\)-axis by angle \(\theta\). Similar formulas hold for \(\exp(\theta A_1)\) and \(\exp(\theta A_2)\).

## Topology note
\(SO(3)\) is connected but not simply connected. Its universal cover is [[lie-groups/example-su2|\(SU(2)\)]], with a two-to-one covering homomorphism; equivalently, \(\operatorname{Spin}(3)\cong SU(2)\).
