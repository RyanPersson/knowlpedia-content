+++
id = "algebra-hyperstructures/sign-hyperfield"
title = "Sign hyperfield"
kind = "example"
summary = "The three-element hyperfield recording only whether a real number is negative, zero, or positive."
aliases = ["hyperfield of signs"]
domains = ["algebra-hyperstructures", "algebra-rings"]
prerequisites = []
dependency_review_count = 1
section_mode = "progressive"
+++

The **sign hyperfield** is
\(\mathbb S=\{0,1,-1\}\) with the usual multiplication of signs and
hyperaddition determined by
\[
1\boxplus1=\{1\},\qquad
(-1)\boxplus(-1)=\{-1\},\qquad
1\boxplus(-1)=\{-1,0,1\}.
\]
Also \(0\boxplus x=\{x\}\). It is a hyperfield whose elements retain only
sign information.

## Quotient realization

The sign map realizes
\[
\mathbb S\cong\mathbb R/\mathbb R_{>0}.
\]
Positive rescaling partitions \(\mathbb R\) into the negative, zero, and
positive orbits. Two numbers of the same nonzero sign have a sum of that
sign, whereas a positive and a negative number can sum to a number of any
sign. This exactly produces the displayed hyperaddition.

## Morphism from the real field

The map
\[
\operatorname{sgn}:\mathbb R\longrightarrow\mathbb S
\]
is a weak hyperfield homomorphism: it preserves zero, one, and multiplication,
and
\(\operatorname{sgn}(x+y)\in
\operatorname{sgn}(x)\boxplus\operatorname{sgn}(y)\).
It is not strong, since a fixed pair \(x,y\) has one sign for its sum while
the target hyper-sum can contain three signs.

## References

1. Oleg Viro, “Hyperfields for Tropical Geometry I: Hyperfields and dequantization,” 2010. [arXiv:1006.3034](https://arxiv.org/abs/1006.3034). Relevant: the hyperfield of signs and factor hyperfields.
2. Matthew Baker and Nathan Bowler, “Matroids over hyperfields,” 2017. [arXiv:1601.01204](https://arxiv.org/abs/1601.01204). Relevant: Example 2.6 and oriented matroids over the sign hyperfield.
