+++
id = "proofs/grh/derivatives-vacuum/normal-form-along-a-tight-frame"
title = "Normal form of the theta product along a tight frame at an inert prime"
kind = "lemma"
summary = "At an inert prime the theta product of the CM curve along the resolution forms of a tight frame of length M has the normal form with a scale of valuation 1/(p^2-1) and unit leading coefficients at all odd exponents."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.exists_hasNormalForm_resolutionForms"]
lean_files = ["src/New/Derivatives/Sharpness/Cases.lean"]
proof_status = "outline"
+++

**Lemma.** Let \((w,c)\) be a tight frame of length \(M\) and \(p\) inert in \(K\). Then there are \(\varpi_p\in\mathbb{C}_p\) with \(\lvert\varpi_p\rvert_p=p^{-1/(p^2-1)}\) and integral \(\lambda_{e,j}\) with \(\lambda_{e,0}\) a unit for all odd \(e\), such that the theta product \(\Theta=\prod_i\theta(\mu_iz)^{c_i}\) of \(\mathcal{E}\) along the [[proofs/grh/derivatives-vacuum/resolution-forms-of-a-frame|resolution forms]] [[?lean:New.HasNormalForm|has the normal form]] for the partner map \(\tau\mapsto[-p^e]\tau\), the scale \(\varpi_p\) and the coefficients \(\lambda\).

## Proof

The theorem of the formal-group chapter ([[?lean:New.Parameters.exists_hasNormalForm|normal form of theta products at non-split primes]]; not reproved here) provides \(\varpi_p\) and \(\lambda^0\), with \(\lambda^0_{e,0}\) units at inert primes for odd \(e\), such that for every resolution of the identity \((u,c)\) integral above \(p\) the product \(\prod_i\theta(u_i^\dagger z)^{c_i}\) has the normal form. By [[proofs/grh/derivatives-vacuum/properties-of-resolution-forms|the properties of resolution forms]] the \(u_i=w_i/\bar\pi_M\) qualify, and \(\mu=\mathfrak{s}u^\dagger\) with \(\mathfrak{s}\) a unit, so \(\Theta(z)=\Theta_u(\mathfrak{s}z)\). Rescaling by the unit \(\mathfrak{s}\) preserves the normal form, with \(\lambda_{e,j}=\mathfrak{s}^{(p^e+1)p^j}\lambda^0_{e,j}\) (Lean `New.HasNormalForm.rescale`; asserted here: \(\Gamma_e\) is homogeneous of degree \(p^e+1\)); units stay units.

## References

1. Lean: `New.Data.exists_hasNormalForm_resolutionForms` in `src/New/Derivatives/Sharpness/Cases.lean`.
