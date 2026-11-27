+++
id = "proofs/grh/spanning-unfolding-b/discriminant-and-link-on-the-big-cell"
title = "Discriminant and link on the big cell"
kind = "theorem"
summary = "For the product of a Weyl element of all hyperbolic pairs with an isometry of the middle space, the frame discriminant is explicit and the link is the graph of the middle block, which it determines."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.frameDisc_weylElem_mul", "New.Filling.mem_link_weylElem_mul_iff", "New.Filling.link_weylElem_mul_eq_iff"]
lean_files = ["src/New/Spanning/Unfolding/Link.lean"]
proof_status = "full"
+++

**Theorem.** Let \(A\) be a field with involution and \(J\) a hermitian invertible split Gram matrix of \(\varrho\) hyperbolic planes and a middle form. Let \(\sigma,\tau\) be isometries that fix all \(e_a,e_a^*\) (elements of the [[?lean:New.Shape.Form.floorGroup|floor group]] of floor \(\varrho\)), with middle blocks \(\sigma_{\mathrm{mid}},\tau_{\mathrm{mid}}\). For a sequence of units \(p=(p_0,p_1,\dots)\) let \(w_p\) be the [[?lean:New.Floors.FloorGroups.weylElem|Weyl element]] with \(e_a\mapsto p_ae_a^*\), \(e_a^*\mapsto\bar p_a^{-1}e_a\) for \(a<\varrho\), fixing the middle space.

1. With \(t=h(z,\sigma z)\) and \(d=\prod_{a<\varrho}p_a\), the frame discriminant of \(w_p\sigma\) for any \(N\in A\) is \(d\bar d\,(t\bar t-N^2)\).
2. A pair \((v_1,v_2)\) of middle vectors lies in the [[?lean:New.link|link]] of \(w_p\sigma\) if and only if \(\sigma_{\mathrm{mid}}v_2=v_1\).
3. For units \(p,q\): the links of \(w_p\sigma\) and \(w_q\tau\) are equal if and only if \(\sigma=\tau\).

## Proof

In the blocks \((e,\mathrm{mid},e^*)\) the matrix of \(w_p\sigma\) is
\[
\begin{pmatrix}0&0&\operatorname{diag}(\bar p_a^{-1})\\0&\sigma_{\mathrm{mid}}&0\\\operatorname{diag}(p_a)&0&0\end{pmatrix}
\]
([[?lean:New.Filling.coe_weylElem_mul|block form on the big cell]]), and its matrix of frame products is diagonal with entries \(p_0,\dots,p_{\varrho-1},t\) ([[?lean:New.Filling.frameGram_weylElem_mul|frame products on the big cell]]).

(1) So \(D_{\varrho+1}=dt\) and \(D_\varrho=d\), whence \(D_{\varrho+1}\overline{D_{\varrho+1}}-N^2D_\varrho\overline{D_\varrho}=d\bar d(t\bar t-N^2)\).

(2) By [[proofs/grh/spanning-unfolding-b/link-in-coordinates|the link in coordinates]], \((v_1,v_2)\) is in the link if and only if for some \(a\), \(w_p\sigma(a,v_2,0)\) has middle block \(v_1\) and \(e^*\)-block \(0\). By the block form, \(w_p\sigma(a,v_2,0)=(0,\sigma_{\mathrm{mid}}v_2,\operatorname{diag}(p)a)\); the \(e^*\)-block vanishes for \(a=0\) (and only then), and the condition becomes \(\sigma_{\mathrm{mid}}v_2=v_1\).

(3) If the links agree, then for every middle vector \(b\) the pair \((\tau_{\mathrm{mid}}b,b)\) lies in the link of \(w_q\tau\), hence of \(w_p\sigma\), so \(\sigma_{\mathrm{mid}}b=\tau_{\mathrm{mid}}b\); thus \(\sigma_{\mathrm{mid}}=\tau_{\mathrm{mid}}\). By the block form, \(w_p\sigma=w_p\tau\), and cancelling \(w_p\) gives \(\sigma=\tau\). The converse is (2).

## References

1. Lean: `New.Filling.frameDisc_weylElem_mul`, `New.Filling.mem_link_weylElem_mul_iff`, `New.Filling.link_weylElem_mul_eq_iff` in `src/New/Spanning/Unfolding/Link.lean`; block forms in `src/Lib/DiscreteSeries/Bruhat/BigCell.lean`.
