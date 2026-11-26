+++
id = "proofs/grh/spanning-core/cut-pair-of-bessel-functions"
title = "Cut pair of Bessel functions"
kind = "definition"
summary = "A normalised Bessel function and its cut: L2 bounds, the support of the cut, and decay below a common integrable majorant."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.IsCutPair", "New.IsDecayMajorant", "New.FullOrCut", "New.FullOrCut.select", "New.scaledBesselLength", "New.one_le_scaledBesselLength", "New.le_scaledBesselLength", "New.InCut"]
lean_files = ["src/New/Spanning/Bessel/Basic.lean"]
+++

Let \(\mathfrak s\) be a [[?lean:New.Shape|shape]], \(G_1\) the real unitary group with [[proofs/grh/spanning-core/bessel-length|Bessel length]] \(\ell\), \(n=\varrho+1\), \(r=2\varrho+k+1\) the rank, and \(\mu\) the [[?lean:New.besselQuotMeasure|measure on \(G_1\) that computes integrals over \(\mathsf U\backslash G_1\)]]. Let \(I\) be a finite set, \(\mathrm{rep}\colon U(\kappa)\to U(I)\) a homomorphism to unitary matrices, \(b\) a real number and \(f\) a natural number. Put
\[
\ell_b(y)=\max\bigl(1,\ \ell(y)/b^{6n}\bigr)\quad(\textbf{scaled length}),\qquad y\ \text{is }\textbf{in the cut}\iff\ell(y)\le b^{6n+2}.
\]
A pair \(W=(W^{\mathrm{full}},W^{\mathrm{cut}})\) of continuous functions \(G_1\to\mathbb{C}^I\) is a **cut pair** for \((b,f,\mathrm{rep})\) if

1. \(W^{\mathrm{full}}\) and \(W^{\mathrm{cut}}\) are [[?lean:New.IsBesselFunction|Bessel functions of type \(\mathrm{rep}\)]] (bounded; \(F(uy)=\psi(u)F(y)\) for \(u\in\mathsf U\), with the fixed character \(\psi\); \(F(hy)=\mathrm{rep}(h)F(y)\) for \(h\in U(\kappa)\));
2. \(W^{\mathrm{full}}\) is \(\mu\)-integrable;
3. \(\int\lVert W^{\mathrm{full}}\rVert^2d\mu=\lvert I\rvert\) and \(\int\lVert W^{\mathrm{cut}}\rVert^2d\mu\le\lvert I\rvert\);
4. \(W^{\mathrm{cut}}(y)\neq0\) implies that \(y\) is in the cut;
5. \(\int\lVert W^{\mathrm{cut}}-W^{\mathrm{full}}\rVert^2d\mu\le b^{-2r^3f}\,\lvert I\rvert\);
6. \(W^{\mathrm{cut}}(y)\ne W^{\mathrm{full}}(y)\) implies \(\ell(y)>\tfrac12b^{6n+2}\);
7. there is a **decay majorant**: a measurable \(A\colon G_1\to[0,\infty]\), invariant under left translation by the Bessel subgroup \(S\), and a finite \(a\) with \(\ell_b(y)^{3r^3f}\lVert W^t(y)\rVert\le A(y)\le a\) for both \(t\in\{\mathrm{full},\mathrm{cut}\}\) and all \(y\), and \(a\int A\,d\mu\le b^{400r^2}\lvert I\rvert\).

## Properties

\(\ell_b\ge1\); and if \(b\ge2\) and \(\ell(y)>\frac12b^{6n+2}\), then \(\ell_b(y)\ge b\) (since \(\ell(y)/b^{6n}>b^2/2\ge b\)).

## References

1. Lean: `New.IsCutPair`, `New.IsDecayMajorant`, `New.scaledBesselLength`, `New.InCut`, `New.le_scaledBesselLength` in `src/New/Spanning/Bessel/Basic.lean`.
