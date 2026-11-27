+++
id = "proofs/grh/reduction-main/theorem-b-enough-forms"
title = "Theorem B: few translates span almost all of the target"
kind = "theorem"
summary = "The target has positive dimension d_T, and there is a set t of translates with #t · dim(source) <= 5 d_T log(1 + 2b^2) whose images of the source span at least (1 - 4/b^2) d_T dimensions."
aliases = ["Theorem B", "enough forms", "enough_forms"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.enough_forms", "New.Data.exists_le_finrank_iSup_range_normalizedPoincare", "New.Data.five_halves_mul_one_add_log_le", "New.Data.targetDim_pos"]
lean_files = ["src/New/Reduction/ShortAndEnough.lean"]
proof_status = "full"
+++

**Theorem B (enough forms).** Let \(D\) be [[proofs/grh/reduction-main/data|data]], \(\mathcal S\) the source, \(\mathcal T\) the target of dimension \(d_T\), \(\bar G\) the finite group and \(s\mathfrak p:\mathcal S\to\mathcal T\) the [[proofs/grh/reduction-main/normalized-poincare|normalised Poincaré maps]]. Then \(d_T\ge1\), and there is a finite set \(t\subseteq\bar G\) with
\[
\#t\cdot\dim\mathcal S\ \le\ 5\,d_T\log(1+2b^2)\qquad\text{and}\qquad\dim\sum_{s\in t}s\mathfrak p(\mathcal S)\ \ge\ \Bigl(1-\frac4{b^2}\Bigr)d_T .
\]

## Proof

Complete relative to: \(\mathcal S_X\ne0\) (`New.Data.sourceFormCoords`); \(d_T\ne0\) (`New.Data.finrank_targetForms_ne_zero`); the spanning theorem [[?lean:New.Data.isSpread_goodPoincare|the good Poincaré maps spread]] with error \(\tfrac32\varepsilon_0\), \(\varepsilon_0=(8b^2)^{-1}\) (for every subspace \(F\subseteq\mathcal T\) of share \(\alpha=\dim F/d_T\) some \(\mathrm{gp}_s^{-1}(F)\) has dimension \(\le(\tfrac{1+\alpha}2+\tfrac32\varepsilon_0)D_X\)); the linear-algebra theorem [[?lean:New.IsSpread.exists_few_le_finrank_iSup_range|few maps span almost everything]]; and the dimension bound \(D_X-\dim\mathcal S\le\frac f{N-1}D_X\le b^{-8}D_X\) ([[?lean:New.Data.le_finrank_ramifiedSourceForms|dimension of the ramified forms]]).

The theorem on few maps needs both spaces nonzero: \(d_T>0\) as quoted, and \(\mathcal S_X\ne0\) because the source coordinate isomorphism (`New.Data.sourceFormCoords`, another area) identifies \(\mathcal S_X\) with a nonzero coordinate space. Since \(0<\varepsilon_0<1/16\), the theorem gives \(t\subseteq\bar G\) with
\[
\#t\cdot D_X\le\tfrac52\bigl(1+\log\tfrac1{16\varepsilon_0}\bigr)d_T,\qquad\dim\sum_{s\in t}\mathrm{gp}_s(\mathcal S_X)\ge(1-16\varepsilon_0)d_T=\bigl(1-\tfrac2{b^2}\bigr)d_T .
\]
Here \(\frac1{16\varepsilon_0}=b^2/2\le1+2b^2\) and \(1\le\log(1+2b^2)\) (as \(b^2\ge2\)), so \(\tfrac52(1+\log\frac{b^2}2)\le5\log(1+2b^2)\); with \(\dim\mathcal S\le D_X\) this is the first claim.

For the second, restricting each map to the subspace \(\mathcal S\) lowers the dimension of the sum of the images by at most \(\#t\,(D_X-\dim\mathcal S)\) (`New.finrank_biSup_range_le`), and
\[
\#t\,(D_X-\dim\mathcal S)\le b^{-8}\,\#t\,D_X\le b^{-8}\cdot5\log(1+2b^2)\,d_T\le\frac2{b^2}d_T .
\]
Finally \(s\mathfrak p(\mathcal S)=\mathrm{gp}_s(\mathcal S)\) (property (4) of the normalised Poincaré maps), so \(\dim\sum_{s\in t}s\mathfrak p(\mathcal S)\ge(1-\tfrac2{b^2}-\tfrac2{b^2})d_T\).

## References

1. Lean: `New.Data.enough_forms`, `New.Data.exists_le_finrank_iSup_range_normalizedPoincare` in `src/New/Reduction/ShortAndEnough.lean`.
