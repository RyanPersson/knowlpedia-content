+++
id = "proofs/grh/upper-elementary-divisors/origin-functions-summand-of-small-colength"
title = "Origin functions form a direct summand in which integral functions have small colength"
kind = "theorem"
summary = "If every edge occurs, the restriction to edges factors as Q d with Q split injective with image in the origin functions and det d dividing w to the |X| times the sum of the dimensions of the deep forms mod the maximal ideal."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.FrobeniusCycle.exists_originFunctions_factorization_det_dvd", "New.FrobeniusCycle.mulVec_mulVec_eq_self_of_mem_originFunctions", "New.FrobeniusCycle.apply_mem_allEdgesForms", "New.FrobeniusCycle.dvd_depthScaling_mulVec_of_dvd_edgeRestriction", "New.exists_mul_inv_eq_mul_diagonal", "New.card_le_mul_finrank_of_dual_rows", "New.prod_dvd_pow_sum_card", "New.FrobeniusCycle.dvd_of_forall_dvd_mul_inv_apply", "New.FrobeniusCycle.residue_mem_translatesIn"]
lean_files = ["src/New/UpperBound/ElementaryDivisors/Edges.lean"]
proof_status = "full"
+++

**Theorem.** Let \(O\) be a valuation ring that is a domain, with residue field \(\bar O\), and \(T\) a [[proofs/grh/upper-elementary-divisors/frobenius-cycle|Frobenius cycle]] for \((N,W,O)\), \(N\ge1\). Let \(X,E\) be finite sets with \(\operatorname{src}\colon E\to X\), \(g\colon E\to\mathrm{GL}_k(W)\), and \(\mathrm{Res}\), \(\mathcal{O}\) as in [[proofs/grh/upper-elementary-divisors/origin-functions|origin functions]]. Assume

- (every edge occurs) the map \(E\to X\times\mathrm{GL}_k(W)/\mathrm{Par}_r(W)\), \(e\mapsto(\operatorname{src}e,\ g_e^{-1}\mathrm{Par}_r(W))\), is surjective;
- \(\operatorname{depth}_r(\beta)\le x\) for all \(\beta\in\mathcal{E}=\mathcal{E}(N,k,n)\).

Then there are matrices \(Q\colon O^{X\times\mathcal{E}}\to O^{E\times\mathcal{E}}\), \(R\colon O^{E\times\mathcal{E}}\to O^{X\times\mathcal{E}}\) and a square matrix \(d\) on \(O^{X\times\mathcal{E}}\) with

1. \(Q\varphi\in\mathcal{O}\) for all \(\varphi\); 2. \(RQ=1\); 3. \(Qd=\mathrm{Res}\);
4. \(\det d\) divides \(w^{\ell}\), \(\ell=\lvert X\rvert\sum_{\delta=1}^{x}\dim_{\bar O}\bar{\mathcal{D}}_n(r,\delta)\), where \(\bar{\mathcal{D}}_n(r,\delta)\) is the space of [[proofs/grh/upper-elementary-divisors/translate-conditions|deep forms]] for the cycle base-changed to \(\bar O\).

