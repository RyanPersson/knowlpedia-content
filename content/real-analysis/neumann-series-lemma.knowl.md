+++
id = "real-analysis/neumann-series-lemma"
title = "Determinant nonvanishing implies local invertibility lemma"
kind = "knowl"
summary = "Invertibility is stable under small perturbations, with a quantitative bound on the inverse"
aliases = ["neumann-series-lemma", "Determinant nonvanishing implies local invertibility lemma"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/neumann-series-lemma.md"
prerequisites = ["linear-algebra/linear-map"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(A:\mathbb{R}^n\to\mathbb{R}^n\) be an invertible [[linear-algebra/linear-map|linear map]], and equip the space of linear maps with an operator norm.

**Neumann series lemma.** If \(B:\mathbb R^n\to\mathbb R^n\) satisfies
\[
\|A^{-1}(B-A)\|<1,
\]
then \(B\) is invertible and
\[
B^{-1}=\sum_{k=0}^\infty \bigl(-A^{-1}(B-A)\bigr)^k\,A^{-1}.
\]
Moreover,
\[
\|B^{-1}\|\le \frac{\|A^{-1}\|}{1-\|A^{-1}(B-A)\|}.
\]
In particular, if \(\|B-A\|\le 1/(2\|A^{-1}\|)\), then \(B\) is invertible and \(\|B^{-1}\|\le 2\|A^{-1}\|\).

## Remarks

This lemma is a key linear-algebraic ingredient in the [[real-analysis/inverse-function-theorem-rk|inverse function theorem]]: once \(Df(a)\) is invertible, \(Df(x)\) remains invertible for all \(x\) sufficiently close to \(a\) (because \(Df\) is [[real-analysis/continuity-on-a-set|continuous]]).
