+++
id = "proofs/grh/derivatives-vacuum/theta-product"
title = "Theta product along the resolution of powers of zeta"
kind = "definition"
summary = "A vector of the finite part whose theta values and jet series at rational translates are products of q1-th powers of translated theta functions of a CM lattice along the frame vectors zeta^k / q1, with integral values and a theta function for the lattice q1 e a0^n."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Parameters.IsThetaProduct", "New.Parameters.zetaCoord", "New.Parameters.zetaCoord_smul", "New.Parameters.zetaCoordThetaTranslate", "New.Parameters.zetaLinearSeries", "New.Parameters.IsThetaProduct.theta_eq_one"]
lean_files = ["src/New/Derivatives/Vacuum/IntegralVacuum.lean"]
+++

Let \(P\) be [[?lean:New.Parameters|parameters]], \(s\in\mathbb{N}\), \(E=K(\zeta)\) with \(\zeta\) of order \(q_1\), CM type \((\Phi_w)_{w\in\Sigma}\), and \(V\) a [[?lean:New.Space|hermitian space]] over \(E\) with finite index set \(n\). Let \(C\) be a [[?lean:New.CMLattice|CM lattice]] for \(d\) with theta function \(\theta_C\), \(\Omega\in\mathbb{C}^\times\) and \(e\ge1\) an integer. For \(0\le k<q_1\) and \(y\in E\) put

* the **coordinate along \(\zeta^k/q_1\)**: \(\kappa_k(y)=-\operatorname{Tr}_{E/K}\bigl(y\,\overline{\zeta^k}\bigr)/q_1\in K\) (it is \(K\)-linear in \(y\));
* \(\vartheta_{k,y}=\tau^{(1)}_{\kappa_k(y)\Omega}\,\theta_C\), the [[?lean:New.CMLattice.twistedTranslate|twisted translate]] of degree \(1\) of \(\theta_C\) by \(\kappa_k(y)\Omega\);
* for \(c\in\mathbb{C}\), \(j\in n\), the linear form \(\ell^{\Omega,c}_{k,j}=\dfrac{\Omega\,c}{q_1c_A}\sum_{w\in\Sigma}\overline{\Phi_w(\zeta^k)}\,X_{(w,j)}\), with \(c_A=\sqrt{2\pi/\sqrt d}\) the [[proofs/grh/derivatives-vacuum/jet-scale|area scale]].

A vector \(F\in\mathcal{S}(V)\) is a **theta product for \(C\), \(\Omega\) of level \(e\)** if

1. \(F\) lies in the [[?lean:New.Space.finitePart|finite part]] of \(V\);
2. for every \(\gamma\in E^n\): \(\theta\bigl(\varrho(\gamma_f)F\bigr)=\prod_{k<q_1}\prod_{j\in n}\vartheta_{k,\gamma_j}(0)^{q_1}\);
3. for every \(\gamma\in E^n\) and \(c\in\mathbb{C}\): the [[?lean:New.Space.jetSeries|jet series]] is \(J_c\bigl(\varrho(\gamma_f)F\bigr)=\prod_{k<q_1}\prod_{j\in n}T(\vartheta_{k,\gamma_j})\bigl(\ell^{\Omega,c}_{k,j}\bigr)^{q_1}\), with \(T\) the Taylor series at \(0\);
4. for every prime \(p\), every [[?lean:New.PadicPlace|\(p\)-adic place]] \(\iota_p\) of \(\mathbb{C}\) and every finite adelic vector \(x\): \(\lvert\iota_pF(x_f)\rvert_p\le1\);
5. the [[?lean:New.Space.entireTheta|entire theta function]] \(\Theta_F\) is a [[?lean:New.IsThetaFunction|theta function]] for the lattice \(q_1e\,\mathfrak{a}_0^{\,n}\).

Here \(\varrho(\gamma_f)\) is translation by the rational vector \(\gamma\) placed at the finite places, and \(x_f\) is the adelic vector with finite part \(\alpha x\) and real part \(0\), as in [[proofs/grh/derivatives-vacuum/resolution-product|resolution products]].

## Properties

For \(\gamma=0\) all coordinates vanish and \(\theta_C(0)=1\), so condition 2 gives \(\theta(F)=1\).

## References

1. Lean: `New.Parameters.IsThetaProduct`, `New.Parameters.zetaCoord`, `New.Parameters.zetaCoord_smul`, `New.Parameters.zetaCoordThetaTranslate`, `New.Parameters.zetaLinearSeries`, `New.Parameters.IsThetaProduct.theta_eq_one` in `src/New/Derivatives/Vacuum/IntegralVacuum.lean`.
