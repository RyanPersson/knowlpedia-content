+++
id = "proofs/grh/derivatives-vacuum/standard-data-as-theta-products"
title = "Standard data are theta products along a resolution times integral series"
kind = "theorem"
summary = "The jet series of standard data of level delta, at scale conj(delta) times area scale over period and read p-adically, is the N-th power of a product of copies of theta along a resolution of the identity whose finite images are integral above p, times an integral series in the parameters."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Parameters.exists_jetSeries_map_eq_thetaProd_pow_mul", "New.Parameters.thetaMultiples", "New.Parameters.mem_thetaMultiples_of_jetSeries_eq_prod", "New.Parameters.map_linearSeries_smul_dagger_resolutionVectors", "New.Parameters.exists_rho_finiteImage_eq_and_coprime_mul_mem", "New.Parameters.mul_neg_sum_mul_conj_mem_cmCurve_lattice", "New.Parameters.mem_integralAfter_of_nsmul_mem", "New.Parameters.finiteImage_resolutionVectors_mem", "New.Parameters.exists_coprime_mul_mem_of_mem_integralAfter", "New.Parameters.ne_zero_of_prime_coprime"]
lean_files = ["src/New/Derivatives/Vacuum/StandardDataProducts.lean"]
proof_status = "full"
+++

Let \(V\) be a [[?lean:New.Space.IsStd|standard]] space over \(E=K(\zeta)\) with finite index set \(n\), \(p\) a prime, \(\iota_p\) a \(p\)-adic place of \(\mathbb{C}\). For a family \(u=(u_j)_{j\in J}\) in \(E^n\) write \(u_j^\dagger\) also for the linear forms with coefficients \(\iota_p(\overline{\Phi_\tau(u_{j,c})})\in\mathbb{C}_p\), and \(\theta\), \(\mathcal{O}[\![y(\mu z)]\!]\) as in [[proofs/grh/derivatives-vacuum/jet-ring|the jet ring]], for the CM curve \(\mathcal{E}\).

**Theorem.** Let \(\delta\in\mathcal{O}_K\), \(\delta\ne0\), \(N=\delta\bar\delta\), and let \(f\) be [[proofs/grh/derivatives-vacuum/standard-data|standard data]] of level \(\delta\) at \(p\). Then there are a finite family \((u_j)_{j\in J}\) in \(E^n\) with multiplicities \(m_j\) such that

1. \((u_j,m_j)\) is a [[?lean:New.IsResolution|resolution of the identity]];
2. every \(\alpha^{-1}u_j\) is integral at the places of \(E\) above \(p\);
3. there is \(H\in\mathcal{O}[\![y(u^\dagger z)]\!]\) with
\[ \iota_p\Bigl(J_{\bar\delta\,c_A/\Omega_0}(f)\Bigr)=\Bigl(\prod_{j\in J}\theta(u_j^\dagger z)^{m_j}\Bigr)^{N}H . \]

## Proof

Fix a [[proofs/grh/derivatives-vacuum/existence-of-vacuum-expansion|vacuum expansion]] \((b,w,F,y,a)\). For \(k\ge1\) let \(u^{(k)}\) be the [[proofs/grh/derivatives-vacuum/resolution-from-tight-frame|resolution vectors]] of \(w\) for \(\nu=bk\), \(\Theta_k=\prod_{(i,c)}\theta(u^{(k)\dagger}_{(i,c)}z)^{k^2}\), and let \(M_k\subset\mathcal{S}(V)\) be the set of \(g\) with \(\iota_p(J_{\bar\delta c_A/\Omega_0}(g))\in\Theta_k^{\,N}\cdot\mathcal{O}[\![y(u^{(k)\dagger}z)]\!]\). Since the jet series is linear in \(g\) and the ring of integral series is stable under integral constants, \(M_k\) is an \(R_p\)-submodule.

*Step 1: translates of \(F\).* Let \(x\) be integral after \(\delta\) above \(p\). We claim there is \(m\) prime to \(p\) with \(\varrho(x_f)F\in M_k\) for all \(k\ne0\) divisible by \(m\); the proof produces \(m=m_0b\), where \(m_0\) clears denominators and \(b\) is the number of the expansion.

