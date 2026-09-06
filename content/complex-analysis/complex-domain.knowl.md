+++
id = "complex-analysis/complex-domain"
title = "Complex domain"
kind = "definition"
summary = "A connected open subset of the complex plane."
aliases = ["domain in the complex plane", "plane domain", "region"]
domains = ["complex-analysis", "topology"]
section_mode = "progressive"
prerequisites = ["topology/open-set", "shared-foundations/complex-numbers-c"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

A **complex domain** is a nonempty, connected [[topology/open-set|open subset]] \(D\subseteq\mathbb C\). Connectedness is part of the term “domain”; an arbitrary open subset of \(\mathbb C\) may have several components.

## Why domains are natural

Local analytic statements can be made on any open set. Global uniqueness results, such as the [[complex-analysis/identity-theorem|identity theorem]], use connectedness to propagate local information throughout \(D\). Each connected component of an open set is itself a domain, so little is lost by working one component at a time.

## Convention

Some authors use “region” as a synonym and reserve “domain” for the source of any function. This knowl uses **complex domain** only in the topological sense above.

## References

1. John B. Conway, *Functions of One Complex Variable I*, 2nd ed., Springer, 1978. [Publisher record](https://doi.org/10.1007/978-1-4612-6313-5). Relevant: Chapter II, §1.
