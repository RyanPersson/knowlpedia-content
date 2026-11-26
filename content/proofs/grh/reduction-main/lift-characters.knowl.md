+++
id = "proofs/grh/reduction-main/lift-characters"
title = "The characters of the lifts"
kind = "definition"
summary = "The characters mu_j^0 of U(1) of weight -kappa_j, their twists mu_j^0 theta, and the character mu_j^0 theta^j used for lift j of a chain."
aliases = ["untwistedLiftChar", "liftChar", "liftTamePart", "chainChar"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.untwistedLiftChar", "New.Data.untwistedLiftChar_hasWeight", "New.Data.liftChar", "New.Data.liftTamePart", "New.Data.hasWeight_liftChar", "New.Data.chainChar"]
lean_files = ["src/New/Reduction/Data/LevelAndTwists.lean"]
+++

Let \(D\) be [[proofs/grh/reduction-main/data|data]], with gap \(\Delta\) and lift weights \(\kappa_j=\kappa+(j+\tfrac12)\Delta\) ([[proofs/grh/reduction-main/data-derived-quantities|derived quantities]]). Three automorphic characters of \(\mathrm U(1)(\mathbb A)\) come from other chapters: [[?lean:New.Data.chiZero|\(\mu^\flat\)]] of weight \(-\kappa_0\) and trivial tame part; [[?lean:New.Data.chiM|\(\chi\)]] of weight \(0\) and tame part [[?lean:New.Data.chiMLocal|\(\omega\)]]; and the [[?lean:New.WeilData.upsilonU1|restricted splitting character \(\upsilon\)]] of weight \(1\) and trivial tame part. For \(j\ge0\) and a [[proofs/grh/reduction-main/twist|tame character]] \(\vartheta\) with tame part \(\psi\) define

- \(\mu_j^0:=\mu^\flat\cdot(\upsilon^{-\Delta}\chi)^j\), the **untwisted character of lift \(j\)**;
- \(\mu_j^0\vartheta\), the **character of lift \(j\) for \(\vartheta\)**, with tame part \(\omega^j\psi\);
- \(\mu_j^0\vartheta^j\), the **chain character**, used for lift \(j\) of a chain.

**Lemma.** \(\mu_j^0\) has weight \(-\kappa_j\) and tame part \(\omega^j\); \(\mu_j^0\vartheta\) has weight \(-\kappa_j\) and tame part \(\omega^j\psi\).

*Proof.* Weights add and tame parts multiply under products and powers of characters. \(\upsilon^{-\Delta}\chi\) has weight \(-\Delta\) and tame part \(\omega\); so \(\mu_j^0\) has weight \(-\kappa_0-j\Delta=-\kappa_j\) and tame part \(\omega^j\). Multiplying by \(\vartheta\) (weight \(0\), tame part \(\psi\)) gives the second claim. \(\square\)

## References

1. Lean: `New.Data.untwistedLiftChar`, `New.Data.untwistedLiftChar_hasWeight`, `New.Data.liftChar`, `New.Data.liftTamePart`, `New.Data.hasWeight_liftChar`, `New.Data.chainChar` in `src/New/Reduction/Data/LevelAndTwists.lean`.
