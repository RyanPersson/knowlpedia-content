+++
id = "proofs/grh/reduction-main/covolume-calculus"
title = "Calculus of covolumes: conjugates of Gram determinants, Hadamard and Fischer"
kind = "lemma"
summary = "A covolume bound bounds every conjugate of the Gram determinant; short vectors have small covolume (Hadamard) and may be adjoined to a family (Fischer)."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.TwistedLattice.map_inner_lift_one", "New.TwistedLattice.CovolumeLe.norm_map_det_gram_le", "New.TwistedLattice.covolumeLe_of_normSqAt_le", "New.TwistedLattice.CovolumeLe.sumElim"]
lean_files = ["src/New/Reduction/Lattices/TwistedLattice.lean"]
proof_status = "full"
+++

**Lemma.** Let \(L\) be a [[proofs/grh/reduction-main/twisted-lattice|twisted lattice]] on \(V\); notation \(\sigma\Theta_1y\), \(\langle\cdot,\cdot\rangle_G\), \(\lVert\Theta_1y\rVert^2_\sigma\) as in [[proofs/grh/reduction-main/covolume-bound|covolume bound]], and \(\sigma'(z)=\overline{\sigma(\bar z)}\).

1. For \(v,w\in V\) and \(\sigma\in\operatorname{Aut}(\mathbb C)\): \(\sigma\bigl(\langle\Theta_1v,\Theta_1w\rangle\bigr)=\langle\sigma'\Theta_1v,\ \sigma\Theta_1w\rangle_G\).
2. **(Conjugates.)** If \(y=(y_k)_{k\in S}\) has covolume at most \(c\), then \(\bigl\lvert\sigma\bigl(\det(\langle\Theta_1y_i,\Theta_1y_k\rangle)_{i,k}\bigr)\bigr\rvert\le e^c\) for every \(\sigma\in\operatorname{Aut}(\mathbb C)\).
3. **(Hadamard.)** If \(z_1,\dots,z_n\in V\) satisfy \(\lVert\Theta_1z_i\rVert_\sigma^2\le e^h\) for all \(i\) and \(\sigma\), then \(z\) has covolume at most \(nh\).
4. **(Adjoining vectors.)** If \(y\) has covolume at most \(c\) and \(z_1,\dots,z_n\) are as in (3), then the concatenated family \((y,z)\) has covolume at most \(c+nh\).

## Proof

(1) By the rational-form axiom, \(\langle\Theta_1v,\Theta_1w\rangle=\sum_{c,c'}\overline{a_c}\,G_{cc'}\,b_{c'}\) with \(a=\operatorname{coord}\Theta_1v\), \(b=\operatorname{coord}\Theta_1w\). Apply \(\sigma\): it fixes the rational numbers \(G_{cc'}\), sends \(b_{c'}\) to \(\sigma(b_{c'})\) and \(\overline{a_c}\) to \(\sigma(\overline{a_c})=\overline{\sigma'(a_c)}\).

(2) By (1) and since \(\sigma\) commutes with determinants, \(\sigma(\det(\langle\Theta_1y_i,\Theta_1y_k\rangle))=\det(\langle v_i,w_k\rangle_G)\) with \(v_i=\sigma'\Theta_1y_i\), \(w_k=\sigma\Theta_1y_k\). The [[?c:Cauchy-Schwarz inequality for Gram determinants|Cauchy–Schwarz inequality in the exterior power]] for the positive semidefinite form \(G\) gives
\[
\lvert\det(\langle v_i,w_k\rangle_G)\rvert^2\le\lvert\det(\langle v_i,v_k\rangle_G)\rvert\cdot\lvert\det(\langle w_i,w_k\rangle_G)\rvert\le e^c\cdot e^c ,
\]
using the covolume bound at \(\sigma'\) and at \(\sigma\).

(3) By [[?c:Hadamard's inequality|Hadamard's inequality]] for the positive semidefinite Gram matrix \((\langle\sigma\Theta_1z_i,\sigma\Theta_1z_k\rangle_G)\), its determinant is at most the product of its diagonal entries, each at most \(e^h\).

(4) Fix \(\sigma\). The Gram matrix of the concatenated family of vectors \(\sigma\Theta_1y_k,\sigma\Theta_1z_i\) for \(\langle\cdot,\cdot\rangle_G\) is positive semidefinite with diagonal blocks the Gram matrices of the two families. By [[?c:Fischer's inequality|Fischer's inequality]] its determinant is at most the product of the determinants of the diagonal blocks, which is at most \(e^c\cdot e^{nh}\) by hypothesis and (3).

## References

1. Lean: `New.TwistedLattice.map_inner_lift_one`, `New.TwistedLattice.CovolumeLe.norm_map_det_gram_le`, `New.TwistedLattice.covolumeLe_of_normSqAt_le`, `New.TwistedLattice.CovolumeLe.sumElim` in `src/New/Reduction/Lattices/TwistedLattice.lean`. Inputs: `New.norm_det_pairing_sq_le`, `New.norm_det_formGram_le` (`src/Lib/General/LinearAlgebra/GramDeterminant.lean`), `New.fischer_det_inequality` (`src/Lib/General/LinearAlgebra/MinorProducts.lean`).
