+++
id = "proofs/grh/derivatives-vacuum/existence-of-theta-products"
title = "Existence of theta products"
kind = "lemma"
summary = "A standard space has a theta product for every CM lattice C of area matched to Omega that contains Omega e; in particular for the CM curve with its period and level one."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Parameters.exists_isThetaProduct", "New.Parameters.exists_isThetaProduct_cmCurve"]
lean_files = ["src/New/Derivatives/Vacuum/IntegralVacuum.lean"]
proof_status = "full"
+++

**Lemma.** Let \(V\) be a [[?lean:New.Space.IsStd|standard]] space over \(E\) with finite index set \(n\), \(C\) a CM lattice for \(d\), \(\Omega\in\mathbb{C}^\times\) and \(e\ge1\) an integer with \(\Omega e\in\Lambda_C\) and \(\operatorname{area}(C)=\lvert\Omega\rvert^2\sqrt d/2\). Then there is a [[proofs/grh/derivatives-vacuum/theta-product|theta product]] \(F\in\mathcal{S}(V)\) for \(C\), \(\Omega\) of level \(e\). In particular there is a theta product of level \(1\) for the [[proofs/grh/derivatives-vacuum/cm-curve-and-period|CM curve]] \(\mathcal{E}\) and its period \(\Omega_0\).

## Proof

Apply [[proofs/grh/derivatives-vacuum/existence-of-resolution-product-along-tight-frame|the existence theorem for resolution products]] with

* \(\delta=q_1e\in\mathbb{Z}\subset\mathcal{O}_K\), \(N=(q_1e)^2\ne0\);
* the frame: the vectors \(\zeta^k\), \(0\le k<q_1\), each repeated \(q_1\) times with multiplicity \(1\); by [[proofs/grh/derivatives-vacuum/roots-of-unity-tight-frame|the tight frame of roots of unity]] (multiplicities \(q_1\), then [[?lean:New.IsTightFrame.repeat_vectors|repeating vectors]]) it is tight of length \(M=q_1^2\);
* exponents \(x_i=(1,0,0)\), i.e. the monomial section \(\theta_C\) of degree \(1\);
* \(a=\Omega e\in\Lambda_C\); the area condition holds since \(\lvert a\rvert^2M/N=\lvert\Omega\rvert^2\).

The scale is \(b=a/\bar\delta=\Omega/q_1\). For the frame vector \(\zeta^k\) and \(y\in E\) the shift of the resolution product is
\[ -\frac{\Omega}{q_1}\sum_w\Phi_w(y)\overline{\Phi_w(\zeta^k)}=-\frac{\Omega}{q_1}\operatorname{Tr}_{E/K}(y\,\overline{\zeta^k})=\kappa_k(y)\,\Omega, \]
because the trace is the sum over the CM type (see [[proofs/grh/derivatives-vacuum/hermitian-product-of-lattice-vectors-is-integral|the lemma on hermitian products]], step 3), and the linear form at scale \(bc/c_A\) is \(\ell^{\Omega,c}_{k,j}\). Grouping the \(q_1\) equal factors of each \(\zeta^k\), the formulas of [[proofs/grh/derivatives-vacuum/resolution-product-theta-values-and-jets|theta values and jets of resolution products]] become conditions 2 and 3; conditions 1, 4, 5 are conclusions of the existence theorem (\(\bar\delta\mathfrak{a}_0^{\,n}=q_1e\,\mathfrak{a}_0^{\,n}\)).

For the CM curve: \(\Omega_0\in\Lambda_{\mathcal{E}}=\Omega_0\mathcal{O}_K\), and the area of \(\Omega_0\mathcal{O}_K\) is \(\lvert\Omega_0\rvert^2\sqrt d/2\) (the covolume of \(\mathcal{O}_K=\mathbb{Z}+\mathbb{Z}\frac{1+i\sqrt d}{2}\) is \(\sqrt d/2\)).

## References

1. Lean: `New.Parameters.exists_isThetaProduct`, `New.Parameters.exists_isThetaProduct_cmCurve` in `src/New/Derivatives/Vacuum/IntegralVacuum.lean`.
