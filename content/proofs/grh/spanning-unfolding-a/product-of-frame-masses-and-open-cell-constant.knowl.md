+++
id = "proofs/grh/spanning-unfolding-a/product-of-frame-masses-and-open-cell-constant"
title = "The product of the frame masses in terms of the Siegel constant and the open cell constant"
kind = "theorem"
summary = "An exact identity relating the product of the frame masses, the open-cell constant c_G, the discriminant, the Siegel constant c_S and vol(O-hat)."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.prod_frameMass_mul_openCellConst_eq", "New.Data.log_openCellConst"]
lean_files = ["src/New/Spanning/Unfolding/FrameMass.lean"]
proof_status = "full"
+++

**Theorem.** Let \(D\) be [[?lean:New.Data|admissible data]] with field \(E\) (with \(f\) [[?c:Infinite place of a number field|infinite places]] and [[algebra-fields-galois/number-field-discriminant|discriminant]] \(\operatorname{disc}E\)), level prime \(N\), ranks \(k\le r=k+2\varrho+1\). Let

- \(\operatorname{fr}_v\) be the [[proofs/grh/spanning-unfolding-a/frame-mass|frame mass]] at the infinite place \(v\);
- \(c_G=\dfrac{\operatorname{vol}U(k)}{\operatorname{vol}U(r)}\cdot\dfrac{2\pi^k}{(k-1)!}\) be the [[?lean:New.Shape.openCellConst|open cell constant]], where \(\operatorname{vol}U(j)=\prod_{i=1}^{j}2\pi^{i}/(i-1)!\) is the [[?lean:New.volU|volume of the compact unitary group]] \(U(j)\);
- \(c_S=\Bigl(\dfrac{\pi^k}{(k-1)!\,N^k}\Bigr)^{f}\lvert\operatorname{disc}E\rvert^{1/4}\operatorname{vol}(\widehat{\mathcal O})^{k}\) be the [[?lean:New.Filling.siegelConst|Siegel constant]] of the [[?lean:New.Data.filling|filling data of \(D\)]];
- \(\operatorname{vol}(\widehat{\mathcal O})=(2/\mathrm{rd}_E)^f\) be the [[?lean:New.volÔ|volume of the integral finite adeles]], \(\mathrm{rd}_E\) the [[?c:Root discriminant|root discriminant]].

Then
\[
\Bigl(\prod_v\operatorname{fr}_v\Bigr)\,c_G^{\,f}\,\lvert\operatorname{disc}E\rvert^{\varrho/2}
= c_S\,N^{2kf}\,\operatorname{vol}(\widehat{\mathcal O})^{\,\varrho+1+2\varrho(\varrho+k)} .
\]

## Proof

Both sides are positive, so it suffices to compare logarithms. Write \(\rho=\log\mathrm{rd}_E\); then \(\lvert\operatorname{disc}E\rvert=\mathrm{rd}_E^{2f}\) and \(\log\operatorname{vol}(\widehat{\mathcal O})=f(\log2-\rho)\).

*The open cell constant.* From the product formula for \(\operatorname{vol}U\), \(\operatorname{vol}U(r)=\operatorname{vol}U(k)\prod_{i=k}^{r-1}2\pi^{i+1}/i!\), so \(c_G=\bigl(\prod_{i=k}^{r-1}2\pi^{i+1}/i!\bigr)^{-1}2\pi^k/(k-1)!\) and, using that there are \(2\varrho+1\) indices with \(\sum(i+1)=(2\varrho+1)(k+\varrho+1)\),
\[
\log c_G=\log2+k\log\pi-\log(k-1)!+\sum_{i=k}^{r-1}\log i!-(2\varrho+1)\bigl(\log2+(k+\varrho+1)\log\pi\bigr).
\]

*Left side.* By property 3 of the [[proofs/grh/spanning-unfolding-a/frame-mass|frame mass]], the sums of \(\log i!\) cancel, and dividing by \(f\) the logarithm of the left side is
\[
k\log N+\bigl((2\varrho+1)(k+\varrho)+1\bigr)\log2+k\log\pi-\log(k-1)!-\bigl((2\varrho+1)(k+\varrho+\tfrac12)-\varrho\bigr)\rho .
\]

*Right side.* Dividing by \(f\), with \(e=\varrho+1+2\varrho(\varrho+k)\),
\[
k\log\pi-\log(k-1)!-k\log N+\tfrac12\rho+k(\log2-\rho)+2k\log N+e(\log2-\rho).
\]

Since \((2\varrho+1)(k+\varrho)+1=k+e\), the coefficients of \(\log2\) agree, and the coefficient of \(\rho\) is \(-(k+e-\tfrac12)\) on both sides; the remaining terms are identical. Hence the logarithms agree.

## References

1. Lean: `New.Data.prod_frameMass_mul_openCellConst_eq` in `src/New/Spanning/Unfolding/FrameMass.lean`.
2. Lean: `New.Data.log_openCellConst` in `src/New/Spanning/Unfolding/FrameMass.lean`.
