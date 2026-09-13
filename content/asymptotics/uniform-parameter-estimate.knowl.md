+++
id = "asymptotics/uniform-parameter-estimate"
title = "Uniform parameter estimate"
kind = "definition"
summary = "An estimate whose constants and validity domain are independent of the declared parameters."
aliases = ["uniform parameter dependence", "uniform implicit constant"]
domains = ["asymptotics"]
section_mode = "progressive"
prerequisites = ["asymptotics/big-o", "real-analysis/multi-index-notation", "real-analysis/mixed-partial-derivative"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

The estimate \(F(\varepsilon,\lambda,x)=O(G(\varepsilon,\lambda,x))\), for \(G>0\), is **uniform in \((\lambda,x)\in\Lambda\times K\)** if there are a single \(C\) and a single \(\varepsilon_*>0\) such that
\[
|F(\varepsilon,\lambda,x)|\le C G(\varepsilon,\lambda,x)
\]
for every \(0<\varepsilon<\varepsilon_*\) and every permitted \((\lambda,x)\). This specifies the quantifiers hidden in [[asymptotics/big-o|Big-O notation]].

## Derivatives and a common domain

A smooth family estimate may assert, for every [[real-analysis/multi-index-notation|multi-index]] \(I\), a constant \(C_I\) controlling \(\partial^I F\). The statement
\[
\exists\varepsilon_*\;\forall I\;\exists C_I\;\forall(\varepsilon,\lambda,x)
\]
on the same domain is stronger than allowing a different \(\varepsilon_{*,I}\) for each derivative order. Constants may depend on fixed profiles or a fixed construction stage while remaining uniform over scales and labels. These dependencies must be named.

## References

- [NIST Digital Library of Mathematical Functions, §2.1: Definitions and elementary properties](https://dlmf.nist.gov/2.1).
