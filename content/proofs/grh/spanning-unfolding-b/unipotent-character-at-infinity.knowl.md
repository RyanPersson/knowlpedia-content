+++
id = "proofs/grh/spanning-unfolding-b/unipotent-character-at-infinity"
title = "The unipotent character at the infinite places"
kind = "lemma"
summary = "The product over the infinite places of the wave of the simple root sum of a rational isometry is the complex conjugate of the finite unipotent character."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.simpleRootSum_adelicToFin", "New.Filling.simpleRootSum_ratToAdelic", "New.Filling.norm_selfDualChar", "New.Filling.simpleRootSum_adelicToInf", "New.Filling.prod_wave_simpleRootSum_adelicToInf", "New.Filling.prod_wave_simpleRootSum_ratToInf"]
lean_files = ["src/New/Spanning/Unfolding/BesselLevelStructure.lean"]
proof_status = "full"
+++

**Lemma.** Let \(S\) be a [[proofs/grh/spanning-unfolding-b/filling-data|filling datum]]. For a matrix \(u\) let \(\sigma(u)=\sum_{a<\varrho}u_{f_a,f_{a+1}}\) be the [[?lean:New.simpleRootSum|simple root sum]], and put \(\operatorname{wave}(c)=\exp(c-\bar c)\) for \(c\in\mathbb{C}\) ([[?lean:New.wave|wave]]). Let \(\psi_{\mathsf U}\) be the [[proofs/grh/spanning-unfolding-b/unipotent-character-agreement-stability|unipotent character]] and \(\psi=\psi_\infty\psi_f\) the [[?lean:New.stdAddChar|standard additive character of the adeles]] of \(E\), with \(\psi_\infty(x)=e^{-2\pi i\sum_v2\operatorname{Re}x_v}\).

1. For every adelic point \(x\in G(\mathbb{A})\), with images \(x_{\infty}\in G_\infty\) and \(x_{\mathrm{fin}}\in G_{\mathrm{fin}}\), and every infinite place \(v\),
\[
\sigma\bigl((x_\infty)_v\bigr)=-2\pi i\,\Bigl(\frac{-\sigma(x)}{M\varpi}\Bigr)_v,\qquad
\prod_v\operatorname{wave}\bigl(\sigma((x_\infty)_v)\bigr)=\frac{\psi\bigl(-\sigma(x)/(M\varpi)\bigr)}{\psi_{\mathsf U}(x_{\mathrm{fin}})} .
\]
2. For every rational \(\gamma\in G(E)\),
\[
\prod_v\operatorname{wave}\bigl(\sigma((\gamma_\infty)_v)\bigr)=\overline{\psi_{\mathsf U}(\gamma_{\mathrm{fin}})} .
\]

## Proof

(1) By [[proofs/grh/spanning-unfolding-b/filling-unitary-groups|the entry formula]], the \((f_a,f_{a+1})\) entry of \((x_\infty)_v\) is the \(v\)-component of the corresponding entry of \(x\) times \(\sigma_v(f_{a+1})/\sigma_v(f_a)=\kappa_v^{\varrho-a-1}/\kappa_v^{\varrho-a}=\kappa_v^{-1}\). Summing over \(a\) gives \(\sigma((x_\infty)_v)=\sigma(x)_v/\kappa_v\), and \(\kappa_v=M\Phi_v(\varpi)/(2\pi i)\), which is the first formula. Put \(z=-\sigma(x)/(M\varpi)\in\mathbb{A}\). With \(c=-2\pi i\,z_v\) one has \(c-\bar c=-2\pi i\cdot2\operatorname{Re}z_v\), so the product of the waves is \(\psi_\infty(z)\). On the other hand, conjugation by the lattice basis matrix does not change the entries \((f_a,f_{a+1})\) (the lattice basis matrix is the identity on the \(e_a\) and \(e_a^*\), and its column at \(z\) is the basis vector \(z\)), so \(\sigma(x_{\mathrm{fin}})\) is the finite component of \(\sigma(x)\), and \(\psi_{\mathsf U}(x_{\mathrm{fin}})=\psi_f(-\sigma(x)_f/(M\varpi))=\psi_f(z_f)\). Since \(\psi(z)=\psi_\infty(z)\psi_f(z_f)\) and \(\psi_f\) has values of modulus one, the second formula follows.

(2) For rational \(\gamma\), \(\sigma\) of the adelic image is the diagonal image of \(\sigma(\gamma)\in E\), so \(z\in E\) and \(\psi(z)=1\) ([[?lean:New.stdAddChar_toAdele|the standard character is trivial on \(E\)]]). Hence the product is \(\psi_{\mathsf U}(\gamma_{\mathrm{fin}})^{-1}=\overline{\psi_{\mathsf U}(\gamma_{\mathrm{fin}})}\), as \(\lvert\psi_{\mathsf U}\rvert=1\).

## References

1. Lean: `New.Filling.simpleRootSum_adelicToInf`, `New.Filling.prod_wave_simpleRootSum_adelicToInf`, `New.Filling.prod_wave_simpleRootSum_ratToInf` in `src/New/Spanning/Unfolding/BesselLevelStructure.lean`.
