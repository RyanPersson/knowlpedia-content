+++
id = "proofs/grh/spanning-unfolding-b/good-forms-near-isometry"
title = "Good forms: the projected map is nearly an isometry"
kind = "theorem"
summary = "For a map P with amplitude blocks into a unitary representation, and central idempotents of the two factors whose complements have small coefficient at the identity, the projection e0 P is almost an isometry from below in mean square with error 5 b^(-4)."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.HasAmplitudeBlocks.isNearIsometry_piTensorElem_comp", "New.Filling.HasAmplitudeBlocks.hilbertSchmidtNorm_one_sub_piTensorElem_comp_sq_le", "New.Filling.HasAmplitudeBlocks.hilbertSchmidtNorm_asAlgebraHom_comp_sq_le"]
lean_files = ["src/New/Spanning/Unfolding/Moments.lean"]
proof_status = "full"
+++

**Theorem (good forms).** Let \(S\) be an [[proofs/grh/spanning-unfolding-b/filling-admissible|admissible]] [[proofs/grh/spanning-unfolding-b/filling-data|filling datum]] over a CM field \(E\) with [[?lean:New.WeilData|Weil data]], and \((\rho,P)\) a pair with [[proofs/grh/spanning-unfolding-b/amplitude-blocks|amplitude blocks]], \(\rho\) a unitary representation of \(\bar G=G_0\times G_1\) on a finite-dimensional space \(V\). Norms are Hilbert–Schmidt norms; elements of group algebras act on \(V\) through \(\rho\).

1. *(One prime.)* If \(x\) is a [[?lean:New.IsCentralProj|central idempotent]] of \(\mathbb{C}[G_i]\) with \(\operatorname{Re}x(1)\le b^{-8}/2\), then \(\lVert\rho(x)P\rVert^2\le2b^{-4}\dim_S\).
2. *(Both primes.)* Let \(g_0,g_1\) be central idempotents of \(\mathbb{C}[G_0]\), \(\mathbb{C}[G_1]\) with \(\operatorname{Re}(1-g_i)(1)\le b^{-8}/2\), and \(e_0=g_0\otimes g_1\in\mathbb{C}[\bar G]\) ([[?lean:New.piTensorElem|tensor product of group algebra elements]]). Then \(\lVert(1-\rho(e_0))P\rVert^2\le4b^{-4}\dim_S\).
3. *(Near isometry.)* Under the hypotheses of 2, \(\rho(e_0)P\) is [[?lean:New.IsNearIsometry|almost an isometry from below in mean square]] with error \(5b^{-4}\): for every subspace \(U\subset\mathcal{X}\) with orthogonal projection \(\mathrm{pr}_U\),
\[
\lVert\rho(e_0)P\,\mathrm{pr}_U\rVert^2\ge\dim U-5b^{-4}\dim_S .
\]

## Proof

(1) \(e=\rho(x)\) is an orthogonal projection ([[proofs/grh/spanning-unfolding-b/remainder-against-a-central-idempotent|central idempotents act as projections]]). Hence \(\lVert eP\rVert^2=\operatorname{tr}(P^*eP)=\operatorname{Re}\sum_tx(t)\operatorname{tr}P_{\phi_i(t)}\). Split \(P_s=r_\psi(s)+P'_s\):
\[
\lVert eP\rVert^2=\operatorname{Re}\sum_tx(t)\operatorname{tr}r_\psi(\phi_i(t))+\operatorname{Re}\operatorname{tr}P'_x,\qquad P'_x=\sum_tx(t)P'_{\phi_i(t)} .
\]
The first term is at most \(b^{-4}\dim_S\) by [[proofs/grh/spanning-unfolding-b/trace-against-a-small-central-idempotent|the trace against a small idempotent]]. For the second, \(\lvert\operatorname{tr}P'_x\rvert=\lvert\langle1,P'_x\rangle\rvert\le\lVert1\rVert\lVert P'_x\rVert\le\sqrt{\dim_S}\cdot\sqrt{b^{-12}\dim_S}\le b^{-4}\dim_S\), by the lemma on the remainder against a central idempotent.

(2) \(\rho(e_0)=e^{(0)}e^{(1)}\) with \(e^{(i)}=\rho(g_i)\), commuting orthogonal projections. For an orthogonal projection \(p\) and any \(q\): \(\lVert(1-pq)P\rVert^2\le\lVert(1-p)P\rVert^2+\lVert(1-q)P\rVert^2\) ([[?lean:New.hilbertSchmidtNorm_one_sub_mul_comp_sq_le|complement of a product]]). The complement \(1-g_i\) is again a central idempotent, so (1) gives \(\lVert(1-e^{(i)})P\rVert^2\le2b^{-4}\dim_S\).

(3) By [[proofs/grh/spanning-unfolding-b/second-moments-of-the-poincare-operators|the moment bounds]], \(\lVert P^*P-1\rVert^2\le b^{-12}\dim_S\le(b^{-4})^2\dim_S\), so \(P\) is almost an isometry with error \(b^{-4}\) ([[?lean:New.isNearIsometry_of_hilbertSchmidtNorm_le|near isometry from the Gram operator]]). Composing with the orthogonal projection \(\rho(e_0)\), whose complement satisfies (2), loses at most \(4b^{-4}\) more ([[?lean:New.IsNearIsometry.proj_comp|near isometries and projections]]).

## References

1. Lean: `New.Filling.HasAmplitudeBlocks.isNearIsometry_piTensorElem_comp`, `New.Filling.HasAmplitudeBlocks.hilbertSchmidtNorm_one_sub_piTensorElem_comp_sq_le`, `New.Filling.HasAmplitudeBlocks.hilbertSchmidtNorm_asAlgebraHom_comp_sq_le` in `src/New/Spanning/Unfolding/Moments.lean`.
