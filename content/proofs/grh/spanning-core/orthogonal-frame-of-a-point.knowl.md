+++
id = "proofs/grh/spanning-core/orthogonal-frame-of-a-point"
title = "Orthogonal frame and Gram–Schmidt matrix of a point"
kind = "construction"
summary = "The Gram–Schmidt vectors of the moved frame at a point of the real unitary group and the unitriangular matrix expressing the frame in them."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.orthoFrame", "New.gramSchmidtMatrix", "New.gramSchmidt_eq_of_sub_mem_span", "New.frameVector_eq_sum_orthoFrame", "New.exists_frameVector_mul_eq_orthoFrame", "New.orthoFrame_besselS_mul", "New.gramSchmidtMatrix_besselS_mul", "New.norm_orthoFrame_le", "New.one_le_norm_mul_norm_orthoFrame", "New.orthoFrame_ne_zero", "New.linearIndependent_orthoFrame", "New.continuous_orthoFrame", "New.continuous_gramSchmidtMatrix", "New.measurable_gramSchmidtMatrix", "New.inner_orthoFrame_eq_zero_of_ne"]
lean_files = ["src/New/Spanning/Bessel/Basic.lean"]
+++

In the setting of the [[proofs/grh/spanning-core/bessel-length|Bessel length]], let \(y\in G_1\). The **orthogonal frame at \(y\)** is the family \(o_1(y),\dots,o_{\varrho+1}(y)\) obtained from the moved frame \(y^{-1}f_1,\dots,y^{-1}f_{\varrho+1}\) by the [[?c:Gram–Schmidt process|Gram–Schmidt process]] for the Euclidean inner product, without normalisation:
\[
o_a(y)=y^{-1}f_a-\sum_{b<a}\frac{\langle o_b(y),y^{-1}f_a\rangle}{\lVert o_b(y)\rVert^2}\,o_b(y).
\]
The **Gram–Schmidt matrix** \(\mathrm{gs}(y)\) is the upper unitriangular \((\varrho+1)\times(\varrho+1)\) matrix with entries \(\mathrm{gs}(y)_{ab}=\langle o_a(y),y^{-1}f_b\rangle/\lVert o_a(y)\rVert^2\) for \(a<b\); thus \(y^{-1}f_b=\sum_a\mathrm{gs}(y)_{ab}\,o_a(y)\).

## Properties

1. The \(o_a(y)\) are pairwise orthogonal and nonzero.
2. There is \(u\) in the Bessel unipotent group \(\mathsf U\) with frame matrix \(\mathrm{gs}(y)\) such that the moved frame at \(uy\) is the orthogonal frame at \(y\): \((uy)^{-1}f_a=o_a(y)\).
3. \(o_a(sy)=o_a(y)\) for every \(s\) in the Bessel subgroup \(S\), and \(\mathrm{gs}(sy)\cdot m(s)=\mathrm{gs}(y)\), where \(m(s)\) is the frame matrix of \(s\).
4. \(\lVert y\rVert^{-1}\le\lVert o_a(y)\rVert\le\lVert y^{-1}f_a\rVert\).
5. \(y\mapsto o_a(y)\) and \(y\mapsto\mathrm{gs}(y)\) are continuous on \(G_1\).

## Proof

*A general remark (G).* If two families \(v,w\) satisfy \(v_a-w_a\in\operatorname{span}\{w_b:b<a\}\) for all \(a\), they have the same Gram–Schmidt vectors. (Induction on \(a\): both Gram–Schmidt vectors differ from \(v_a\), resp. \(w_a\), by an element of the span \(B\) of the earlier ones and are orthogonal to \(B\); their difference lies in \(B\cap B^\perp=0\).)

(2) For every upper unitriangular matrix there is \(u\in\mathsf U\) with that frame matrix (`New.exists_mem_besselU_frameMatrix_eq`). Take \(u\) with frame matrix \(\mathrm{gs}(y)\). By Property 5 of the Bessel length, \(y^{-1}f_b=\sum_a\mathrm{gs}(y)_{ab}(uy)^{-1}f_a\); comparing with \(y^{-1}f_b=\sum_a\mathrm{gs}(y)_{ab}o_a(y)\) and using unitriangularity, induction on \(b\) gives \((uy)^{-1}f_b=o_b(y)\).

(4) Upper bound: \(\langle o_a,y^{-1}f_a\rangle=\lVert o_a\rVert^2\) by orthogonality, so \(\lVert o_a\rVert^2\le\lVert o_a\rVert\lVert y^{-1}f_a\rVert\). Lower bound: by (2) and Property 5 for \(u^{-1}\), \(o_a(y)=\sum_bm'_{ba}\,y^{-1}f_b\) with \(m'\) unitriangular, so the coordinate of \(y\,o_a(y)\) at the basis vector \(f_a\) is \(1\); hence \(1\le\lVert y\,o_a(y)\rVert\le\lVert y\rVert\lVert o_a(y)\rVert\). In particular \(o_a(y)\neq0\), which with orthogonality gives (1).

(3) Write \(s=u\,h\) with \(u\in\mathsf U\), \(h\in H\). The element \(h\) fixes the frame, so the moved frames at \(hy\) and \(y\) agree. For \(u\): \((hy)^{-1}f_a=\sum_bm(u)_{ba}(uhy)^{-1}f_b\) with \(m(u)\) unitriangular, so the moved frames at \(hy\) and at \(uhy\) satisfy the hypothesis of (G). For the matrices: both \(\mathrm{gs}(sy)m(s)\) and \(\mathrm{gs}(y)\) express the moved frame at \(y\) in the same linearly independent family \(o(y)=o(sy)\) (using \(m(uh)=m(u)\) on the frame).

(5) Induction along the Gram–Schmidt recursion, which divides only by the nonzero numbers \(\lVert o_b(y)\rVert^2\). \(\blacksquare\)

## References

1. Lean: `New.orthoFrame`, `New.gramSchmidtMatrix`, `New.orthoFrame_besselS_mul`, `New.gramSchmidtMatrix_besselS_mul`, `New.exists_frameVector_mul_eq_orthoFrame`, `New.continuous_gramSchmidtMatrix` in `src/New/Spanning/Bessel/Basic.lean`.
