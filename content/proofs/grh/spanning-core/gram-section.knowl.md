+++
id = "proofs/grh/spanning-core/gram-section"
title = "The Gram section on the open cell"
kind = "construction"
summary = "An explicit element gamma_Z of the real unitary group whose frame Gram matrix is a given matrix Z of the open cell."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.RealPlace.diagLast", "New.RealPlace.sectionCoeff", "New.RealPlace.sectionFrame", "New.RealPlace.sectionMatrix", "New.RealPlace.gramSection", "New.RealPlace.coe_gramSection", "New.RealPlace.gramSection_eventuallyEq", "New.RealPlace.sqrt_eq_sqrt_oneSubNormSqInvCorner"]
lean_files = ["src/New/Spanning/Bessel/GramSection.lean"]
+++

In the setting of the [[proofs/grh/spanning-core/bessel-length|Bessel length]], let \(F\) be the matrix whose columns are the frame \((e_1,\dots,e_\varrho,z)\), \(F'\) the matrix with columns \((e_1^*,\dots,e_\varrho^*,x_{k_0})\) (\(k_0\in\kappa\) the distinguished index), and for \(x\in\mathbb{C}\) let \(\delta(x)=\operatorname{diag}(1,\dots,1,x)\) of size \(\varrho+1\). For invertible \((\varrho+1)\times(\varrho+1)\) matrices \(Z,W\) with \(\xi\) as in the [[proofs/grh/spanning-core/open-cell-of-frame-matrices|open cell]], and \(s=\sqrt{1-\xi(Z)\xi(W)}\) (principal branch), put
\[
\begin{aligned}
Y(Z,W)&=\delta(0)-1-\delta(0)\,W^{-1}\bigl(1-\delta(\tfrac12)\bigr)Z^{-1}\,\delta(2),\\
S(Z,W)&=\bigl(F\,Y(Z,W)+F'\,\delta(s)\bigr)Z,\\
M(Z,W)&=1+\bigl(S(Z,W)-F\bigr)F^*+\Bigl(\bigl(FW^{-1}-S(Z,W)\,Y(W,Z)\bigr)\delta(s^{-1})-F'\Bigr)F'^* .
\end{aligned}
\]
(\(Y(Z,W)\) has last row \((0,\dots,0,-1)\) and other entries \(-(W^{-1})_{a,\varrho+1}(Z^{-1})_{\varrho+1,b}\), halved unless \(b=\varrho+1\).) The **Gram section** is the map \(Z\mapsto\gamma_Z\in G_1\) defined by: for \(Z\in\Omega\), \(\gamma_Z\) is the element with matrix \(M(Z,Z^*)\) (for which \(s=\nu(Z)\)); for \(Z\notin\Omega\), \(\gamma_Z=1\).

That \(M(Z,Z^*)\) is an isometry for \(Z\in\Omega\), and that \(Z(\gamma_Z)=Z\), is the theorem [[proofs/grh/spanning-core/gram-section-is-a-section|the Gram section is a section]].

## Remarks

For \(W=Z^*\) the columns of \(F^\vee(Z)=F\,Y(Z,Z^*)+F'\delta(\nu(Z))\) form a family dual to the frame; \(\gamma_Z\) sends \(F\) to \(F^\vee(Z)Z\) and \(F^\vee(Z^*)\) to \(F(Z^*)^{-1}\), and fixes the \(x_i\), \(i\neq k_0\). The second variable \(W\) is kept independent so that \(M\) is holomorphic in \((Z,W)\).

## References

1. Lean: `New.RealPlace.sectionCoeff`, `New.RealPlace.sectionFrame`, `New.RealPlace.sectionMatrix`, `New.RealPlace.gramSection`, `New.RealPlace.coe_gramSection` in `src/New/Spanning/Bessel/GramSection.lean`.
