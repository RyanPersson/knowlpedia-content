+++
id = "real-analysis/completeness-equivalences"
title = "Completeness Equivalences"
kind = "knowl"
summary = "The least-upper-bound, Cauchy, monotone-convergence, and nested-interval properties are equivalent completeness principles for the real numbers."
aliases = ["completeness-equivalences", "Completeness Equivalences"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/completeness-equivalences.md"
+++

**Completeness equivalences.** For the ordered field $\mathbb R$, the following statements are equivalent:

1. **Least-upper-bound property:** every nonempty [[real-analysis/bounded-above|bounded-above]] subset of $\mathbb R$ has a [[real-analysis/supremum|supremum]].
2. **Cauchy completeness:** every [[topology/cauchy-sequence|Cauchy sequence]] in $\mathbb R$ converges in $\mathbb R$.
3. **Monotone convergence:** every bounded [[real-analysis/monotone-sequence|monotone sequence]] in $\mathbb R$ converges.
4. **Nested-interval property:** if $(I_n)$ is a nested sequence of nonempty closed bounded [[real-analysis/interval|intervals]] whose lengths tend to $0$, then $\bigcap_{n=1}^{\infty}I_n$ contains exactly one point.

## Remarks

For general ordered fields, additional hypotheses are needed for some of these formulations to be equivalent; the statement above concerns $\mathbb R$.
