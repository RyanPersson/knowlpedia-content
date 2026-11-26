+++
id = "proofs/grh/upper-elementary-divisors/interlacing-determinant"
title = "Interlacing as a determinant of indicators"
kind = "lemma"
summary = "For two weakly decreasing real sequences, the determinant of the matrix of indicators y_c < x_b is 1 if they interlace and 0 otherwise."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.det_interlacing_indicator"]
lean_files = ["src/New/UpperBound/ElementaryDivisors/PieriCone.lean"]
proof_status = "full"
+++

**Lemma.** Let \(x_0\ge x_1\ge\dots\ge x_{k-1}\) and \(y_0\ge\dots\ge y_{k-1}\) be real numbers and let \(M\) be the \(k\times k\) matrix with \(M_{bc}=1\) if \(y_c<x_b\) and \(0\) otherwise. Then \(\det M=1\) if \(x_0>y_0\ge x_1>y_1\ge\dots\ge x_{k-1}>y_{k-1}\) (that is, \(y_b<x_b\) for all \(b\) and \(x_{b+1}\le y_b\) for all \(b<k-1\)), and \(\det M=0\) otherwise.

## Proof

Induction on \(k\); the case \(k=0\) is trivial. Let \(k\ge1\).

*Case 1: \(y_0<x_b\) for some \(b\ge1\).* Then \(y_c\le y_0<x_b\le x_0\) for all \(c\), so rows \(0\) and \(b\) of \(M\) consist of ones and \(\det M=0\). Interlacing fails, since it would require \(x_b\le x_1\le y_0\).

*Case 2: \(x_b\le y_0\) for all \(b\ge1\).* Column \(0\) of \(M\) vanishes below its top entry, so expanding along it, \(\det M=[y_0<x_0]\cdot\det M'\), where \(M'\) is the matrix of the sequences \((x_b)_{b\ge1}\), \((y_c)_{c\ge1}\). By induction \(\det M'\) is the indicator of interlacing of the tails. Since \(x_1\le y_0\) holds in this case, interlacing of \((x,y)\) is equivalent to \(y_0<x_0\) together with interlacing of the tails. \(\square\)

## References

1. Lean: `New.det_interlacing_indicator` in `src/New/UpperBound/ElementaryDivisors/PieriCone.lean`.
