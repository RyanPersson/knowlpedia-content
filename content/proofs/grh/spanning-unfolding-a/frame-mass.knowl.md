+++
id = "proofs/grh/spanning-unfolding-a/frame-mass"
title = "Mass of frames at an infinite place"
kind = "definition"
summary = "The number fr_v = N^k sph_{k+1} ... sph_r at an infinite place v, with its positivity, lower bound and logarithm."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.frameMass", "New.Data.frameMass_pos", "New.Data.inv_pow_le_frameMass", "New.Data.prod_frameMass_eq_mul_prod", "New.Data.log_prod_frameMass"]
lean_files = ["src/New/Spanning/Unfolding/FrameMass.lean"]
+++

Let \(D\) be [[?lean:New.Data|admissible data]] with level prime \(N\) and ranks \(k\le r\). For an [[?c:Infinite place of a number field|infinite place]] \(v\) of the field \(E\) of the data, the **frame mass** at \(v\) is
\[
\operatorname{fr}_v \;=\; N^{k}\prod_{i=k}^{r-1}\operatorname{sph}_{i+1}(v),
\]
where \(\operatorname{sph}_l(v)\) is the [[proofs/grh/spanning-unfolding-a/unit-sphere-mass|mass of the unit sphere]] of rank \(l\) at \(v\).

## Properties

Let \(f\) be the number of infinite places of \(E\), \(\mathrm{rd}_E\) the [[?c:Root discriminant|root discriminant]], \(b\) and \(x\) the scales of the data and \(\varrho\) the number of hyperbolic planes, so that \(r=k+2\varrho+1\) (from \(r+1=k+m\) and \(m=2\varrho+2\)); in particular there are \(2\varrho+1\) integers \(i\) with \(k\le i<r\), and their sum is \((2\varrho+1)(k+\varrho)\).

1. **Positivity.** \(\operatorname{fr}_v>0\).
2. **Lower bound.** \(\operatorname{fr}_v\ge b^{-(\varrho+1)r}\). Each of the \(2\varrho+1\) factors satisfies \(\operatorname{sph}_{i+1}(v)\ge x^{-18(i+1)}\ge x^{-18r}\) (property 3 of the sphere mass and \(x\ge1\)), and \(N^k\ge1\); so \(\operatorname{fr}_v\ge x^{-18r(2\varrho+1)}\ge x^{-36(\varrho+1)r}\ge b^{-(\varrho+1)r}\), the last step because \(x^{36}\le b\) by the size calculus of the data ([[?lean:New.Data.le_of_hasLogBound|comparison of logarithmic bounds]]).
3. **Product over the places.** \(\prod_v\operatorname{fr}_v=N^{kf}\prod_{i=k}^{r-1}\prod_v\operatorname{sph}_{i+1}(v)\), and therefore, by property 4 of the sphere mass,
\[
\log\prod_v\operatorname{fr}_v=f\Bigl(k\log N-\sum_{i=k}^{r-1}\log i!+(2\varrho+1)\bigl((k+\varrho+1)\log(2\pi)-(k+\varrho+\tfrac12)\log\mathrm{rd}_E\bigr)\Bigr).
\]
Here one uses \(\sum_{k\le i<r}(i+\tfrac12)=(2\varrho+1)(k+\varrho+\tfrac12)\) and \(\sum_{k\le i<r}(i+1)=(2\varrho+1)(k+\varrho+1)\).

## References

1. Lean: `New.Data.frameMass`, `New.Data.frameMass_pos`, `New.Data.inv_pow_le_frameMass`, `New.Data.prod_frameMass_eq_mul_prod`, `New.Data.log_prod_frameMass` in `src/New/Spanning/Unfolding/FrameMass.lean`.
