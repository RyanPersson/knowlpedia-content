+++
id = "measure-theory/complete-measure"
title = "Complete measure"
kind = "definition"
summary = "A measure for which every subset of a measurable null set is measurable."
aliases = ["complete measure space", "measure completeness"]
domains = ["measure-theory"]
section_mode = "progressive"
prerequisites = ["measure-theory/measure-space", "measure-theory/null-set", "shared-foundations/subset"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

A [[measure-theory/measure-space|measure space]] \((X,\Sigma,\mu)\) is **complete** if every subset of every measurable set of measure zero belongs to \(\Sigma\). Such subsets necessarily have measure zero by monotonicity.

## Two notions of completeness

This property concerns the sigma-algebra and its null sets. It is distinct from completeness of a metric or Banach space. An incomplete measure space still has complete \(L^p\) spaces: metric completeness of \(L^p\) does not require the measure to contain all subsets of null sets.
