+++
id = "proofs/grh/spanning-unfolding-b/bounds-for-near-terms"
title = "Bounds for the frame products of near terms"
kind = "lemma"
summary = "For an admissible filling datum, nearness is preserved by unipotent elements fixing the frame, and the frame products and leading minors of a near term are bounded by explicit powers of b at every infinite place."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.IsNear.norm_frameProducts_le", "New.Filling.IsNear.norm_map_leadingMinor_sq_le", "New.Filling.IsNear.mul_of_mem_besselU0"]
lean_files = ["src/New/Spanning/Unfolding/Terms.lean"]
proof_status = "full"
+++

**Lemma.** Let \(S\) be a [[proofs/grh/spanning-unfolding-b/filling-data|filling datum]] and \(\gamma\in G(E)\) a [[proofs/grh/spanning-unfolding-b/near-term|near]] rational isometry, with \(n=\varrho+1\).

1. If \(u,u'\in\mathsf{U}^0(E)\) (unipotent, fixing the frame), then \(u\gamma u'\) is near.
2. If \(S\) is [[proofs/grh/spanning-unfolding-b/filling-admissible|admissible]], then for every infinite place \(w\) and all \(0\le i,j\le\varrho\)
\[
\bigl\lvert\Phi_w\bigl(Z(\gamma)_{ij}\bigr)\bigr\rvert\le b^{134n}.
\]
3. If \(S\) is admissible, then for every \(0\le l\le\varrho+1\) and every infinite place \(w\), the leading minor \(D_l\) of \(Z(\gamma)\) satisfies \(\lvert\Phi_w(D_l)\rvert^2\le b^{270n^2}\).

## Proof

(1) Let \(y\) be a boxed point with \(\gamma_\infty^{-1}y\) boxed. The set of boxed points is invariant under left multiplication by elements all of whose components lie in \(\mathsf{U}^0\subset G_1\) ([[?lean:New.Filling.mul_mem_boxedPoints_iff|invariance of boxed points]]), and the components of \(u_\infty\), \(u'_\infty\) lie in \(\mathsf{U}^0\) ([[proofs/grh/spanning-unfolding-b/norm-one-pairs-at-infinite-places|images at infinity]]). So \(u_\infty y\) is boxed, and \((u\gamma u')_\infty^{-1}(u_\infty y)=u'^{-1}_\infty\gamma_\infty^{-1}y\) is boxed.

(2) Let \(y\) be as above. The frame vectors \(y_w^{-1}f_i\) and \((\gamma_\infty^{-1}y)_w^{-1}f_j\) have norm at most the [[proofs/grh/spanning-unfolding-b/filling-constants|box radius]] \(b^{37n}\) ([[?lean:New.Filling.mem_frameBox_of_mem_boxedPoints|boxed points lie in the frame box]]). The entry \((i,j)\) of the frame products of \(g=(\gamma_\infty)_w\) is bounded by the product of these two norms ([[?lean:New.norm_realFrameGram_le_mul|Cauchy–Schwarz for frame products]]), and by [[proofs/grh/spanning-unfolding-b/frame-products-at-infinity|the formula at infinity]] it equals \(\kappa_w^{(\varrho-i)+(\varrho-j)}N^{-1}\Phi_w(Z(\gamma)_{ij})\). Hence
\[
\lvert\kappa_w\rvert^{(\varrho-i)+(\varrho-j)}\,\lvert\Phi_w(Z(\gamma)_{ij})\rvert\le N\,b^{37n}\,b^{37n}\le b^{60n+74n},
\]
using \(N\le b^{60n}\); and \(\lvert\kappa_w\rvert\ge1\) by admissibility.

(3) The minor \(D_l\) is a sum of \(l!\le l^l\) products of \(l\) entries, so by (2) \(\lvert\Phi_w(D_l)\rvert\le l^l\,b^{134nl}\le b^{l+134nl}\), since \(l\le\varrho+1\le b\). As \(l\le n\), the exponent of the square is \(2(l+134nl)\le2n+268n^2\le270n^2\), and \(b\ge1\).

## References

1. Lean: `New.Filling.IsNear.mul_of_mem_besselU0`, `New.Filling.IsNear.norm_frameProducts_le`, `New.Filling.IsNear.norm_map_leadingMinor_sq_le` in `src/New/Spanning/Unfolding/Terms.lean`.
