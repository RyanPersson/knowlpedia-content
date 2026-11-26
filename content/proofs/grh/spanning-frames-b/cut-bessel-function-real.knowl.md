+++
id = "proofs/grh/spanning-frames-b/cut-bessel-function-real"
title = "Cut Bessel function at a real place"
kind = "definition"
summary = "The cut, at box radius rho, of a normalised Bessel function of irreducible type on G1, together with the numerical constraints on the sizes."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Floors.IsCutBessel", "New.Floors.IsCutBessel.isCut_complexData", "New.Floors.IsCutBessel.mul_pow_four_le_s", "New.Floors.IsCutBessel.volumeExponent_eq"]
lean_files = ["src/New/Spanning/Frames/RealShells.lean"]
+++

In the [[proofs/grh/spanning-frames-b/real-place-setting|notation at a real place]], let \(I\) be a finite set, \(\mathrm{rep}\colon U(\kappa)\to U(I)\) a homomorphism from the compact unitary group of \(X_0\) to the unitary matrices on \(\mathbb{C}^I\), \(F,F_0\colon G_1\to\mathbb{C}^I\) continuous functions, \(\rho,b\) real numbers and \(s,f\) natural numbers. Then \(F\) is a **cut Bessel function** with data \((\mathrm{rep},\rho,s,b,F_0,f)\) if

1. \((F_0,F)\) is a [[?lean:New.IsCutPair|cut pair]] of base \(b\) and decay rate \(f\) for \(\mathrm{rep}\), with \(F_0\) the full and \(F\) the cut member: both are [[?lean:New.IsBesselFunction|Bessel functions of type \(\mathrm{rep}\)]] (bounded, transforming on the left by the Bessel character under \(U\) and by \(\mathrm{rep}\) under \(U(\kappa)\)); \(F_0\) is integrable on \(U\backslash G_1\) with \(\int_{U\backslash G_1}\lVert F_0\rVert^2=\lvert I\rvert\) and \(\int_{U\backslash G_1}\lVert F\rVert^2\le\lvert I\rvert\); \(F(y)=0\) unless the [[?lean:New.besselLength|Bessel length]] of \(y\) is at most \(b^{6n+2}\); \(F=F_0\) where the Bessel length is at most \(b^{6n+2}/2\); \(\int_{U\backslash G_1}\lVert F-F_0\rVert^2\le b^{-2r^3f}\lvert I\rvert\); and \(F_0,F\) lie below a common [[?lean:New.IsDecayMajorant|decay majorant]];
2. \((\rho,s,b)\) satisfy the numerical hypotheses of the real place: \(\rho=b^{6n+2}\ge8r\), \(b\ge2\), \(k=s+3n+6\ge n^7\), \(s>10^9n^3\), \(\varrho\ge10^8\);
3. \(\mathrm{rep}\) is irreducible in the sense that every matrix \(C\in M_I(\mathbb{C})\) commuting with all \(\mathrm{rep}(h)\) is scalar.

## Properties

* A cut Bessel function is a [[?lean:New.Floors.PlaceData.IsCut|cut Bessel function for the place datum]] at \(\mathbb{C}\): it has frequency \(1=M^{-1}\), and if \(F(x)\ne0\) then the Bessel length of \(x\) is at most \(\rho\), so \(\lVert ux\rVert\le\rho\) for some \(u\in U\) ([[?lean:New.RealPlace.exists_norm_le_of_besselLength_le|Lean]]).
* \(s\ge10^{10}n^4\): indeed \(s+3n+6=k\ge n^7\) and \(n>10^8\).
* The volume exponent of the place datum is \(s\), since \(\operatorname{rk}X'=k-5\) and \(s=(k-5)-(3n+1)\).

## References

1. Lean: `New.Floors.IsCutBessel`, `New.Floors.IsCutBessel.isCut_complexData`, `New.Floors.IsCutBessel.mul_pow_four_le_s`, `New.Floors.IsCutBessel.volumeExponent_eq` in `src/New/Spanning/Frames/RealShells.lean`.
