+++
id = "probability/normal-distribution"
title = "Normal distribution"
kind = "definition"
summary = "The probability distribution on the real line with a Gaussian density determined by a mean and positive variance."
aliases = ["normal-distribution", "Normal distribution", "Gaussian distribution", "Gaussian law"]
domains = ["probability"]
prerequisites = ["probability/probability-measure", "measure-theory/lebesgue-measure", "measure-theory/radon-nikodym-derivative", "probability/probability-density-function"]
dependency_heuristic = "component-dependency-review-v1"
dependency_review_count = 2
+++

For \(\mu\in\mathbb R\) and \(\sigma>0\), the **normal distribution** \(\mathcal N(\mu,\sigma^2)\) is the [[probability/probability-measure|probability distribution]] on \(\mathbb R\) with [[probability/probability-density-function|density]]
\[
f_{\mu,\sigma}(x)=\frac{1}{\sigma\sqrt{2\pi}}
\exp\!\left(-\frac{(x-\mu)^2}{2\sigma^2}\right)
\]
with respect to [[measure-theory/lebesgue-measure|Lebesgue measure]].

## Parameters and examples

The parameter \(\mu\) is the mean and \(\sigma^2\) is the variance. The standard normal distribution is \(\mathcal N(0,1)\). Affine transformations satisfy \(aX+b\sim\mathcal N(a\mu+b,a^2\sigma^2)\) when \(X\sim\mathcal N(\mu,\sigma^2)\) and \(a\ne0\).

## References

1. Geoffrey Grimmett and David Stirzaker, *Probability and Random Processes*, 3rd ed., Oxford University Press, 2001, §7.2.
