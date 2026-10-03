+++
id = "measure-theory/probability-kernel"
title = "Probability kernel"
kind = "definition"
summary = "A measurable family of probability measures indexed by another measurable space."
aliases = ["measurable family of probability measures"]
domains = ["measure-theory"]
section_mode = "progressive"
prerequisites = ["probability/probability-measure", "measure-theory/measurable-function"]
+++

A **probability kernel** from \((Y,\mathcal T)\) to \((X,\Sigma)\) assigns a [[probability/probability-measure|probability measure]] \(\mu_y\) on \(X\) to each \(y\in Y\), such that \(y\mapsto\mu_y(E)\) is measurable for every \(E\in\Sigma\).

## Integrating a kernel

Given probability \(\nu\) on \(Y\), the formula \(\mu(E)=\int_Y\mu_y(E)\,d\nu(y)\) defines a probability measure on \(X\). A [[measure-theory/disintegration-theorem|disintegration]] uses such a kernel to describe conditional probabilities on fibers of a measurable map.
