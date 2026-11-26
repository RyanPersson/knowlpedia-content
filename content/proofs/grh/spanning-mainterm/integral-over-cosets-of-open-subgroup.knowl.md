+++
id = "proofs/grh/spanning-mainterm/integral-over-cosets-of-open-subgroup"
title = "Integral of a function constant on the cosets of an open subgroup"
kind = "lemma"
summary = "For a left invariant measure and an open subgroup J of finite volume, the integral of a function of the coset yJ is the volume of J times the sum over the cosets."
aliases = ["integral_comp_quotientMk"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.integral_comp_quotientMk"]
lean_files = ["src/New/Spanning/MainTerm/KloostermanSum.lean"]
proof_status = "full"
+++

**Lemma.** Let \(G\) be a second countable [[?c:Topological group|topological group]] with its
Borel \(\sigma\)-algebra, let \(\mu\) be a measure on \(G\) invariant under left translations,
and let \(J\subseteq G\) be an open subgroup with \(\mu(J)<\infty\). For every function
\(f\colon G/J\to\mathbb C\) on the set of left [[algebra-groups/coset|cosets]],

\[
  \int_Gf(yJ)\,d\mu(y)\;=\;\mu(J)\sum_{q\in G/J}f(q),
\]

with the convention that both sides are \(0\) when \(f\) is not absolutely summable.

## Proof

Since \(J\) is open, \(G/J\) is discrete, and since \(G\) is second countable (hence separable),
\(G/J\) is countable. The quotient map \(\pi\colon G\to G/J\) is measurable for the discrete
\(\sigma\)-algebra. The fibre of \(\pi\) over \(aJ\) is the translate \(aJ\), of measure
\(\mu(aJ)=\mu(J)\) by left invariance. A measure on a countable set is determined by its values
on points, so the [[measure-theory/pushforward-measure|pushforward]] \(\pi_*\mu\) is \(\mu(J)\)
times the [[?c:Counting measure|counting measure]]. By the change of variables formula for the
pushforward,
\(\int_Gf\circ\pi\,d\mu=\int_{G/J}f\,d\pi_*\mu=\mu(J)\int_{G/J}f\,d(\text{counting})\). The
integral for the counting measure on a countable set is the sum \(\sum_qf(q)\) when \(f\) is
absolutely summable; otherwise \(f\) is not integrable and both the integral and (by convention)
the sum are \(0\). \(\blacksquare\)

## References

1. Lean: `New.integral_comp_quotientMk` in `src/New/Spanning/MainTerm/KloostermanSum.lean`.
