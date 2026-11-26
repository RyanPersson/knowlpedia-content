+++
id = "proofs/grh/upper-objects/chain-of-lifts"
title = "Chain of theta lifts along a tower of definite unitary groups"
kind = "definition"
summary = "For a tower of abstract theta kernels between finite adelic definite unitary groups: the composite of the first j lifts, the chain of double lifts, and the product of the jet maps along a tuple of points."
aliases = ["chain of lifts", "kernel product", "double lift chain"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.chain", "New.doubleLiftChain", "New.twoKernelAction", "New.kernelProduct", "New.kernelProduct_succ", "New.classPoints", "New.exists_linearMap_chain_eq_apply_pure"]
lean_files = ["src/New/UpperBound/Objects/LiftChains.lean"]
+++

Let \(E\) be a [[?c:CM field|CM field]]. For \(j\ge0\) let \(n_j\) be a finite index set, \(G_j=U(I_{n_j})(\mathbb A_{E^+,f})\) the finite adelic points of the standard definite unitary group ([[?lean:New.Gf|finite adelic unitary group]]), \(K_j\subseteq G_j\) a level, \(\mathcal V_j\) the Weyl module of rank \(n_j\) with column numbers \(\kappa\), \(\mathcal A_j\) the space of [[?lean:New.AlgForm|algebraic modular forms]] on \(G_j\) of weight \((\kappa,e_j)\) with values in \(\mathcal V_j\), and
\(k_j\) a [[?lean:New.Kernel|theta kernel]] from stage \(j\) to stage \(j+1\): a complex vector space \(S_j\) of data, a representation \(\omega_j\) of \(G_j\times G_{j+1}\) on \(S_j\), and a linear *jet map* \(S_j\to\operatorname{Hom}(\mathcal V_j,\mathcal V_{j+1})\), equivariant for the rational points, every datum having an open stabiliser. Each datum \(\Phi\in S_j\) defines the [[?lean:New.Kernel.lift|lift]] \(k_j.\mathrm{lift}(\Phi)\colon\mathcal A_j\to\mathcal A_{j+1}\), linear in \(\Phi\):
\[
(k_j.\mathrm{lift}(\Phi)\varphi)(h)=\int \operatorname{jet}\big(\omega_j(g,h)\Phi\big)\big(\varphi(g)\big)\,dg ,
\]
the [[?lean:New.classIntegral|class integral]] over \(g\): the integral over \(\Gamma_j\backslash G_j\) (\(\Gamma_j\) the rational points) for the Haar measure with \(\operatorname{vol}(K_j)=1\), defined without measure theory as a weighted finite sum over double cosets.

**Definition.**

1. For a family \(\Phi=(\Phi_j)_j\), \(\Phi_j\in S_j\), the **chain** of \(j\) lifts is \(\operatorname{chain}_j(\Phi)=k_{j-1}.\mathrm{lift}(\Phi_{j-1})\circ\dots\circ k_0.\mathrm{lift}(\Phi_0)\colon\mathcal A_0\to\mathcal A_j\).
2. For \(\Phi_i\in S_{2i}\otimes S_{2i+1}\), the **chain of \(p\) double lifts** \(\mathcal A_0\to\mathcal A_{2p}\) is the composite over \(i<p\) of the maps obtained by extending \((\Phi,\Phi')\mapsto k_{2i+1}.\mathrm{lift}(\Phi')\circ k_{2i}.\mathrm{lift}(\Phi)\) linearly to \(S_{2i}\otimes S_{2i+1}\). A tuple \(a=(a_j)\), \(a_j\in G_j\), acts on \(S_{2i}\otimes S_{2i+1}\) by \(\omega_{2i}(a_{2i},a_{2i+1})\otimes\omega_{2i+1}(a_{2i+1},a_{2i+2})\).
3. For \(\varphi\in\mathcal A_0\) and a tuple of points \(g=(g_j)\), the **kernel product** is
\[
\Pi_m(\Phi,\varphi,g)=\operatorname{jet}\big(\omega_{m-1}(g_{m-1},g_m)\Phi_{m-1}\big)\circ\dots\circ\operatorname{jet}\big(\omega_0(g_0,g_1)\Phi_0\big)\big(\varphi(g_0)\big)\in\mathcal V_m .
\]

## Remarks

For fixed \(\varphi\) and \(g\in G_j\), the value \((\operatorname{chain}_j(\Phi)\varphi)(g)\) is \(\beta(\Phi_{j-1}\otimes\dots\otimes\Phi_0)\) for a linear map \(\beta\colon S_{j-1}\otimes\dots\otimes S_0\to\mathcal V_j\), because each lift is linear in its datum. Likewise the kernel product is linear in the pure tensor of the data.

## References

1. Lean: `New.chain`, `New.doubleLiftChain`, `New.kernelProduct` in `src/New/UpperBound/Objects/LiftChains.lean`; `New.Kernel` in `src/Lib/Weil/CompactLift/ThetaKernelDefs.lean`.
