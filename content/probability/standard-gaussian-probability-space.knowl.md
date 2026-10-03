+++
id = "probability/standard-gaussian-probability-space"
title = "Standard Gaussian probability space"
kind = "definition"
summary = "Euclidean space with the centered Gaussian probability of identity covariance."
aliases = ["standard Gaussian measure on Euclidean space"]
domains = ["probability"]
section_mode = "progressive"
prerequisites = ["probability/normal-distribution", "measure-theory/product-measure", "measure-theory/measure-completion"]
+++

The **standard Gaussian probability space** in dimension \(d\geq1\) is \((\mathbb R^d,\Sigma,\gamma_d)\), where \(\Sigma\) is the completed Borel sigma-algebra and
\[
\gamma_d(E)=(2\pi)^{-d/2}\int_E e^{-\|x\|^2/2}\,dx.
\]
It is the product of \(d\) [[probability/normal-distribution|standard normal laws]]. Its mean is zero and its covariance matrix is \(I_d\).

## Observable spaces

Although \(\mathbb R^d\) has finite dimension, \(L^2(\gamma_d)\) and \(L^\infty(\gamma_d)\) are infinite dimensional. The probability space is atomless and standard. Integration defines a state on the bounded function algebra.

## A useful nonlinear observable

For \(r(x)=\|x\|^2-d\), independence and the standard normal moments give \(\int r\,d\gamma_d=0\) and \(\|r\|_2^2=2d\). This nonzero centered observable is fixed by every orthogonal transformation.
