+++
id = "proofs/grh/derivatives-vacuum/resolution-product-theta-values-and-jets"
title = "Theta values and jet series of the translates of a resolution product"
kind = "lemma"
summary = "The theta value of a rational translate of a resolution product is the product of the values at 0 of the translated factors, and its jet series is the product of their Taylor series at the linear forms of the family."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Parameters.IsResolutionProduct.theta_translate", "New.Parameters.IsResolutionProduct.jetSeries_translate"]
lean_files = ["src/New/Derivatives/Vacuum/TightFrames.lean"]
proof_status = "full"
+++

Let \(F\) be the [[proofs/grh/derivatives-vacuum/resolution-product|resolution product]] of the \(f_i\) along \(w\) at scale \(b\) with degrees \(m\) on \(C\), in the notation of that definition, and let \(\gamma\in E^n\). Write \(g_i=\tau^{(m_j)}_{l_i(\gamma)}f_i\) for \(i=(j,k)\).

**Lemma.**

1. \(\theta(\varrho(\gamma_f)F)=\prod_{i\in I\times n}g_i(0)\).
2. Suppose \(V\) is [[?lean:New.Space.IsStd|standard]] (all signs \(+1\), point the identity). Then for every \(c\in\mathbb{C}\) the [[?lean:New.Space.jetSeries|jet series]] at scale \(c\) is
\[ J_c\bigl(\varrho(\gamma_f)F\bigr)=\prod_{i=(j,k)}T(g_i)\Bigl(\frac{b\,c}{c_A}\sum_{\tau}\overline{\Phi_\tau(w_j)}\,X_{(\tau,k)}\Bigr), \]
where \(T(g)\) is the Taylor series of \(g\) at \(0\).

## Proof

Condition 3 of the definition says \(\Theta_{\varrho(\gamma_f)F}(cz)=\prod_ig_i(A_i^{\,bc/c_A}(z))\), because \(A^{b/c_A}_i(cz)=A^{bc/c_A}_i(z)\). The functions \(g_i\) are entire (an entire function times an exponential of a linear function, translated), and \(\varrho(\gamma_f)F\) is again in the finite part, which is stable under the finite Heisenberg operators. Both statements are therefore the two parts of [[proofs/grh/derivatives-vacuum/jet-series-of-product-of-linear-forms|the lemma on products of functions of linear forms]].

## References

1. Lean: `New.Parameters.IsResolutionProduct.theta_translate`, `New.Parameters.IsResolutionProduct.jetSeries_translate` in `src/New/Derivatives/Vacuum/TightFrames.lean`.
