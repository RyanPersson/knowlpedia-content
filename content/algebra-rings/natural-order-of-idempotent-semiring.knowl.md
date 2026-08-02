+++
id = "algebra-rings/natural-order-of-idempotent-semiring"
title = "Natural order of an idempotent semiring"
kind = "proposition"
summary = "Idempotent addition defines a partial order in which addition is binary join."
aliases = ["canonical order of an idempotent semiring", "idempotent semiring order"]
domains = ["algebra-rings", "algebra-hyperstructures"]
section_mode = "progressive"
+++

Let \(S\) be an [[algebra-rings/idempotent-semiring|idempotent semiring]].
Its **natural order** is
\[
a\le_S b\quad\Longleftrightarrow\quad a+b=b.
\]
This relation is a [[shared-foundations/partial-order|partial order]], \(a+b\) is the join \(a\vee b\), and both
addition and multiplication are monotone in each variable.

## Why it is an order

Idempotence gives reflexivity, commutativity gives antisymmetry, and
associativity gives transitivity. Distributivity proves monotonicity of
multiplication: if \(a+b=b\), then
\(ca+cb=c(a+b)=cb\), so \(ca\le_S cb\), and similarly on the right.
The additive identity \(0\) is the least element.

## Tropical order warning

For the [[algebra-rings/tropical-semifield|max-plus tropical semifield]], \(\le_S\) is the usual order:
\(\max(a,b)=b\) exactly when \(a\le b\). For the min-plus presentation,
\[
a\le_S b\quad\Longleftrightarrow\quad \min(a,b)=b,
\]
so the natural order is the reverse of the usual numerical order. Switching
between max-plus and min-plus therefore reverses the order even though the
two presentations are isomorphic after negating finite elements.

## References

1. Grigori L. Litvinov, Viktor P. Maslov, and Grigori B. Shpiz, “Idempotent (Asymptotic) Mathematics and the Representation Theory,” 2002. [arXiv:math/0206025](https://arxiv.org/abs/math/0206025). Relevant: canonical order and idempotent addition.
