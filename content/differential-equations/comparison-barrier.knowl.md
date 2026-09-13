+++
id = "differential-equations/comparison-barrier"
title = "Scalar comparison barriers for an ODE"
kind = "proposition"
summary = "Subsolutions and supersolutions bound a scalar solution when the vector field is locally Lipschitz."
aliases = ["ODE subsolution and supersolution", "comparison barrier"]
domains = ["differential-equations"]
section_mode = "progressive"
prerequisites = ["differential-equations/gronwall-inequality", "topology/locally-lipschitz-map", "differential-equations/ordinary-differential-equation"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

Let \(y'=F(t,y)\), with \(F\) continuous and [[topology/locally-lipschitz-map|locally uniformly Lipschitz]] in its scalar state. Suppose differentiable barriers \(a,b\) satisfy
\[
a'\le F(t,a),\qquad b'\ge F(t,b),\qquad
a(t_0)\le y(t_0)\le b(t_0).
\]
As long as all three functions stay in the common equation domain, \(a(t)\le y(t)\le b(t)\) for \(t\ge t_0\).

## Why touching does not permit crossing

On a compact interval, the positive part of \(a-y\) is bounded by a Lipschitz constant times its own accumulated integral. Gronwall forces it to vanish; apply the same reasoning to \(y-b\). A barrier can therefore preserve positivity or separation from a singular denominator. For systems, componentwise comparison needs further order-preserving hypotheses and does not follow from this scalar statement.
