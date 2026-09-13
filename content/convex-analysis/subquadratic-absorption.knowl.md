+++
id = "convex-analysis/subquadratic-absorption"
title = "Absorbing a subquadratic power"
kind = "theorem"
summary = "A power below two can be bounded by any positive multiple of the square plus a controlled constant."
aliases = ["Young inequality with epsilon", "absorption by dissipation"]
domains = ["convex-analysis"]
section_mode = "progressive"
prerequisites = ["convex-analysis/youngs-inequality", "real-analysis/real-power"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For \(0<\alpha<2\), \(A,b\ge0\), and \(\delta>0\),
\[
bA^\alpha\le\delta A^2+C_\alpha\delta^{-\alpha/(2-\alpha)}b^{2/(2-\alpha)}.
\]
This is a **subquadratic absorption estimate**, a rescaled form of [[convex-analysis/youngs-inequality|Young's inequality]].

## Derivation and radius factors

Apply Young with conjugate exponents \(2/\alpha\) and \(2/(2-\alpha)\), rescaling the two factors so the first term is \(\delta A^2\). Equivalently, maximize \(bA^\alpha-\delta A^2\) over \(A\ge0\). If \(b=R^{-1}\) and \(\alpha=3/2\), the remainder is \(C_\delta R^{-4}\). The strict inequality \(\alpha<2\) is what permits an arbitrarily small coefficient in front of \(A^2\).
