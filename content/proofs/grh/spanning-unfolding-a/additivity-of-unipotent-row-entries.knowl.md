+++
id = "proofs/grh/spanning-unfolding-a/additivity-of-unipotent-row-entries"
title = "Additivity of a row entry under right multiplication in the unipotent group"
kind = "lemma"
summary = "In the real Bessel unipotent group, the entry (e_a, j) of x u is the sum of those of x and u once the later coordinates of u vanish."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.besselU_mul_apply_eq_add", "New.Filling.rowCoords_mul_fst", "New.Filling.mul_apply_eStar_of_rowCoords"]
lean_files = ["src/New/Spanning/Unfolding/CutoffIntegral.lean"]
proof_status = "full"
+++

**Lemma.** Let \(\mathsf U\) be the [[?lean:New.Shape.Form.besselU|Bessel unipotent group]] of the real unitary group [[?lean:New.Shape.G₁|\(G_1\)]]: the [[?c:Isometry of a hermitian space|isometries]] of the [[?c:Hermitian form|hermitian form]] \(J\) on \(\mathbb C^{r}\) with basis \(e_1,\dots,e_\varrho\), a middle block (an orthonormal basis of \(X_0\) and a vector \(z\) with \(h(z,z)=-1\)), \(e_1^{*},\dots,e_\varrho^{*}\), \(h(e_a,e_a^{*})=1\), that are [[?c:Unitriangular matrix|block upper unitriangular]] for the levels \(\operatorname{level}(e_a)=a\), \(\operatorname{level}(\text{middle})=\varrho\), \(\operatorname{level}(e_a^{*})=2\varrho-a\). Call a position \((a,j)\) *free* if \(j\) is in the middle block, or \(j=e_b\) or \(j=e_b^{*}\) with \(b>a\) ([[?lean:New.RealPlace.IsFreeEntry|free entry]]).

Let \(x,u\in\mathsf U\), \(a\in\{1,\dots,\varrho\}\), and let \(j\) be a column with \(j=e_a^{*}\) or \((a,j)\) free. Assume:

1. for every \(b>a\), the entry \(u_{e_b,e_b^{*}}\) is real;
2. for every \(b\) with \(b>a\) or \(j=e_b^{*}\), and every free position \((b,k)\), \(u_{e_b,k}=0\).

Then \((xu)_{e_a,j}=u_{e_a,j}+x_{e_a,j}\).

## Proof

Since \(e_a\ne j\), it suffices to show \(\bigl((x-1)(u-1)\bigr)_{e_a,j}=\sum_k(x-1)_{e_a,k}(u-1)_{k,j}=0\). If \(\operatorname{level}(k)\le a\) then \((x-1)_{e_a,k}=0\) by unitriangularity. So let \(\operatorname{level}(k)>a\); we show \(u_{k,j}=\delta_{kj}\).

*Claim.* Let \(k\) be a row such that, if \(k=e_b\), then \(b>a\) or \(j=e_b^{*}\); and let \(l\) be a column that is not one of the \(e_d^{*}\). Then \(u_{k,l}=\delta_{kl}\). Indeed, if \(\operatorname{level}(l)\le\operatorname{level}(k)\) this is unitriangularity. Otherwise \(l\) has higher level than \(k\) and is \(e_{b'}\) or in the middle block, which forces \(k=e_b\) with \((b,l)\) free; then \(u_{k,l}=0\) by hypothesis 2.

If \(j\) is not an \(e_d^{*}\), the claim applies to \(k\) (if \(k=e_b\) then \(b>a\)) and gives \(u_{k,j}=\delta_{kj}\).

Let \(j=e_c^{*}\); then \(c=a\) or \(c>a\), and in both cases hypothesis 2 covers the row \(e_c\). Since \(u^{-1}=Ju^{*}J\), the \((k,e_c^{*})\) entry of \(u\,(Ju^{*}J)=1\) reads, after using the claim for the row \(e_c\) (whose entries outside the columns \(e_d^{*}\) are those of the identity),
\[
\sum_{d}u_{k,e_d}\,\overline{u_{e_c,e_d^{*}}}+u_{k,e_c^{*}}=\delta_{k,e_c^{*}},
\]
and by the claim \(u_{k,e_d}=\delta_{k,e_d}\). If \(k\) is in the middle block or \(k=e_d^{*}\), this gives \(u_{k,e_c^{*}}=\delta_{k,e_c^{*}}\). If \(k=e_d\) with \(d>a\), it gives \(\overline{u_{e_c,e_d^{*}}}+u_{e_d,e_c^{*}}=0\): for \(c>d\) the position \((d,e_c^{*})\) is free in a row \(d>a\), so \(u_{e_d,e_c^{*}}=0\); for \(c<d\) the position \((c,e_d^{*})\) is free in the row \(c\), so \(u_{e_c,e_d^{*}}=0\) and hence \(u_{e_d,e_c^{*}}=0\); for \(c=d\) the entry \(u_{e_d,e_d^{*}}\) is purely imaginary, and real by hypothesis 1 (as \(d>a\)), hence \(0\).

## Remarks

Two consequences are used for tuples \(u=(u_v)_v\), \(x=(x_v)_v\) over the [[?c:Infinite place of a number field|infinite places]], in terms of the [[proofs/grh/spanning-unfolding-a/row-coordinates-of-real-unipotent-group|row coordinates]]: if the free entries and the imaginary parts at \((e_d,e_d^{*})\) of \(u\) vanish in all rows \(d>a\), then the free entries of the row \(e_a\) of \(xu\) are the sums of those of \(u\) and \(x\); if moreover the free entries of the row \(e_a\) of \(u\) vanish, then \((xu)_{e_a,e_a^{*}}=u_{e_a,e_a^{*}}+x_{e_a,e_a^{*}}\).

## References

1. Lean: `New.Filling.besselU_mul_apply_eq_add` in `src/New/Spanning/Unfolding/CutoffIntegral.lean`.
2. Lean: `New.Filling.rowCoords_mul_fst` in `src/New/Spanning/Unfolding/CutoffIntegral.lean`.
3. Lean: `New.Filling.mul_apply_eStar_of_rowCoords` in `src/New/Spanning/Unfolding/CutoffIntegral.lean`.
