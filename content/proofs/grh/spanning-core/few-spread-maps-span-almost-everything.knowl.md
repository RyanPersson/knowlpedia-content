+++
id = "proofs/grh/spanning-core/few-spread-maps-span-almost-everything"
title = "Few spread maps span almost everything"
kind = "theorem"
summary = "The images of a logarithm times dim W / dim V members of a spread family span all but a small share of W."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.IsSpread.exists_few_le_finrank_iSup_range", "New.IsSpread.exists_codim_le", "New.IsSpread.exists_codim_le_max", "New.finrank_sup_range_add_finrank_comap"]
lean_files = ["src/New/Spanning/SecondMoment/FewTranslates.lean"]
proof_status = "full"
+++

**Theorem (few maps span almost everything).** Let \(V\neq0\) and \(W\neq0\) be finite-dimensional complex vector spaces, \(0<\varepsilon<\tfrac1{16}\), and \((B_s)_{s\in\Theta}\) a family of linear maps \(V\to W\) that is [[proofs/grh/spanning-core/spread-family-of-linear-maps|spread]] with error \(\tfrac32\varepsilon\). Then there is a finite set \(t\subseteq\Theta\) with
\[
\lvert t\rvert\cdot\dim V\le\frac52\Bigl(1+\log\frac1{16\varepsilon}\Bigr)\dim W\qquad\text{and}\qquad\dim\sum_{s\in t}B_s(V)\ \ge\ (1-16\varepsilon)\dim W .
\]

## Proof

Write \(\mathrm{rate}=\dfrac{2\dim V}{5\dim W}>0\) and, for a subspace \(F\subseteq W\), \(\operatorname{codim}F=\dim W-\dim F\).

*Step 0 (a dimension count).* For a linear map \(A\colon V\to W\) and a subspace \(F\subseteq W\),
\[
\dim\bigl(F+A(V)\bigr)+\dim A^{-1}(F)=\dim F+\dim V .
\]
Indeed \(A\) maps \(A^{-1}(F)\) onto \(F\cap A(V)\) with kernel \(\ker A\), so \(\dim A^{-1}(F)=\dim(F\cap A(V))+\dim\ker A\); combine with \(\dim(F+A(V))+\dim(F\cap A(V))=\dim F+\dim A(V)\) and the [[linear-algebra/rank-nullity-theorem|rank–nullity theorem]].

*Step 1 (one greedy step).* Let \(F\subseteq W\) with \(\operatorname{codim}F>16\varepsilon\dim W\). Then some \(s\) has
\[
\operatorname{codim}\bigl(F+B_s(V)\bigr)\le(1-\mathrm{rate})\operatorname{codim}F .
\]
Let \(\alpha=\dim F/\dim W\le1\); the hypothesis says \(16\varepsilon<1-\alpha\). Spreading gives \(s\) with \(\dim B_s^{-1}(F)\le\bigl(\tfrac{1+\alpha}2+\tfrac32\varepsilon\bigr)\dim V\le\bigl(1-\tfrac25(1-\alpha)\bigr)\dim V\), since \(\tfrac32\varepsilon<\tfrac3{32}(1-\alpha)\) and \(\tfrac12-\tfrac3{32}\ge\tfrac25\). By Step 0, \(\dim(F+B_s(V))\ge\dim F+\tfrac25(1-\alpha)\dim V\), and \(\tfrac25(1-\alpha)\dim V=\mathrm{rate}\cdot\operatorname{codim}F\).

*Step 2 (\(l\) steps).* For every \(l\ge0\) there is \(t\subseteq\Theta\) with \(\lvert t\rvert\le l\) and
\[
\operatorname{codim}\sum_{s\in t}B_s(V)\le\max\bigl(16\varepsilon,\ e^{-l\cdot\mathrm{rate}}\bigr)\dim W .
\]
Induction on \(l\): for \(l=0\) take \(t=\emptyset\). Given \(t\) for \(l\), with span \(F\): if \(\operatorname{codim}F\le16\varepsilon\dim W\) keep \(t\). Otherwise \(\operatorname{codim}F\le e^{-l\cdot\mathrm{rate}}\dim W\), and Step 1 gives \(s\) with \(\operatorname{codim}(F+B_s(V))\le(1-\mathrm{rate})\operatorname{codim}F\le e^{-\mathrm{rate}}e^{-l\cdot\mathrm{rate}}\dim W\), using \(1-u\le e^{-u}\) and \(\operatorname{codim}F\ge0\); take \(t\cup\{s\}\).

*Step 3 (\(\mathrm{rate}\le1\)).* Step 1 applies to \(F=0\) because \(16\varepsilon<1\), and gives \(0\le\operatorname{codim}B_s(V)\le(1-\mathrm{rate})\dim W\).

*Step 4.* As \(16\varepsilon<1\), \(\log\frac1{16\varepsilon}\ge0\). Let \(l=\bigl\lceil\log\frac1{16\varepsilon}/\mathrm{rate}\bigr\rceil\). Then \(\log\frac1{16\varepsilon}\le l\cdot\mathrm{rate}\le\mathrm{rate}+\log\frac1{16\varepsilon}\le1+\log\frac1{16\varepsilon}\). The first inequality gives \(e^{-l\cdot\mathrm{rate}}\le16\varepsilon\), so the set \(t\) of Step 2 spans a subspace of codimension at most \(16\varepsilon\dim W\). Finally \(\lvert t\rvert\dim V\le l\dim V=\tfrac52\,(l\cdot\mathrm{rate})\dim W\le\tfrac52\bigl(1+\log\frac1{16\varepsilon}\bigr)\dim W\). \(\blacksquare\)

## References

1. Lean: `New.IsSpread.exists_few_le_finrank_iSup_range`, with the steps `New.finrank_sup_range_add_finrank_comap`, `New.IsSpread.exists_codim_le`, `New.IsSpread.exists_codim_le_max`, in `src/New/Spanning/SecondMoment/FewTranslates.lean`.
2. L. A. Wolsey, An analysis of the greedy algorithm for the submodular set covering problem, 1982 (cited in the Lean file head for greedy covering with a logarithmic loss).
