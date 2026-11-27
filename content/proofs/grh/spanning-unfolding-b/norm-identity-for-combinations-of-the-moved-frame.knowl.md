+++
id = "proofs/grh/spanning-unfolding-b/norm-identity-for-combinations-of-the-moved-frame"
title = "Norm identity for combinations of the moved frame"
kind = "lemma"
summary = "A combination of the image of the frame that is orthogonal to the isotropic frame vectors has no dual part, and the squared length of its X0-part is given by its product with z and its z-coefficient."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.norm_sq_middle_part_eq", "New.Filling.frameImage_mulVec_eStar_eq_zero", "New.Filling.neg_mul_frameImage_mulVec_z_eq", "New.Filling.mul_sum_norm_sq_frameImage_mulVec_eq", "New.Filling.exists_frameImage_one_mulVec_eq_of_nonpos", "New.Filling.form_frameImage_mulVec", "New.Filling.star_mul_last_eq_of_frameImage_eq", "New.Filling.frameProducts_mulVec_of_frameImage_eq", "New.Filling.eq_zero_of_ratMiddle_form_eq_zero", "New.Filling.frameImage_mul", "New.Filling.frameImage_mul_of_mem_besselU0", "New.Filling.frameImage_inv_mul_eq_iff"]
lean_files = ["src/New/Spanning/Unfolding/Terms.lean"]
proof_status = "full"
+++

**Lemma.** Let \(S\) be a [[proofs/grh/spanning-unfolding-b/filling-data|filling datum]], \(\gamma\in G(E)\) with [[proofs/grh/spanning-unfolding-b/filling-classes-and-terms|frame products]] \(Z(\gamma)\), and \(y\in E^{\varrho+1}\). Put \(t=\gamma f\cdot y=\sum_by_b\gamma f_b\) and suppose that \(Z(\gamma)y=(0,\dots,0,D)\), that is, \(h(e_a,t)=0\) for all \(a<\varrho\) and \(h(z,t)=D\). Then:

1. \(t\) has no component along \(e_0^*,\dots,e_{\varrho-1}^*\);
2. the \(z\)-coordinate \(t_z\) of \(t\) satisfies \(-Nt_z=D\);
3. for every infinite place \(v\),
\[
N\sum_{i\in\kappa}\lvert\Phi_v(t_{x_i})\rvert^2=\lvert\Phi_v(D)\rvert^2-N^2\lvert\Phi_v(y_\varrho)\rvert^2 ;
\]
4. if the left side of 3 is \(\le0\) at some place, then \(t=f\cdot x\) for some \(x\in E^{\varrho+1}\).

Moreover, if \(f\cdot x=\gamma f\cdot y\) for some \(x,y\in E^{\varrho+1}\), then \(\bar x_\varrho x_\varrho=\bar y_\varrho y_\varrho\) and \(Z(\gamma)y=(0,\dots,0,-Nx_\varrho)\). Finally, a vector \(w\) of the middle space with \(w_z=0\) and \(h(w,w)=0\) is zero.

## Proof

(1), (2): \(h(e_a,t)\) is the \(e_a^*\)-coordinate of \(t\), and \(h(z,t)=-Nt_z\), by the shape of the Gram matrix.

(3) Since \(\gamma\) is an isometry, \(h(t,t)=h(f\cdot y,f\cdot y)=-N\bar y_\varrho y_\varrho\) (the \(e_a\) are isotropic and orthogonal to \(z\)). By (1) the hyperbolic part of \(h(t,t)\) vanishes, so \(h(t,t)=\sum_i\bar t_{x_i}t_{x_i}-N\bar t_zt_z\). Applying \(\Phi_v\): \(\sum_i\lvert\Phi_v(t_{x_i})\rvert^2-N\lvert\Phi_v(t_z)\rvert^2=-N\lvert\Phi_v(y_\varrho)\rvert^2\). By (2), \(\lvert\Phi_v(D)\rvert=N\lvert\Phi_v(t_z)\rvert\). Multiplying by \(N\) gives (3).

(4) A sum of squares that is \(\le0\) vanishes termwise, and \(N\ne0\); so \(t_{x_i}=0\) for all \(i\). With (1), \(t\) has only coordinates at \(e_a\) and \(z\), that is, \(t=f\cdot x\) with \(x_b\) the \(f_b\)-coordinate of \(t\).

For the additional statements: if \(f\cdot x=\gamma f\cdot y\), then \(h(f\cdot x,f\cdot x)=h(\gamma f\cdot y,\gamma f\cdot y)=h(f\cdot y,f\cdot y)\), i.e. \(-N\bar x_\varrho x_\varrho=-N\bar y_\varrho y_\varrho\); cancel \(N\ne0\). The products of \(f\cdot x\) with the frame are \(h(e_a,f\cdot x)=0\) and \(h(z,f\cdot x)=-Nx_\varrho\). For the last statement, at one infinite place \(\Phi_v(h(w,w))=\sum_{i\in\kappa}\lvert\Phi_v(w_i)\rvert^2\), which vanishes only if \(w=0\).

## References

1. Lean: `New.Filling.norm_sq_middle_part_eq`, `New.Filling.star_mul_last_eq_of_frameImage_eq`, `New.Filling.frameProducts_mulVec_of_frameImage_eq`, `New.Filling.eq_zero_of_ratMiddle_form_eq_zero` in `src/New/Spanning/Unfolding/Terms.lean`.
