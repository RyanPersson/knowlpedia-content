+++
id = "proofs/grh/derivatives-divisibility/schur-entry-to-minor-product"
title = "From entries of the Schur matrix to products of minors"
kind = "lemma"
summary = "The norm of a jet along an entry of the Schur matrix is at most the norm of the jet along a product of minors P_y for suitable integral y."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.exists_norm_schurJet_le_norm_jet_minorProd", "New.minorProd_eq_sum", "New.exists_norm_le_norm_sum_mul_eval"]
lean_files = ["src/New/Derivatives/Divisibility/Count.lean"]
proof_status = "full"
+++

**Lemma.** Let \(p\) be a prime, \(\Phi,n,n'\) finite sets and \(\kappa\) column counts such that \(\lvert n\rvert\le\lvert n'\rvert\) and \(\kappa(\tau,h)=0\) for all \(\tau\) and \(\lvert n\rvert<h<\lvert n'\rvert\). Let \(F\in\mathbb{C}_p[\![z_{(\tau,b,a)}]\!]\) (\(\tau\in\Phi,b\in n',a\in n\)), and let \(i'\), \(i\) be [[?lean:New.WeylIndex|standard fillings]] with rows in \(n'\) and in \(n\). Let \(S_\kappa(z)_{i',i}\) be the entry of the [[?lean:New.schur|Schur matrix]] of the matrices of variables \(z_\tau\); the jet of \(F\) along it is the entry \((i',i)\) of the [[?lean:New.schurJet|matrix of Schur jets]] of \(F\). Then there are \(y_{\tau,a,k}\in\mathcal{O}\) such that, for the [[proofs/grh/derivatives-divisibility/product-of-minors|product of minors]] \(P_y\) of the filling \(i'\),
\[
\bigl\lvert S_\kappa(z)_{i',i}(\partial)F(0)\bigr\rvert\le\bigl\lvert P_y(\partial)F(0)\bigr\rvert .
\]

## Proof

*Expansion.* For each standard filling \(t\) with rows in \(n\) let \(b_t\) be the polynomial, with integer coefficients, in variables \(y_{\tau,a,k}\): the product of minors of the matrices \(y_\tau\) attached to \(t\), times \(\prod_\tau\det(y_\tau\ \text{on all rows and the first }\lvert n\rvert\text{ columns})^{\delta_\tau}\), where \(\delta_\tau=\kappa(\tau,\lvert n\rvert)\) if \(\lvert n\rvert<\lvert n'\rvert\) and \(0\) otherwise. Under the hypothesis on \(\kappa\), the [[?lean:New.sum_schur_smul_nablaBasis|defining expansion of the Schur matrix]] reads, for every \(y\) with entries in a commutative ring,
\[
P_y(z)=\sum_tb_t(y)\;S_\kappa(z)_{i',t} .
\]
Taking jets, \(P_y(\partial)F(0)=\sum_t\alpha_t\,b_t(y)\) with \(\alpha_t=S_\kappa(z)_{i',t}(\partial)F(0)\in\mathbb{C}_p\).

*A good point.* The polynomials \(b_t\) remain [[?lean:New.GL.linearIndependent_nablaBasis_mul_detPow|linearly independent over the residue field]] \(k\) of \(\mathcal{O}\). We claim that for any \(\alpha_t\in\mathbb{C}_p\) and any index \(t_1\) there is \(y\) with entries in \(\mathcal{O}\) and \(\lvert\alpha_{t_1}\rvert\le\lvert\sum_t\alpha_tb_t(y)\rvert\). Choose \(t_0\) with \(\lvert\alpha_{t_0}\rvert\) maximal; if \(\alpha_{t_0}=0\) any \(y\) works. Otherwise \(\beta_t=\alpha_t/\alpha_{t_0}\in\mathcal{O}\) and \(\beta_{t_0}=1\), so the reduction of \(\sum_t\beta_tb_t\) modulo the maximal ideal is a nonzero polynomial over \(k\). The field \(k\) is algebraically closed, hence infinite, so this polynomial has a nonzero value at some point of \(k\); lift the point to \(y\) over \(\mathcal{O}\). Then \(\sum_t\beta_tb_t(y)\) is a unit and \(\lvert\sum_t\alpha_tb_t(y)\rvert=\lvert\alpha_{t_0}\rvert\ge\lvert\alpha_{t_1}\rvert\). Apply this with \(t_1=i\). \(\blacksquare\)

## References

1. Lean: `New.exists_norm_schurJet_le_norm_jet_minorProd`, `New.minorProd_eq_sum`, `New.exists_norm_le_norm_sum_mul_eval` in `src/New/Derivatives/Divisibility/Count.lean`; `New.schur`, `New.FitsRanks`, `New.nablaBasis`, `New.detPow` in `src/Lib/GLn/SchurModule/Basic.lean`.
