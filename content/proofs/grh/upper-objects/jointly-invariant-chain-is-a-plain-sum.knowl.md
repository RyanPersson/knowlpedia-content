+++
id = "proofs/grh/upper-objects/jointly-invariant-chain-is-a-plain-sum"
title = "At free levels a jointly invariant combination of chains is a plain sum"
kind = "theorem"
summary = "If the levels have trivial stabilisers, a jointly invariant combination of chains of lifts equals the sum over tuples of double cosets of the kernel products, without denominators; consequences for integrality and size."
aliases = ["a chain of lifts is a plain sum"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.IsJointlyInvariant.sum_chain_eq_sum_kernelProduct", "New.IsJointlyInvariant.sum_chain_mem_nsmul", "New.kernelProduct_induction", "New.apply_kernelProduct_le_prod_mul", "New.sum_classPoints_succ", "New.classPoints", "New.classPoints_of_le"]
lean_files = ["src/New/UpperBound/Objects/LiftChains.lean"]
proof_status = "full"
+++

Notation as in [[proofs/grh/upper-objects/chain-of-lifts|chain of lifts]]. Let \(\Gamma_j\subset G_j\) be the rational points and \(\mathrm{Cl}_j=\Gamma_j\backslash G_j/K_j\) the finite set of double cosets, with chosen representatives. The level \(K_j\) is **free** if \(\Gamma_j\cap gK_jg^{-1}=1\) for every \(g\in G_j\) ([[?lean:New.classAut|stabiliser of a class]]).

**Theorem.** Let \(\sum_{x\in s}L_x\otimes\Phi_x\) be a [[proofs/grh/upper-objects/jointly-invariant-combination|jointly invariant combination]] of length \(m\) with values in \(\mathsf M\), let \(K_j\) be free for all \(j<m\), and let \(\varphi\in\mathcal A_0\) be fixed by \(K_0\). Then for every tuple of points \(g=(g_j)\),
\[
\sum_{x\in s}L_x\Big(\big(\operatorname{chain}_m(\Phi_x)\varphi\big)(g_m)\Big)=\sum_{c\in\prod_{j<m}\mathrm{Cl}_j}\ \sum_{x\in s}L_x\Big(\Pi_m\big(\Phi_x,\varphi,(c,g)\big)\Big),
\]
where \((c,g)\) is the tuple of points whose \(j\)-th entry is the representative of \(c_j\) for \(j<m\) and \(g_j\) for \(j\ge m\), and \(\Pi_m\) is the kernel product.

**Corollary 1 (membership).** Let moreover \(P_j(g,v)\) be properties of a point \(g\in G_j\) and a vector \(v\in\mathcal V_j\) such that \(P_0(g,\varphi(g))\) for all \(g\), and \(P_j(g,v)\Rightarrow P_{j+1}(g',\operatorname{jet}(\omega_j(g,g')\Phi_{x,j})v)\) for all \(x\in s\), \(j<m\), \(g,g'\). Let \(p\in G_m\) and let \(A\subseteq\mathsf M\) be a set such that \(\sum_xL_x(\beta(\bigotimes_j\Phi_{x,j}))\in A\) for every linear \(\beta\colon S_{m-1}\otimes\dots\otimes S_0\to\mathcal V_m\) for which all the vectors \(\beta(\bigotimes_j\Phi_{x,j})\), \(x\in s\), satisfy \(P_m(p,\cdot)\). Then \(\sum_xL_x((\operatorname{chain}_m(\Phi_x)\varphi)(p))\) is a sum of \(\prod_{j<m}\lvert\mathrm{Cl}_j\rvert\) elements of \(A\).

**Corollary 2 (size).** If \(\operatorname{size}_j(g,v)\) are real functions with \(\operatorname{size}_{j+1}(g',\operatorname{jet}(\omega_j(g,g')\Phi_j)v)\le r_j\operatorname{size}_j(g,v)\) for \(j<m\) with \(r_j\ge0\), and \(\operatorname{size}_0(g,\varphi(g))\le B\) for all \(g\), then \(\operatorname{size}_m(g_m,\Pi_m(\Phi,\varphi,g))\le\big(\prod_{j<m}r_j\big)B\).

## Proof

