+++
id = "proofs/grh/upper-divisibility/only-collisions-lose"
title = "Only collisions lose: the divisibility bound is at least the gain"
kind = "theorem"
summary = "At a small non-split prime the divisibility bound of each stage is at least gain/m, less the collision sum and an error f a (log b)^2/(m p), plus a surplus for removed long rows."
aliases = ["only collisions lose"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.le_divisibilityBound", "New.Data.localPrimeSum_add_le_mul_tsum_partnerTerm_add", "New.Data.posPart_sub_weight_le_posPart_longRow", "New.Data.mul_posPart_weight_le", "New.Data.sub_le_predictedDivisibility", "New.Data.min_longRow_add_lowColumns_add_min_lowBoxes_le", "New.Data.gammaPrime_mul_lowColumns_le", "New.Data.lowColumns_lowBoxes_bounds", "New.Data.lowColumns_le", "New.Data.lowBoxes_le", "New.Data.mul_weight_le_lowBoxes", "New.Data.one_add_logb_boxes_le", "New.Data.boxes_sub_boxes_eraseHeightOne", "New.Data.boxes_eq_aPlaces_add_low", "New.Data.summable_partnerTerm"]
lean_files = ["src/New/UpperBound/Divisibility/JetExponent.lean"]
proof_status = "outline"
+++

**Theorem.** Let \(D\) be [[?lean:New.Data|admissible data]], \(p\) a prime with \(p<x_1\) and \(\chi_K(p)\ne1\), \(j<m\), and \(S\) a finite set of infinite places of \(E\). Then
\[
\frac{\operatorname{gain}(p)}{m}-\operatorname{coll}_p(S)+v(\pi_p)\,\lvert\Phi_a\cap S\rvert\,\frac{a}{x_1}-\frac{f(\log b)^2}{m}\cdot\frac ap\;\le\;\operatorname{db}_{p,j}(S),
\]
where \(\operatorname{gain}\) is the [[proofs/grh/upper-divisibility/gain|gain]], \(\operatorname{coll}_p(S)\) the [[proofs/grh/upper-divisibility/collisions|collision sum outside \(S\)]] and \(\operatorname{db}\) the [[proofs/grh/upper-divisibility/divisibility-bound|divisibility bound]].

## Proof

Notation \(L,c_j,l_j,T,\gamma_p,v=v(\pi_p)\in\{\tfrac12,1\}\) as in the definition of the divisibility bound; \(w\) is the weight, \(\tau'=\tau^{(e)}=u(-p^{e})\tau\), and \(u_0=a/(pm)\).

*Step 0 (sizes of the low part; quoted comparisons).* For \(j<m\) and every place \(\sigma\):
\[
k\,w(\sigma)\le l_j(\sigma)\le k\,w(\sigma)+x^{60},\qquad c_j(\sigma)\le w(\sigma)+x^{60}.
\]
The lower bound holds because the \(c(\sigma,k)\ge w(\sigma)\) columns of height \(k\) alone have \(k\,c(\sigma,k)\) boxes. The upper bounds follow from \(c(\sigma,h)\le\kappa_1(\sigma)[h=k]+\Delta\) for \(h\ne1\) ([[?lean:New.Data.columnCount_le|`columnCount_le`]]), \(\kappa_1(\sigma)\le w(\sigma)+{}\)(small), and size comparisons of the data proved by [[?lean:New.Data.le_of_hasLogBound|`le_of_hasLogBound`]]; these comparisons are quoted, as are the further ones marked (q) below.

*Step 1 (one place, one exponent).* Let \(e\in I_p\) and \(\tau\in\Phi\).

(a) *Long rows.* If \(\tau\in\Phi_a\),
\[
\Bigl(\frac a{p^{e}}-w(\tau')\Bigr)^{+}+[e=1,\ \tau\in S]\frac a{x_1}\le\Bigl(\frac{L(\tau)}{p^{e}}-L(\tau')-c_j(\tau')\Bigr)^{+}+[\tau\in S]\frac a{p^{e}}+[(\tau,e)\text{ collision}]\frac a{p^{e}}+x^{60}.
\]
Indeed, if \(\tau\in S\): as \(w(\tau')\ge a/x_1\) and \(p\le x_1\), the left side is at most \(a/p^{e}\) (if the positive part is positive it is at most \(a/p^{e}-a/x_1\); if it is zero and \(e=1\), \(a/x_1\le a/p\)). If \(\tau\notin S\) then \(L(\tau)=a\); either \(\tau'\in\Phi_a\setminus S\), a collision, and the left side is at most \(a/p^{e}\); or \(L(\tau')=0\) and \(c_j(\tau')\le w(\tau')+x^{60}\) by Step 0.

(b) *Low boxes.* For \(z>0\): \(k\bigl(w(\tau)/z-w(\tau')\bigr)^{+}\le\bigl(l_j(\tau)/z-l_j(\tau')\bigr)^{+}+x^{60}\), by Step 0.

Adding (a) and (b) with \(z=p^{e}\) and inserting \(\pm c_j(\tau)/p^{e}\):
\[
[\tau\in\Phi_a]\Bigl(\frac a{p^{e}}-w(\tau')\Bigr)^{+}+k\Bigl(\frac{w(\tau)}{p^{e}}-w(\tau')\Bigr)^{+}+[e=1,\tau\in\Phi_a\cap S]\frac a{x_1}
\le T(\tau,e)+\frac{c_j(\tau)+[\tau\in\Phi_a\cap S]a}{p^{e}}+[\text{collision}]\frac a{p^{e}}+2x^{60}.
\]
If \(p^{e}\ge x_1\) the left side is \(0\) (every weight is at least \(a/x_1\), and \(e\ne1\)), while \(T(\tau,e)+c_j(\tau)/p^{e}\ge0\); so the term \(2x^{60}\) is needed only for the fewer than \(\lceil\log_p\lceil x_1\rceil\rceil\) exponents with \(p^{e}<x_1\). For \(e\notin I_p\) both sides vanish except for nonnegative terms on the right (note \(1\in I_p\) as \(p\) is non-split).

*Step 2 (sum over \(e\)).* All series converge (terms are \(O(p^{-e})\)). Summing Step 1 over \(e\), multiplying by \(v\), and using \(v\sum_{e\in I_p}p^{-e}=\gamma_p\):
\[
[\tau\in\Phi_a]s_p(a,\tau)+k\,s_p(w(\tau),\tau)+v[\tau\in\Phi_a\cap S]\frac a{x_1}
\le v\sum_eT(\tau,e)+\gamma_p\bigl(c_j(\tau)+[\tau\in\Phi_a\cap S]a\bigr)+v\!\!\sum_{e:\ \text{collision}}\frac a{p^{e}}+v\lceil\log_p\lceil x_1\rceil\rceil2x^{60}.
\]
Now \(\gamma_pc_j(\tau)\le\frac2p\bigl(w(\tau)+x^{60}\bigr)\le u_0\) (q), \(v\lceil\log_p\lceil x_1\rceil\rceil2x^{60}\le u_0\) (q), and \(v\le1\).

*Step 3 (sum over \(\tau\)).* Summing over the \(f\) places,
\[
\frac{\operatorname{gain}(p)}m+v\lvert\Phi_a\cap S\rvert\frac a{x_1}\le v\sum_\tau\sum_eT(\tau,e)+\gamma_p\,a\lvert\Phi_a\cap S\rvert+\operatorname{coll}_p(S)+2fu_0.
\]

*Step 4 (the predicted divisibility).* By definition \(\operatorname{pd}_{p,j}(S)=v\sum_{\tau,e}T(\tau,e)\) minus, if \(p=d\), a correction. For \(p=d\) and \(\tau^{(0)}=u(-1)\tau\): \(\tau\) and \(\tau^{(0)}\) have different classes modulo \(q_0\), so they are not both a-places, and not both b-places (b-places have class \(-1\)). Hence \(\min(L(\tau),L(\tau^{(0)})+c_j(\tau^{(0)}))\), \(c_j(\tau)\) and \(\min(l_j(\tau),l_j(\tau^{(0)}))\) are each at most \(a/(dm)\) by Step 0 and (q) (away from the b-places \(l_j\le k\,a/x_1+x^{60}\)). So the correction is at most \(\tfrac12f\cdot3a/(dm)\le2fu_0\), and in all cases
\[
v\sum_\tau\sum_eT(\tau,e)-2fu_0\le\operatorname{pd}_{p,j}(S).
\]

*Step 5 (conclusion).* The removed boxes are \(B-B'=a\lvert\Phi_a\cap S\rvert\), and \(n_{j+1}^3\bigl(1+\log_p\max(B,1)\bigr)\le n_{j+1}^{3}(\log b)^2\le u_0\) (q; here \(B\le fa+fM+1\) and \(\log p\ge\tfrac12\)). Therefore
\[
\frac{\operatorname{gain}(p)}m+v\lvert\Phi_a\cap S\rvert\frac a{x_1}-\operatorname{coll}_p(S)\le\operatorname{db}_{p,j}(S)+5fu_0,
\]
and \(5fu_0\le f(\log b)^2a/(pm)\) since \((\log b)^2\ge5\). \(\blacksquare\)

*Status.* The structure and every inequality between the displayed quantities was checked against the Lean proof. The numerical comparisons marked (q), all of the form "a polynomial in the small scales is below \(a/(pm)\)" and discharged in Lean by `le_of_hasLogBound`, are asserted.

## References

1. Lean: `New.Data.le_divisibilityBound` and the lemmas listed in the front matter, in `src/New/UpperBound/Divisibility/JetExponent.lean`.
