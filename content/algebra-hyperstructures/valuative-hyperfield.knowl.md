+++
id = "algebra-hyperstructures/valuative-hyperfield"
title = "Valuative hyperfield"
kind = "construction"
summary = "The ordered-group generalization of the tropical hyperfield."
aliases = ["generalized tropical hyperfield", "value-group hyperfield"]
domains = ["algebra-hyperstructures", "algebra-fields-galois", "algebra-rings"]
section_mode = "progressive"
+++

Let \(\Gamma\) be a totally
[[algebra-groups/ordered-abelian-group|ordered abelian group]], written
multiplicatively. Adjoin a new element \(\mathbf0\) below every element of
\(\Gamma\), extend multiplication by making \(\mathbf0\) absorbing, and
define
\[
x\boxplus y=
\begin{cases}
\{\max(x,y)\},&x\ne y,\\
\{z\in\Gamma\sqcup\{\mathbf0\}:z\leq x\},&x=y.
\end{cases}
\]
Together with the group multiplication, this makes
\(\Gamma_{\max}=\Gamma\sqcup\{\mathbf0\}\) a **valuative hyperfield**.

## Hyperfield structure

The hyper-additive identity is \(\mathbf0\), while the multiplicative identity
is the group identity \(1_\Gamma\). Every \(x\in\Gamma\) is its own additive
hyperinverse because \(\mathbf0\in x\boxplus x\). Translation-invariance of
the total order makes multiplication distribute over hyperaddition.

## Relation to tropical hyperfields

Taking \(\Gamma=(\mathbb R,+,\leq)\) in additive notation and writing the
adjoined bottom as \(-\infty\) gives the max-convention
[[algebra-hyperstructures/tropical-hyperfield|tropical hyperfield]]. Taking
the trivial one-element ordered group gives the Krasner hyperfield. Thus
**valuative hyperfield** names the whole ordered-value-group construction,
not only the real-valued example.

## Valuations as morphisms

A multiplicative non-Archimedean norm \(K\to\Gamma_{\max}\) is a weak
hyperfield homomorphism when \(K\) has singleton hyper-sums. In the additive
valuation and max convention, the corresponding statement is the
[[algebra-hyperstructures/valuation-as-tropical-hyperfield-morphism|valuation
as a tropical-hyperfield morphism]] proposition.

This does not assert that \(\Gamma_{\max}\) is an orbit quotient of every
field carrying such a valuation. Quotient hyperfields retain the realized
orbit sums, whereas this construction depends only on the ordered group.

## References

1. Matthew Baker and Nathan Bowler, “Matroids over partial hyperstructures,” *Advances in Mathematics* 343 (2019), 821–863. [arXiv:1709.09707](https://arxiv.org/abs/1709.09707). Relevant: Example 2.12 on valuative hyperfields.
2. Oleg Viro, “Hyperfields for Tropical Geometry I: Hyperfields and dequantization,” 2010. [arXiv:1006.3034](https://arxiv.org/abs/1006.3034). Relevant: tropical hyperfields and non-Archimedean norms.
