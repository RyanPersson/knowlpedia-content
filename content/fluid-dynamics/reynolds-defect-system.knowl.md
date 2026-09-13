+++
id = "fluid-dynamics/reynolds-defect-system"
title = "Reynolds defect system"
kind = "definition"
summary = "Momentum balance with the divergence of a symmetric error tensor."
aliases = ["Euler–Reynolds system", "Navier–Stokes–Reynolds system"]
domains = ["fluid-dynamics"]
section_mode = "progressive"
prerequisites = ["fluid-dynamics/navier-stokes-equations", "linear-algebra/symmetric-matrix", "real-analysis/divergence", "linear-algebra/outer-product", "real-analysis/laplacian", "real-analysis/gradient"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 2
+++

A **Reynolds defect system**, with the right-hand-side sign convention, is
\[
\partial_t v+\operatorname{div}(v\otimes v)+\nabla p
=\nu\Delta v+f+\operatorname{div}R,\qquad \operatorname{div}v=0.
\]
Here \(R(x,t)\) is a [[linear-algebra/symmetric-matrix|symmetric matrix field]], its [[real-analysis/divergence|divergence]] is \((\operatorname{div}R)_i=\sum_j\partial_jR_{ij}\), and \(v\otimes v\) is an [[linear-algebra/outer-product|outer product]]. For \(\nu>0\) this is called **Navier–Stokes–Reynolds**; for \(\nu=0\), **Euler–Reynolds**. The [[fluid-dynamics/navier-stokes-equations|Navier–Stokes equation]] is recovered when the defect divergence vanishes.

The pressure term is its [[real-analysis/gradient|gradient]] and \(\Delta\) is the componentwise [[real-analysis/laplacian|Laplacian]].

## Pressure and trace

Writing \(R=R^\circ+rI\) with \(r=\operatorname{tr}R/n\), replace \(p\) by \(p-r\) to use the trace-free tensor \(R^\circ\). Thus trace parts can be put into pressure. The sign of a tensor called Reynolds stress must be checked against its displayed equation.
