+++
id = "algebra-rings/boolean-semifield"
title = "Boolean semifield"
kind = "example"
summary = "The two-element idempotent semifield with OR as addition and AND as multiplication."
aliases = ["Boolean semiring", "binary Boolean semifield"]
domains = ["algebra-rings", "algebra-hyperstructures"]
section_mode = "progressive"
prerequisites = ["algebra-rings/idempotent-semifield"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

The **Boolean semifield** is
\[
\mathbb B=\{0,1\},\qquad
a+b=\max\{a,b\},\qquad ab=\min\{a,b\}.
\]
Equivalently, addition is logical OR and multiplication is logical AND.
It is an [[algebra-rings/idempotent-semifield|idempotent semifield]] because
\(1+1=1\) and \(1\) is the only nonzero element.

## Order and universal behavior

The natural order is \(0<1\), and addition is join. For every nontrivial
[[algebra-rings/idempotent-semiring|idempotent semiring]] \(S\), the map \(\mathbb B\to S\) sending \(0\) to \(0\)
and \(1\) to \(1\) is the unique unit-preserving [[algebra-rings/semiring-homomorphism|semiring homomorphism]] from
\(\mathbb B\).

## Not the Krasner hyperfield

The Boolean semifield and the
[[algebra-hyperstructures/krasner-hyperfield|Krasner hyperfield]] have the
same carrier, zero, one, and multiplication, but not the same addition:
\[
1+_{\mathbb B}1=1,\qquad
1\boxplus_{\mathbb K}1=\{0,1\}.
\]
The first is a single-valued semiring operation; the second is a hyperaddition
containing the additive inverse relation.

## References

1. Grigori L. Litvinov, Viktor P. Maslov, and Grigori B. Shpiz, “Idempotent (Asymptotic) Mathematics and the Representation Theory,” 2002. [arXiv:math/0206025](https://arxiv.org/abs/math/0206025).
2. Matthew Baker and Nathan Bowler, “Matroids over hyperfields,” 2017. [arXiv:1601.01204](https://arxiv.org/abs/1601.01204). Relevant: examples distinguishing the Krasner hyperfield from ordinary single-valued algebra.
