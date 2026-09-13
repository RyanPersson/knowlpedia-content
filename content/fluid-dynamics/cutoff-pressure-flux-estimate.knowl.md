+++
id = "fluid-dynamics/cutoff-pressure-flux-estimate"
title = "Cutoff pressure-flux estimate for a velocity difference"
kind = "theorem"
summary = "The pressure flux at a large radius is bounded by subquadratic powers of a localized L6 norm."
aliases = []
domains = ["fluid-dynamics"]
section_mode = "progressive"
prerequisites = ["fluid-dynamics/canonical-pressure-from-integrable-stress", "harmonic-analysis/double-riesz-kernel-three-dimensions", "harmonic-analysis/calderon-zygmund-lp-bound", "harmonic-analysis/scaled-cutoff-commutator-estimate", "functional-analysis/weighted-cutoff-sobolev-estimate", "measure-theory/lp-interpolation-inequality", "functional-analysis/local-sobolev-space", "linear-algebra/outer-product", "real-analysis/cutoff-function"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 2
+++

Let \(u\in L^2\cap L^6(\mathbb R^3)\), \(w\in L^2\cap H^1_{\mathrm{loc}}\), and \(g=w\otimes w+w\otimes u+u\otimes w\). Let \(\pi_*\) be its [[fluid-dynamics/canonical-pressure-from-integrable-stress|canonical pressure]]. For \(0\le\phi\le1\) smooth and compactly supported, put \(\phi_R(x)=\phi(x/R)\), \(\chi_R=\phi_R^8\), and \(B_R=\|\phi_R^4w\|_6\). If \(R\ge1\) and \(\|w\|_2+\|u\|_2+\|u\|_6\le M\), then
\[
\left|\int\pi_* w\cdot\nabla\chi_R\right|
\le C_{M,\phi}R^{-1}\left((B_R+1)B_R^{1/2}+R^{-3/4}B_R^{3/4}\right).
\]
The pressure is locally integrable for these inputs, and the pairing is well-defined.

## Local and commutator parts

For \(T_{ij}=R_iR_j\), write
\[
\phi_R^4\pi_* =\sum_{i,j}T_{ij}(\phi_R^4g_{ij})
+\sum_{i,j}[M_{\phi_R^4},T_{ij}]g_{ij}.
\]
The first sum has \(L^{3/2}\) norm at most \(C_M(B_R+1)\): use \(\|\phi_R^4w_iw_j\|_{3/2}\le B_R\|w\|_2\) and \(\|\phi_R^4w_i u_j\|_{3/2}\le\|w\|_2\|u\|_6\). The second has \(L^{4/3}\) norm at most \(C_MR^{-3/4}\). These identities extend from compact smooth approximations using \(L^1\) convergence of \(g\), the negative Sobolev pressure bound, and the commutator bound.

Since \(|\nabla\chi_R|\le C R^{-1}\phi_R^7\), it remains to pair these terms with \(\phi_R^3w\). Hölder interpolation gives \(\|\phi_R^3w\|_3\le B_R^{1/2}\|w\|_2^{1/2}\) and \(\|\phi_R^3w\|_4\le B_R^{3/4}\|w\|_2^{1/4}\), proving the estimate. Local integrability follows by choosing cutoffs equal to one on each compact set.
