+++
id = "convex-analysis/nonnegative-real-less-than-every-0-must-be-zero"
title = "A nonnegative real below every epsilon is zero"
kind = "knowl"
summary = "A nonnegative real number smaller than every positive real number must be zero."
aliases = ["nonnegative-real-less-than-every-0-must-be-zero", "A nonnegative real below every epsilon is zero"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/nonnegative-real-less-than-every-0-must-be-zero.md"
+++

**Lemma.**
Let \(\ell\ge 0\) be a real number. If
\[
\ell<\varepsilon \quad\text{for every }\varepsilon>0,
\]

then \(\ell=0\).

**Proof.** If \(\ell>0\), choose \(\varepsilon=\ell/2\). Then \(\varepsilon<\ell\), contradicting the hypothesis. Hence \(\ell=0\).

## Remarks

This lemma is commonly used to conclude equality from estimates that hold for all \(\varepsilon>0\), e.g. in [[convex-analysis/uniqueness-of-limits-in-metric-spaces|uniqueness of limits]].
