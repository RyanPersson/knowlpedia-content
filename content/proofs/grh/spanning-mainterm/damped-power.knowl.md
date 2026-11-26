+++
id = "proofs/grh/spanning-mainterm/damped-power"
title = "Damped power"
kind = "definition"
summary = "The function r^k min(1,r)^6 that measures the decay of a transform at an infinite place."
aliases = ["dampedPower", "gain at a ratio"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.dampedPower"]
lean_files = ["src/New/Spanning/MainTerm/SieveSystem.lean"]
+++

For a natural number \(k\) and a real number \(r\), the **damped power** is

\[
  \operatorname{dp}_k(r) \;=\; r^{k}\,\min(1,r)^{6}.
\]

## Remarks

In the [[proofs/grh/spanning-mainterm/sieve-over-all-places|sieve over all places]] it is
evaluated at \(r=\lvert \xi_v\rvert^{-1}\), the inverse modulus of the component of a frequency
\(\xi\) at an infinite place \(v\) (with the convention \(0^{-1}=0\)): the factor \(r^k\) records
the gain of the transform, and the factor \(\min(1,r)^6\) is the extra decay for large
frequencies that makes the
[[proofs/grh/spanning-mainterm/sum-over-frequencies-bound|sum over the frequencies]] converge.

## References

1. Lean: `New.dampedPower` in `src/New/Spanning/MainTerm/SieveSystem.lean`.
