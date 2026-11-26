+++
id = "proofs/grh/spanning-unfolding-a/unit-sphere-mass"
title = "Mass of the unit sphere at an infinite place"
kind = "definition"
summary = "The number sph_l = (2 pi)^l / (|varpi|_v^(l-1/2) (l-1)!) attached to a rank l and an infinite place v."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.unitSphereMass", "New.Data.unitSphereMass_pos", "New.Data.one_le_inv_unitSphereMass", "New.Data.inv_unitSphereMass_le_pow", "New.Data.log_prod_unitSphereMass", "New.Data.abs_log_prod_unitSphereMass_sub_le"]
lean_files = ["src/New/Spanning/Unfolding/FrameMass.lean"]
+++

Let \(D\) be [[?lean:New.Data|admissible data]] with [[?c:CM field|CM field]] \(E\), and let \(\varpi\) be the [[?lean:New.Parameters.deltaE|generator of the different]] of \(E\). For an integer \(l\ge 0\) and an [[?c:Infinite place of a number field|infinite place]] \(v\) of \(E\), the **mass of the unit sphere** of rank \(l\) at \(v\) is the positive real number
\[
\operatorname{sph}_l(v)=\frac{(2\pi)^l}{\lvert\varpi\rvert_v^{\,l-1/2}\,(l-1)!},
\]
where \(\lvert\varpi\rvert_v\) is the complex absolute value of \(\varpi\) at \(v\) and, for \(l=0\), \((l-1)!\) is read as \(0!=1\) (so \(\operatorname{sph}_0(v)=\lvert\varpi\rvert_v^{1/2}\)).

## Remarks

For \(l\ge1\) this is the total mass of the unit sphere \(\{y\in\mathbb{C}^l:\langle y,y\rangle=1\}\) for the fibre measure \(dy/d\langle y,y\rangle\), when \(\mathbb{C}\) carries \(2/\lvert\varpi\rvert_v\) times and \(\mathbb{R}\) carries \(\lvert\varpi\rvert_v^{-1/2}\) times [[?c:Lebesgue measure|Lebesgue measure]]: with standard Lebesgue measures the sphere has fibre mass \(\pi^l/(l-1)!\), and the normalisations contribute \((2/\lvert\varpi\rvert_v)^l\cdot\lvert\varpi\rvert_v^{1/2}\). This interpretation is a comment of the source; only the formula is used.

## Properties

Let \(f\) be the number of infinite places of \(E\), \(\mathrm{rd}_E\) its [[?c:Root discriminant|root discriminant]], \(x\) and \(b\) the scales and \(k\le r=k+2\varrho+1\) the ranks of the data. Write \(w=\lvert\varpi\rvert_v\).

1. **Positivity.** \(\operatorname{sph}_l(v)>0\), because \(\varpi\ne0\).
2. **At most one.** If \(l\ge1\) then \(\operatorname{sph}_l(v)\le 1\). Indeed the size calculus of the data ([[?lean:New.Data.le_of_hasLogBound|comparison of logarithmic bounds]]) gives \(w\ge1\) and \(2\pi\le\sqrt w\); hence \((2\pi)^l\le w^{l/2}\le w^{l-1/2}\le w^{l-1/2}(l-1)!\), using \(l/2\le l-1/2\).
3. **Lower bound.** If \(l\le r\) then \(\operatorname{sph}_l(v)^{-1}\le x^{18l}\). Indeed \(\operatorname{sph}_l(v)^{-1}=w^{l-1/2}(l-1)!/(2\pi)^l\le w^{l-1/2}(l-1)!\le w^l r^l\), because \(w\ge1\) and \((l-1)!\le l!\le l^l\le r^l\); and \(w\,r\le x^{18}\) by the size calculus.
4. **Product over the places.** For every \(i\ge0\),
\[
\log\prod_{v}\operatorname{sph}_{i+1}(v)=-f\Bigl(\bigl(i+\tfrac12\bigr)\log \mathrm{rd}_E+\log i!-(i+1)\log(2\pi)\Bigr).
\]
This follows from the definition and the identity \(\prod_v\lvert\varpi\rvert_v=\mathrm{rd}_E^{\,f}\) ([[?lean:New.Parameters.prod_deltaE_eq_rootDiscr_pow|product of the absolute values of the generator of the different]]; its square is the absolute norm of the different, which is the absolute value of the [[algebra-fields-galois/number-field-discriminant|discriminant]]).
5. **Comparison with masses.** Let \(\operatorname{mass}_l\) be the [[?lean:New.mass|mass]] of the genus of the standard hermitian lattice \(\mathcal{O}_E^l\). For \(i\ge k\),
\[
\Bigl\lvert \log\prod_v\operatorname{sph}_{i+1}(v)-\bigl(\log\operatorname{mass}_i-\log\operatorname{mass}_{i+1}\bigr)\Bigr\rvert\le \frac{2}{2^{\varrho}} .
\]
By item 4 this is the [[?lean:New.abs_log_mass_ratio_sub_le|approximate mass formula for consecutive ranks]] applied with \(j=i\) and \(u=\varrho\); its hypotheses \(8f\le2^\varrho\) and \(4\varrho+12\le k\le i\) hold by the size calculus of the data.

## References

1. Lean: `New.Data.unitSphereMass`, `New.Data.unitSphereMass_pos`, `New.Data.one_le_inv_unitSphereMass`, `New.Data.inv_unitSphereMass_le_pow`, `New.Data.log_prod_unitSphereMass`, `New.Data.abs_log_prod_unitSphereMass_sub_le` in `src/New/Spanning/Unfolding/FrameMass.lean`.
2. The approximate mass formula is `New.abs_log_mass_ratio_sub_le` in `src/Lib/SiegelWeil/OneVector/SiegelClassSum.lean`, which refers to Shimura (1997) for the mass formula for unitary groups.
