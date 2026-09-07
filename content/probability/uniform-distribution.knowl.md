+++
id = "probability/uniform-distribution"
title = "Uniform distribution"
kind = "definition"
summary = "The probability distribution with constant density on a specified finite interval."
aliases = ["uniform-distribution", "Uniform distribution", "continuous uniform distribution"]
domains = ["probability"]
prerequisites = ["probability/probability-measure", "measure-theory/lebesgue-measure", "shale-paper/radon-nikodym-derivative"]
dependency_heuristic = "missing-links-calibration-v1"
dependency_review_count = 0
+++

For \(a<b\), the **uniform distribution** on the interval \([a,b]\), written \(\operatorname{Unif}[a,b]\), is the [[probability/probability-measure|probability distribution]] with [[shale-paper/radon-nikodym-derivative|density]]
\[
f(x)=\frac{1}{b-a}\mathbf 1_{[a,b]}(x)
\]
with respect to [[measure-theory/lebesgue-measure|Lebesgue measure]].

## Properties

If \(X\sim\operatorname{Unif}[a,b]\), then \(\mathbb E[X]=(a+b)/2\) and \(\operatorname{Var}(X)=(b-a)^2/12\). The phrase “uniform distribution” can also refer to the uniform probability measure on a finite set; that discrete convention is stated when needed.

## References

1. Geoffrey Grimmett and David Stirzaker, *Probability and Random Processes*, 3rd ed., Oxford University Press, 2001, §3.4.
