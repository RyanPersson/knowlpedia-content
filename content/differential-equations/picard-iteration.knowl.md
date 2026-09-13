+++
id = "differential-equations/picard-iteration"
title = "Picard iteration"
kind = "definition"
summary = "Successive substitution into the integral equation for an initial-value problem."
aliases = ["successive approximation for ODEs"]
domains = ["differential-equations"]
section_mode = "progressive"
prerequisites = ["differential-equations/initial-value-problem", "shared-foundations/sequence"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For \(y'=F(t,y)\), \(y(t_0)=y_0\), **Picard iteration** starts from a trial curve, often \(y^{(0)}(t)=y_0\), and sets
\[
y^{(n+1)}(t)=y_0+\int_{t_0}^tF(s,y^{(n)}(s))\,ds.
\]
This is fixed-point iteration for the [[differential-equations/initial-value-problem|integral equation]].

## Convergence mechanism

On a time interval of length at most \(h\) from \(t_0\), a state Lipschitz bound \(L\) gives
\(\|Ty-Tz\|_{\sup}\le hL\|y-z\|_{\sup}\).
One must also keep the iterates in a ball where \(F\) is defined and bounded. The [[differential-equations/picard-lindelof-theorem|local existence theorem]] makes both requirements precise. Repeated time integration also gives factorial bounds, which can prove convergence without a one-step contraction on a longer interval.
