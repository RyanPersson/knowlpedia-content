+++
id = "algebra-rings/idempotent-semiring"
title = "Idempotent semiring"
kind = "definition"
summary = "A semiring whose addition satisfies a+a=a."
aliases = ["additively idempotent semiring", "dioid"]
domains = ["algebra-rings", "algebra-hyperstructures"]
prerequisites = ["algebra-rings/semiring"]
dependency_review_count = 1
section_mode = "progressive"
+++

An **idempotent semiring** is a [[algebra-rings/semiring|semiring]] \(S\)
whose addition is idempotent:
\[
a+a=a\qquad\text{for every }a\in S.
\]
In the tropical-algebra pages, idempotent semirings are normally assumed
commutative unless noncommutative multiplication is explicitly mentioned.

## Order-theoretic meaning

Idempotent addition is a join operation for the
[[algebra-rings/natural-order-of-idempotent-semiring|natural order]]
\(a\le b\iff a+b=b\). Thus finite sums behave like finite suprema rather
than like repeated counting. Multiplication distributes over these joins and
is monotone in each variable.

## Examples

The [[shared-foundations/power-set|power set]] of a set, with union as addition and intersection as
multiplication, is an idempotent [[algebra-rings/commutative-semiring|commutative semiring]]. The Boolean and
tropical semifields are further examples. An ordinary nonzero ring cannot
be additively idempotent: \(a+a=a\) and additive cancellation would force
\(a=0\).

## Terminology

The word **dioid** is not uniform: some authors use it for every idempotent
semiring, while others add order-completeness assumptions. The explicit
phrase “idempotent semiring” is used here.

## References

1. Grigori L. Litvinov, Viktor P. Maslov, and Grigori B. Shpiz, “Linear functionals on idempotent spaces: an algebraic approach,” 2000. [arXiv:math/0012268](https://arxiv.org/abs/math/0012268). Relevant: the algebraic idempotent-semiring viewpoint.
2. Grigori L. Litvinov, Viktor P. Maslov, and Grigori B. Shpiz, “Idempotent (Asymptotic) Mathematics and the Representation Theory,” 2002. [arXiv:math/0206025](https://arxiv.org/abs/math/0206025).
