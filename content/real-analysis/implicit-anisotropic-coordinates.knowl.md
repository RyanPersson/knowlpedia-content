+++
id = "real-analysis/implicit-anisotropic-coordinates"
title = "Implicit anisotropic similarity coordinates"
kind = "definition"
summary = "A smooth positive scale defined by an implicit equation balancing time distance and an axial coordinate."
aliases = []
domains = ["real-analysis"]
section_mode = "progressive"
prerequisites = ["real-analysis/implicit-function-theorem", "real-analysis/real-power", "asymptotics/comparable-functions", "real-analysis/intermediate-value-theorem"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

Fix \(0<d<1/2\). For \(\tau>0\), \(z\in\mathbb R\), define \(q\) as the unique root with \(q>|z|^{1/d}\) of
\[
q-z^2q^{1-2d}=\tau.
\]
For \(r\ge0\), set \(\eta=zq^{-d}\), \(X=r^2/(2q)\), and \(L=1-(1-2d)\eta^2\). Then
\[
\tau=q(1-\eta^2),\quad |\eta|<1,\quad L\ge2d,
\qquad q\asymp\tau+|z|^{1/d}.
\]
The constants of [[asymptotics/comparable-functions|comparability]] depend only on \(d\).

## Existence, uniqueness, and smoothness

The left side is zero at \(q=|z|^{1/d}\), tends to infinity, and has derivative \(1-(1-2d)z^2q^{-2d}\ge2d\) on that branch. For \(z=0\) the solution is \(q=\tau\). The [[real-analysis/implicit-function-theorem|implicit function theorem]] gives smooth dependence wherever \(q>0\).

The lower bound follows from \(q\ge\max(\tau,|z|^{1/d})\). If \(q\le2\tau\), the upper bound is immediate. Otherwise \(q/2\le z^2q^{1-2d}\), so \(q\le2^{1/(2d)}|z|^{1/d}\). At \(\tau=0,z\ne0\), the scale extends smoothly locally with \(q=|z|^{1/d}\) and \(L=2d\); the corner \((\tau,z)=(0,0)\) is excluded.
