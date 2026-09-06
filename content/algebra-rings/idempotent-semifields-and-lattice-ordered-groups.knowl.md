+++
id = "algebra-rings/idempotent-semifields-and-lattice-ordered-groups"
title = "Idempotent semifields and lattice-ordered groups"
kind = "theorem"
summary = "Idempotent semifields are equivalent to lattice-ordered abelian groups after adjoining or removing the additive bottom element."
aliases = ["idempotent semifield l-group equivalence", "characteristic-one semifields and l-groups"]
domains = ["algebra-rings", "algebra-groups", "algebra-hyperstructures"]
prerequisites = ["algebra-rings/idempotent-semifield", "algebra-rings/semiring-homomorphism", "algebra-groups/lattice-ordered-abelian-group"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

The category of commutative [[algebra-rings/idempotent-semifield|idempotent
semifields]] with unit-preserving [[algebra-rings/semiring-homomorphism|semiring homomorphisms]] is equivalent to the
category of [[algebra-groups/lattice-ordered-abelian-group|lattice-ordered
abelian groups]] with \(\ell\)-group homomorphisms.

The functor from semifields sends \(S\) to its multiplicative group
\(S^\times=S\setminus\{0_S\}\), equipped with the natural order of the
idempotent addition. The inverse construction adjoins a new bottom element
\(\bot\) to an \(\ell\)-group \(\Gamma\), uses the group law as multiplication,
and defines
\[
x\oplus y=x\vee y,\qquad 0_S=\bot.
\]

## Why the nonzero elements form a lattice

If \(a,b\in S^\times\), their join in the natural order is \(a+b\), which is
again nonzero because it lies above \(a\). Since multiplication by any
nonzero element is an order automorphism, meets can be recovered from joins:
in multiplicative notation,
\[
a\wedge b=\bigl(a^{-1}\vee b^{-1}\bigr)^{-1}.
\]
Thus \(S^\times\) is an abelian \(\ell\)-group, not merely an ordered group.

## Constructing the semifield

Let \(\Gamma\) be an abelian \(\ell\)-group, written multiplicatively with
identity \(1\). Extend multiplication to
\(S=\Gamma\sqcup\{\bot\}\) by making \(\bot\) absorbing, and set addition
equal to join after declaring \(\bot\leq\gamma\) for every
\(\gamma\in\Gamma\). Translation-invariance of the lattice order gives
distributivity:
\[
a(b\vee c)=ab\vee ac.
\]
Every element of \(\Gamma\) remains multiplicatively invertible, so \(S\) is
an idempotent semifield.

## Morphisms and examples

A semiring homomorphism restricts to a [[algebra-groups/group-homomorphism|group homomorphism]] preserving joins;
an \(\ell\)-group homomorphism extends uniquely by sending \(\bot\) to
\(\bot\). These assignments are mutually inverse on morphisms as well as on
objects.

The trivial \(\ell\)-group corresponds to the [[algebra-rings/boolean-semifield|Boolean semifield]].
The totally ordered additive group \(\mathbb R\) corresponds to the max-plus
tropical semifield. Partially ordered \(\ell\)-groups give idempotent
semifields whose natural orders are not total.

## Convention warning

Here “characteristic one” means additively idempotent. The adjoined
\(\bot=0_S\) is the semiring's additive identity and is not the identity
element of the group. Omitting it produces a
[[algebra-rings/parasemifield|parasemifield]], not the unital semiring used
elsewhere in this corpus.

## References

1. Guillaume Tahar, “Ordered algebraic structures and classification of semifields,” 2017. [arXiv:1709.06923](https://arxiv.org/abs/1709.06923). Relevant: the equivalence between characteristic-one semifields and lattice-ordered groups.
2. Grigori L. Litvinov, Viktor P. Maslov, and Grigori B. Shpiz, “Idempotent (Asymptotic) Mathematics and the Representation Theory,” 2002. [arXiv:math/0206025](https://arxiv.org/abs/math/0206025). Relevant: canonical order and idempotent semifields.
