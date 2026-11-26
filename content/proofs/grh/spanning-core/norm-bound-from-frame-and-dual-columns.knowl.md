+++
id = "proofs/grh/spanning-core/norm-bound-from-frame-and-dual-columns"
title = "A norm bound from the frame and the dual columns"
kind = "theorem"
summary = "If the images under the inverse of y of the frame vectors and of the dual isotropic vectors have length at most M, then the operator norm of y plus one is at most 8(rho+1)M."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.norm_add_one_le_of_mem_frameBox", "New.norm_J₁", "New.norm_sum_rankOne_col"]
lean_files = ["src/New/Spanning/Bessel/Basic.lean"]
proof_status = "full"
+++

**Theorem.** In the setting of the [[proofs/grh/spanning-core/bessel-length|Bessel length]], let \(M\ge1\) and \(y\in G_1\) be such that

* \(\lVert y^{-1}e_a\rVert\le M\) for \(1\le a\le\varrho\) and \(\lVert y^{-1}z\rVert\le M\) (that is, \(y\) lies in the frame box of radius \(M\)), and
* \(\lVert y^{-1}e_a^*\rVert\le M\) for \(1\le a\le\varrho\).

Then \(\lVert y\rVert+1\le8(\varrho+1)M\).

## Proof

Let \(J\) be the Gram matrix of \(h\) and \(A=y^{-1}\). Since \(A\) is an isometry of \(h\), \(AJA^*=J\). Also \(\lVert J\rVert=1\), \(\lVert A\rVert=\lVert y\rVert\ge1\). Hence
\[
\lVert A\rVert^2=\lVert AA^*\rVert=\lVert J+A(1-J)A^*\rVert\le1+\lVert A(1-J)\rVert\,\lVert A\rVert .
\]
The columns of \(1-J\) are \(e_a-e_a^*\) at \(e_a\), \(e_a^*-e_a\) at \(e_a^*\), \(0\) at \(x_i\) and \(2z\) at \(z\). The operator norm of a matrix is at most the sum of the lengths of its columns, so
\[
\lVert A(1-J)\rVert\le\sum_{a}\lVert Ae_a-Ae_a^*\rVert+\lVert2Az\rVert+\sum_a\lVert Ae_a^*-Ae_a\rVert\le(4\varrho+2)M .
\]
Thus \(\lVert A\rVert^2\le(1+(4\varrho+2)M)\lVert A\rVert\), and dividing by \(\lVert A\rVert>0\): \(\lVert y\rVert+1\le2+(4\varrho+2)M\le8(\varrho+1)M\) because \(M\ge1\). \(\blacksquare\)

## References

1. Lean: `New.norm_add_one_le_of_mem_frameBox` in `src/New/Spanning/Bessel/Basic.lean`.
