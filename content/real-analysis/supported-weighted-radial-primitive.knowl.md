+++
id = "real-analysis/supported-weighted-radial-primitive"
title = "Compactly supported weighted radial primitive"
kind = "theorem"
summary = "A weighted first-order radial equation has a compactly supported solution exactly when its weighted source integral vanishes."
aliases = ["supported radial inverse"]
domains = ["real-analysis"]
section_mode = "progressive"
prerequisites = ["real-analysis/weighted-radial-moment", "real-analysis/cumulative-weighted-integral", "real-analysis/product-rule", "real-analysis/compactly-supported-function", "partial-differential-equations/solvability-compatibility-condition", "real-analysis/class-ck-map"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

Let \(f\in C_c^\infty((a,b))\), where \(0<a<b\), and \(e\in\mathbb R\). The equation
\[
u'(r)+\frac er u(r)=f(r)
\]
has a solution \(u\in C_c^\infty((a,b))\) exactly when the [[real-analysis/weighted-radial-moment|weighted moment]] \(\int_a^b r^ef(r)\,dr\) is zero. The solution is unique and equals
\[
u(r)=r^{-e}\int_a^r s^ef(s)\,ds.
\]

## Proof and support

Multiplying the equation by \(r^e\) gives \((r^eu)'=r^ef\). Compact support forces the integral of the right side to vanish. Conversely, under that condition the displayed integral vanishes near both endpoints and solves the equation smoothly. A homogeneous solution is \(cr^{-e}\), which cannot have compact support unless \(c=0\).

The primitive can fill gaps between separated pieces of the source support; it is contained in their radial interval hull, not necessarily their union. The restriction \(a>0\) avoids a separate regularity problem at the axis.
