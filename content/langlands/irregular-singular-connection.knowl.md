+++
id = "langlands/irregular-singular-connection"
title = "Irregular-singular connection"
kind = "definition"
summary = "A meromorphic flat connection whose singularity is not regular singular and whose local classification requires exponential and Stokes data."
aliases = ["irregular connection", "irregular singularity"]
domains = ["langlands", "algebraic-geometry-foundations"]
section_mode = "progressive"
prerequisites = ["langlands/regular-singular-connection", "fiber-bundles/gauge-transformation"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(X\) be a smooth complex curve, let \(D\subset X\) be a finite set, and
write \(U=X\setminus D\). A meromorphic flat connection on \(X\), with poles
along \(D\), has an **irregular singularity** at \(x\in D\) if it is
not [[langlands/regular-singular-connection|regular singular]] there.

## Formal description

After a finite ramified cover and a formal [[fiber-bundles/gauge-transformation|gauge transformation]], an
irregular connection decomposes into pieces containing nonconstant
exponential factors. These factors, together with formal monodromy, describe
its formal type.

## Analytic classification

Formal type does not determine the analytic connection. Sectorial
fundamental solutions differ by
[[langlands/stokes-data|Stokes data]], which record the missing analytic
information.

## References

1. Philip Boalch, “Geometry and braiding of Stokes data; fission and wild
   character varieties,” *Annals of Mathematics* 179 (2014), 301–365.
   [arXiv](https://arxiv.org/abs/1111.6228).
