+++
id = "real-analysis/divergence"
title = "Divergence of a Euclidean vector field"
kind = "definition"
summary = "The trace of the Cartesian derivative of a vector field."
aliases = ["div", "divergence operator"]
domains = ["real-analysis"]
section_mode = "progressive"
prerequisites = ["real-analysis/euclidean-vector-field", "real-analysis/partial-derivative", "shared-foundations/finite-sum"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For a [[real-analysis/class-ck-map|\(C^1\)]] [[real-analysis/euclidean-vector-field|vector field]] \(u:U\to\mathbb R^n\), its **divergence** is
\[
\operatorname{div}u=\nabla\cdot u=\sum_{i=1}^n\partial_{x_i}u_i.
\]
It is a scalar field. The condition \(\operatorname{div}u=0\) defines a [[real-analysis/divergence-free-field|divergence-free field]].

## Product identity

For a scalar \(f\), the product rule gives
\(\operatorname{div}(fu)=\nabla f\cdot u+f\operatorname{div}u\).

## Cylindrical expression

Writing \(u=u_r e_r+u_\theta e_\theta+u_z e_z\) in the [[real-analysis/cylindrical-coordinates|cylindrical frame]] gives, for \(r>0\),
\[
\operatorname{div}u=\frac1r\partial_r(ru_r)+\frac1r\partial_\theta u_\theta+\partial_z u_z.
\]
The \(u_r/r\) term arises from differentiating the moving basis. Coordinate singularities at \(r=0\) require a separate Cartesian regularity check.

## References

- [Arthur Mattuck, MIT 18.02SC, The Del Operator](https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/a5910abd3b1b31bdb0c26ff1e0185ef2_MIT18_02SC_MNotes_v15.1.pdf).
- [MIT 6.013, Differential operators in cylindrical and spherical coordinates](https://ocw.mit.edu/courses/6-013-electromagnetics-and-applications-fall-2005/59e100001186c03a19ca3361dcd3b240_formula_sheet2.pdf).
