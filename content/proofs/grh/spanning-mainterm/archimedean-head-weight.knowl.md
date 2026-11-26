+++
id = "proofs/grh/spanning-mainterm/archimedean-head-weight"
title = "Weight of a head at an infinite place"
kind = "definition"
summary = "The product over the partial products of a head of max(1, 1/|delta|)^K, or zero when a partial product is larger than R."
aliases = ["headWeight", "head weight at a real place"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.headWeight", "New.headWeight_nonneg"]
lean_files = ["src/New/Spanning/MainTerm/SieveSystem.lean"]
+++

Let \(R\) be a real number, let \(K, i\) be natural numbers and let
\(p=(p_0,p_1,\dots)\) be a sequence of nonzero complex numbers (a *head* at an infinite place).
For \(l<i\) put \(\delta_l = p_0p_1\cdots p_l\). The **weight of the head \(p\) of length \(i\)**
is

\[
  \Lambda^{\infty}_{R,K,i}(p)\;=\;\prod_{l=0}^{i-1}
  \begin{cases}
    \max\bigl(1,\lvert\delta_l\rvert^{-1}\bigr)^{K} & \text{if } \lvert\delta_l\rvert\le R,\\
    0 & \text{otherwise.}
  \end{cases}
\]

It is a nonnegative real number, and it depends only on \(p_0,\dots,p_{i-1}\).

## Remarks

This is the weight \(\Lambda\) of the
[[proofs/grh/spanning-mainterm/sieve-system|sieve systems]] at the infinite places; its analogue
at a finite set of places is [[?lean:New.finHeadWeight|the weight of a head at the finite places]].
The two are multiplied in the
[[proofs/grh/spanning-mainterm/global-weight|global weight]].

## References

1. Lean: `New.headWeight`, `New.headWeight_nonneg` in `src/New/Spanning/MainTerm/SieveSystem.lean`.
