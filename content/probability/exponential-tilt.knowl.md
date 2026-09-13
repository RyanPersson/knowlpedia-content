+++
id = "probability/exponential-tilt"
title = "Exponential tilt"
kind = "definition"
summary = "A probability measure reweighted by an exponential and divided by its total mass."
aliases = ["exponentially tilted measure", "exponential reweighting"]
domains = ["probability"]
section_mode = "progressive"
prerequisites = ["probability/probability-measure", "probability/random-variable", "probability/moment-generating-function", "real-analysis/exponential-function", "measure-theory/lebesgue-integral", "measure-theory/radon-nikodym-derivative"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 2
+++

Let \(X\) be a real random variable on \((\Omega,P)\). If \(M(\theta)=\mathbb E_P e^{\theta X}<\infty\), the **exponential tilt** of \(P\) at \(\theta\) is
\[
P_\theta(A)=\frac{\int_A e^{\theta X}\,dP}{M(\theta)}.
\]
The [[probability/moment-generating-function|normalizing factor]] is strictly positive, so this defines a probability measure. Its density relative to \(P\) is \(e^{\theta X}/M(\theta)\).

## Parameter domain

The tilt is defined only where the normalizing integral is finite. If \(X\) is bounded, every real parameter is allowed. The new measure is equivalent to \(P\), since its density is everywhere positive up to the usual almost-everywhere convention. For a periodic observable with normalized angular measure, the same operation is simply a positive reweighting of that angular average.

## References

- [Fithian, Exponential Families (derivatives of the log-partition function)](https://www.stat.berkeley.edu/~wfithian/courses/stat210a/exponential-families.html).
