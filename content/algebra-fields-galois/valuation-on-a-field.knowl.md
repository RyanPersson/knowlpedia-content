+++
id = "algebra-fields-galois/valuation-on-a-field"
title = "Valuation on a field"
kind = "definition"
summary = "A function into an ordered abelian group that converts products to sums and satisfies the ultrametric inequality."
aliases = ["Krull valuation", "additive valuation", "valued field"]
domains = ["algebra-fields-galois", "algebra-rings", "algebra-hyperstructures"]
prerequisites = ["algebra-rings/field", "algebra-groups/ordered-abelian-group"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(K\) be a [[algebra-rings/field|field]] and let \(\Gamma\) be an
[[algebra-groups/ordered-abelian-group|ordered abelian group]], written
additively. A **valuation** on \(K\) with values in \(\Gamma\) is a map
\[
v:K\longrightarrow\Gamma\cup\{\infty\}
\]
such that
\[
v(0)=\infty,\qquad v(1)=0,\qquad
v(xy)=v(x)+v(y),\qquad
v(x+y)\ge\min\{v(x),v(y)\}.
\]
Here \(\infty\) is larger than every element of \(\Gamma\) and
\(\infty+\gamma=\infty\). The pair \((K,v)\) is a **valued field**.

## Dominance and cancellation

If \(v(x)\ne v(y)\), then the ultrametric inequality forces
\[
v(x+y)=\min\{v(x),v(y)\}.
\]
When \(v(x)=v(y)\), equality may fail because leading terms can cancel,
raising the valuation. This unequal-versus-tied dichotomy is exactly what
the [[algebra-hyperstructures/tropical-hyperfield|tropical hyperfield]] records.

## Valuation ring and residue field

The [[algebra-fields-galois/valuation-ring|valuation ring]] and its maximal
ideal are
\[
\mathcal O_v=\{x\in K:v(x)\ge0\},\qquad
\mathfrak m_v=\{x\in K:v(x)>0\}
\]
respectively. The quotient
\(\kappa(v)=\mathcal O_v/\mathfrak m_v\) is the
[[algebra-commutative/residue-field|residue field]]. The subgroup
\(v(K^\times)\) is the
[[algebra-fields-galois/value-group|value group]]; one may replace
\(\Gamma\) by this subgroup when a surjective valuation is desired.

## Additive and multiplicative conventions

The [[shared-foundations/p-adic-valuation|\(p\)-adic valuation]] is additive
as above. A
[[algebra-fields-galois/non-archimedean-absolute-value|non-Archimedean
absolute value]] is the multiplicative-size convention, satisfying
\(|x+y|\le\max(|x|,|y|)\). For real-valued \(v\), a typical conversion is
\(|x|=e^{-v(x)}\). Thus larger additive valuation means smaller absolute
value, and formulas must not mix the two order conventions.

## References

1. Irving Kaplansky, “Maximal fields with valuations,” *Duke Mathematical Journal* 9 (1942), 303–321. [Project Euclid DOI record](https://doi.org/10.1215/S0012-7094-42-00922-0). Relevant: valued fields and value groups.
2. Oleg Viro, “Hyperfields for Tropical Geometry I: Hyperfields and dequantization,” 2010. [arXiv:1006.3034](https://arxiv.org/abs/1006.3034). Relevant: non-Archimedean norms and tropical hyperfields.
