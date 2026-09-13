+++
id = "real-analysis/weighted-shifted-radial-primitive"
title = "Weighted shifted radial primitive"
kind = "theorem"
summary = "Changing the radial coordinate and conjugating by a power gives a compact inverse modulo a transported cutoff defect."
aliases = ["shifted weighted radial inverse"]
domains = ["real-analysis"]
section_mode = "progressive"
prerequisites = ["partial-differential-equations/localized-characteristic-primitive", "real-analysis/supported-weighted-radial-primitive", "real-analysis/chain-rule-multivariable", "real-analysis/real-power", "real-analysis/compactly-supported-function", "harmonic-analysis/rapid-decay-of-shifted-torus-integral"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 2
+++

Let \(0<a<b\), \(d>0\), \(e\in\mathbb R\), and let \(f(R,y)\) be smooth and supported in \([a,b]\times\mathbb T^n\). Put \(U=R^d\) and
\[
F(U,y)=\frac{R^e f(R,y)}{dR^{d-1}},\qquad
\mathcal T_e f(R,y)=R^{-e}I_\chi F(R^d,y),
\]
where \(I_\chi\) is the [[partial-differential-equations/localized-characteristic-primitive|localized transport primitive]] and its transition lies in a compact subset of \(U>0\). For
\[
\mathcal D_R=\partial_R+MdR^{d-1}v\cdot\nabla_y,
\]
the exact weighted identity is
\[
(\mathcal D_R+e/R)\mathcal T_e f
=f-R^{-e}dR^{d-1}\chi'(R^d)J_MF(R^d,y).
\]

## Consequences

This follows by the chain rule and cancellation of the derivative of \(R^{-e}\) with \(e/R\). All radial powers and the coordinate change have bounded derivatives on the fixed positive shell. The output is compactly supported, and fixed coefficient derivatives have no loss in powers of \(M\) by the fixed-shift formula.

The zero weighted mean condition \(\int R^e\langle f\rangle_y\,dR=0\) is exactly \(\int\langle F\rangle_y\,dU=0\). Under a Diophantine drift, it gives arbitrarily high inverse-power bounds for the defect when the source has the required derivative bounds. For an auxiliary-independent source the defect is zero. Parameter derivatives of a moving coordinate map or of the drift require a separate chain-rule calculation.
