+++
id = "harmonic-analysis/double-riesz-kernel-three-dimensions"
title = "Kernel of a double Riesz transform in three dimensions"
kind = "theorem"
summary = "The Hessian of the Newtonian kernel represents a double Riesz transform with a diagonal identity term."
aliases = []
domains = ["harmonic-analysis"]
section_mode = "progressive"
prerequisites = ["harmonic-analysis/riesz-transform", "partial-differential-equations/newtonian-fundamental-solution-three-dimensions", "harmonic-analysis/principal-value-singular-integral", "functional-analysis/distributional-derivative", "linear-algebra/kronecker-delta"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

In three dimensions, the [[harmonic-analysis/riesz-transform|double Riesz transform]] satisfies, for a test function \(f\),
\[
R_iR_jf(x)=\operatorname{p.v.}\int_{\mathbb R^3}
\frac{3z_iz_j-\delta_{ij}|z|^2}{4\pi|z|^5}f(x-z)\,dz
-\frac{\delta_{ij}}3 f(x).
\]
Here \(\delta_{ij}\) is the Kronecker delta. In particular its off-diagonal kernel obeys \(|K_{ij}(z)|\le C|z|^{-3}\).

## Distributional Hessian

Differentiate \(\Gamma(z)=1/(4\pi|z|)\) twice outside zero. The displayed kernel results. Its angular mean is zero because the spherical average of \(z_iz_j/|z|^2\) is \(\delta_{ij}/3\), making the principal value converge for smooth inputs. Integration by parts across a small sphere contributes \(-\delta_{ij}\delta_0/3\) to \(\partial_i\partial_j\Gamma\). Fourier transformation yields the symbol \(-\xi_i\xi_j/|\xi|^2\), proving the formula. Summing \(i=j\) gives \(\sum_iR_i^2=-I\), which also checks the local term's sign.

## Operator bounds

The off-diagonal kernel and its first derivatives have the Calderón–Zygmund bounds. The Fourier symbol has absolute value at most one, giving \(L^2\) boundedness. The Calderón–Zygmund theorem therefore applies for \(1<p<\infty\).
