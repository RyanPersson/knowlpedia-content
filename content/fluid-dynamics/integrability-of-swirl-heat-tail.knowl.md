+++
id = "fluid-dynamics/integrability-of-swirl-heat-tail"
title = "Integrability of the subtracted swirl heat tail"
kind = "theorem"
summary = "The Gamma-integral heat profile differs from its terminal power by two extra powers of radial decay."
aliases = []
domains = ["fluid-dynamics"]
section_mode = "progressive"
prerequisites = ["fluid-dynamics/integral-profile-for-swirl-heat-flow", "real-analysis/smooth-endpoint-of-gamma-average", "measure-theory/reference-subtracted-integral", "real-analysis/real-power"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For the [[fluid-dynamics/integral-profile-for-swirl-heat-flow|Gamma-integral swirl profile]] with \(A>1/2\), put \(K_{\rm ref}(r)=c(r^2/2)^{-A}\). For \(\tau=T-t\ge0\),
\[
|K-K_{\rm ref}|\le C\tau r^{-2A-2},\qquad
|\partial_tK|\le Cr^{-2A-2}.
\]
The constants depend on the fixed parameters \(A,c,\nu\).

## Weighted tail integral

The bounds \(|F(z)-1|\le ab z\) and \(|F'(z)|\le ab\) give the stated estimates. Therefore for every \(R>0\),
\[
\int_R^\infty r^2|K-K_{\rm ref}|\,dr
\le C\tau\frac{R^{1-2A}}{2A-1}.
\]
The same bound without \(\tau\) controls the weighted time derivative. Thus the angular moment after reference subtraction converges at infinity and may be differentiated on compact time intervals. Behavior at the axis remains a separate condition; this tail estimate alone does not prove convergence of an integral starting at zero.
