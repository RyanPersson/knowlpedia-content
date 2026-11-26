+++
id = "proofs/grh/reduction-zeros/legendre-as-jacobi-of-odd-part"
title = "Reciprocity: the Legendre symbol modulo d as a Jacobi symbol of -d"
kind = "lemma"
summary = "For a prime d = 7 mod 8 and n >= 1, (n/d) equals the Jacobi symbol (-d / odd part of n)."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.legendreSym_eq_jacobiSym_ordCompl"]
lean_files = ["src/Lib/Analytic/QuadraticTwist.lean"]
proof_status = "full"
+++

**Lemma.** Let \(d\) be a prime with \(d\equiv7\pmod8\) and \(n\ge1\) an integer with odd part \(n^{\circ}\). Then
\[
\Bigl(\frac nd\Bigr)=\Bigl(\frac{-d}{n^{\circ}}\Bigr),
\]
a [[?c:Legendre symbol|Legendre symbol]] on the left and a [[?c:Jacobi symbol|Jacobi symbol]] on the right.

## Proof

Write \(n=2^{k}m\) with \(m=n^\circ\) odd. Since \(d\equiv7\pmod 8\), \((2/d)=1\), so \((n/d)=(m/d)\). By [[?c:quadratic reciprocity for the Jacobi symbol|quadratic reciprocity]] and \(d\equiv3\pmod4\): \((m/d)=(-1)^{(m-1)/2}(d/m)=(-1/m)(d/m)=(-d/m)\). \(\blacksquare\)

## References

1. Lean: `New.legendreSym_eq_jacobiSym_ordCompl` in `src/Lib/Analytic/QuadraticTwist.lean`.
