+++
id = "complex-analysis/three-lines-theorem"
title = "Hadamard three-lines theorem"
kind = "theorem"
summary = "A holomorphic function on a vertical strip is bounded by geometric interpolation of its boundary bounds."
domains = ["complex-analysis"]
section_mode = "progressive"
prerequisites = ["complex-analysis/maximum-modulus-principle"]
+++

Let \(a<b\). Suppose \(f\) is bounded and continuous on \(a\le\Re z\le b\) and holomorphic in the interior. Write \(M_x=\sup_{t\in\mathbb R}|f(x+it)|\). Then for \(0<\theta<1\),
\[
 M_{(1-\theta)a+\theta b}\le M_a^{1-\theta}M_b^\theta .
\]

## Proof idea

Normalize \(f\) by an exponential so its two boundary bounds are one. Apply the [[complex-analysis/maximum-modulus-principle|maximum modulus principle]] on finite rectangles after a small damping factor suppresses the horizontal edges. Let the rectangles grow and remove the damping.

## References

- [Lib/Analytic/QuadraticTwist.lean](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/QuadraticTwist.lean)
