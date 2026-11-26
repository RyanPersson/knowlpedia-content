+++
id = "proofs/grh/spanning-mainterm/bessel-coset-sum-is-kloosterman-sum"
title = "A sum of finite Bessel functions over cosets is a Kloosterman sum"
kind = "lemma"
summary = "The sum over cosets yK(M) of chi(y s^{-1}) conj chi(x^{-1} y) equals the Kloosterman sum of x at an integral point s."
aliases = ["tsum_extendedBesselChar_mul_star_extendedBesselChar"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Floors.PlaceData.tsum_extendedBesselChar_mul_star_extendedBesselChar", "New.Floors.PlaceData.unipotentCosets_eq_of_inv_mul_mem", "New.Floors.PlaceData.exists_out_inv_mul_mem", "New.Floors.PlaceData.inv_mul_mem_congruenceSubgroup_iff", "New.Floors.IntegralPlace.extendedBesselChar_eq_of_inv_mul_mem"]
lean_files = ["src/New/Spanning/MainTerm/KloostermanSum.lean"]
proof_status = "full"
+++

**Lemma.** In the setting of the
[[proofs/grh/spanning-mainterm/kloosterman-sum-at-finite-places|Kloosterman sum]] (unitary group
\(G\), Bessel unipotent group \(\mathsf U\), principal congruence subgroup \(K=K(M)\), finite
Bessel function \(\chi\)), let \(x\in G\) and let \(s\in G\) be an integral point. Fix a
representative \(\dot q\) of each coset \(q\in G/K\). Then

\[
  \sum_{q\in G/K}\chi(\dot q\,s^{-1})\,\overline{\chi(x^{-1}\dot q)}\;=\;\operatorname{Kl}_F(x,s).
\]

## Proof

We use three facts.

(a) \(\chi(zk)=\chi(z)\) for \(k\in K\)
([[?lean:New.Floors.IntegralPlace.extendedBesselChar_mul_of_mem_unitaryLevel|right invariance of the finite Bessel function]]),
and if \(\chi(z)\ne0\) then \(z\in\mathsf UK\)
([[?lean:New.Floors.IntegralPlace.exists_besselU_of_extendedBesselChar_ne_zero|support of the finite Bessel function]]).

(b) An integral point \(s\) normalises \(K\) (the principal congruence subgroup is normal in the
group of integral points), so \(s^{-1}z\in K\iff zs^{-1}\in K\).

(c) If the representatives of two unipotent cosets \(w,w'\) satisfy \(\dot w^{-1}\dot w'\in K\),
then \(w=w'\); and every \(y\in\mathsf UK\) lies in \(\dot wK\) for some unipotent coset \(w\).
Both are immediate from the definition of \(\mathsf U/(\mathsf U\cap K)\).

Consider the map \(\phi\colon(w,w')\mapsto x\dot w'K\) from the set \(P\) of pairs of unipotent
cosets with \(\dot w^{-1}x\dot w'\in sK\) to \(G/K\). We show that \(\phi\) is a bijection from
\(P\) onto a set containing the support of the left-hand sum and that it preserves the terms;
this identifies the two unconditional sums.

*Terms.* Let \((w,w')\in P\) and \(y=\dot q\) with \(q=x\dot w'K\). Then
\(\dot w'^{-1}x^{-1}y\in K\), so \(\chi(x^{-1}y)=\chi(\dot w')\) by (a). Moreover
\(s^{-1}\dot w^{-1}x\dot w'\in K\) and \((x\dot w')^{-1}y\in K\) give \(s^{-1}\dot w^{-1}y\in K\),
hence \(\dot w^{-1}ys^{-1}\in K\) by (b), so \(\chi(ys^{-1})=\chi(\dot w)\) by (a). Thus the term
of the left-hand side at \(q\) is \(\chi(\dot w)\overline{\chi(\dot w')}\).

*Injectivity.* If \(\phi(w_1,w_1')=\phi(w_2,w_2')\) then \(\dot w_1'^{-1}\dot w_2'\in K\), so
\(w_1'=w_2'\) by (c). Then \(\dot w_1^{-1}x\dot w_1's^{-1}\) and \(\dot w_2^{-1}x\dot w_1's^{-1}\)
both lie in \(K\) by (b), so \(\dot w_1^{-1}\dot w_2\in K\) and \(w_1=w_2\) by (c).

*Surjectivity onto the support.* Let \(q\) have a nonzero term and \(y=\dot q\). By (a),
\(ys^{-1}\in\mathsf UK\) and \(x^{-1}y\in\mathsf UK\), so by (c) there are unipotent cosets
\(w,w'\) with \(\dot w^{-1}ys^{-1}\in K\) and \(\dot w'^{-1}x^{-1}y\in K\). By (b) the first gives
\(s^{-1}\dot w^{-1}y\in K\); multiplying by the inverse of the second,
\(s^{-1}\dot w^{-1}x\dot w'\in K\), so \((w,w')\in P\), and \(x\dot w'K=yK=q\). \(\blacksquare\)

## References

1. Lean: `New.Floors.PlaceData.tsum_extendedBesselChar_mul_star_extendedBesselChar` and the
   auxiliary lemmas listed in the front matter, in
   `src/New/Spanning/MainTerm/KloostermanSum.lean`.
