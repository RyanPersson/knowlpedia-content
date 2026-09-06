+++
id = "algebra-hyperstructures/valuation-as-tropical-hyperfield-morphism"
title = "Valuations as tropical hyperfield morphisms"
kind = "proposition"
summary = "Negating an additive non-Archimedean valuation gives a weak morphism to a max tropical hyperfield."
aliases = ["tropicalization as a hyperfield morphism", "non-Archimedean norm as hyperfield morphism"]
domains = ["algebra-hyperstructures", "algebra-fields-galois", "algebra-rings"]
prerequisites = ["algebra-fields-galois/valuation-on-a-field", "algebra-groups/ordered-abelian-group", "algebra-hyperstructures/hyperring-homomorphism"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(v:K\to\Gamma\cup\{\infty\}\) be a
[[algebra-fields-galois/valuation-on-a-field|valuation on a field]], where
\(\Gamma\) is a
[[algebra-groups/ordered-abelian-group|totally ordered abelian group]], written
additively. Give
\(\mathbb T_\Gamma=\Gamma\cup\{-\infty\}\) tropical multiplication
\(a\odot b=a+b\) and max-convention hyperaddition
\[
a\boxplus b=
\begin{cases}
\{\max(a,b)\},&a\ne b,\\
\{c:c\le a\},&a=b.
\end{cases}
\]
Then
\[
\operatorname{trop}_v:K\longrightarrow\mathbb T_\Gamma,\qquad
\operatorname{trop}_v(0)=-\infty,\quad
\operatorname{trop}_v(x)=-v(x)\ \ (x\ne0),
\]
is a weak [[algebra-hyperstructures/hyperring-homomorphism|hyperfield
homomorphism]].

## Verification

Multiplicativity follows from
\(-v(xy)=-v(x)-v(y)\). If \(v(x)\ne v(y)\), then
\[
v(x+y)=\min\{v(x),v(y)\},
\]
so \(\operatorname{trop}_v(x+y)\) is the unique maximum of the two target
values. If the valuations tie, cancellation can only increase \(v(x+y)\),
so its negative lies anywhere at or below their common value. In both cases,
\[
\operatorname{trop}_v(x+y)\in
\operatorname{trop}_v(x)\boxplus\operatorname{trop}_v(y).
\]

## Converse and sign convention

Conversely, a weak hyperfield homomorphism \(w:K\to\mathbb T_\Gamma\) defines
an additive valuation by \(v(x)=-w(x)\) for \(x\ne0\) and \(v(0)=\infty\).
Thus the hyperfield-morphism axiom packages the ultrametric inequality.

The minus sign is forced by the house **max** convention. With a min
[[algebra-hyperstructures/tropical-hyperfield|tropical hyperfield]], one may instead send \(x\) directly to \(v(x)\). A
multiplicative [[algebra-fields-galois/non-archimedean-absolute-value|non-Archimedean absolute value]] maps directly to the
nonnegative multiplicative presentation of the max tropical hyperfield.

## Weak, not usually strong

For fixed \(x,y\), the source field has the singleton sum \(\{x+y\}\).
When their tropical values tie, the target hyper-sum is an entire lower
interval, so its image is usually a proper subset. The map is therefore weak
and generally not strong.

## References

1. Oleg Viro, “Hyperfields for Tropical Geometry I: Hyperfields and dequantization,” 2010. [arXiv:1006.3034](https://arxiv.org/abs/1006.3034). Relevant: tropical hyperfields and non-Archimedean norms.
2. Matthew Baker and Nathan Bowler, “Matroids over hyperfields,” 2017. [arXiv:1601.01204](https://arxiv.org/abs/1601.01204). Relevant: hyperfield homomorphisms and the tropical hyperfield.
