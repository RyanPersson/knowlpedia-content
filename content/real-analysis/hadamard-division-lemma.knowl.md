+++
id = "real-analysis/hadamard-division-lemma"
title = "Hadamard division lemma in one normal variable"
kind = "theorem"
summary = "Finite-order vanishing along a hyperplane factors as a power of its normal coordinate times a smooth function."
aliases = ["Hadamard lemma", "smooth division by a coordinate"]
domains = ["real-analysis"]
section_mode = "progressive"
prerequisites = ["real-analysis/class-ck-map", "real-analysis/fundamental-theorem-of-calculus-ii", "measure-theory/differentiation-under-integral", "shared-foundations/factorial"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

Let \(f\in C^\infty(( -\varepsilon,\varepsilon)\times U)\), with \(U\subseteq\mathbb R^n\) open. If \(m\ge1\) and
\[
\partial_t^j f(0,x)=0\qquad(0\le j<m),
\]
then \(f(t,x)=t^m g(t,x)\) for a smooth function \(g\), given by
\[
g(t,x)=\frac1{(m-1)!}\int_0^1(1-s)^{m-1}\partial_t^m f(st,x)\,ds.
\]
This is **smooth division by the normal coordinate**.

## Proof and boundary value

Repeated use of the [[real-analysis/fundamental-theorem-of-calculus-ii|fundamental theorem of calculus]] gives the integral remainder formula. Smoothness follows by [[measure-theory/differentiation-under-integral|differentiation under the integral]] on the compact interval \([0,1]\). In particular,
\[
g(0,x)=\frac{\partial_t^m f(0,x)}{m!}.
\]

## Limitation

This divides by a finite power of \(t\). Flatness of two functions at zero does not by itself make their quotient smooth or bounded; for example \(e^{-1/t^2}/e^{-2/t^2}=e^{1/t^2}\) on \(t>0\).
