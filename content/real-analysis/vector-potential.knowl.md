+++
id = "real-analysis/vector-potential"
title = "Vector potential for a divergence-free field"
kind = "definition"
summary = "A field A whose curl equals the given three-dimensional vector field."
aliases = ["curl potential"]
domains = ["real-analysis"]
section_mode = "progressive"
prerequisites = ["real-analysis/curl", "real-analysis/divergence", "real-analysis/class-ck-map"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

A **vector potential** for a field \(u\) is a field \(A\) whose [[real-analysis/curl|curl]] satisfies
\[
u=\nabla\times A.
\]
If \(A\) is \(C^2\), then \(u\) is divergence-free. Adding a gradient \(\nabla\phi\) to \(A\) leaves its curl unchanged, so potentials are generally nonunique.

## A local construction

On a region star-shaped about zero, a smooth divergence-free field has the potential
\[
A(x)=\int_0^1 t\,u(tx)\times x\,dt.
\]
Indeed,
\(\nabla\times[t\,u(tx)\times x]=\partial_t[t^2u(tx)]\)
when \(\operatorname{div}u=0\); integration gives \(\nabla\times A=u\). This local formula does not assert that an arbitrary domain admits a global potential with prescribed boundary conditions or compact support.

## Localization

If a smooth scalar cutoff \(\chi\) equals one in a region, then \(\nabla\times(\chi A)=u\) there and stays divergence-free everywhere. The transition region contains the correction \(\nabla\chi\times A\).
