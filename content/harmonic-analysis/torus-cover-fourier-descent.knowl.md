+++
id = "harmonic-analysis/torus-cover-fourier-descent"
title = "Fourier criterion for descent under a torus covering"
kind = "theorem"
summary = "Smooth functions descending through an integer torus covering have Fourier frequencies in the transposed image lattice."
aliases = ["pullback frequency lattice"]
domains = ["harmonic-analysis"]
section_mode = "progressive"
prerequisites = ["shared-foundations/descent-through-surjection", "topology/integer-matrix-torus-cover", "topology/deck-transformation", "harmonic-analysis/fourier-coefficient", "harmonic-analysis/smooth-fourier-reconstruction", "linear-algebra/matrix-transpose"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

A smooth function \(f\) on \(\mathbb T^n\) [[shared-foundations/descent-through-surjection|descends]] through \(p_A\) precisely when
\[
\widehat f(m)=0\qquad(m\notin A^T\mathbb Z^n).
\]
Here \(A\) is a nonsingular integer matrix.

## Proof and operations preserving descent

If \(f=F\circ p_A\), pullback sends frequency \(k\) to \(A^Tk\). Conversely, if the stated support condition holds, set \(\widehat F(k)=\widehat f(A^Tk)\); these coefficients decay faster than every power and reconstruct a smooth \(F\) with \(f=F\circ p_A\).

The same criterion follows from deck invariance: a frequency \(m\) is invariant under every translation \(A^{-1}z\), \(z\in\mathbb Z^n\), exactly when \(A^{-T}m\in\mathbb Z^n\). Translations, averaging, and Fourier multipliers preserve this frequency lattice whenever the multiplier defines a smooth output. This also applies to a directional Fourier inverse when its denominators obey a suitable lower bound. These operations preserve descent, not arbitrary support in the auxiliary variable.
