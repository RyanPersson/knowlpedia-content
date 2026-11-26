+++
id = "proofs/grh/determinant-exchange/vector-valued-theta-kernel"
title = "Vector-valued theta kernel of a descent pair"
kind = "definition"
summary = "The theta kernel of a descent pair (W, V) with values in the weight representation of U(V), characterised by its Gram pairings with weight vectors."
aliases = ["vector kernel", "theta kernel with values in the weight representation"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.DescentPair.vectorKernel", "New.DescentPair.gramForm_vectorKernel", "New.DescentPair.gramForm_vectorKernel_left", "New.DescentPair.conjKernel_apply"]
lean_files = ["src/New/Determinant/Norms/VectorKernel.lean"]
+++

Let \(E\) be a [[?c:CM field|CM field]] with a fixed [[?c:CM type|CM type]] and fixed [[?lean:New.WeilData|Weil data]], and let \(O\) be a [[?lean:New.DescentPair|descent pair]] over \(E\): a [[?c:Hermitian space|hermitian space]] \(W\) of rank \(r\), the standard definite hermitian space \(V=I_n\) of rank \(n>r\), characters \(\nu_W\), \(\nu_V\) of \(U(1)(\mathbb{A})\), and the weight \((k,e)\) (column numbers \(k\) and determinant exponents \(e\) at the infinite places) of the forms on \(V\). Let \(\rho\) be the [[?lean:New.Space.weightRep|representation of weight \((k,e)\)]] of \(U(V)\), written in the coordinates indexed by the [[?lean:New.WeylIndex|Weyl index set]], and let \(\langle\zeta,\eta\rangle\) be its [[?lean:New.gramForm|Gram pairing]], conjugate linear in \(\zeta\), with positive definite Gram matrix \(\mathcal{G}\). For a vector \(\xi\) of \(\rho\) let \(\varphi_\xi\) be the [[?lean:New.DescentPair.fockDatum|datum]] \(v_{P_\xi}\otimes\Psi_{\mathrm{bl}}\otimes\mathrm{vac}\) of the [[?c:Weil representation|Weil representation]] on \(\operatorname{Hom}(W,V)\), and let \(\theta_\varphi(g,h)\) be the [[?lean:New.pairTheta|theta kernel]] of a datum \(\varphi\) formed with \(\nu_W,\nu_V\).

For \(g\in U(W)(\mathbb{A})\) and a finite adelic point \(h\in U(V)(\mathbb{A}_f)\), the **vector-valued theta kernel** \(\theta_W(g,h)\) is the vector of \(\rho\) with coordinates
\[
\theta_W(g,h)=\mathcal{G}^{-1}\bigl(\theta_{\varphi_{e_i}}(g,(1,h))\bigr)_i ,
\]
where \(e_i\) are the coordinate vectors (which are real) and \((1,h)\) is the point of \(U(V)(\mathbb{A})\) with trivial component at the infinite places. Equivalently, it is the unique vector such that for every \(\zeta\)
\[
\langle \zeta,\theta_W(g,h)\rangle=\theta_{\varphi_{\bar\zeta}}\bigl(g,(1,h)\bigr).
\]

## Properties

The map \(\xi\mapsto\varphi_\xi\) is linear, so \(\xi\mapsto\overline{\theta_{\varphi_{\bar\xi}}(g,(1,h))}\) is a linear form; it is the [[?lean:New.DescentPair.conjKernel|conjugate kernel]] \(\kappa_{g,h}\) used to define the [[?lean:New.DescentPair.normalizedDescent|normalized descent]]. The characterisation above is checked as follows. By definition \(\mathcal{G}\,\theta_W(g,h)\) has \(i\)-th coordinate \(\overline{\kappa_{g,h}(e_i)}\), so
\[
\langle \zeta,\theta_W(g,h)\rangle=\overline{\sum_i \zeta_i\,\kappa_{g,h}(e_i)}=\overline{\kappa_{g,h}(\zeta)}=\theta_{\varphi_{\bar\zeta}}(g,(1,h)),
\]
using linearity of \(\kappa_{g,h}\). Since the pairing is hermitian, also
\[
\langle\theta_W(g,h),\xi\rangle=\kappa_{g,h}(\xi)=\overline{\theta_{\varphi_{\bar\xi}}(g,(1,h))}.
\]
Uniqueness holds because \(\mathcal{G}\) is positive definite, hence invertible.

## References

1. Lean: `New.DescentPair.vectorKernel`, `New.DescentPair.gramForm_vectorKernel`, `New.DescentPair.gramForm_vectorKernel_left` in `src/New/Determinant/Norms/VectorKernel.lean`.
