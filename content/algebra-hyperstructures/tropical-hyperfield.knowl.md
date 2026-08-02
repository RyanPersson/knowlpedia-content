+++
id = "algebra-hyperstructures/tropical-hyperfield"
title = "Tropical hyperfield"
kind = "example"
summary = "The max-plus hyperfield whose tied sum is the full lower interval."
aliases = ["tropical real hyperfield", "max tropical hyperfield"]
domains = ["algebra-hyperstructures", "algebra-rings"]
section_mode = "progressive"
+++

The **tropical hyperfield** in the house max convention has carrier
\[
\mathbb T=\mathbb R\cup\{-\infty\}.
\]
Its multiplication is \(x\odot y=x+y\), with multiplicative identity \(0\)
and absorbing element \(-\infty\). Its hyperaddition is
\[
x\boxplus y=
\begin{cases}
\{\max(x,y)\},&x\ne y,\\
\{z\in\mathbb T:z\le x\},&x=y.
\end{cases}
\]
The additive identity is \(-\infty\), and every finite element is its own
additive inverse because \(-\infty\in x\boxplus x\).

## The tied-sum mechanism

When one input is strictly larger, it uniquely dominates the hyper-sum.
When the inputs tie, cancellation can lower the result by any amount, even
to the additive zero. This is the hyperfield form of the non-Archimedean
rule that equal leading valuations may cancel.

## Other presentations

Exponentiating finite elements gives the equivalent carrier
\(\mathbb R_{\ge0}\), with ordinary multiplication and
\[
a\boxplus b=
\begin{cases}
\{\max(a,b)\},&a\ne b,\\
[0,a],&a=b.
\end{cases}
\]
Some sources instead use a min convention. The max convention here is chosen
to align weak morphisms \(K\to\mathbb T\) with non-Archimedean absolute
values, or with the negative of an [[algebra-fields-galois/valuation-on-a-field|additive valuation]].

## References

1. Oleg Viro, “Hyperfields for Tropical Geometry I: Hyperfields and dequantization,” 2010. [arXiv:1006.3034](https://arxiv.org/abs/1006.3034). Relevant: tropical real hyperfields and dequantization.
2. Matthew Baker and Nathan Bowler, “Matroids over hyperfields,” 2017. [arXiv:1601.01204](https://arxiv.org/abs/1601.01204). Relevant: Example 2.5.
