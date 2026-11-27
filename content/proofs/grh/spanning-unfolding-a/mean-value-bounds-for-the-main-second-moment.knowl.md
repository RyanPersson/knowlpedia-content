+++
id = "proofs/grh/spanning-unfolding-a/mean-value-bounds-for-the-main-second-moment"
title = "Mean value bounds by the main second moment"
kind = "theorem"
summary = "Two products of group orders, class number, frame masses, dimensions and degrees are at most (1 + b^-9) times the main second moment."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.card_mul_prod_frameMass_le", "New.Data.card_mul_card_classes_mul_prod_le", "New.Data.card_sq_mul_mass_mul_prod_le", "New.Data.prod_frameMass_mul_div_eq", "New.Data.prod_unitSphereMass_mul_div_eq"]
lean_files = ["src/New/Spanning/Unfolding/FillingAdmissible.lean"]
proof_status = "full"
+++

**Theorem (mean values).** Let \(D\) be [[?lean:New.Data|admissible data]] with [[?lean:New.Data.filling|filling data]] \(S_D\). For an [[?c:Infinite place of a number field|infinite place]] \(v\) let \(\operatorname{fr}_v\) be the [[proofs/grh/spanning-unfolding-a/frame-mass|frame mass]], \(\operatorname{sph}_k(v)\) the [[proofs/grh/spanning-unfolding-a/unit-sphere-mass|sphere mass]] in rank \(k\), \(d_v\) and \(\deg_v\) the number of coordinates and the degree of the Bessel system, and \(c_v=\operatorname{fr}_vN^kd_v^2/(\operatorname{sph}_k(v)\deg_v)\). Let \(n_X\) be the number of classes, \(\bar H\) the reduction of \(U(X_0)\), and \(\mathcal M=(n_X\prod_vd_v)^2/(\operatorname{mass}_r\prod_v\deg_v)\) the [[?lean:New.Filling.mainSecondMoment|main second moment]]. Then

\[
\lvert\bar H\rvert\,n_X\prod_v\frac{\operatorname{fr}_vd_v^2}{\deg_v}\le(1+b^{-9})\,\mathcal M,\qquad\lvert\bar H\rvert^2\operatorname{mass}_k\prod_v\operatorname{sph}_k(v)\,c_v\le(1+b^{-9})\,\mathcal M .
\]

## Proof

Put \(Q=\bigl(\prod_v\operatorname{fr}_v\bigr)d^2/\deg\), with \(d=\prod d_v\), \(\deg=\prod\deg_v\); then \(\prod_v\operatorname{fr}_vd_v^2/\deg_v=Q\) and \(\prod_v\operatorname{sph}_k(v)c_v=N^{kf}Q\) (the sphere masses cancel). By the theorem on the [[proofs/grh/spanning-unfolding-a/number-of-classes-of-the-source-level|number of classes]], \(n_X=\lvert\bar H\rvert(N^k-1)^f\operatorname{mass}_k\) and \(\mathcal M=(\lvert\bar H\rvert(N^k-1)^f\operatorname{mass}_kd)^2/(\deg\operatorname{mass}_r)\).

*Second inequality.* Its left side is \(\lvert\bar H\rvert^2\operatorname{mass}_kN^{kf}Q\). A direct computation gives
\[
\lvert\bar H\rvert^2\operatorname{mass}_kN^{kf}Q=\Bigl(\prod_v\operatorname{fr}_v\Bigr)\operatorname{mass}_r\Bigl(\frac{N^k}{N^k-1}\Bigr)^{2f}\cdot\frac{\mathcal M}{N^{kf}\operatorname{mass}_k},
\]
and by the [[proofs/grh/spanning-unfolding-a/product-of-frame-masses-upper-bound|upper bound for the product of the frame masses]] the first three factors are at most \((1+b^{-9})N^{kf}\operatorname{mass}_k\).

*First inequality.* Its left side is \(\lvert\bar H\rvert^2\operatorname{mass}_k(N^k-1)^fQ\le\lvert\bar H\rvert^2\operatorname{mass}_kN^{kf}Q\), which is the left side of the second.

## References

1. Lean: `New.Data.card_mul_prod_frameMass_le` in `src/New/Spanning/Unfolding/FillingAdmissible.lean`.
2. Lean: `New.Data.card_mul_card_classes_mul_prod_le` in `src/New/Spanning/Unfolding/FillingAdmissible.lean`.
3. Lean: `New.Data.card_sq_mul_mass_mul_prod_le` in `src/New/Spanning/Unfolding/FillingAdmissible.lean`.
4. Lean: `New.Data.prod_frameMass_mul_div_eq` in `src/New/Spanning/Unfolding/FillingAdmissible.lean`.
5. Lean: `New.Data.prod_unitSphereMass_mul_div_eq` in `src/New/Spanning/Unfolding/FillingAdmissible.lean`.
