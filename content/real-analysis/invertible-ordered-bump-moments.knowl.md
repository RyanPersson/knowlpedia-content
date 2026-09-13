+++
id = "real-analysis/invertible-ordered-bump-moments"
title = "Invertibility of moments on ordered bump supports"
kind = "theorem"
summary = "Distinct power weights paired with positive bumps on ordered disjoint intervals give an invertible moment matrix."
aliases = []
domains = ["real-analysis"]
section_mode = "progressive"
prerequisites = ["linear-algebra/moment-pairing-matrix", "real-analysis/zero-count-for-distinct-powers", "differential-geometry/bump-function", "linear-algebra/determinant", "measure-theory/fubinis-theorem", "topology/connected-set"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

Let \(\alpha_1,\ldots,\alpha_m\) be distinct real numbers, and let nonnegative nonzero smooth bumps \(\beta_j\) have supports in ordered disjoint compact intervals \(I_1<\cdots<I_m\subset(0,\infty)\). Then the [[linear-algebra/moment-pairing-matrix|moment matrix]]
\[
B_{ij}=\int x^{\alpha_i}\beta_j(x)\,dx
\]
is invertible.

## Proof

On \(0<x_1<\cdots<x_m\), the evaluation determinant \(\det[x_j^{\alpha_i}]\) never vanishes by the zero-count theorem. It has a constant sign on this connected region. Multilinearity of the determinant and Fubini's theorem give
\[
\det B=\int_{I_1\times\cdots\times I_m}
\det[x_j^{\alpha_i}]\prod_j\beta_j(x_j)\,dx_1\cdots dx_m.
\]
The integrand has one sign and is nonzero on a set of positive measure, proving the claim. Smoothly varying data on a compact parameter set give bounded inverse derivatives at each fixed order, provided the hypotheses hold throughout that set. This does not provide uniformity as exponents coalesce or supports lose their separation.

## Geometrically scaled copies

For \(\beta_j(x)=a_j^{-1}\beta_0(x/a_j)\) with \(a_j=e^{jd}\),
\[
\int x^p\beta_j(x)\,dx=\mu_p e^{jdp},\qquad
\mu_p=\int x^p\beta_0(x)\,dx>0.
\]
For distinct \(p\)'s, dividing the rows by \(\mu_p\) gives the transpose of a [[linear-algebra/vandermonde-matrix|Vandermonde matrix]] in the distinct nodes \(e^{dp}\), when \(d\ne0\). A narrow enough initial bump places finitely many such copies on ordered disjoint intervals within a prescribed positive radial patch.
