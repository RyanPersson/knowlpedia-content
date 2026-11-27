+++
id = "proofs/grh/derivatives-vacuum/vacuum-expansion"
title = "Expansion of the integral vacuum along a tight frame"
kind = "definition"
summary = "The data of a tight frame of length b^2 with b prime to p, a vector F whose translates have theta functions that are products of translated theta functions of the CM curve along the frame, and an expression of the integral vacuum as a p-integral combination of translates of F."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Parameters.IsVacuumExpansion"]
lean_files = ["src/New/Derivatives/Vacuum/StandardDataProducts.lean"]
+++

Let \(V\) be a [[?lean:New.Space.IsStd|standard]] space over \(E=K(\zeta)\) with finite index set \(n\), \(p\) a prime and \(\iota_p\) a \(p\)-adic place of \(\mathbb{C}\) with valuation ring \(R_p\). A **vacuum expansion** at \(p\) consists of \(b\in\mathbb{N}\), a finite family \((w_i)_{i\in I}\) in \(E\), a vector \(F\in\mathcal{S}(V)\), finitely many finite adelic vectors \((y_j)_{j\in J}\) and coefficients \(a_j\in R_p\) such that the conditions below hold. In them, for a finite adelic vector \(y\), \(y_f\) is the adelic vector with real part \(0\) and finite part \(\alpha y\) (\(\alpha\) the idele of the Weil data), while for a rational vector \(\gamma\in E^n\), \(\gamma_f\) is the adelic vector with real part \(0\) and finite part \(\gamma\) (it is \((\alpha^{-1}\gamma)_f\) in the first notation).

1. \(p\nmid b\);
2. \((w_i)\) with multiplicities \(1\) is a [[?lean:New.IsTightFrame|tight frame]] of length \(b^2\);
3. \(F\) lies in the [[?lean:New.Space.finitePart|finite part]] of \(V\);
4. \(b\,y_j\in\widehat{\mathcal{O}}_E^{\,n}\) for all \(j\);
5. the [[proofs/grh/derivatives-vacuum/integral-vacuum|integral vacuum]] is \(\theta^\circ=\sum_ja_j\,\varrho((y_j)_f)F\);
6. for every \(\gamma\in E^n\) and \(c\in\mathbb{C}\), with \(c_A/\Omega_0\) the quotient of the [[proofs/grh/derivatives-vacuum/jet-scale|area scale]] by the [[proofs/grh/derivatives-vacuum/cm-curve-and-period|period]],
\[ J_{c\,c_A/\Omega_0}\bigl(\varrho(\gamma_f)F\bigr)=\prod_{(i,k)\in I\times n}T\Bigl(\tau^{(1)}_{t_{i,k}(\gamma)}\theta_{\mathcal{E}}\Bigr)\bigl(c\,u_{(i,k)}^\dagger X\bigr),\qquad t_{i,k}(\gamma)=-\frac{\Omega_0}{b}\langle\gamma_k,w_i\rangle, \]
where \(u_{(i,k)}=(w_i/b)\mathbf{e}_k\) are the [[proofs/grh/derivatives-vacuum/resolution-from-tight-frame|resolution vectors]], \(u^\dagger X=\sum_xu^\dagger_xX_x\), \(T\) is the Taylor series at \(0\) and \(\theta_{\mathcal{E}}\) the theta function of the CM curve.

## References

1. Lean: `New.Parameters.IsVacuumExpansion` in `src/New/Derivatives/Vacuum/StandardDataProducts.lean`.
