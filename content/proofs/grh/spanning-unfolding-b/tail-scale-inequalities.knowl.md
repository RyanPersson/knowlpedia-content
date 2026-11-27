+++
id = "proofs/grh/spanning-unfolding-b/tail-scale-inequalities"
title = "Inequalities for the tail scale"
kind = "lemma"
summary = "For an admissible filling datum, powers of b with exponent at most 10^5 n^9 f are at most the tail scale, its fourth power is b^(kf), and the main second moment is at least its 44th power times the identity second moment."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.pow_le_tailScale", "New.Filling.tailScale_pow_four", "New.Filling.tailScale_pow_mul_identitySecondMoment_le", "New.Filling.two_le_M", "New.Filling.two_le_b", "New.Filling.b_pos", "New.Filling.two_le_tailScale", "New.Filling.one_le_tailScale", "New.Filling.identitySecondMoment_nonneg", "New.Filling.mainSecondMoment_nonneg", "New.Filling.mul_sq_le_cube"]
lean_files = ["src/New/Spanning/Unfolding/Terms.lean"]
proof_status = "full"
+++

**Lemma.** Let \(S\) be an [[proofs/grh/spanning-unfolding-b/filling-admissible|admissible]] [[proofs/grh/spanning-unfolding-b/filling-data|filling datum]] with [[proofs/grh/spanning-unfolding-b/filling-constants|tail scale]] \(\tau=b^{kf/4}\), and \(n=\varrho+1\).

1. If \(e\le10^5n^9f\) is a natural number, then \(b^e\le\tau\). In particular \(\tau\ge b\ge2\).
2. \(\tau^4=b^{kf}\).
3. \(\tau^{44}\,\mathcal{M}_{\mathrm{id}}\le\mathcal{M}_{\mathrm{main}}\).
4. \(M\ge2\), \(\mathcal{M}_{\mathrm{id}}\ge0\), \(\mathcal{M}_{\mathrm{main}}\ge0\); and \(Cn^2\le n^3\) for every natural number \(C\le10^5\).

## Proof

(1) From \(1000(2\varrho+2)^9\le k\) we get \(k\ge1000\cdot2^9n^9\), so \(kf/4\ge128000\,n^9f\ge e\); as \(b\ge1\), \(b^e\le b^{kf/4}\). The case \(e=1\) gives \(\tau\ge b\ge1000\). (2) is the rule for powers, as \(b>0\). (3) By (2), \(\tau^{44}=b^{11kf}\), and the inequality is condition 6 of admissibility. (4) \(M\) is a product of two primes; \(\mathcal{M}_{\mathrm{id}}\) is a product of cardinalities; \(\mathcal{M}_{\mathrm{main}}\) is a square divided by the positive number \(\deg\cdot\operatorname{mass}(r)\); and \(n>\varrho\ge10^5\ge C\).

## References

1. Lean: `New.Filling.pow_le_tailScale`, `New.Filling.tailScale_pow_four`, `New.Filling.tailScale_pow_mul_identitySecondMoment_le` in `src/New/Spanning/Unfolding/Terms.lean`.
