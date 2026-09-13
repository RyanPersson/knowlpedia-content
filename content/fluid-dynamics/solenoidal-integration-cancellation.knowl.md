+++
id = "fluid-dynamics/solenoidal-integration-cancellation"
title = "Integration cancellation for divergence-free transport and pressure"
kind = "theorem"
summary = "Divergence-free fields remove transport and pressure terms from unweighted whole-domain energy integrals."
aliases = []
domains = ["fluid-dynamics"]
section_mode = "progressive"
prerequisites = ["real-analysis/divergence-free-field", "real-analysis/product-rule", "real-analysis/integration-by-parts", "differential-geometry/stokes-theorem"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For smooth fields with compact support on \(\mathbb R^n\), or smooth periodic fields integrated over a fundamental cell, \(\nabla\cdot a=0\) implies
\[
\int(a\cdot\nabla)b\cdot b=0.
\]
Also, if \(\nabla\cdot b=0\), then \(\int\nabla p\cdot b=0\), provided the pressure is smooth on the support in the compact-support case and periodic in the periodic case. These are **[[real-analysis/divergence-free-field|solenoidal]] energy cancellations**.

## Proof

The transport integrand is \(a\cdot\nabla(|b|^2/2)\). Integration by parts moves the derivative onto \(a\), and its divergence is zero. Similarly, \(\int\nabla p\cdot b=-\int p\,\nabla\cdot b\). Compact support removes boundary terms; on a periodic cell opposite faces cancel. Multiplying by a nonconstant spatial cutoff leaves flux terms involving derivatives of that cutoff.
