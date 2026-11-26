+++
id = "proofs/grh/spanning-core/equal-multiplicities-of-eigensystems"
title = "Equality of multiplicities"
kind = "theorem"
summary = "Each Hecke eigensystem has the same multiplicity in the good forms on two hermitian spaces that differ only in their signs; in particular the good forms on Y_0 and on W_j have the same dimension."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.finrank_goodForms_inf_eigenPart_eq", "New.Data.trace_heckeOnGood_eq_finrank", "New.Data.goodForms_inf_eigenPart_eq_bot_of_eq_bot", "New.Data.targetDim_eq_finrank_goodForms_spaceW"]
lean_files = ["src/New/Spanning/Multiplicities/EqualMultiplicities.lean"]
proof_status = "full"
+++

**Theorem (equality of multiplicities).** Let \(D\) be [[?lean:New.Data|admissible data]] and \(V,V'\) hermitian spaces of rank \(r\) over \(E\), with signs \(s,s'\) for both of which the doubled parameter [[?lean:New.HCParam.HasGap|has gap]] \(\Delta\) at every infinite place (as in [[proofs/grh/spanning-core/equal-traces-on-good-forms|equal traces]]). Let \(\mathcal G_V\) be the good forms and \(\mathcal F_V[q]\) the [[proofs/grh/spanning-core/hecke-eigensystem-part|eigensystem parts]]. Then for every eigensystem \(q\)
\[
\dim\bigl(\mathcal G_V\cap\mathcal F_V[q]\bigr)=\dim\bigl(\mathcal G_{V'}\cap\mathcal F_{V'}[q]\bigr).
\]
**Corollaries.**

1. An eigensystem that does not occur in the good forms of \(V'\) does not occur in those of \(V\).
2. For \(1\le j\le m\), the good forms on [[?lean:New.Data.spaceW|\(W_j\)]] have the dimension \(d_{\mathrm{tar}}\) of the [[?lean:New.Data.targetForms|target forms]] (the good forms on \(Y_0\)).

## Proof

The forms of principal level on \(V\) and \(V'\) are finite-dimensional. By [[proofs/grh/spanning-core/eigensystem-parts-decompose-the-forms|the decomposition]], the set \(F\) of eigensystems with a nonzero part on \(V\) or on \(V'\) is finite, and the parts span. By the [[proofs/grh/spanning-core/hecke-projector-onto-an-eigensystem|projector lemma]] there is \(T\in\mathcal H\) which, on \(V\) and on \(V'\), is the identity on the \(q\)-part and zero on the \(d\)-part for \(d\in F\), \(d\neq q\); for \(d\notin F\) the \(d\)-parts are zero, so the same holds for all \(d\).

*Trace of \(T\).* On \(W\in\{V,V'\}\): \(T_W\) maps every part into \(\mathcal F_W[q]\), hence all of \(\mathcal F_W\), and it preserves \(\mathcal G_W\); so \(T\) maps \(\mathcal G_W\) into \(\mathcal G_W\cap\mathcal F_W[q]\) and is the identity there. Thus \(T|_{\mathcal G_W}\) is a projection onto \(\mathcal G_W\cap\mathcal F_W[q]\), and its trace is \(\dim(\mathcal G_W\cap\mathcal F_W[q])\). By [[proofs/grh/spanning-core/equal-traces-on-good-forms|equal traces]] the two traces agree.

Corollary 1 is the case of dimension \(0\). For Corollary 2, apply equal traces to \(T=1\), \(V=Y_0\), \(V'=W_j\) (the gap hypothesis holds for the signs of \(Y_0\) and of \(W_j\), \(1\le j\le m\), by instances of the data): the trace of the identity is the dimension. \(\blacksquare\)

## References

1. Lean: `New.Data.finrank_goodForms_inf_eigenPart_eq`, `New.Data.goodForms_inf_eigenPart_eq_bot_of_eq_bot`, `New.Data.targetDim_eq_finrank_goodForms_spaceW` in `src/New/Spanning/Multiplicities/EqualMultiplicities.lean`.
