+++
id = "proofs/grh/spanning-core/bad-types-are-rare"
title = "Bad types are rare"
kind = "theorem"
summary = "The good idempotent is a tensor product of two central idempotents, one for each level prime, whose complements have a small coefficient at the identity."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.bad_types_rare", "New.Data.goodIdempotentAbove", "New.Data.isCentralProj_goodIdempotentAbove", "New.Data.levelRepresentation_goodIdempotentAbove_eq", "New.Data.re_coeff_one_sub_goodIdempotentAbove_le"]
lean_files = ["src/New/Spanning/SecondMoment/SpanningTheorem.lean"]
proof_status = "outline"
+++

Let \(D\) be [[?lean:New.Data|admissible data]]. For \(i\in\{0,1\}\) let \(G_i=\prod_{w\mid p_i}\mathrm{GL}_r(\mathbb{F}_w)\), the product over the chosen places above the level prime \(p_i\), and define the **good idempotent above \(p_i\)**
\[
e_{p_i}=\sum_{c}\ \bigotimes_{w\mid p_i}e_{c_w}\ \in\ \mathbb{C}[G_i],
\]
the sum over the [[?lean:New.goodTuples|good tuples]] \(c=(c_w)_w\) of labels (each \(c_w\) a [[?lean:New.IsLabel|label]] of degree \(r\) over \(\mathbb{F}_w\) with no \(q_2\)-th root of unity of \(\mathbb{F}_w\) as a root, at least one \(c_w\) primitive), where \(\bigotimes_we_{c_w}\) is the [[?lean:New.tupleIdem|tuple idempotent]] built from the [[?lean:New.labelIdem|label idempotents]].

**Theorem (bad types are rare).**

1. Each \(e_{p_i}\) is a [[?lean:New.IsCentralProj|central idempotent]] of \(\mathbb{C}[G_i]\) (an idempotent whose coefficient function is a [[algebra-groups/class-function|class function]]).
2. The [[?lean:New.piTensorElem|tensor product]] \(e_{p_0}\otimes e_{p_1}\in\mathbb{C}[G_0\times G_1]\) acts through the [[proofs/grh/spanning-core/scaled-poincare-map|level representation]] as the [[?lean:New.Data.e₀|good idempotent \(e_0\)]] acts through \(\rho\).
3. For \(i=0,1\), the coefficient of \(1-e_{p_i}\) at the identity satisfies \(\operatorname{Re}\,(1-e_{p_i})(1)\le\tfrac12b^{-8}\), where \(b\) is the scale [[?lean:New.Data.b|\(b\)]] of the data.

## Proof

(1) is `New.isCentralProj_sum_tupleIdem` (Lean statement: a sum of distinct tuple idempotents is a central idempotent).

(2) Both elements have the same coefficients: the coefficient of \(e_{p_0}\otimes e_{p_1}\) at \((s_0,s_1)\) is the product of the coefficients, hence the sum over pairs of good tuples \((c^0,c^1)\) of \(\prod_i\prod_{w\mid p_i}e_{c^i_w}(s_{i,w})\); and \(e_0\) is by definition the sum over the [[?lean:New.Data.goodTupleFamilies|good families]], which are exactly such pairs, of the same products. The two groups are identified by sorting the chosen places by the prime below them, which is how the level representation is defined.

(3) *Outline.* Apply the estimate [[?lean:New.re_coeff_one_sub_sum_tupleIdem_le|`New.re_coeff_one_sub_sum_tupleIdem_le`]] (area of `New/Spanning/MainTerm/BadTypes`): for \(f\) fields with \(q\) elements, \(1<r<q\), \((1+M+2r)/q\le\varepsilon\le1\) and \(2r(2r\log q+1)L\le f\), the real part of the coefficient at \(1\) of one minus the sum of the good tuple idempotents is at most \(f\varepsilon+e^{-L}\). Here \(q=p_i\) (each residue field at a chosen place above \(p_i\) has \(p_i\) elements), the number of chosen places above \(p_i\) is the number \(f\) of infinite places of \(E\), \(M=q_2\), \(\varepsilon=(1+q_2+2r)/p_i\) and \(L=9\log b\). The four numerical conditions and the final inequality \(f\varepsilon+b^{-9}\le\tfrac12b^{-8}\) are instances of the size inequalities of the data (`New.Data.le_of_hasLogBound`), which we do not reproduce. \(\blacksquare\)

## References

1. Lean: `New.Data.bad_types_rare` and its three parts in `src/New/Spanning/SecondMoment/SpanningTheorem.lean`.
