+++
id = "algebra-hyperstructures/fields-semifields-and-hyperfields"
title = "Field embeddings into semifields and hyperfields"
kind = "theorem"
summary = "Fields embed fully faithfully as semifields and as singleton-addition hyperfields."
aliases = ["fields semifields and hyperfields", "field as a semifield and hyperfield"]
domains = ["algebra-hyperstructures", "algebra-rings"]
prerequisites = ["algebra-rings/field", "algebra-rings/semifield", "algebra-hyperstructures/hyperfield", "algebra-groups/abelian-group"]
dependency_review_count = 1
section_mode = "progressive"
+++

There are fully faithful embeddings
\[
\mathbf{Field}\hookrightarrow\mathbf{SemiField},
\qquad
\mathbf{Field}\hookrightarrow\mathbf{HyperField}.
\]
The first sends a [[algebra-rings/field|field]] to its underlying
[[algebra-rings/semifield|semifield]]. The second regards each ordinary sum
\(a+b\) as the singleton hyper-sum \(\{a+b\}\), producing a
[[algebra-hyperstructures/hyperfield|hyperfield]].

The essential image of the first embedding consists of the semifields whose
additive commutative monoid is an [[algebra-groups/abelian-group|abelian group]]. The essential image of the
second consists of the hyperfields whose every hyper-sum is a singleton.

## Full faithfulness

A unit-preserving [[algebra-rings/semiring-homomorphism|semiring homomorphism]] between fields preserves additive
inverses, because
\[
f(a)+f(-a)=f(0)=0.
\]
It is therefore a field homomorphism. A weak hyperfield homomorphism between
singleton-addition hyperfields satisfies
\[
\{f(a+b)\}\subseteq\{f(a)+f(b)\},
\]
so it preserves addition by equality and is likewise a field homomorphism.

## Scope

This theorem identifies two copies of the category of fields; it does not
identify all semifields with all hyperfields. Semifield addition is a
single-valued operation without required additive inverses, whereas
hyperfield addition is nonempty-set-valued and satisfies the inverse and
reversibility axioms of a [[algebra-hyperstructures/canonical-hypergroup|canonical hypergroup]].

## References

1. Matthew Baker and Nathan Bowler, “Matroids over hyperfields,” 2017. [arXiv:1601.01204](https://arxiv.org/abs/1601.01204). Relevant: §2.
2. Jaiung Jun, “Algebraic Geometry Over Hyperrings,” *Advances in Mathematics* 323 (2018), 142–192. [arXiv:1512.04837](https://arxiv.org/abs/1512.04837). Relevant: §2.
