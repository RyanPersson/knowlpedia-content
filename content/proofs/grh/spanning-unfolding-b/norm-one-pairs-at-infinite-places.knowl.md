+++
id = "proofs/grh/spanning-unfolding-b/norm-one-pairs-at-infinite-places"
title = "Norm-one pairs pass to the infinite places"
kind = "lemma"
summary = "If a norm-one pair occurs from an index for a rational isometry, the same holds for its rescaled image at every infinite place."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.NormOnePairOccursFrom.ratToInf", "New.Filling.frameImage_ratToInf_mulVec", "New.Filling.ratToInf_mem_besselU0"]
lean_files = ["src/New/Spanning/Unfolding/Terms.lean"]
proof_status = "full"
+++

**Lemma.** Let \(S\) be a [[proofs/grh/spanning-unfolding-b/filling-data|filling datum]], \(\gamma\in G(E)\), \(v\) an infinite place and \(j\ge0\). If [[proofs/grh/spanning-unfolding-b/cell-rank-of-a-term|a norm-one pair occurs from \(j\)]] for \(\gamma\), then a norm-one pair occurs from \(j\) for \((\gamma_\infty)_v\in G_1\). Also, if \(u\in G(E)\) lies in the subgroup \(\mathsf{U}^0\) of unipotent elements fixing the frame, then so does \((u_\infty)_v\).

## Proof

Let \(c\in E\) with \(c\bar c=1\) be as in the hypothesis; then \(\Phi_v(c)\overline{\Phi_v(c)}=1\). Fix \(a\ge j\) and \(x,y\in E^{\varrho+1}\) with \(f\cdot x=\gamma f\cdot y\), \(x_a=c\), \(y_a=1\), \(x_b=y_b=0\) for \(b>a\). Recall \((\gamma_\infty)_v=D_v^{-1}\Phi_v(\gamma)D_v\) with \(D_v=\operatorname{diag}(\sigma_v)\). For any \(y\) and any basis index \(i\), a direct computation with the entry formula gives
\[
\Bigl((\gamma_\infty)_vf\cdot y'\Bigr)_i=\frac{\sigma_v(f_a)}{\sigma_v(i)}\,\Phi_v\bigl((\gamma f\cdot y)_i\bigr),\qquad y'_l=\frac{\sigma_v(f_a)}{\sigma_v(f_l)}\,\Phi_v(y_l),
\]
and the same with \(\gamma=1\) and \(x\). Hence \(f\cdot x'=(\gamma_\infty)_vf\cdot y'\) with \(x'_l=\sigma_v(f_a)\sigma_v(f_l)^{-1}\Phi_v(x_l)\). The rescaling factor is \(1\) at \(l=a\), so \(x'_a=\Phi_v(c)\), \(y'_a=1\), and \(x'_b=y'_b=0\) for \(b>a\).

The last statement holds because the conditions defining \(\mathsf{U}^0\) say that certain entries equal those of the identity, and these are preserved by \(\Phi_v\) and by conjugation with a diagonal matrix.

## References

1. Lean: `New.NormOnePairOccursFrom.ratToInf`, `New.Filling.frameImage_ratToInf_mulVec`, `New.Filling.ratToInf_mem_besselU0` in `src/New/Spanning/Unfolding/Terms.lean`.
