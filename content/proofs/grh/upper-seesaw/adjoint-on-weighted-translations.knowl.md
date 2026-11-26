+++
id = "proofs/grh/upper-seesaw/adjoint-on-weighted-translations"
title = "Adjoints of integral matrices on weighted translations"
kind = "lemma"
summary = "The adjoint of an integral matrix maps one group of weighted translations into another when its entries vanish at the conjugate place wherever the weights differ."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Seesaw.conjTranspose_mulVec_mem_weightedTranslations", "New.Seesaw.star_mem_weightedTranslations", "New.Seesaw.mem_weightedTranslations"]
lean_files = ["src/New/UpperBound/Seesaw/NeighbourLattice.lean"]
proof_status = "full"
+++

Let \(E\) be a [[?c:CM field|CM field]], \(q\) a natural number, and \(d=(d_i)_{i\in n}\),
\(d'=(d'_j)_{j\in n_0}\) families of [[?c:Finite adele ring of a number field|finite adeles]]. Recall
the [[proofs/grh/upper-seesaw/translation-groups|groups of weighted translations]] \(T_q(d)\):
\(y\in T_q(d)\) iff \(\lvert d_i\rvert_w\lvert y_i\rvert_w\le1\) for all \(i\) and all finite places
\(w\nmid q\).

**Lemma.**

1. Let \(M\) be an \(n\times n_0\) matrix with integral entries such that \(M_{ij}\) vanishes at
   the place \(\bar w\) whenever \(d_i\) and \(d'_j\) have different valuations at \(w\). Then
   \(M^{*}\) maps \(T_q(d)\) into \(T_q(d')\).
2. Let \(c\) be an integral adele, \(x\in T_q(d)\) and \(f\colon X\to n\) any map of index sets.
   Then \(\bigl(c\,\overline{x_{f(i)}}\bigr)_{i\in X}\in T_q\bigl((\overline{d_{f(i)}})_{i\in X}\bigr)\).

## Proof

Complex conjugation exchanges the places \(w\) and \(\bar w\):
\(\lvert\bar a\rvert_w=\lvert a\rvert_{\bar w}\); and \(w\nmid q\) iff \(\bar w\nmid q\), since \(q\)
is rational.

(1) \((M^{*}y)_j=\sum_i\overline{M_{ij}}\,y_i\), and \(T_q(d')\) is a group, so it suffices to treat
one summand. Let \(w\nmid q\). If \(d_i\) and \(d'_j\) have the same valuation at \(w\), then
\(\lvert d'_j\rvert_w\lvert\overline{M_{ij}}y_i\rvert_w=\lvert M_{ij}\rvert_{\bar w}\cdot\lvert d_i\rvert_w\lvert y_i\rvert_w\le1\).
Otherwise \(\overline{M_{ij}}\) vanishes at \(w\).

(2) For \(w\nmid q\):
\(\lvert\overline{d_{f(i)}}\rvert_w\lvert c\,\overline{x_{f(i)}}\rvert_w=\lvert c\rvert_w\cdot\lvert d_{f(i)}x_{f(i)}\rvert_{\bar w}\le1\).
\(\blacksquare\)

## References

1. Lean: `New.Seesaw.conjTranspose_mulVec_mem_weightedTranslations`, `New.Seesaw.star_mem_weightedTranslations` in `src/New/UpperBound/Seesaw/NeighbourLattice.lean`.
