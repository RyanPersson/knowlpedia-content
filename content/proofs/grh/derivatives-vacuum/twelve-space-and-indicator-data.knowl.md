+++
id = "proofs/grh/derivatives-vacuum/twelve-space-and-indicator-data"
title = "The space of twelve copies, its Taylor series and indicator data"
kind = "definition"
summary = "The hermitian space of 12 x 1 matrices over E, the jet series at the period scale pi_M times the jet scale, and the vectors obtained from the vacuum by replacing its part at the places dividing a modulus by the indicator of a residue class."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.twelveSpace", "New.Data.twelveTaylor", "New.Data.indicatorDatum", "New.copyEmbedding", "New.copyExponent", "New.copyEmbedding_apply", "New.copyExponent_apply", "New.coeff_prod_rename_copyEmbedding"]
lean_files = ["src/New/Derivatives/Sharpness/BoundAttained.lean"]
+++

Let \(D\) be [[?lean:New.Data|admissible data]] with field \(E\), places \(\Phi\), and \(\pi_M\) the conjugate of the [[?lean:New.Data.piMBar|integer \(\bar\pi_M\)]] of \(K\) of norm \(M\).

* The **space of twelve copies** \(V_{12}\) is the [[?lean:New.Space.hom|Hom space]] of the [[?lean:New.stdSpace|standard spaces]] of ranks \(1\) and \(12\) over \(E\): the hermitian space of \(12\times1\) matrices, with all signs \(+1\). Its jet series have variables \(z_{\tau,b}\), \(\tau\in\Phi\), \(1\le b\le12\) (twelve copies of the variables \(z_\tau\)).
* The **Taylor series** of \(F\in\mathcal{S}(V_{12})\) is \(\mathcal{T}(F)=J_{\pi_M\lambda}(F)\), the [[?lean:New.Space.jetSeries|jet series]] at the scale \(\pi_M\lambda\), \(\lambda\) the [[proofs/grh/derivatives-vacuum/jet-scale|jet scale]].
* For a [[?lean:New.Modulus|modulus]] \(\mathfrak{m}\) of \(E\) and a class \(y_0\) of \(12\times1\) matrices over \(\mathcal{O}_E/\mathfrak{m}\), the **indicator datum** \(\mathbb{1}_{\mathfrak{m},y_0}\in\mathcal{S}(V_{12})\) is the vector whose part at infinity is the Gaussian, whose part at the places dividing \(\mathfrak{m}\) is the indicator of \(y_0\), and which agrees with the [[?lean:New.Space.vacElem|vacuum]] at the other finite places ([[?lean:New.modDatum|datum of a modulus]]).

For exponents \(\alpha_1,\dots,\alpha_{12}\) on \(\Phi\), the **copy exponent** is the exponent \(\gamma\) on \(\Phi\times\{1,\dots,12\}\) with \(\gamma_{\tau,b}=(\alpha_b)_\tau\).

## Properties

If \(\Psi_b\) is a power series in the variables of the copy \(b\), then the coefficient of \(\prod_b\Psi_b\) at the copy exponent of \((\alpha_b)\) is \(\prod_b[z^{\alpha_b}]\Psi_b\).

## References

1. Lean: `New.Data.twelveSpace`, `New.Data.twelveTaylor`, `New.Data.indicatorDatum`, `New.copyEmbedding`, `New.copyExponent`, `New.copyEmbedding_apply`, `New.copyExponent_apply`, `New.coeff_prod_rename_copyEmbedding` in `src/New/Derivatives/Sharpness/BoundAttained.lean`.