*Theorem.* Induction on \(m\), generalising \(g\); \(m=0\) is trivial. For \(m=j+1\) the last lift is a class integral over \(a\in G_j\) of the integrand
\[
F(a)=\sum_xL_x\Big(\operatorname{jet}\big(\omega_j(a,g_{j+1})\Phi_{x,j}\big)\big(\operatorname{chain}_j(\Phi_x)\varphi\big)(a)\Big).
\]
*\(F\) is right \(K_j\)-invariant.* Fix \(a\) and \(b\in K_j\). Choose the linear map \(\beta\) with \((\operatorname{chain}_j(\Phi)\varphi)(a)=\beta(\bigotimes_{i<j}\Phi_i)\) and let \(T\) be the linear map on \(S_j\otimes(\dots)\) with \(T(f_j\otimes r)=\operatorname{jet}(\omega_j(a,g_{j+1})f_j)\beta(r)\). Apply joint invariance to the tuple that is \(b\) in slot \(j\) and \(1\) elsewhere, with test map \(T\): the data \(\Phi_{x,j-1}\) are moved by \(\omega_{j-1}(1,b)\) and \(\Phi_{x,j}\) by \(\omega_j(b,1)\). By part 2 of the [[proofs/grh/upper-objects/chain-equivariance|equivariance lemma]], moving the data of the chain of length \(j\) by \((1,\dots,1,b)\) translates its value: \((\dots)(a)\) becomes \((\dots)(ab)\). So the moved sum is \(F(ab)\) and the unmoved is \(F(a)\).

*Class integral.* The lift is by definition a [[?lean:New.classIntegral|class integral]] (the integral over \(\Gamma_j\backslash G_j\) for the measure with \(\operatorname{vol}(K_j)=1\), defined as a class sum at the level \(K_j\cap\operatorname{Stab}\) divided by an index); it is additive and commutes with additive maps of the values (Lean: `New.classIntegral_sum`, cited), which gives the expression of the left side as the class integral of \(F\). For a right \(K_j\)-invariant function the class integral is, by its definition, the class sum \(\sum_{r\in\mathrm{Cl}_j}F(r)/\lvert\Gamma_j\cap rK_jr^{-1}\rvert\), and all the stabilisers are trivial by freeness. Thus the left side for \(m=j+1\) is \(\sum_{r\in\mathrm{Cl}_j}F(r)\).

*Induction.* For fixed \(r\), \(F(r)=\sum_xL'_x((\operatorname{chain}_j(\Phi_x)\varphi)(r))\) with \(L'_x=L_x\circ\operatorname{jet}(\omega_j(r,g_{j+1})\Phi_{x,j})\); the combination \(\sum L'_x\otimes\Phi_x\) of length \(j\) is jointly invariant (apply joint invariance of the original with tuples that are \(1\) from slot \(j\) on and test maps \(T\) built from \(r\)). The induction hypothesis with the tuple \(g\) modified to \(r\) at slot \(j\), and the bijection between tuples of \(j+1\) classes and (last class, tuple of \(j\) classes), give the claim.

*Corollary 2.* Induction on \(m\) along the definition \(\Pi_{j+1}=\operatorname{jet}(\omega_j(g_j,g_{j+1})\Phi_j)\Pi_j\); more generally any property preserved by each kernel and true for the values of \(\varphi\) holds for \(\Pi_m\).

*Corollary 1.* By the theorem (with \(g_m=p\)) the left side is a sum over \(c\) of terms \(\sum_xL_x(\Pi_m(\Phi_x,\varphi,(c,g)))\). For fixed \(c\) the kernel product is \(\beta_c\) of the pure tensor of the data for one linear map \(\beta_c\), and its values satisfy \(P_m(p,\cdot)\) by the induction principle. So each term lies in \(A\). \(\square\)

## Remarks

The point of the theorem is the absence of denominators: with free levels every class has volume \(1\).

## References

1. Lean: `New.IsJointlyInvariant.sum_chain_eq_sum_kernelProduct`, `New.IsJointlyInvariant.sum_chain_mem_nsmul`, `New.apply_kernelProduct_le_prod_mul` in `src/New/UpperBound/Objects/LiftChains.lean`.
