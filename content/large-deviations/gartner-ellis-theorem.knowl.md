+++
id = "large-deviations/gartner-ellis-theorem"
title = "Gärtner–Ellis theorem"
kind = "knowl"
summary = "A large deviation principle obtained from limits of scaled log moment generating functions."
aliases = ["gartner-ellis-theorem", "Gärtner–Ellis theorem"]
domains = ["large-deviations"]
legacy_source_path = "large-deviations/gartner-ellis-theorem.md"
prerequisites = ["probability/random-variable", "large-deviations/log-moment-generating-function", "large-deviations/large-deviation-principle", "large-deviations/rate-function", "large-deviations/good-rate-function", "convex-analysis/legendre-fenchel-transform"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

**Gärtner–Ellis theorem.** Let \((Z_n)\) be \(\mathbb{R}^d\)-valued [[probability/random-variable|random variables]] and let \(a_n\to\infty\). Define the scaled [[large-deviations/log-moment-generating-function|log moment generating function]]
\[
\Lambda_n(\theta)=\frac{1}{a_n}\log \mathbb{E}\bigl[\exp\bigl(a_n\langle \theta, Z_n\rangle\bigr)\bigr],\qquad \theta\in\mathbb{R}^d,
\]
and assume the pointwise limit \(\Lambda(\theta)=\lim_{n\to\infty}\Lambda_n(\theta)\) exists in \((-\infty,\infty]\) for every \(\theta\). Suppose \(0\) lies in the interior of the effective domain of \(\Lambda\), and that \(\Lambda\) is lower semicontinuous and essentially smooth: it is differentiable throughout that interior and is steep at its boundary. Then \((Z_n)\) satisfies a [[large-deviations/large-deviation-principle|large deviation principle]] on \(\mathbb{R}^d\) with speed \(a_n\) and good [[large-deviations/rate-function|rate function]]
\[
I(x)=\sup_{\theta\in\mathbb{R}^d}\bigl\{\langle \theta,x\rangle-\Lambda(\theta)\bigr\}.
\]

The function \(I\) is the [[convex-analysis/legendre-fenchel-transform|Legendre–Fenchel transform]] of \(\Lambda\). For empirical means of i.i.d. real variables, this recovers [[large-deviations/cramers-theorem|Cramér's theorem]] under standard regularity assumptions.
