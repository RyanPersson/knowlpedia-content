+++
id = "asymptotics/laplaces-method"
title = "Laplace's method"
kind = "knowl"
summary = "Asymptotic evaluation of integrals dominated by a single interior maximizer of the exponent."
aliases = ["laplaces-method", "Laplace's method"]
domains = ["asymptotics"]
prerequisites = []
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
legacy_source_path = "asymptotics/laplaces-method.md"
+++

Laplace's method approximates integrals of the form
\[
I(n)=\int_a^b e^{n f(x)}\,g(x)\,dx
\]

for large \(n\), when the main contribution comes from a neighborhood of the point where \(f\) is maximal.

Let \(a<b\) be finite. Assume that \(f\in C^2([a,b])\) has a unique global maximizer \(x_0\in(a,b)\), that \(f''(x_0)<0\), and that \(g\) is continuous on \([a,b]\) with \(g(x_0)\ne 0\). Then, as \(n\to\infty\),

\[
\int_a^b e^{n f(x)}\,g(x)\,dx
\sim
e^{n f(x_0)}\,g(x_0)\,\sqrt{\frac{2\pi}{n\,|f''(x_0)|}}.
\]

## Why it works

Near \(x_0\), the second-order Taylor approximation is
\[
f(x) = f(x_0) + \tfrac12 f''(x_0)(x-x_0)^2 + \text{higher-order terms}.
\]

For large \(n\), the factor \(e^{n f(x)}\) is sharply peaked at \(x_0\). Replacing the exponent locally by its quadratic part yields the displayed Gaussian factor. More refined expansions require stronger smoothness and retain higher-order Taylor terms.

## Multidimensional version (informal)
For \(x\in\mathbb{R}^d\),
\[
I(n)=\int_{\Omega} e^{n f(x)} g(x)\,dx,
\]

if suitable global hypotheses hold and \(f\) has a unique interior maximizer \(x_0\) with negative-definite Hessian \(H=\nabla^2f(x_0)\), then the corresponding leading term is
\[
I(n)\sim e^{n f(x_0)}\,g(x_0)\,(2\pi/n)^{d/2}\,(\det(-H))^{-1/2}.
\]

## Common variants and caveats
- If the maximum occurs at an endpoint (\(x_0=a\) or \(x_0=b\)), the leading order usually changes, often to an \(n^{-1}\) scale rather than \(n^{-1/2}\).
- If there are multiple maximizers, the leading term is typically the sum of contributions from each (when they are well-separated and nondegenerate).
- If \(f''(x_0)=0\), the maximum is degenerate and the power of \(n\) depends on the first nonzero higher derivative.

## Where it shows up
- Normal approximations and local limit behavior.
- Large-\(n\) asymptotics of combinatorial sums via integral representations.
- As the real-variable building block for the complex steepest-descent/saddle-point techniques (see [[asymptotics/saddle-point-method|saddle-point-method]]).
