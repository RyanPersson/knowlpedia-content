+++
id = "proofs/grh/reduction-main/log-bound-calculus"
title = "Calculus of logarithmic bounds for the sizes of the data"
kind = "notation"
summary = "The bookkeeping device by which inequalities between quantities of the data are proved: upper and lower exponents on a logarithmic scale, compared by a linear problem in log x, log x1, log b, log log b, log log x1 and the constant bound."
aliases = ["HasLogBound", "HasLogUpper", "HasLogLower", "le_of_hasLogBound", "scale inequalities"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.HasLogBound", "New.Data.HasLogUpper", "New.Data.HasLogLower", "New.Data.le_constantBound", "New.Data.scale_inequalities", "New.Data.lt_of_hasLogBound", "New.Data.le_of_hasLogBound", "New.Data.nat_lt_of_hasLogBound", "New.Data.nat_le_of_hasLogBound", "New.Data.HasLogBound.pos", "New.Data.HasLogBound.of_mem_Icc", "New.Data.HasLogBound.of_lower_of_upper"]
lean_files = ["src/New/Reduction/Data/Magnitudes.lean"]
+++

Let \(D\) be [[proofs/grh/reduction-main/data|data]]. For a real number \(F\) and an exponent \(l\in\mathbb R\) we say \(F\) **has upper exponent \(l\)** if \(\lvert F\rvert\le e^{l}\), and **has lower exponent \(l\)** if \(e^{l}\le F\) (so \(F>0\)).

Exponents are propagated by the rules: \(1\) has exponents \(0,0\); \(e^c\) has \(c,c\); a product has the sums of the exponents; a power \(F^A\) has \(A\) times them; \(\sqrt F\) half of them; an inverse the negatives (swapped); a sum \(F+G\) of quantities has upper exponent \(\max(l,l')+1\) and, for the lower bound, \(\max(l,l')\). The basic quantities have the exponents given by the definition of the data, e.g. \(m\): \([\tfrac12\log x,\tfrac12\log x+2]\); \(r\): \([5\log x,5\log x+3]\); \(p_i\): \([10\log b,11\log b]\); \(\log b\): \(\log\log b\).

**Comparison principle.** If \(F\) has upper exponent \(l\), \(G\) has lower exponent \(l'\) and \(l<l'\), then \(F<G\). The inequality \(l<l'\) is in every use a linear inequality in \(\log x,\log x_1,\log b,\log\log b,\log\log x_1\) and \(c_P\), which follows from the five scale inequalities (S1)–(S5) of the data.

## Remarks

In the Lean source this is a type class with the exponent as output parameter, so that the exponents are computed by instance search and the final linear problem is decided by the tactic `grind`. In this human-readable proof, a step justified "by the sizes of the data" or "by the calculus of logarithmic bounds" means such a comparison; where the knowls of this chapter give the comparison explicitly it has been checked by hand, and elsewhere it is asserted with the Lean declaration that proves it.

## References

1. Lean: `New.Data.HasLogBound` and the declarations in the front matter, in `src/New/Reduction/Data/Magnitudes.lean`.
