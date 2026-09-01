+++
id = "algebra-hyperstructures/tropical-hyperfield-versus-semifield"
title = "Tropical semifield and hyperfield tied-sum distinction"
kind = "proposition"
summary = "The tropical semifield and hyperfield share their carrier and multiplication but differ exactly at tied addition."
aliases = ["tropical hyperfield and tropical semiring comparison"]
domains = ["algebra-hyperstructures", "algebra-rings"]
prerequisites = ["algebra-rings/tropical-semifield", "algebra-hyperstructures/tropical-hyperfield"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

On the common carrier \(\mathbb R\cup\{-\infty\}\), the
[[algebra-rings/tropical-semifield|tropical semifield]]
\(\mathbb T_{\mathrm{semi}}\) and the
[[algebra-hyperstructures/tropical-hyperfield|tropical hyperfield]]
\(\mathbb T_{\mathrm{hyp}}\) have the same multiplicative operation
\(x\odot y=x+y\), the same multiplicative identity \(0\), and the same
absorbing/additive-zero element \(-\infty\). Their additions agree on unequal
inputs and differ precisely at a tie:
\[
x\oplus y=\max(x,y),
\qquad
x\boxplus y=
\begin{cases}
\{\max(x,y)\},&x\ne y,\\
\{z:z\le x\},&x=y.
\end{cases}
\]

## Idempotence versus cancellation

In the semifield, \(x\oplus x=x\); addition is single-valued and idempotent.
In the hyperfield,
\[
x\boxplus x=\{z:z\le x\}
\]
contains \(-\infty\), so \(x\) is its own hyper-additive inverse. The lower
values represent possible cancellation when two terms have equal leading
valuation.

## Order warning

The semifield's natural order is defined algebraically by
\(x\le y\iff x\oplus y=y\), and in the max presentation it is the usual
order. The hyperfield uses that same external order to describe its tied
hyper-sum, but hyperaddition itself is not a join operation and does not make
the hyperfield an [[algebra-rings/idempotent-semiring|idempotent semiring]].

In the min-plus presentation all displayed numerical inequalities reverse.
One must switch both the distinguished infinity and the order convention,
not merely replace the word “max” by “min.”

## Pointwise inclusion is not structural identity

After replacing a semifield sum by its singleton, one does have the pointwise
inclusion
\[
\{x\oplus y\}\subseteq x\boxplus y.
\]
At a tie this inclusion is proper. It does not make one tropical object a
subobject of the other: one addition has values in the carrier and the other
in its nonempty power set, so the structures live in different categories.
Constructions that need linear optimization often use the semifield, while
valuation cancellation and matroids over hyperfields use the hyperfield.

## References

1. Oleg Viro, “Hyperfields for Tropical Geometry I: Hyperfields and dequantization,” 2010. [arXiv:1006.3034](https://arxiv.org/abs/1006.3034). Relevant: tropical semiring and hyperfield presentations.
2. Jaiung Jun, “Algebraic Geometry Over Hyperrings,” *Advances in Mathematics* 323 (2018), 142–192. [arXiv:1512.04837](https://arxiv.org/abs/1512.04837). Relevant: the hyperfield canonically associated with a totally ordered idempotent semifield.
