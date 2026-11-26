+++
id = "proofs/grh/derivatives-vacuum/resolution-forms-of-a-frame"
title = "The resolution forms and the Taylor scale of a tight frame of length M"
kind = "definition"
summary = "The p-adic linear forms with coefficients period factor times conjugate embeddings of the frame vectors, the resolution vectors w / conj(pi_M), and the Taylor scale period factor times pi_M."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Parameters.resolutionForms", "New.Data.resolutionVectors", "New.Data.taylorScale", "New.Data.piMBar_mul_conj", "New.Data.coe_piMBar_ne_zero", "New.Data.phi_resolutionVectors"]
lean_files = ["src/New/Derivatives/Sharpness/Cases.lean"]
+++

Let \(D\) be [[?lean:New.Data|admissible data]] over parameters \(P\), with field \(E=K(\zeta)\), places \(\Phi\), level \(M=p_0p_1\) and the [[?lean:New.Data.piMBar|integer \(\bar\pi_M\) of \(K\)]] with \(\bar\pi_M\pi_M=M\) (\(\pi_M\) its conjugate). Let \(p\) be a prime with a \(p\)-adic place \(\iota_p\), \(\varpi\) the [[proofs/grh/derivatives-vacuum/jet-scale|period factor]], and \(w=(w_i)_{i\in J}\) a finite family in \(E\).

* The **resolution forms** of \(w\) are the linear forms \(\mu_i(z)=\sum_{\tau\in\Phi}\mu_{i,\tau}z_\tau\) over \(\mathbb{C}_p\) with \(\mu_{i,\tau}=\iota_p\bigl(\varpi\,\overline{\Phi_\tau(w_i)}\bigr)\).
* The **resolution vectors** are \(u_i=w_i/\bar\pi_M\in E\) (vectors of \(E^1\)).
* The **Taylor scale** is \(\mathfrak{s}=\iota_p(\varpi\,\pi_M)\in\mathbb{C}_p\).

Then \(\mu_i=\mathfrak{s}\,u_i^\dagger\), where \(u_i^\dagger\) has coefficients \(\iota_p(\overline{\Phi_\tau(u_i)})\).

## References

1. Lean: `New.Parameters.resolutionForms`, `New.Data.resolutionVectors`, `New.Data.taylorScale`, `New.Data.piMBar_mul_conj`, `New.Data.coe_piMBar_ne_zero`, `New.Data.phi_resolutionVectors` in `src/New/Derivatives/Sharpness/Cases.lean`.
