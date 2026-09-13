+++
id = "fluid-dynamics/leray-projection"
title = "Leray projection on Euclidean space"
kind = "definition"
summary = "The orthogonal L2 projection onto distributionally divergence-free vector fields."
aliases = ["Helmholtz–Leray projector"]
domains = ["fluid-dynamics"]
section_mode = "progressive"
prerequisites = ["harmonic-analysis/euclidean-l2-fourier-multiplier", "linear-algebra/orthogonal-projection", "real-analysis/divergence", "linear-algebra/outer-product"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

The **Leray projection** \(\mathbb P\) on \(L^2(\mathbb R^n;\mathbb R^n)\) is the [[harmonic-analysis/euclidean-l2-fourier-multiplier|Fourier multiplier]]
\[
\widehat{\mathbb Pu}(\xi)=\left(I-\frac{\xi\otimes\xi}{|\xi|^2}\right)\widehat u(\xi),\qquad \xi\ne0.
\]
The [[linear-algebra/outer-product|matrix]] is the [[linear-algebra/orthogonal-projection|orthogonal projection]] onto \(\xi^\perp\); its value at the single frequency zero is immaterial on Euclidean \(L^2\). Thus \(\mathbb P\) is the orthogonal projection onto the closed subspace of fields with [[real-analysis/divergence|distributional divergence]] zero.

## Projected momentum

For sufficiently regular decaying fields, \(\mathbb P\nabla p=0\), so applying \(\mathbb P\) eliminates the pressure from momentum. The symmetric Euler bilinear operator is
\[
B(u,v)=-\tfrac12\mathbb P\bigl((u\cdot\nabla)v+(v\cdot\nabla)u\bigr).
\]
On divergence-free fields, ordinary Navier–Stokes takes the form \(u_t=\nu\Delta u+B(u,u)+\mathbb P f\).
