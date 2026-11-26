+++
id = "proofs/grh/spanning-unfolding-b/filling-amplitude"
title = "Bessel kernel, amplitude of a term and amplitude sums"
kind = "definition"
summary = "The tensor of Bessel functions W(y) with the conjugate of W at the translate by a rational term, its integral against two class cutoffs (the amplitude), the majorant, and the sum of amplitudes over a set of terms in a block."
aliases = ["amplitude", "amplitude sum", "Bessel kernel of a term", "amplitude majorant"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.besselFn", "New.Filling.besselKernel", "New.Filling.amplitude", "New.Filling.amplitudeMajorant", "New.Filling.amplitudeSum"]
lean_files = ["src/New/Spanning/Unfolding/Setup.lean"]
+++

Let \(S\) be a [[proofs/grh/spanning-unfolding-b/filling-data|filling datum]] with Bessel systems \(\mathcal{B}_v\) and Bessel coordinates \(I=\prod_vI_v\). Fix a *side*: *full* or *cut*; each \(\mathcal{B}_v\) provides a continuous function \(W_v\colon G_1\to\mathbb{C}^{I_v}\), the Bessel function on the full side and its cut \(W_v^\flat\) on the cut side. Let \(G_\infty=\prod_vG_1\) carry the product of the [[harmonic-analysis/haar-measure|Haar measures]] fixed on \(G_1\), and let \(\gamma\mapsto\gamma_\infty\) be the [[proofs/grh/spanning-unfolding-b/filling-unitary-groups|map \(G(E)\to G_\infty\)]].

* The **Bessel function** of the side is \(W\colon G_\infty\to\mathbb{C}^{I}\), \(W_i(y)=\prod_vW_{v,i_v}(y_v)\).
* For \(\gamma\in G(E)\), the **Bessel kernel** is the vector \(\mathcal{K}_\gamma(y)\in\mathbb{C}^{I\times I}\) (with the Euclidean norm) with coordinates
\[
\mathcal{K}_\gamma(y)_{(i,j)}=W_i(y)\,\overline{W_j(\gamma_\infty^{-1}y)} .
\]
* For [[proofs/grh/spanning-unfolding-b/filling-classes-and-terms|classes]] \(c,c'\) with [[proofs/grh/spanning-unfolding-b/class-cutoff|class cutoffs]] \(\beta_c,\beta_{c'}\), the **amplitude** of \(\gamma\) is
\[
A(c,c';\gamma)=\int_{G_\infty}\beta_c(y)\,\beta_{c'}(\gamma_\infty^{-1}y)\,\mathcal{K}_\gamma(y)\,dy\ \in\mathbb{C}^{I\times I},
\]
and its **majorant** is \(\widehat A(c,c';\gamma)=\int_{G_\infty}\beta_c(y)\,\beta_{c'}(\gamma_\infty^{-1}y)\,\lVert\mathcal{K}_\gamma(y)\rVert\,dy\in[0,\infty]\).
* For a set \(T\subset G(E)\), classes \(c,c'\) and \(s\in\bar G\), the **amplitude sum** is
\[
A_T(c,s,c')=\sum_{\gamma\in T\cap\mathcal{T}(c,s,c')}A(c,c';\gamma),
\]
the sum over the elements of \(T\) that are terms over the block \((c,s,c')\).

## Remarks

The integral defining \(A\) is a Bochner integral with the convention that it is \(0\) when the integrand is not integrable, and the sum \(A_T\) is \(0\) when the family is not summable; the product \(\beta_c(y)\beta_{c'}(\gamma_\infty^{-1}y)\in[0,\infty]\) enters through its real value (\(\infty\) read as \(0\)). The estimates of the area show integrability and summability in the cases used. Divided by the [[proofs/grh/spanning-unfolding-b/filling-constants|unipotent covolume]], \(A_T(c,s,c')\) is the contribution of \(T\) to the block \((c,s,c')\) of the second moment.

## References

1. Lean: `New.Filling.besselFn`, `New.Filling.besselKernel`, `New.Filling.amplitude`, `New.Filling.amplitudeMajorant`, `New.Filling.amplitudeSum` in `src/New/Spanning/Unfolding/Setup.lean`.
