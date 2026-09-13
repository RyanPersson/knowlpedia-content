+++
id = "functional-analysis/frozen-linear-inverse-residual-update"
title = "Residual update with a fixed linear inverse"
kind = "theorem"
summary = "A quadratic equation admits an exact residual formula when corrections use the derivative at one fixed reference point."
aliases = ["fixed-inverse correction step"]
domains = ["functional-analysis"]
section_mode = "progressive"
prerequisites = ["linear-algebra/quadratic-map", "functional-analysis/bounded-bilinear-map", "functional-analysis/bounded-linear-operator", "real-analysis/linearization", "linear-algebra/right-inverse", "linear-algebra/normed-vector-space"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 2
+++

Let \(F(x)=c+Lx+B(x,x)\) between normed spaces, with \(L\) bounded linear and \(B\) bounded symmetric bilinear. Fix \(x_0\), put \(A=DF(x_0)\), and suppose a bounded linear \(R\) satisfies \(AR=I\). At \(x=x_0+w\), let \(r=F(x)\) and choose \(h=-Rr\). Then
\[
F(x+h)=2B(w,h)+B(h,h).
\]
This is the **residual update using the [[real-analysis/linearization|linearization]] at the fixed point \(x_0\)**.

## Exact cancellation

The quadratic expansion gives \(F(x+h)=r+Ah+2B(w,h)+B(h,h)\). Since \(Ah=-r\), the first two terms cancel. Therefore
\[
\|F(x+h)\|\le2\|B\|\|w\|\|R\|\|r\|+\|B\|\|R\|^2\|r\|^2.
\]
The reference derivative and inverse remain fixed. This formula holds for arbitrary input size; a gain estimate requires the displayed products to be small in the chosen scale.

## Decay exponents

For a parameter \(\varepsilon\), suppose \(\|B\|=O(\varepsilon^{-b})\), \(\|R\|=O(\varepsilon^{-\ell})\), \(\|w\|=O(\varepsilon^\alpha)\), and \(\|r\|=O(\varepsilon^\beta)\). The new residual is
\[
O(\varepsilon^{\beta+\alpha-\ell-b})+
O(\varepsilon^{2\beta-2\ell-b}).
\]
Both improve on order \(\beta\) if \(\alpha>\ell+b\) and \(\beta>2\ell+b\). These are sufficient conditions, not a guarantee for every nonlinear iteration. New residuals must be recomputed from the complete updated state, including the quadratic term.
