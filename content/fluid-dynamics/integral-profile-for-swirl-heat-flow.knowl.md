+++
id = "fluid-dynamics/integral-profile-for-swirl-heat-flow"
title = "Integral profile for radial swirl heat flow"
kind = "theorem"
summary = "A positive Gamma-integral profile solves the swirl heat equation away from the axis up to a specified terminal time."
aliases = ["Gamma integral swirl heat profile"]
domains = ["fluid-dynamics"]
section_mode = "progressive"
prerequisites = ["fluid-dynamics/swirl-diffusion-operator", "real-analysis/gamma-average-profile", "differential-equations/equation-for-gamma-average", "real-analysis/chain-rule-multivariable", "real-analysis/real-power", "real-analysis/smooth-endpoint-of-gamma-average"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 2
+++

Fix \(A>1/2\), \(c,\nu>0\), and a time \(T\). Put \(s=r^2/2\), \(\tau=T-t\), and
\[
K(r,t)=c\,s^{-A}F_{A+1/2,A-1/2}(2\nu\tau/s),
\qquad r>0,\ t\le T.
\]
Then \(K\) is positive, smooth up to \(t=T\) from below for every \(r>0\), and solves the [[fluid-dynamics/swirl-diffusion-operator|swirl heat equation]]
\[
\partial_tK=\nu(K_{rr}+r^{-1}K_r-r^{-2}K).
\]

## Verification

Set \(z=2\nu\tau/s\) and \(F=F_{A+1/2,A-1/2}\). The two sides are respectively \(-2\nu c s^{-A-1}F'\) and
\[
2\nu c s^{-A-1}\bigl[z^2F''+(2A+1)zF'+(A^2-1/4)F\bigr].
\]
The Gamma-average equation makes them equal. Moreover \(-zF'/F\) is the average of \((A-1/2)zv/(1+zv)\) against a positive normalized density. It lies in \([0,A-1/2)\), hence \(rK_r/(2K)=-A-zF'/F<-1/2\), proving \(K_r<0\).

The statement is on \(r>0\). It does not give a regular field on the axis or solve a general backward heat initial-value problem. At the terminal time its value is the power law \(c(r^2/2)^{-A}\).
