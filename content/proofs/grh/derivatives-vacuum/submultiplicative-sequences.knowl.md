+++
id = "proofs/grh/derivatives-vacuum/submultiplicative-sequences"
title = "A lower bound along a sparse set extends to a submultiplicative sequence"
kind = "lemma"
summary = "If a submultiplicative sequence with values in [0,1] and c_0 = 1 satisfies b^q <= c_q for arbitrarily large q, with 0 < b <= 1, then b^n <= c_n for all n."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.pow_le_of_submultiplicative"]
lean_files = ["src/New/Derivatives/Sharpness/OneCurve.lean"]
proof_status = "full"
+++

**Lemma.** Let \(0<b\le1\) and let \((c_n)_{n\ge0}\) be real numbers with \(c_0=1\), \(0\le c_n\le1\) and \(c_{m+n}\le c_mc_n\). If for every \(M\) there is \(q\ge M\) with \(b^q\le c_q\), then \(b^n\le c_n\) for all \(n\).

## Proof

This is a form of [[?c:Fekete's subadditive lemma|Fekete's lemma]]. Let \(n\ge1\) and suppose \(c_n<b^n\); put \(r=c_n/b^n<1\). Choose \(k\) with \(r^k<b^n\) and \(q\ge kn\) with \(b^q\le c_q\). Write \(q=n\lfloor q/n\rfloor+(q\bmod n)\). Then, using \(b\le1\) and \(q<n(\lfloor q/n\rfloor+1)\),
\[ b^{n}\,(b^n)^{\lfloor q/n\rfloor}\le b^q\le c_q\le c_{n\lfloor q/n\rfloor}\,c_{q\bmod n}\le c_n^{\lfloor q/n\rfloor}, \]
so \(b^n\le r^{\lfloor q/n\rfloor}\le r^k<b^n\) (as \(\lfloor q/n\rfloor\ge k\)), a contradiction.

## References

1. Lean: `New.pow_le_of_submultiplicative` in `src/New/Derivatives/Sharpness/OneCurve.lean`.
