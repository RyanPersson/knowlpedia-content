+++
id = "complex-analysis/isolated-singularity-classification"
title = "Classification of isolated singularities"
kind = "theorem"
summary = "An isolated singularity is removable, a pole, or essential according to its Laurent principal part."
aliases = ["isolated singularity classification"]
domains = ["complex-analysis"]
prerequisites = ["complex-analysis/laurent-series"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(f\) be holomorphic on a punctured disc \(0<|z-a|<R\). Exactly one of the following occurs:

1. \(a\) is **removable**, when \(f\) extends holomorphically across \(a\);
2. \(a\) is a **pole**, when \(|f(z)|\to\infty\) as \(z\to a\);
3. \(a\) is **essential**, when it is neither removable nor a pole.

In the [[complex-analysis/laurent-series|Laurent expansion]], these cases correspond respectively to no negative terms, finitely many negative terms, and infinitely many negative terms.

This correspondence follows directly from the Laurent series. With no principal part the series converges at \(a\), giving a removable extension. If the principal part has largest exponent \(-m\), then \((z-a)^m f(z)\) extends holomorphically and is nonzero at \(a\), so \(f\) has a pole of order \(m\). An infinite principal part is neither of these, hence is essential; uniqueness makes the alternatives mutually exclusive.

## Analytic criteria

Riemann's removable singularity theorem says that local boundedness near \(a\) is enough for removability. A pole of order \(m\) is characterized by
\[
f(z)=(z-a)^{-m}g(z),\qquad g(a)\ne0.
\]
At an essential singularity, the [[complex-analysis/casorati-weierstrass-theorem|Casorati–Weierstrass theorem]] makes the image of every punctured neighborhood dense in \(\mathbb C\); the [[complex-analysis/great-picard-theorem|great Picard theorem]] is stronger.

## Meromorphic functions

A function is [[complex-analysis/meromorphic-function|meromorphic]] precisely when its isolated singularities are only poles. Essential singularities are therefore excluded from meromorphic behavior.

## References

1. John B. Conway, *Functions of One Complex Variable I*, 2nd ed., Springer, 1978. [Publisher record](https://doi.org/10.1007/978-1-4612-6313-5). Relevant: Chapter V, §§1–3.
