+++
id = "differential-equations/peano-baker-series"
title = "Peano–Baker series"
kind = "definition"
summary = "The time-ordered matrix series for the propagator of a nonautonomous linear ODE."
aliases = ["Picard series for a linear ODE", "time-ordered exponential"]
domains = ["differential-equations"]
section_mode = "progressive"
prerequisites = ["differential-equations/fundamental-matrix", "measure-theory/ordered-integration-simplex", "functional-analysis/absolutely-convergent-banach-series"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For continuous \(A\), the **Peano–Baker series** for the [[differential-equations/fundamental-matrix|propagator]] is
\[
\Phi(t,s)=I+\sum_{n=1}^\infty
\int_{s<t_n<\cdots<t_1<t}A(t_1)\cdots A(t_n)\,dt_n\cdots dt_1
\quad(t\ge s).
\]
It is obtained by repeatedly substituting in \(\Phi(t,s)=I+\int_s^tA(\tau)\Phi(\tau,s)\,d\tau\).

## Convergence and order

The [[measure-theory/ordered-integration-simplex|simplex estimate]] bounds the \(n\)-th term by \((M|t-s|)^n/n!\) on any compact interval where \(\|A\|\le M\). The series converges uniformly, and its integral equation identifies it with the unique propagator. Later-time factors stand on the left. Unless the coefficient matrices commute at different times, their order cannot be rearranged.
