+++
id = "proofs/grh/derivatives-vacuum/loss-product"
title = "The loss product of consecutive integers"
kind = "definition"
summary = "The product B of n-sharp = ceil(6b/k) consecutive integers ending at l when l is at least n-sharp, whose valuation absorbs the losses at one place."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.lossProduct", "New.Data.lossFactorCount", "New.Data.lossProduct_ne_zero", "New.Data.padicValNat_factorial_lossFactorCount_le", "New.Data.padicValNat_factorial_le_add_lossProduct", "New.Data.lossFactorCount_div_sub_one_le", "New.Data.x_pow_le_lossFactorCount", "New.padicValNat_mono_of_dvd", "New.padicValNat_factorial_eq_div_add", "New.div_sub_one_le_padicValNat_factorial"]
lean_files = ["src/New/Derivatives/Sharpness/NearPairs.lean"]
+++

Let \(D\) be [[?lean:New.Data|admissible data]] with size parameters \(b\), \(k\). The **loss factor count** is \(n^\sharp=\lceil6b/k\rceil\). For \(l\in\mathbb{N}\) put \(l^-=\max(l-n^\sharp,0)\); the **loss product** is
\[ B(l)=(l^-+1)(l^-+2)\cdots(l^-+n^\sharp). \]

## Properties

For every prime \(p\), with \(v=v_p\):

1. \(v(n^\sharp!)\le v(B(l))\), since a product of \(n^\sharp\) consecutive integers is divisible by \(n^\sharp!\);
2. \(v(l!)\le v(l^-!)+v(B(l))\), since \(l!\) divides \((l^-+n^\sharp)!=l^-!\,B(l)\);
3. \(n^\sharp/p-1\le v(n^\sharp!)\le v(B(l))\) (the first term \(\lfloor n/p\rfloor\) of Legendre's formula);
4. \(x^{42}\le n^\sharp\) (a scale inequality of the data, verified by the magnitude calculus).

## References

1. Lean: `New.Data.lossProduct`, `New.Data.lossFactorCount`, `New.Data.lossProduct_ne_zero`, `New.Data.padicValNat_factorial_lossFactorCount_le`, `New.Data.padicValNat_factorial_le_add_lossProduct`, `New.Data.lossFactorCount_div_sub_one_le`, `New.Data.x_pow_le_lossFactorCount`, `New.padicValNat_mono_of_dvd`, `New.padicValNat_factorial_eq_div_add`, `New.div_sub_one_le_padicValNat_factorial` in `src/New/Derivatives/Sharpness/NearPairs.lean`.
