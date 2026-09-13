+++
id = "shared-foundations/nearest-integer"
title = "Nearest integer"
kind = "definition"
summary = "An integer minimizing distance to a given real number, with a stated tie convention."
aliases = ["rounding", "nearest nonzero integer"]
domains = ["shared-foundations"]
section_mode = "progressive"
prerequisites = ["shared-foundations/floor-function", "shared-foundations/integers", "shared-foundations/real-numbers", "real-analysis/absolute-value"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

A **nearest integer** to \(x\in\mathbb R\) is an integer \(n\) minimizing the [[real-analysis/absolute-value|absolute value]] \(|x-n|\). It always satisfies \(|x-n|\le1/2\). The minimizer is unique unless \(x\) is halfway between two consecutive integers.

## A convention

One deterministic rule is \(n(x)=\lfloor x+1/2\rfloor\), which resolves a tie toward the larger integer. Other rules, such as rounding ties to an even integer, must be specified if used. A nearest **nonzero** integer minimizes over \(\mathbb Z\setminus\{0\}\) and can differ from ordinary rounding near zero; a tie between \(-1\) and \(1\) occurs at zero.

## Example

The nearest integer to \(2.3\) is \(2\), while both \(2\) and \(3\) minimize distance to \(2.5\). Rounding is a discrete selection operation, so differentiability cannot be assumed at the selection boundaries.
