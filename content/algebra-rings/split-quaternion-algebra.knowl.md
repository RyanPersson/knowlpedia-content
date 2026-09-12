+++
id = "algebra-rings/split-quaternion-algebra"
title = "Split quaternion algebra"
kind = "definition"
summary = "A quaternion algebra isomorphic to the two-by-two matrix algebra over its base field."
aliases = ["split quaternion algebra over a field"]
domains = ["algebra-rings"]
section_mode = "progressive"
prerequisites = ["algebra-rings/quaternion-algebra", "linear-algebra/matrix"]
+++

A [[algebra-rings/quaternion-algebra|quaternion algebra]] \(B\) over \(F\) is **split** if it is isomorphic as an \(F\)-algebra to \(M_2(F)\). Such an isomorphism is called a splitting.

## Example by matrices

For \((1,b)_F\), take
\[
i=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\qquad
j=\begin{pmatrix}0&b\\1&0\end{pmatrix}.
\]
They satisfy the quaternion relations, and \(1,i,j,ij\) are linearly independent when \(b\ne0\) and the characteristic is not two. This gives an explicit splitting.

## Change of field

Splitting depends on the field: Hamilton's real quaternion algebra is not split over \(\mathbb R\), but becomes split over \(\mathbb C\). Every quaternion algebra over an algebraically closed field of characteristic different from two splits: its presentation parameters have square roots, reducing to the matrix construction above.
