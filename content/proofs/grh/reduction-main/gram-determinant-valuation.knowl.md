+++
id = "proofs/grh/reduction-main/gram-determinant-valuation"
title = "Valuations of Gram determinants in a twisted lattice"
kind = "lemma"
summary = "An index bound for a family, completed by vectors with controlled denominators, bounds the height of the Gram determinants of the twisted lifts by twice the index."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.TwistedLattice.norm_det_mul_det_gram_le_one", "New.TwistedLattice.exists_matrix_elim_mem_lattice", "New.TwistedLattice.norm_pow_mul_det_gram_le", "New.TwistedLattice.heightLe_pow_mul_det_gram"]
lean_files = ["src/New/Reduction/Lattices/TwistedLattice.lean"]
proof_status = "full"
+++

**Lemma.** Let \(L\) be a [[proofs/grh/reduction-main/twisted-lattice|twisted lattice]] on a complex inner product space \(V\), with lifts \(\Theta_\xi\), lattices \(\Lambda_{\xi,\iota}\) and integral vectors \(L_\iota\). For a finite family \(w\) in \(V\) write \(\operatorname{Gram}_\xi(w)=\det(\langle\Theta_\xi w_i,\Theta_\xi w_k\rangle)_{i,k}\).

1. Let \(\iota\mid\ell\), let \(\xi\) be allowed at \(\ell\), and let \(u,u'\) be complex square matrices with \(\sum_ku_{ik}\Theta_\xi w_k\in\Lambda_{\xi,\iota}\) and \(\sum_ku'_{ik}\Theta_\xi w_k\in\Lambda_{\xi,\bar\iota}\) for all \(i\). Then
\[
\lvert\det u'\rvert_{\bar\iota}\cdot\lvert\operatorname{Gram}_\xi(w)\rvert_\iota\cdot\lvert\det u\rvert_\iota\le1 .
\]
2. Let \(y_1,\dots,y_n,z_1,\dots,z_{n'}\in V\), let \(\iota\mid\ell\), \(\xi\) allowed at \(\ell\), \(a\in\mathbb R\) and \(\gamma\in\mathbb C\). Suppose a matrix over \(\mathcal O_\iota\) carries \(y\) into \(L_\iota\) with loss \(a\), a matrix over \(\mathcal O_{\bar\iota}\) carries \(y\) into \(L_{\bar\iota}\) with loss \(a\), and \(\gamma\Theta_\xi z_i\in\Lambda_{\xi,\iota}\cap\Lambda_{\xi,\bar\iota}\) for all \(i\). Then
\[
\bigl\lvert\,\lvert\gamma\rvert^{2n'}\operatorname{Gram}_\xi(y,z)\bigr\rvert_\iota\le\ell^{\,2a}.
\]
3. Let \(y\) have [[proofs/grh/reduction-main/index-bound|index at most \(\delta\)]]; for each finite place \(\iota\mid\ell\) let \(\xi_\iota\) be a twist allowed at \(\ell\) and \(\gamma_\iota\in\mathbb C\) with \(\gamma_\iota\Theta_{\xi_\iota}z_i\in\Lambda_{\xi_\iota,\iota}\cap\Lambda_{\xi_\iota,\bar\iota}\) for all \(i\). Then the family
\[
\iota\ \longmapsto\ \lvert\gamma_\iota\rvert^{2n'}\operatorname{Gram}_{\xi_\iota}(y,z)
\]
has [[proofs/grh/reduction-main/height-bound|height at most \(2\delta\)]].

Here \(\lvert\gamma\rvert\) is the usual complex absolute value, a real number viewed in \(\mathbb C\).

## Proof

(1) Put \(\varphi_i=\sum_ku'_{ik}\Theta_\xi w_k\) and \(\varphi'_j=\sum_ku_{jk}\Theta_\xi w_k\). The matrix \((\langle\varphi_i,\varphi'_j\rangle)\) equals \(\overline{u'}\cdot(\langle\Theta_\xi w_i,\Theta_\xi w_k\rangle)\cdot u^{\mathsf T}\), so its determinant is \(\overline{\det u'}\operatorname{Gram}_\xi(w)\det u\). By the integrality axiom every entry has \(\lvert\cdot\rvert_\iota\le1\), hence so has the determinant, as \(\lvert\cdot\rvert_\iota\) is nonarchimedean. Finally \(\lvert\overline{\det u'}\rvert_\iota=\lvert\det u'\rvert_{\bar\iota}\).

(2) Let \(u\), \(u'\) be the two matrices. The block diagonal matrix \(v=\operatorname{diag}(u,\gamma\cdot1_{n'})\) has \(\det v=\det u\cdot\gamma^{n'}\) and takes the family \(\Theta_\xi(y,z)\) into \(\Lambda_{\xi,\iota}\): for the first block because \(\sum_ku_{ik}y_k\in L_\iota\) and \(\xi\) is allowed at \(\ell\), for the second by hypothesis. Likewise \(v'=\operatorname{diag}(u',\gamma\cdot1_{n'})\) at \(\bar\iota\) (which lies over the same prime \(\ell\)). By (1),
\[
\lvert\det u'\rvert_{\bar\iota}\lvert\gamma\rvert_{\bar\iota}^{n'}\cdot\lvert\operatorname{Gram}_\xi(y,z)\rvert_\iota\cdot\lvert\det u\rvert_\iota\lvert\gamma\rvert_\iota^{n'}\le1 .
\]
Since \(\lvert\gamma\rvert^2=\bar\gamma\gamma\), we have \(\bigl\lvert\lvert\gamma\rvert^{2n'}\bigr\rvert_\iota=\lvert\gamma\rvert_{\bar\iota}^{n'}\lvert\gamma\rvert_\iota^{n'}\); and \(\lvert\det u\rvert_\iota,\lvert\det u'\rvert_{\bar\iota}\ge\ell^{-a}\). The claim follows.

(3) Let \(\delta_\ell\) be the numbers of the index bound. At \(\iota\mid\ell\) the index bound provides matrices carrying \(y\) into \(L_\iota\) and into \(L_{\bar\iota}\), both with loss \(\delta_\ell\) (the places \(\iota,\bar\iota\) have the same prime), and they do not depend on the twist, so they serve for \(\xi_\iota\). By (2) the member at \(\iota\) has \(\lvert\cdot\rvert_\iota\le\exp(2\delta_\ell\log\ell)\). As \(\sum_{\ell\in U}2\delta_\ell\log\ell\le2\delta\), rule (4) of [[proofs/grh/reduction-main/height-calculus|the calculus of heights]] applies.

## References

1. Lean: `New.TwistedLattice.norm_det_mul_det_gram_le_one`, `.exists_matrix_elim_mem_lattice`, `.norm_pow_mul_det_gram_le`, `.heightLe_pow_mul_det_gram` in `src/New/Reduction/Lattices/TwistedLattice.lean`; step (1) uses `New.norm_det_mul_det_gram_mul_det_le_one` in `src/Lib/General/LinearAlgebra/GramDeterminant.lean`.
