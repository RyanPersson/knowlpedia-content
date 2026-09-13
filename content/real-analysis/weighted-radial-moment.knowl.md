+++
id = "real-analysis/weighted-radial-moment"
title = "Weighted radial moment"
kind = "definition"
summary = "An integral of a radial function against a specified power of radius."
aliases = ["radial moment", "power-weighted integral"]
domains = ["real-analysis"]
section_mode = "progressive"
prerequisites = ["measure-theory/lebesgue-integral", "real-analysis/real-power", "measure-theory/lebesgue-integrable-function"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For a real exponent \(e\), the **weighted radial moment** of a scalar function \(f\) is
\[
M_e(f)=\int_0^\infty r^e f(r)\,dr,
\]
provided \(r^ef(r)\) is [[measure-theory/lebesgue-integrable-function|integrable]]. The radial variable uses the one-dimensional measure \(dr\); any geometric volume factor is included explicitly in the weight.

## Parameters and constraints

If \(f=f(r,z,t)\), this moment is a function of \((z,t)\). Requiring \(M_e(f)=0\) means an identity at every parameter value, not just a finite collection of scalar equalities. Support in a fixed compact interval away from zero avoids endpoint issues for every real exponent. Weighted moments can also be defined componentwise for vector-valued functions.