Moreover: (a) if \(O\) has characteristic \(0\) and \(Q,R,d\) satisfy 2 and 3, then \(QR\psi=\psi\) for every \(\psi\in\mathcal{O}\) (so \(\mathcal{O}=\operatorname{im}Q\) is a direct summand, free of rank \(\lvert X\rvert\,\#\mathcal{E}\)); (b) under the first assumption (for any commutative \(O\)), for every \(\psi\in\mathcal{O}\) and \(e\in E\) the vector \(\psi(e,\cdot)\) lies in the module \(\mathcal{A}(k,n,r)\) of [[proofs/grh/upper-elementary-divisors/edges-and-halfway-lattices|forms in all halfway lattices]].

## Proof

*From edges to all bases.* Let \(z\in O\) divide all entries of \(\mathrm{Res}\,\varphi\). Then \(z\) divides all entries of \(\Delta\rho_n(\gamma)\varphi(y,\cdot)\) for all \(y\in X\), \(\gamma\in\mathrm{GL}_k(W)\). Indeed, choose \(e\) with \(\operatorname{src}e=y\) and \(g_e^{-1}\mathrm{Par}_r=\gamma^{-1}\mathrm{Par}_r\), so \(u=\gamma g_e^{-1}\in\mathrm{Par}_r(W)\); by [[proofs/grh/upper-elementary-divisors/parahoric-preserves-halfway-lattice|the lemma on the stabiliser]] \(\Delta\rho_n(u)=A\Delta\) with \(A\) integral, so \(\Delta\rho_n(\gamma)\varphi(y,\cdot)=A\cdot\Delta\rho_n(g_e)\varphi(y,\cdot)=A\cdot(\mathrm{Res}\varphi)(e,\cdot)\). This gives (b): if \(w^{m}\psi=\mathrm{Res}\varphi\), take \(h=\rho_n(g_e)\varphi(\operatorname{src}e,\cdot)\); then \(w^{m}\psi(e,\cdot)=\Delta h\) and \(w^{m}\mid\Delta\rho_n(\gamma)h=\Delta\rho_n(\gamma g_e)\varphi(\operatorname{src}e,\cdot)\).

*Elementary divisors.* \(\operatorname{src}\) is surjective, so \(\mathrm{Res}\) has at least as many rows as columns. Over a valuation domain, by the Hermite form ([[?lean:New.IsValuationPair.hermite|Hermite form]]: \(\mathrm{Res}=U'D\) with \(U'\) a set of columns of an invertible matrix and \(D\) square) and the Smith normal form of \(D\) ([[?c:Smith normal form|Smith normal form]]: \(D=K\operatorname{diag}(t)\Pi\) with \(K,\Pi\) invertible), there are an invertible \(\Pi\), a matrix \(Q\) with a left inverse \(R\), and \(t=(t_i)_{i\in X\times\mathcal{E}}\) with \(\mathrm{Res}\,\Pi^{-1}=Q\operatorname{diag}(t)\). Put \(d=\operatorname{diag}(t)\Pi\); then 2 and 3 hold and \(\det d=(\text{unit})\prod_it_i\).

Column \(i\) of \(\mathrm{Res}\,\Pi^{-1}\) is \(\mathrm{Res}\) of the column \(\pi_i\) of \(\Pi^{-1}\) and is divisible by \(t_i\). By the first step,
\[
t_i\mid w^{\operatorname{depth}\beta}\bigl(\rho_n(\gamma)\pi_i(y,\cdot)\bigr)_\beta\quad\text{for all }y,\gamma,\beta.\tag{*}
\]
With \(\gamma=1\): \(t_i\mid w^{x}(\Pi^{-1})_{(y,\beta),i}\) for all \((y,\beta)\); since \(\sum_j\Pi_{ij}(\Pi^{-1})_{ji}=1\), \(t_i\mid w^{x}\). Writing \(w^{x}=t_it'_i\), \(w^{x}Q\varphi=Q\operatorname{diag}(t)\operatorname{diag}(t')\varphi=\mathrm{Res}(\Pi^{-1}\operatorname{diag}(t')\varphi)\), which is 1.

*Counting.* Fix \(\delta<x\) and let \(S_\delta=\{i:t_i\nmid w^{\delta}\}\). For \(i\in S_\delta\), \(y\in X\), \(\gamma\) and \(\beta\) with \(\operatorname{depth}\beta\le\delta\), the coefficient \((\rho_n(\gamma)\pi_i(y,\cdot))_\beta\) is not a unit (otherwise \((*)\) gives \(t_i\mid w^{\operatorname{depth}\beta}\mid w^{\delta}\)). So the reduction of \(\pi_i(y,\cdot)\) modulo the maximal ideal of \(O\) lies in \(\bar{\mathcal{D}}_n(r,\delta+1)\) (the twisted representation commutes with base change). The columns \(\pi_i\) of the invertible matrix \(\Pi^{-1}\) have dual rows in \(\Pi\), so their reductions are linearly independent over \(\bar O\); those with \(i\in S_\delta\) lie in \(\bar{\mathcal{D}}_n(r,\delta+1)^{X}\), whence \(\#S_\delta\le\lvert X\rvert\dim\bar{\mathcal{D}}_n(r,\delta+1)\). Finally, in a valuation ring, if \(l_i\) is least with \(t_i\mid w^{l_i}\) then \(l_i\le\#\{\delta<x:t_i\nmid w^{\delta}\}\), so \(\prod_it_i\mid w^{\sum_il_i}\mid w^{\sum_{\delta<x}\#S_\delta}\mid w^{\ell}\). This is 4.

*(a).* If \(w^{m}\psi=\mathrm{Res}\varphi=Qd\varphi\), then \(w^{m}QR\psi=QRQd\varphi=Qd\varphi=w^{m}\psi\), and \(w^{m}\ne0\) is cancellable (\(w^{2}=p\ne0\) in characteristic \(0\)). \(\square\)

## References

1. Lean: `New.FrobeniusCycle.exists_originFunctions_factorization_det_dvd`, `New.FrobeniusCycle.mulVec_mulVec_eq_self_of_mem_originFunctions`, `New.FrobeniusCycle.apply_mem_allEdgesForms`, `New.FrobeniusCycle.dvd_depthScaling_mulVec_of_dvd_edgeRestriction`, `New.exists_mul_inv_eq_mul_diagonal`, `New.card_le_mul_finrank_of_dual_rows`, `New.prod_dvd_pow_sum_card`, `New.FrobeniusCycle.dvd_of_forall_dvd_mul_inv_apply`, `New.FrobeniusCycle.residue_mem_translatesIn` in `src/New/UpperBound/ElementaryDivisors/Edges.lean`.
