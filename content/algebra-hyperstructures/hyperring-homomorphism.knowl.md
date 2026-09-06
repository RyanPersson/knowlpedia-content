+++
id = "algebra-hyperstructures/hyperring-homomorphism"
title = "Hyperring homomorphism"
kind = "definition"
summary = "A unit-preserving multiplicative map that weakly or strongly preserves hyperaddition."
aliases = ["weak hyperring homomorphism", "strong hyperring homomorphism", "strict hyperring homomorphism"]
domains = ["algebra-hyperstructures", "algebra-rings"]
prerequisites = ["algebra-hyperstructures/hyperring"]
dependency_review_count = 1
section_mode = "progressive"
+++

For [[algebra-hyperstructures/hyperring|hyperrings]] \(R\) and \(S\), a
**hyperring homomorphism** in the house **weak** convention is a function
\(f:R\to S\) such that
\[
f(0)=0,\qquad f(1)=1,\qquad f(ab)=f(a)f(b),
\]
and
\[
f(a\boxplus_R b)\subseteq f(a)\boxplus_S f(b),
\qquad
f(A)=\{f(x):x\in A\}.
\]
A **strong** or **strict hyperring homomorphism** requires equality in the
last display for every \(a,b\).

## Why the weak convention matters

For an ordinary ring regarded as a singleton-valued hyperring, the weak
condition says
\[
f(a+b)\in f(a)\boxplus f(b).
\]
This permits [[algebra-fields-galois/valuation-on-a-field|valuations]] and
[[algebra-hyperstructures/quotient-hyperring|quotient maps]] into genuinely
multivalued hyperfields. Strong preservation would require the target
hyper-sum to be the singleton image of \(a+b\), excluding these central
examples.

## Relations between the notions

Every strong homomorphism is weak, but not conversely. When both source and
target have singleton-valued addition, weak and strong preservation coincide
with the usual additive equality. An isomorphism of hyperrings is a bijection
whose map and inverse are weak homomorphisms; it is then strong.

## Convention warning

The adjectives **weak** and **strong** in matroid theory over hyperfields
refer to different axiom systems and are not the morphism distinction above.
Sources also vary on whether the unqualified word “homomorphism” means weak
or strict, so the convention must be checked.

## References

1. Jaiung Jun, “Algebraic Geometry Over Hyperrings,” *Advances in Mathematics* 323 (2018), 142–192. [arXiv:1512.04837](https://arxiv.org/abs/1512.04837). Relevant: definitions of hyperring homomorphisms and strict homomorphisms.
2. Matthew Baker and Nathan Bowler, “Matroids over hyperfields,” 2017. [arXiv:1601.01204](https://arxiv.org/abs/1601.01204). Relevant: hyperfield homomorphisms.
