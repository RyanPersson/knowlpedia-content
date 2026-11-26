+++
id = "proofs/grh/derivatives-vacuum/existence-of-resolution-product-along-tight-frame"
title = "A product of monomial sections along a tight frame is the theta function of an integral vector"
kind = "theorem"
summary = "For a tight frame of length M, an integer delta of K of norm N and a CM lattice of area matched to M and N, the product of monomial sections pulled back along the frame is the entire theta function of a vector of the finite part that is a resolution product and has p-integral values at every prime."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Parameters.exists_isResolutionProduct_of_isTightFrame", "New.Parameters.normalizedShift_prod_comp_of_mem_lattice", "New.Parameters.cmPeriod_mem_cmCurve_lattice", "New.Parameters.norm_map_selfDualAddChar"]
lean_files = ["src/New/Derivatives/Vacuum/TightFrames.lean"]
proof_status = "outline"
+++

Notation as in [[proofs/grh/derivatives-vacuum/resolution-product|the definition of resolution products]] and [[proofs/grh/derivatives-vacuum/resolution-product-integral-values|the integrality lemma]].

**Theorem.** Let \(V\) be a [[?lean:New.Space.IsStd|standard]] hermitian space over \(E\) with finite index set \(n\). Let \(\delta\in\mathcal{O}_K\), \(N\in\mathbb{N}\) with \(N\ne0\) and \(\delta\bar\delta=N\). Let \((w_j)_{j\in I}\) with multiplicities \((m_j)\) be a [[?lean:New.IsTightFrame|tight frame of length \(M\)]], and let \(x_i\in\mathbb{N}^3\), \(i\in I\times n\), be exponent triples with \(\deg x_{(j,k)}=m_j\). Let \(C\) be a [[?lean:New.CMLattice|CM lattice]] for \(d\) and \(a\in\Lambda_C\) with
\[ \operatorname{area}(C)=\frac{\lvert a\rvert^2}{N}\cdot\frac{M\sqrt d}{2}. \]
Then there is \(F\in\mathcal{S}(V)\) such that

1. \(F\) is the resolution product of the monomial sections \(s_i\) of the \(x_i\) along \(w\) at scale \(b=a/\bar\delta\), with degrees \(m\), on \(C\);
2. for every prime \(p\), every \(p\)-adic place \(\iota_p\) of \(\mathbb{C}\) and every finite adelic vector \(y\), \(\lvert\iota_p(F(y_f))\rvert_p\le1\);
3. the entire theta function \(\Theta_F\) is a [[?lean:New.IsThetaFunction|theta function]] for the lattice \(\bar\delta\,\mathfrak{a}_0^{\,n}\subset E^n\): it is entire and fixed by the [[?lean:New.signedShift|signed translations]] along all \(\gamma\in\bar\delta\,\mathfrak{a}_0^{\,n}\).

## Proof

Put \(b=a/\bar\delta\), \(A_i=A_i^{\,b/c_A}\) and
\[ S(z)=\prod_{i\in I\times n}s_i\bigl(A_i(z)\bigr),\qquad z\in\mathbb{C}^{\Sigma\times n}. \]
\(S\) is entire, since the monomial sections are.

*Isometry.* As \(\lvert\bar\delta\rvert^2=N\), the area hypothesis reads \(\operatorname{area}(C)=\lvert b\rvert^2M\sqrt d/2\). By [[proofs/grh/derivatives-vacuum/frame-forms-sum-to-standard-hermitian-form|the lemma on frame forms]] the form \(B=\sum_im_j\,A_i^{*}H_C\) is the standard hermitian form \(\bar u\cdot v\), which is the form of the Fock model.

*Periods.* For \(\gamma\in\mathfrak{a}_0^{\,n}\), by the property noted after the definition of resolution products and [[proofs/grh/derivatives-vacuum/hermitian-product-of-lattice-vectors-is-integral|integrality of hermitian products]],
\[ A_i\bigl(\operatorname{realImage}(\bar\delta\gamma)\bigr)=b\,\bar\delta\,\langle\gamma_k,w_j\rangle=a\,\langle\gamma_k,w_j\rangle\in\Lambda_C . \]

*\(S\) is a theta function for \(\bar\delta\mathfrak{a}_0^{\,n}\).* A monomial section of degree \(m\) satisfies \(\tau^{(m)}_ls=\chi_C(l)^m s\) for \(l\in\Lambda_C\), where \(\chi_C\) is the [[?lean:New.CMLattice.multiplier|multiplier]] of \(C\) (Lean `New.CMLattice.monomialSection_mem`). The translation operator of the form \(B\) by a vector \(u\) acts on a product \(\prod_if_i\circ A_i\) factor by factor, through \(\tau^{(m_j)}_{A_i(u)}\). If all \(A_i(u)\) are periods, the product is therefore multiplied by \(\prod_i\chi_C(A_i(u))^{m_j}\), and this number is the canonical multiplier of the form \(B\) at \(u\) (with the characteristic \(\bar\beta\cdot1\), \(\beta=(1+i\sqrt d)/2\)); this compatibility of multipliers is Lean `New.CMLattice.multiplier_eq_canonicalMultiplier` together with the additivity of Riemann forms under pull-back and sum. Hence the normalised translation by \(u\) fixes \(S\). For \(u=\operatorname{realImage}(\bar\delta\gamma)\) the normalised translation of the Fock form is the signed translation by \(\bar\delta\gamma\) (Lean `New.normalizedShift_realImage`, using that the element of trace one of the Weil data is \(\beta\)). These identifications of multipliers are asserted here, not reproved.

*Fourier inversion.* By [[?lean:New.Space.exists_entireTheta_eq_of_isThetaFunction|the characterisation of entire theta functions]] (applied with the integer \(\delta\) of \(E\), \(\delta\bar\delta=N\ne0\)), every theta function for \(\bar\delta\mathfrak{a}_0^{\,n}\) is \(\Theta_F\) for some \(F\) in the finite part of \(V\). Take such an \(F\) with \(\Theta_F=S\); this gives 3.

*Translates (1).* Translation of \(F\) by the finite image of \(\gamma\in E^n\) translates \(\Theta_F\) by the \(B\)-translation operator at \(-\operatorname{realImage}\gamma\) ([[?lean:New.Space.entireTheta_translate_finiteImage|theta functions of finite translates]]); acting factor by factor as above, it replaces \(s_i\) by \(\tau^{(m_j)}_{l}s_i\) with \(l=-A_i(\operatorname{realImage}\gamma)=l_i(\gamma)\). This is condition 3 of the definition; conditions 1 and 2 hold by construction.

*Integrality (2).* Apply [[proofs/grh/derivatives-vacuum/resolution-product-integral-values|the integrality lemma]]: the \(w_j\) lie in \(\mathfrak{a}_0\) since they form a tight frame, and \(b\bar\delta=a\in\Lambda_C\).

## References

1. Lean: `New.Parameters.exists_isResolutionProduct_of_isTightFrame`, `New.Parameters.normalizedShift_prod_comp_of_mem_lattice`, `New.Parameters.cmPeriod_mem_cmCurve_lattice`, `New.Parameters.norm_map_selfDualAddChar` in `src/New/Derivatives/Vacuum/TightFrames.lean`.
2. The Lean file head names as related work: J. H. Conway and N. J. A. Sloane, Low-dimensional lattices V, 1989; T. Finis, Divisibility of anticyclotomic L-functions and theta functions with CM, 2006; D. Mumford, On the equations defining abelian varieties I, 1966 (no locators are given there).
