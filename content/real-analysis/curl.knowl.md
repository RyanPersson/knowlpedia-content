+++
id = "real-analysis/curl"
title = "Curl of a three-dimensional vector field"
kind = "definition"
summary = "The oriented antisymmetric first derivatives of a vector field on a subset of R^3."
aliases = ["rot", "curl operator"]
domains = ["real-analysis"]
section_mode = "progressive"
prerequisites = ["real-analysis/euclidean-vector-field", "real-analysis/partial-derivative", "linear-algebra/cross-product"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For a [[real-analysis/class-ck-map|\(C^1\)]] [[real-analysis/euclidean-vector-field|field]] \(u\) on an open subset of standard oriented \(\mathbb R^3\), its **curl** is
\[
\nabla\times u=(\partial_yu_z-\partial_zu_y,\
\partial_zu_x-\partial_xu_z,\
\partial_xu_y-\partial_yu_x).
\]
For \(C^2\) fields, commuting mixed partials proves \(\operatorname{div}(\nabla\times u)=0\). Similarly \(\nabla\times\nabla f=0\) for \(C^2\) scalars.

## Cylindrical components

For \(r>0\), differentiating the cylindrical basis gives
\[
\begin{aligned}
(\nabla\times u)_r&=r^{-1}\partial_\theta u_z-\partial_z u_\theta,\\
(\nabla\times u)_\theta&=\partial_z u_r-\partial_r u_z,\\
(\nabla\times u)_z&=r^{-1}\partial_r(ru_\theta)-r^{-1}\partial_\theta u_r.
\end{aligned}
\]

## Cutting off a potential

The [[real-analysis/product-rule|product rule]] yields
\(\nabla\times(\chi A)=\nabla\chi\times A+\chi\nabla\times A\).
The extra term is essential when localizing a divergence-free field through a vector potential.

## References

- [Arthur Mattuck, MIT 18.02SC, The Del Operator](https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/a5910abd3b1b31bdb0c26ff1e0185ef2_MIT18_02SC_MNotes_v15.1.pdf).
- [MIT 6.013, Differential operators in cylindrical and spherical coordinates](https://ocw.mit.edu/courses/6-013-electromagnetics-and-applications-fall-2005/59e100001186c03a19ca3361dcd3b240_formula_sheet2.pdf).
