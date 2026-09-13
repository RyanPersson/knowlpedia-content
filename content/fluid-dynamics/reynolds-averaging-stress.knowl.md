+++
id = "fluid-dynamics/reynolds-averaging-stress"
title = "Reynolds averaging stress"
kind = "definition"
summary = "The covariance of a fluctuating velocity that appears when averaging its quadratic transport."
aliases = ["Reynolds stress covariance"]
domains = ["fluid-dynamics"]
section_mode = "progressive"
prerequisites = ["probability/covariance-matrix", "linear-algebra/outer-product", "fluid-dynamics/navier-stokes-equations", "probability/expectation"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For a random velocity field \(u(x,t,\omega)\) with finite second moments, let \(v=\mathbb E u\). The **Reynolds averaging stress** in the covariance convention is
\[
C=\mathbb E[(u-v)\otimes(u-v)]
  =\mathbb E[u\otimes u]-v\otimes v.
\]
It is the [[probability/covariance-matrix|covariance matrix]] of velocity, using [[probability/expectation|expectation]] and the [[linear-algebra/outer-product|outer product]]. If averaging commutes with the derivatives and each realization solves [[fluid-dynamics/navier-stokes-equations|Navier–Stokes]], then
\[
\partial_t v+\operatorname{div}(v\otimes v)+\nabla\mathbb E p
=\nu\Delta v+\mathbb E f-\operatorname{div}C.
\]

## Sign convention

For every vector \(a\), \(a^TCa=\mathbb E|a\cdot(u-v)|^2\geq0\). If a defect tensor is instead placed as \(+\operatorname{div}R\) on the right, then \(R=-C\). A general defect tensor need not be an actual covariance.

## References

- [De Lellis and Székelyhidi, The h-principle and the equations of fluid dynamics (2012)](https://www.math.ias.edu/delellis/sites/math.ias.edu.delellis/files/bull1376.pdf).
