+++
id = "algebra-rings/tropical-semifield"
title = "Tropical semifield"
kind = "example"
summary = "The max-plus idempotent semifield on the extended real line."
aliases = ["max-plus semifield", "max-plus tropical semifield", "tropical semiring"]
domains = ["algebra-rings", "algebra-hyperstructures"]
section_mode = "progressive"
+++

The **tropical semifield** in the house max-plus convention is
\[
\mathbb T_{\max}=\mathbb R\cup\{-\infty\},\qquad
x\oplus y=\max\{x,y\},\qquad
x\odot y=x+y.
\]
Its additive zero is \(-\infty\), its multiplicative one is the real number
\(0\), and the multiplicative inverse of a finite \(x\) is \(-x\). Hence it
is an [[algebra-rings/idempotent-semifield|idempotent semifield]].

## Natural order

The [[algebra-rings/natural-order-of-idempotent-semiring|natural order]]
induced by \(\oplus\) agrees with the usual order on the extended real line:
\[
x\le_{\mathbb T}y\quad\Longleftrightarrow\quad x\oplus y=y.
\]
Thus tropical addition is supremum and tropical multiplication is translation
by ordinary addition.

## Min-plus convention

The min-plus presentation uses
\(\mathbb R\cup\{+\infty\}\), minimum as addition, and ordinary addition as
multiplication. Negation of finite elements, together with
\(-\infty\leftrightarrow+\infty\), is a semiring isomorphism from max-plus to
min-plus. It reverses the usual numerical order: the natural order of the
min-plus semiring is opposite to the displayed ordinary order.

## Not the tropical hyperfield

The [[algebra-hyperstructures/tropical-hyperfield|tropical hyperfield]] uses
the same max-plus carrier and multiplication and agrees with max when two
inputs differ. At a tie, however, its sum is the entire lower interval rather
than a singleton. The two structures must not be identified.

## References

1. Oleg Viro, “Hyperfields for Tropical Geometry I: Hyperfields and dequantization,” 2010. [arXiv:1006.3034](https://arxiv.org/abs/1006.3034). Relevant: tropical algebra and tropical hyperaddition.
2. Grigori L. Litvinov, Viktor P. Maslov, and Grigori B. Shpiz, “Idempotent (Asymptotic) Mathematics and the Representation Theory,” 2002. [arXiv:math/0206025](https://arxiv.org/abs/math/0206025). Relevant: max-plus idempotent mathematics.
