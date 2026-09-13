+++
id = "complex-analysis/common-holomorphic-neighborhood"
title = "Common holomorphic neighborhood for a parameter family"
kind = "definition"
summary = "A single complex domain and bound that work for every member of a family near a real parameter set."
aliases = ["uniform complex neighborhood", "common analytic domain"]
domains = ["complex-analysis"]
section_mode = "progressive"
prerequisites = ["differential-geometry/holomorphic-map", "topology/neighborhood", "complex-analysis/cauchy-derivative-estimate"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

A family \(f_\lambda\) has a **common bounded holomorphic neighborhood** of a compact real interval \(I\) if there exist an open \(\Omega\subset\mathbb C\), a radius \(r>0\), and \(M<\infty\) such that every closed radius-\(r\) disc centered on \(I\) lies in \(\Omega\), every \(f_\lambda\) is holomorphic there, and \(\sup_{\lambda,z\in\Omega}|f_\lambda(z)|\le M\).

## Consequence and failure of uniformity

Cauchy estimates give \(\sup_{\lambda,x\in I}|f_\lambda^{(m)}(x)|\le M m!r^{-m}\) at every order. Individual real analyticity gives no such common radius: \(f_n(z)=1/(1+n^2z^2)\) has poles at \(\pm i/n\), approaching the real interval containing zero. A bound only on the real interval also cannot replace a bound on the complex domain.
