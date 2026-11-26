+++
id = "proofs/grh/derivatives-vacuum/resolution-product"
title = "Resolution product of entire functions along a family of vectors"
kind = "definition"
summary = "A vector of the finite part whose theta functions, for all rational translates, are products of twisted translates of given entire functions on a CM lattice, evaluated at the linear forms of a family of vectors of E."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Parameters.IsResolutionProduct", "New.Parameters.resolutionShift", "New.Parameters.resolutionFormCoeff", "New.Parameters.resolutionLinearForm", "New.Parameters.resolutionLinearForm_apply_eq_dotProduct", "New.Parameters.resolutionLinearForm_realImage"]
lean_files = ["src/New/Derivatives/Vacuum/TightFrames.lean"]
+++

Let \(P\) be [[?lean:New.Parameters|parameters]], \(s\in\mathbb{N}\), \(E=K(\zeta)\) the CM field of \((P,s)\) with CM type \((\Phi_\tau)_{\tau\in\Sigma}\), and \(\langle x,y\rangle=\sum_\tau\Phi_\tau(x)\overline{\Phi_\tau(y)}\) for \(x,y\in E\). Let \(V\) be a [[?lean:New.Space|hermitian space]] over \(E\) with finite index set \(n\), \(C\) a [[?lean:New.CMLattice|CM lattice]] for \(d\) with area \(A\), \(b\in\mathbb{C}\), \(I\) a finite set, \(w=(w_j)_{j\in I}\) a family in \(E\), \(m=(m_j)_{j\in I}\) natural numbers, and \(f=(f_i)_{i\in I\times n}\) functions \(\mathbb{C}\to\mathbb{C}\). Let \(c_A=\sqrt{2\pi/\sqrt d}\) be the [[proofs/grh/derivatives-vacuum/jet-scale|area scale]]. For \(i=(j,k)\in I\times n\), \(a\in\mathbb{C}\) and \(\gamma\in E^n\) define

* the **shift** \(l_i(\gamma)=-b\,\langle\gamma_k,w_j\rangle\in\mathbb{C}\);
* the **linear form** \(A^{a}_i\colon\mathbb{C}^{\Sigma\times n}\to\mathbb{C}\), \(A^a_i(z)=a\sum_{\tau}\overline{\Phi_\tau(w_j)}\,z_{(\tau,k)}\).

A vector \(F\in\mathcal{S}(V)\) is the **resolution product of the \(f_i\) along \(w\) at scale \(b\)** (with degrees \(m\), on \(C\)) if

1. \(F\) lies in the [[?lean:New.Space.finitePart|finite part]] of \(V\);
2. every \(f_i\) is entire;
3. for every \(\gamma\in E^n\) and every \(z\in\mathbb{C}^{\Sigma\times n}\),
\[ \Theta_{\varrho(\gamma_f)F}(z)=\prod_{i=(j,k)\in I\times n}\bigl(\tau^{(m_j)}_{l_i(\gamma)}f_i\bigr)\bigl(A_i^{\,b/c_A}(z)\bigr). \]

Here \(\Theta\) is the [[?lean:New.Space.entireTheta|entire theta function]], \(\varrho(\gamma_f)F\) is the translate of \(F\) under the Heisenberg representation by the [[?lean:New.finiteImage|finite image]] \(\alpha^{-1}\gamma\) of \(\gamma\) (the adelic vector with finite part \(\gamma\) and real part \(0\)), and \(\tau^{(m)}_l\) is the [[?lean:New.CMLattice.twistedTranslate|twisted translation]] of degree \(m\) on \(C\):
\[ (\tau^{(m)}_lg)(z)=\exp\!\Bigl(-\frac{m\pi}{A}\bigl(z\bar l+\tfrac12\lvert l\rvert^2\bigr)\Bigr)\,g(z+l). \]

## Properties

The real image of \(\gamma\in E^n\) in Fock coordinates has entry \(c_A\Phi_\tau(\gamma_k)\) at \((\tau,k)\). Hence \(A_i^{\,b/c_A}(\operatorname{realImage}\gamma)=b\,\langle\gamma_k,w_j\rangle=-l_i(\gamma)\): the shift of the factor \(i\) is minus the value of its linear form at the real image of \(\gamma\).

## References

1. Lean: `New.Parameters.IsResolutionProduct`, `New.Parameters.resolutionShift`, `New.Parameters.resolutionFormCoeff`, `New.Parameters.resolutionLinearForm`, `New.Parameters.resolutionLinearForm_apply_eq_dotProduct`, `New.Parameters.resolutionLinearForm_realImage` in `src/New/Derivatives/Vacuum/TightFrames.lean`.
