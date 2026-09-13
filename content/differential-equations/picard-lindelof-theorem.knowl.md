+++
id = "differential-equations/picard-lindelof-theorem"
title = "Picard–Lindelöf local existence and uniqueness theorem"
kind = "theorem"
summary = "Continuity in time and local uniform Lipschitz control in the state give a unique local solution."
aliases = ["Picard existence theorem", "Picard-Lindelof theorem"]
domains = ["differential-equations"]
section_mode = "progressive"
prerequisites = ["differential-equations/picard-iteration", "topology/locally-lipschitz-map", "functional-analysis/continuous-banach-valued-functions", "functional-analysis/contraction-on-a-closed-ball"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

Let \(F\) be continuous on an open set in \(\mathbb R\times\mathbb R^m\) and [[topology/locally-lipschitz-map|locally Lipschitz in the state, locally uniformly in time]]. Through every point \((t_0,y_0)\) in that set there is a unique local solution of \(y'=F(t,y)\), \(y(t_0)=y_0\). Uniqueness means that two solutions with this data agree wherever their intervals overlap.

## Quantitative construction

On a closed rectangle \(|t-t_0|\le a\), \(|y-y_0|\le r\) inside the domain, choose \(|F|\le M\) and a state Lipschitz constant \(L\). For \(0<h\le a\) with \(hM\le r\) and \(hL<1\), the Picard map preserves the radius-\(r\) ball in the complete space of continuous curves on \([t_0-h,t_0+h]\) and contracts it. Its fixed point solves the equation by the fundamental theorem of calculus.

## References

- [Gerald Teschl, Ordinary Differential Equations and Dynamical Systems, Chapters 2–4](https://www.mat.univie.ac.at/~gerald/ftp/book-ode/ode.pdf).
