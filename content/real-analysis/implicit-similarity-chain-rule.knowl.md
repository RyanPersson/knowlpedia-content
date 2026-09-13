+++
id = "real-analysis/implicit-similarity-chain-rule"
title = "Chain rule in implicit anisotropic coordinates"
kind = "lemma"
summary = "Explicit time and axial derivatives of a rescaled profile in an implicitly defined chart."
aliases = []
domains = ["real-analysis"]
section_mode = "progressive"
prerequisites = ["real-analysis/implicit-anisotropic-coordinates", "real-analysis/chain-rule-multivariable", "real-analysis/product-rule"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

Use [[real-analysis/implicit-anisotropic-coordinates|implicit anisotropic coordinates]] \((q,X,\eta)\) with parameter \(d\), and write \(\tau=T-t\). For a smooth \(f(X,\eta)\) and a fixed \(b\in\mathbb R\), derivatives at fixed physical spatial coordinates satisfy
\[
\partial_t(q^bf)=\frac{q^{b-1}}{L}
\left(-bf+d\eta f_\eta+Xf_X\right),
\]
\[
\partial_z(q^bf)=\frac{q^{b-d}}{L}
\left(2b\eta f+(1-\eta^2)f_\eta-2\eta Xf_X\right).
\]

## Derivation

Implicit differentiation gives \(q_\tau=1/L\) and \(q_z=2\eta q^{1-d}/L\). Consequently \(\eta_t=d\eta/(qL)\), \(X_t=X/(qL)\), \(\eta_z=q^{-d}(1-\eta^2)/L\), and \(X_z=-2\eta Xq^{-d}/L\). Substitute these identities into the product and chain rules. The positive lower bound on \(L\) prevents a denominator singularity away from \(q=0\).
