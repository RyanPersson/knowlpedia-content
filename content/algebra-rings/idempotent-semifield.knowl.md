+++
id = "algebra-rings/idempotent-semifield"
title = "Idempotent semifield"
kind = "definition"
summary = "A semifield with idempotent addition."
aliases = ["tropical semifield in the broad sense"]
domains = ["algebra-rings", "algebra-hyperstructures"]
section_mode = "progressive"
+++

An **idempotent semifield** is a [[algebra-rings/semifield|semifield]]
\(S\) that is also an
[[algebra-rings/idempotent-semiring|idempotent semiring]], so
\[
a+a=a
\]
for every \(a\in S\), and every nonzero element is multiplicatively
invertible.

## Structure

The nonzero elements form an abelian group, while idempotent addition gives
the whole carrier its
[[algebra-rings/natural-order-of-idempotent-semiring|natural partial order]].
Multiplication by a nonzero element is an order automorphism because it has a
multiplicative inverse. This interaction between group and order is the
algebraic basis of tropical linear constructions.

Removing the additive zero produces a lattice-ordered multiplicative group,
and adjoining a bottom element reverses this construction. See the
[[algebra-rings/idempotent-semifields-and-lattice-ordered-groups|categorical
equivalence with lattice-ordered abelian groups]].

## Examples and scope

The [[algebra-rings/boolean-semifield|Boolean semifield]] is the smallest example. The max-plus and min-plus
[[algebra-rings/tropical-semifield|tropical semifields]] are linearly ordered examples. Some authors use
**tropical semifield** for any idempotent semifield; this corpus reserves that
name without qualification for the standard max-plus object.

## References

1. Grigori L. Litvinov, Viktor P. Maslov, and Grigori B. Shpiz, “Linear functionals on idempotent spaces: an algebraic approach,” 2000. [arXiv:math/0012268](https://arxiv.org/abs/math/0012268).
2. Jaiung Jun, “Algebraic Geometry Over Hyperrings,” *Advances in Mathematics* 323 (2018), 142–192. [arXiv:1512.04837](https://arxiv.org/abs/1512.04837). Relevant: totally ordered idempotent semifields and their associated hyperfields.
