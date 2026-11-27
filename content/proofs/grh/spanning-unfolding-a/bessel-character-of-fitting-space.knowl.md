+++
id = "proofs/grh/spanning-unfolding-a/bessel-character-of-fitting-space"
title = "The Bessel character of a fitting space"
kind = "definition"
summary = "The character r -> psi(-(M varpi)^-1 sigma(r)) on the adelic group of a fitting space, sigma the sum of the entries at the simple roots; on real points its inverse is a product of local waves."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.Fits.besselChar", "New.Filling.Fits.besselChar_inl_inv"]
lean_files = ["src/New/Spanning/Unfolding/BesselFormula.lean"]
+++

Let \(V\) [[proofs/grh/spanning-unfolding-a/space-fitting-filling-data|fit]] the [[?lean:New.Filling|filling data]] \(S\) over a [[?c:CM field|CM field]] \(E\), with identification \(\alpha:G\to G_S(\mathbb A)\); let \(M\) be the level and \(\varpi\) the generator of the different. The **Bessel character** is the function on \(G\)
\[
\chi_R(r)=\psi\Bigl(-\frac{1}{M\varpi}\,\sigma(\alpha(r))\Bigr),
\]
where \(\psi\) is the [[?lean:New.stdAddChar|standard additive character]] of the adeles of \(E\) and \(\sigma\) is the [[?lean:New.simpleRootSum|simple root sum]]: the sum of the entries just above the diagonal in the block of the frame \((e_1,\dots,e_\varrho,z)\).

## Properties

For a real point \(s\in G_\infty\), with components \(c(s)_v\in G_1\) ([[proofs/grh/spanning-unfolding-a/real-bessel-group-is-product-of-local-groups|components of real points]]),
\[
\chi_R(s,1)^{-1}=\prod_v\operatorname{wave}\bigl(-\sigma(c(s)_v)\bigr),\qquad\operatorname{wave}(w)=\exp(w-\bar w).
\]
*Proof.* Let \(z=-(M\varpi)^{-1}\sigma(\alpha(s,1))\in\mathbb A_E\). The finite part of \(\alpha(s,1)\) in the lattice basis is \(1\), so \(z_f=0\). At an [[?c:Infinite place of a number field|infinite place]] the rescaling gives \(\sigma(c(s)_v)=-2\pi i\,z_v\) ([[?lean:New.Filling.simpleRootSum_adelicToInf|simple root sum at the infinite places]]; this is the reason for the scales \(\kappa_v=M\Phi_v(\varpi)/(2\pi i)\)). Hence \(\operatorname{wave}(-\sigma(c(s)_v))=\exp(2\pi i\cdot2\operatorname{Re}z_v)\), and the standard character at an adele with trivial finite part is \(\exp(-2\pi i\sum_v2\operatorname{Re}z_v)\).

## Remarks

According to the source, on \(R(\mathbb A)\) this is a character trivial on \(H(\mathbb A)\) that extends the generic character \(\psi_U\) of the unipotent group of the grading when the constant of \(\psi_U\) is matched with \(-(M\varpi)^{-1}\); this remark is not proved in the file.

## References

1. Lean: `New.Filling.Fits.besselChar` in `src/New/Spanning/Unfolding/BesselFormula.lean`.
2. Lean: `New.Filling.Fits.besselChar_inl_inv` in `src/New/Spanning/Unfolding/BesselFormula.lean`.
