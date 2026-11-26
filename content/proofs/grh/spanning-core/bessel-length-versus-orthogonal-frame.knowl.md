+++
id = "proofs/grh/spanning-core/bessel-length-versus-orthogonal-frame"
title = "The Bessel length is comparable to the lengths of the orthogonal frame"
kind = "theorem"
summary = "The Bessel length bounds the lengths of the Gram–Schmidt vectors of the moved frame from both sides, and conversely."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.norm_orthoFrame_mem_Icc", "New.besselLength_le_of_norm_orthoFrame", "New.besselLength_le_of_dual", "New.norm_inner_J₁_le"]
lean_files = ["src/New/Spanning/Bessel/Basic.lean"]
proof_status = "full"
+++

**Theorem.** Let \(y\in G_1\), with [[proofs/grh/spanning-core/bessel-length|Bessel length]] \(\ell(y)\) and [[proofs/grh/spanning-core/orthogonal-frame-of-a-point|orthogonal frame]] \(o_a(y)\), \(1\le a\le\varrho+1\).

1. If \(\ell(y)\le M\), then \(M^{-1}\le\lVert o_a(y)\rVert\le M\) for all \(a\).
2. If \(M\ge1\) and \(M^{-1}\le\lVert o_a(y)\rVert\le M\) for all \(a\), then \(\ell(y)\le8(\varrho+1)M\).
3. (Bounded frame with bounded triangular dual.) Let \(M\ge1\) and let \(V_0,V_1,\dots\) be vectors with: (a) \(V_{a-1}=y^{-1}f_a\) for \(1\le a\le\varrho+1\); (b) \(\lVert V_a\rVert\le M\) for \(a\le2\varrho\); (c) for all \(a,b\) with \(a+b\le2\varrho\), \(h(V_a,V_b)=-1\) if \(a+b=2\varrho\) and \(=0\) if \(a+b<2\varrho\). Then \(\ell(y)\le8(\varrho+1)M\).

## Proof

We use \(\lvert h(v,w)\rvert\le\lVert v\rVert\lVert w\rVert\) (as \(\lVert J\rVert=1\)).

(1) By Property 2 of the Bessel length there is \(u\in\mathsf U\) with \(\lVert uy\rVert\le M\) (so \(M>0\)), and \(o_a(uy)=o_a(y)\). By Property 4 of the orthogonal frame, \(\lVert uy\rVert^{-1}\le\lVert o_a(uy)\rVert\le\lVert(uy)^{-1}f_a\rVert\le\lVert uy\rVert\).

(2) Choose \(u\in\mathsf U\) with \((uy)^{-1}f_a=o_a:=o_a(y)\) (Property 2 of the orthogonal frame). For \(1\le a\le\varrho\) put \(v_a=o_a/\lVert o_a\rVert^2\). Then \(\langle(uy)^{-1}f_a,v_b\rangle=\delta_{ab}\) for \(a\le\varrho+1\), \(b\le\varrho\), by orthogonality; and \(h(v_b,v_a)=0\) for \(a,b\le\varrho\), because the \(o_a\) are the images under the isometry \((uy)^{-1}\) of \(e_1,\dots,e_\varrho\), which span an isotropic space. So the vectors \(Jv_a\) are dual, for \(h\), to the moved frame at \(uy\), and span an isotropic space. By the library lemma `New.exists_mul_unipotentOf_dualCols_eq` (for such a system there is \(n\) in the group \(\mathsf U^0\) of the elements of \(\mathsf U\) fixing the frame with \((uy)^{-1}n\,e_a^*=Jv_a\) for all \(a\le\varrho\)), we get \(n\in\mathsf U^0\). Put \(y'=n^{-1}uy\). Its moved frame is \((uy)^{-1}nf_a=o_a\), of length at most \(M\); and \(y'^{-1}e_a^*=Jv_a\) has length \(\lVert v_a\rVert=\lVert o_a\rVert^{-1}\le M\). By the [[proofs/grh/spanning-core/norm-bound-from-frame-and-dual-columns|norm bound]], \(\lVert y'\rVert+1\le8(\varrho+1)M\), and \(n^{-1}u\in\mathsf U\subseteq S\), so \(\ell(y)\le\lVert y'\rVert+1\).

(3) By (2) it suffices to show \(M^{-1}\le\lVert o_a(y)\rVert\le M\); index \(a\) from \(0\) to \(\varrho\), so \(o_a\) comes from \(V_a\). Upper bound: \(\lVert o_a\rVert\le\lVert V_a\rVert\le M\). Lower bound: \(o_a=V_a+\sum_{b<a}c_bV_b\) for some scalars \(c_b\) (Property 2 of the orthogonal frame). By (c), \(h(V_{2\varrho-a},V_b)=0\) for \(b<a\) and \(h(V_{2\varrho-a},V_a)=-1\), so \(h(V_{2\varrho-a},o_a)=-1\), whence \(1\le\lVert V_{2\varrho-a}\rVert\lVert o_a\rVert\le M\lVert o_a\rVert\). \(\blacksquare\)

## References

1. Lean: `New.norm_orthoFrame_mem_Icc`, `New.besselLength_le_of_norm_orthoFrame`, `New.besselLength_le_of_dual` in `src/New/Spanning/Bessel/Basic.lean`.
