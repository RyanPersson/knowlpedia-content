+++
id = "fluid-dynamics/euler-subsolution"
title = "Euler subsolution with prescribed energy"
kind = "definition"
summary = "A linear momentum solution whose velocity and trace-free flux lie below a prescribed energy matrix."
aliases = ["strict Euler subsolution"]
domains = ["fluid-dynamics"]
section_mode = "progressive"
prerequisites = ["fluid-dynamics/euler-equations", "functional-analysis/distributional-derivative", "linear-algebra/symmetric-matrix", "linear-algebra/trace", "linear-algebra/positive-semidefinite-matrix", "linear-algebra/outer-product", "measure-theory/locally-integrable-function", "functional-analysis/distribution", "real-analysis/divergence"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 2
+++

Let \(e\geq0\) be locally integrable on a space-time cylinder in dimension \(n\geq2\). An **Euler subsolution with energy bound \(e\)** is a triple \((v,S,q)\), with \(v\in L^2_{\rm loc}\), \(S\in L^1_{\rm loc}\) [[linear-algebra/symmetric-matrix|symmetric]] and [[linear-algebra/trace|trace free]], and \(q\) a distribution, such that
\[
\partial_t v+\operatorname{div}S+\nabla q=0,\qquad
\operatorname{div}v=0,\qquad
v\otimes v-S\leq\frac{2e}{n}I.
\]
The equations use [[functional-analysis/distributional-derivative|distributional derivatives]]; the inequality says that \((2e/n)I-v\otimes v+S\) is [[linear-algebra/positive-semidefinite-matrix|positive semidefinite]] almost everywhere. A **smooth strict subsolution** has smooth \(v,S,q\), continuous \(e\), and a positive definite gap everywhere.

The products are [[linear-algebra/outer-product|outer products]], the coefficients have the indicated [[measure-theory/locally-integrable-function|local integrability]], and the pressure is a [[functional-analysis/distribution|distribution]]. This formulation relaxes [[fluid-dynamics/euler-equations|Euler]] while keeping its [[real-analysis/divergence|divergence]] constraints.

## Recovering Euler

Taking the trace gives \(|v|^2/2\leq e\). If equality holds almost everywhere, the positive semidefinite gap has zero trace and is zero. Then \(S=v\otimes v-(2e/n)I\), and \(v\) satisfies [[fluid-dynamics/euler-equations|Euler]] with pressure \(p=q-2e/n\).

## References

- [De Lellis and Székelyhidi, The Euler equations as a differential inclusion (2009)](https://annals.math.princeton.edu/wp-content/uploads/annals-v170-n3-p09-p.pdf).
