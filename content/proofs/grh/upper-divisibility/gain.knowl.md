+++
id = "proofs/grh/upper-divisibility/gain"
title = "Gain at a prime"
kind = "definition"
summary = "The exponent of p asked to divide the composite of the m lifts: m times the prime sums at the a-places plus k times the total."
aliases = ["gain", "gain at p"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.gain"]
lean_files = ["src/New/UpperBound/Size/ShortColumns.lean"]
+++

Let \(D\) be [[?lean:New.Data|admissible data]], with number of lifts \(m\), rank \(k\) of \(X_0\), long order \(a=xb\) and set \(\Phi_a\) of [[?lean:New.Data.aPlaces|a-places]]. For a natural number \(p\), the **gain at \(p\)** is the real number
\[
\operatorname{gain}(p)\;=\;m\Bigl(\sum_{\tau\in\Phi_a}s_p(a,\tau)\;+\;k\,F(p)\Bigr),
\]
where \(s_p\) is the [[proofs/grh/upper-divisibility/local-prime-sum|local prime sum]] and \(F(p)\) its total over all infinite places.

## Remarks

The gain is the exponent of \(p\) that the [[proofs/grh/upper-divisibility/local-divisibility-of-the-composite-lift|local divisibility theorem]] shows, up to an explicit error, to divide the [[?lean:New.Data.compositeLift|composite lift]] of an integral source form. The first summand comes from the derivatives of order \(a\) at the a-places; the second from the \(k\) further directions in which each lift differentiates.

## References

1. Lean: `New.Data.gain` in `src/New/UpperBound/Size/ShortColumns.lean`.
