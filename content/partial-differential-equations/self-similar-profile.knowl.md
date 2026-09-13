+++
id = "partial-differential-equations/self-similar-profile"
title = "Self-similar profile"
kind = "definition"
summary = "A fixed profile that determines an evolving field by dilation and amplitude rescaling."
aliases = []
domains = ["partial-differential-equations"]
section_mode = "progressive"
prerequisites = ["partial-differential-equations/similarity-variables", "real-analysis/anisotropic-dilation"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

A field is **self-similar** for prescribed exponents if it has the form
\[
u(t,x)=(T-t)^{-a}V\bigl(D_{T-t}^{-1}x\bigr),\qquad t<T,
\]
with a profile \(V\) independent of time. In [[partial-differential-equations/similarity-variables|similarity variables]], this is a stationary rescaled field \(U(s,y)=V(y)\).

## Profile equations

If \(u\) is also required to solve a PDE, substitution gives an equation for \(V\), provided the time powers balance. A concentrating ansatz is not automatically a solution or a symmetry of the PDE. Slowly varying profiles and additional corrections generally destroy exact self-similarity even when they have a self-similar leading term.
