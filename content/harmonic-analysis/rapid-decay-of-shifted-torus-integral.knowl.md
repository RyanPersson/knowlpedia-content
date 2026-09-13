+++
id = "harmonic-analysis/rapid-decay-of-shifted-torus-integral"
title = "Rapid decay of a shifted torus integral"
kind = "theorem"
summary = "A zero integrated mean and a Diophantine drift give any fixed inverse power of a large shift, at a finite derivative cost."
aliases = ["nonstationary shifted-torus averaging"]
domains = ["harmonic-analysis"]
section_mode = "progressive"
prerequisites = ["partial-differential-equations/shifted-characteristic-primitive", "harmonic-analysis/diophantine-directional-inverse", "measure-theory/zero-mean-function", "real-analysis/integration-by-parts", "real-analysis/compact-derivative-seminorm", "harmonic-analysis/diophantine-direction", "asymptotics/big-o"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 2
+++

Let \(v\) be a Diophantine direction on \(\mathbb T^n\), and let smooth \(F(s,y)\) be supported in a fixed bounded \(s\)-interval. Assume \(\int\langle F(s,\cdot)\rangle_y\,ds=0\). For \(M\ge1\), define
\[
J_MF(U,y)=\int_{\mathbb R}F(U+z,y+Mzv)\,dz.
\]
For every fixed pair of integers \(m,p\ge0\), there is a finite integer \(r=r(m,p)\) and a constant independent of \(M\) such that
\[
\|J_MF\|_{C^m_{U,y}}\le C_{m,p}M^{-p}\|F\|_{C^r_{s,y}}.
\]
This uses the [[harmonic-analysis/diophantine-directional-inverse|zero-mean directional inverse]].

## Repeated integration by parts

Let \(L=v\cdot\nabla_y\), and let \(F^\circ=F-\langle F\rangle_y\). The omitted mean has zero full-line integral. Integrating the total \(z\)-derivative of \(L^{-1}F^\circ(U+z,y+Mzv)\) gives
\[
J_MF=(-M^{-1})^p\int_{\mathbb R}
\partial_s^pL^{-p}F^\circ(U+z,y+Mzv)\,dz.
\]
All boundary terms vanish. A fixed finite loss for each application of \(L^{-1}\), together with \(p\) source derivatives, gives a finite \(r\); for example, if one inverse costs \(\ell\) derivatives, \(r=m+p+p\ell\) suffices. The fixed-shift form handles additional \(U\) derivatives without an \(M\) factor.

## Quantifiers

The constant and required derivative order can grow with \(p\). A family with uniform bounds at every fixed derivative order therefore gives decay faster than every inverse power of \(M\). A single finite regularity bound gives only the corresponding finite range of powers. No estimate uniform in \(p\) is asserted.
