+++
id = "probability/probability-density-function"
title = "Probability density function"
kind = "definition"
summary = "A nonnegative measurable function whose integrals give probabilities relative to Lebesgue measure."
aliases = ["probability density function", "PDF"]
domains = ["probability"]
section_mode = "progressive"
prerequisites = ["probability/probability-measure", "measure-theory/lebesgue-integral", "measure-theory/lebesgue-measure", "measure-theory/measurable-function"]
dependency_heuristic = "probability-foundations-review-v1"
dependency_review_count = 1
+++

A **probability density function** of a [[probability/probability-measure|probability measure]] \(P\) on \(\mathbb R^d\) is a nonnegative measurable function \(f\) such that, for every Borel set \(A\),
\[
P(A)=\int_A f(x)\,dx,
\]
where the [[measure-theory/lebesgue-integral|integral]] is with respect to [[measure-theory/lebesgue-measure|Lebesgue measure]].

## Properties

Necessarily \(\int_{\mathbb R^d}f(x)\,dx=1\). Densities are unique only up to changes on sets of Lebesgue measure zero. The density of a random variable means a density of its [[probability/distribution-law|law]].

A density can exceed one; probabilities are integrals over sets. Not every probability measure has a density with respect to Lebesgue measure.

## General reference measures

Relative to another measure \(\nu\), a density is a [[measure-theory/radon-nikodym-derivative|Radon–Nikodym derivative]] \(dP/d\nu\). A [[probability/probability-mass-function|probability mass function]] is a density relative to counting measure on a countable state space.

## Examples

The [[probability/normal-distribution|normal distribution]] has a Gaussian density; the [[probability/uniform-distribution|uniform distribution on an interval]] has constant density on that interval.