Since \(F\) is in the finite part, there is \(\gamma\in E^n\) with \(\alpha^{-1}\gamma-x\in\widehat{\mathcal{O}}_E^{\,n}\) and \(\varrho(\gamma_f)F=\varrho(x_f)F\) ([[?lean:New.exists_finiteImage_approx|approximation]]). Then \(\delta\alpha^{-1}\gamma\) is integral above \(p\); clearing the finitely many denominators at other primes, there is \(m_0\) prime to \(p\) with \(m_0\delta\gamma\in\mathfrak{a}_0^{\,n}\). Put \(m=m_0b\), prime to \(p\). By condition 6 of the expansion with \(c=\bar\delta\),
\[ J_{\bar\delta c_A/\Omega_0}(\varrho(\gamma_f)F)=\prod_{(i,c)}T\bigl(\tau^{(1)}_{t_{i,c}}\theta_{\mathcal{E}}\bigr)\bigl(\bar\delta\,u^{(1)\dagger}_{(i,c)}X\bigr),\qquad t_{i,c}=-\frac{\Omega_0}{b}\langle\gamma_c,w_i\rangle. \]
If \(m\mid k\), say \(k=m_0b\,l\), then \(k\delta\,t_{i,c}=-l\,\langle m_0\delta\gamma_c,w_i\rangle\,\Omega_0\in\Omega_0\mathcal{O}_K=\Lambda_{\mathcal{E}}\) by [[proofs/grh/derivatives-vacuum/hermitian-product-of-lattice-vectors-is-integral|integrality of hermitian products]]. Also \(\bar\delta\,u^{(1)\dagger}=\overline{k\delta}\,u^{(k)\dagger}\). Apply [[proofs/grh/derivatives-vacuum/product-of-translated-thetas-as-theta-power|the lemma on division points]] to the integer \(k\delta\) of norm \(k^2N\), the points \(t_{i,c}\) and the forms \(\mu=u^{(k)\dagger}\): the product, read \(p\)-adically, is \(\prod\theta(u^{(k)\dagger}z)^{k^2N}H=\Theta_k^{\,N}H\) with \(H\) integral. This proves the claim.

*Step 2: generators.* Let \(g=h(x)\theta^\circ\) with \(x\) integral after \(\delta\) above \(p\). By condition 5, \(g=\sum_ja_j\,h(x)\varrho((y_j)_f)F=\sum_ja_jr_j\,\varrho((x+y_j)_f)F\) with \(a_j,r_j\in R_p\). Since \(by_j\) is integral and \(p\nmid b\), each \(y_j\) is integral above \(p\), hence integral after \(\delta\); so is \(x+y_j\). Step 1 gives \(m_j\) for each \(j\); with \(m=\prod_jm_j\), prime to \(p\), \(g\in M_k\) for all \(k\ne0\) divisible by \(m\).

*Step 3: all standard data.* The property "there is \(m\) prime to \(p\) with \(f\in M_k\) for all \(k\ne0\) divisible by \(m\)" is preserved by sums (take the product of the two numbers \(m\)) and by multiplication by elements of \(R_p\). Hence it holds for every \(f\in\mathcal{D}_p(V,\delta)\).

*Conclusion.* Take \(k=m\) and \(u=u^{(m)}\) with multiplicities \(m^2\): it is a resolution of the identity by [[proofs/grh/derivatives-vacuum/resolution-from-tight-frame|the lemma on resolutions]]; \(bm\,u^{(m)}_{(i,c)}=w_i\mathbf{e}_c\) has integral finite image and \(bm\) is a unit above \(p\), which gives 2; and \(f\in M_m\) is 3.

## References

1. Lean: `New.Parameters.exists_jetSeries_map_eq_thetaProd_pow_mul`, `New.Parameters.thetaMultiples`, `New.Parameters.mem_thetaMultiples_of_jetSeries_eq_prod`, `New.Parameters.map_linearSeries_smul_dagger_resolutionVectors`, `New.Parameters.exists_rho_finiteImage_eq_and_coprime_mul_mem`, `New.Parameters.mul_neg_sum_mul_conj_mem_cmCurve_lattice`, `New.Parameters.mem_integralAfter_of_nsmul_mem`, `New.Parameters.finiteImage_resolutionVectors_mem`, `New.Parameters.exists_coprime_mul_mem_of_mem_integralAfter`, `New.Parameters.ne_zero_of_prime_coprime` in `src/New/Derivatives/Vacuum/StandardDataProducts.lean`.
