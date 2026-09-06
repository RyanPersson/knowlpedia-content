+++
id = "algebra-rings/ring-homomorphism"
title = "Ring homomorphism"
kind = "knowl"
summary = "A function between rings preserving addition and multiplication."
aliases = ["ring-homomorphism", "Ring homomorphism"]
domains = ["algebra-rings"]
legacy_source_path = "algebra-rings/ring-homomorphism.md"
prerequisites = ["shared-foundations/function", "algebra-rings/ring"]
dependency_heuristic = "semantic-curriculum-review-v1"
dependency_review_count = 1
+++

A **ring homomorphism** is a [[shared-foundations/function|function]] \(\varphi:R\to S\) between [[algebra-rings/ring|rings]] such that for all \(a,b\in R\),
\[
\varphi(a+b)=\varphi(a)+\varphi(b),\qquad \varphi(ab)=\varphi(a)\varphi(b).
\]
## Unital homomorphisms

If \(R,S\) are unital, some authors additionally require \(\varphi(1_R)=1_S\); this is then called a *unital* homomorphism. The definition above does not impose that condition, so it also applies to the nonunital rings allowed here.

## Remarks

Homomorphisms organize rings into a category; they compose via [[shared-foundations/composition|composition]]. Two fundamental invariants are the [[algebra-rings/kernel-ring|kernel]] and image, which control quotients and embeddings.

## Examples

- The inclusion \(2\mathbb Z\hookrightarrow \mathbb Z\) is a ring homomorphism under the nonunital convention: neither the domain nor the map is required to preserve a multiplicative identity.

- The reduction map \(\mathbb Z\to \mathbb Z/n\mathbb Z\), \(a\mapsto \overline a\), is a ring homomorphism.
- The inclusion \(\mathbb Z\hookrightarrow \mathbb Q\) is a ring homomorphism.
- Evaluation at \(c\in k\) gives a homomorphism \(k[x]\to k\), \(f\mapsto f(c)\).
