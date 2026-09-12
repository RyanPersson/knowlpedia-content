+++
id = "algebra-rings/quaternion-reduced-norm"
title = "Reduced norm in a quaternion algebra"
kind = "definition"
summary = "The scalar-valued multiplicative quadratic form obtained by multiplying an element by its standard conjugate."
aliases = ["quaternion norm", "reduced norm of a quaternion"]
domains = ["algebra-rings"]
section_mode = "progressive"
prerequisites = ["algebra-rings/quaternion-conjugation"]
+++

The **reduced norm** of \(x\) in a quaternion algebra \(B=(a,b)_F\) is
\[
\operatorname{nrd}(x)=x\bar x\in F,
\]
using [[algebra-rings/quaternion-conjugation|standard conjugation]]. For \(x=x_0+x_1i+x_2j+x_3ij\), it is
\[
\operatorname{nrd}(x)=x_0^2-a x_1^2-b x_2^2+ab x_3^2.
\]

## Multiplication and inversion

Because \(y\bar y\) is central, \((xy)\overline{xy}=x(y\bar y)\bar x\), proving multiplicativity. An element is invertible exactly when its reduced norm is nonzero, with \(x^{-1}=\bar x/\operatorname{nrd}(x)\).

## Split case

For \(B=M_2(F)\), the reduced norm is the determinant. Over a general field it is not a positive metric norm; it can vanish on a nonzero element of a split algebra.
