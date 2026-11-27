+++
id = "proofs/grh/derivatives-vacuum/resolution-product-integral-values"
title = "Values of a resolution product of monomial sections are p-integral"
kind = "lemma"
summary = "A resolution product of monomial sections of a CM lattice along vectors of the lattice a0, at a scale b with b times the conjugate of delta in the lattice, has p-integral values at all finite adelic vectors."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Parameters.IsResolutionProduct.norm_iota_apply_le_one"]
lean_files = ["src/New/Derivatives/Vacuum/TightFrames.lean"]
proof_status = "full"
+++

Notation as in [[proofs/grh/derivatives-vacuum/resolution-product|the definition of resolution products]]; \(d\) is a prime \(\equiv7\bmod8\), as for all parameters. For a triple \(x=(r,t,u)\in\mathbb{N}^3\) the [[?lean:New.CMLattice.monomialSection|monomial section]] of \(C\) is \(\theta_C^{\,r}(\sigma_C^2)^{t}G_C^{\,u}\), of degree \(\deg x=r+2t+3u\), where \(\theta_C\) and \(\sigma_C\) are the theta and sigma functions of \(C\) and \(G_C\) is the entire function equal to \(y\,\theta_C^3\) away from the poles of the translated coordinate \(y\).

**Lemma.** Let \(\delta\in\mathcal{O}_K\) and \(N\in\mathbb{N}\), \(N\ne0\), with \(\delta\bar\delta=N\). Let \(w_j\in\mathfrak{a}_0\) for all \(j\in I\), let \(x_i\in\mathbb{N}^3\) with \(\deg x_i=m_j\) for all \(i=(j,k)\), and let \(b\bar\delta\in\Lambda_C\). If \(F\) is the resolution product of the monomial sections of the \(x_i\) along \(w\) at scale \(b\) with degrees \(m\) on \(C\), then for every prime \(p\), every \(p\)-adic place \(\iota_p\) of \(\mathbb{C}\) and every \(y\in\mathbb{A}_{E,f}^{\,n}\),
\[ \bigl\lvert\iota_p\bigl(F(y_f)\bigr)\bigr\rvert_p\le1, \]
where \(y_f\) is the adelic vector with finite part \(\alpha y\) and real part \(0\).

## Proof

*Reduction to a rational translate.* The value \(F(y_f)\) equals \(\theta(\varrho(y_f)F)\) (the theta functional of the translate; Lean `theta_rho`). Since \(F\) is in the finite part, it is fixed by an open subgroup of finite translations, and \(E^n\) is dense in the finite adelic vectors, so there is \(\gamma\in E^n\) with \(\varrho(\gamma_f)F=\varrho(y_f)F\) ([[?lean:New.exists_finiteImage_approx|approximation by a rational vector]]). By [[proofs/grh/derivatives-vacuum/resolution-product-theta-values-and-jets|the formula for theta values]],
\[ F(y_f)=\prod_{i=(j,k)}\bigl(\tau^{(m_j)}_{l_i(\gamma)}s_i\bigr)(0),\qquad s_i=\text{monomial section of }x_i. \]
It suffices to bound each factor.

*The shifts are torsion points.* There is an integer \(L\ne0\) with \(L\,\alpha^{-1}\gamma_k\) integral for all \(k\), i.e. \(L\gamma_k\in\mathfrak{a}_0\). By [[proofs/grh/derivatives-vacuum/hermitian-product-of-lattice-vectors-is-integral|integrality of hermitian products]], \(t=\langle L\gamma_k,w_j\rangle\in\mathcal{O}_K\) and \(b\bar\delta\,t\in\Lambda_C\). Then
\[ NL\cdot l_i(\gamma)=-\delta\bar\delta\,b\,\langle L\gamma_k,w_j\rangle=-\delta\,(b\bar\delta\,t)\in\Lambda_C, \]
as \(\Lambda_C\) is an \(\mathcal{O}_K\)-module. So \(l_i(\gamma)\) is a torsion point of \(\mathbb{C}/\Lambda_C\), of order dividing \(NL\ne0\).

*Torsion values are integral.* The factor \((\tau^{(m_j)}_{l}s_i)(0)\) is by definition the torsion value of \(s_i\) in degree \(m_j=\deg x_i\) at \(l=l_i(\gamma)\). By [[?lean:New.CMLattice.hasIntegralValues_monomialSection|integrality of torsion values of monomial sections]], its image under \(\iota_p\) has absolute value at most \(1\). A product of elements of absolute value \(\le1\) has absolute value \(\le1\).

## References

1. Lean: `New.Parameters.IsResolutionProduct.norm_iota_apply_le_one` in `src/New/Derivatives/Vacuum/TightFrames.lean`.
