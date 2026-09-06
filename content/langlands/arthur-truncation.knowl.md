+++
id = "langlands/arthur-truncation"
title = "Arthur truncation"
kind = "construction"
summary = "An alternating subtraction of parabolic constant terms that makes automorphic kernels rapidly decreasing in cuspidal directions."
aliases = ["Arthur truncation operator", "Langlands-Arthur truncation", "Lambda^T truncation"]
domains = ["langlands", "harmonic-analysis"]
section_mode = "progressive"
prerequisites = ["algebraic-geometry-foundations/reductive-algebraic-group", "langlands-letter/knowls/global-local-fields-completions", "algebraic-geometry-foundations/parabolic-subgroup", "langlands/automorphic-form", "langlands/automorphic-constant-term"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(G\) be a connected
[[algebraic-geometry-foundations/reductive-algebraic-group|reductive group]]
over a
[[langlands-letter/knowls/global-local-fields-completions|global field]],
choose a minimal
[[algebraic-geometry-foundations/parabolic-subgroup|parabolic subgroup]], and
let \(T\) be a sufficiently regular point in the associated real chamber.
**Arthur's truncation operator** \(\Lambda^T\) replaces an
[[langlands/automorphic-form|automorphic function]] by an alternating sum of its
[[langlands/automorphic-constant-term|parabolic constant terms]], cut off by
chamber characteristic functions.

Schematically,

\[
(\Lambda^T\phi)(g)=
\sum_P(-1)^{\dim(A_P/A_G)}
\sum_{\delta\in P(F)\backslash G(F)}
\widehat\tau_P(H_P(\delta g)-T)\,\phi_P(\delta g),
\]

where \(P\) ranges over standard parabolic subgroups, \(H_P\) is the height
map, and \(\widehat\tau_P\) selects a positive cone.

## Purpose

Automorphic quotients are generally noncompact, so the kernel of a
[[harmonic-analysis/convolution-on-locally-compact-group|convolution]] operator
need not be integrable on the diagonal.  Truncation cancels its
asymptotic constant terms in the cusps.  The integral of the truncated kernel
is then defined and depends polynomial-exponentially on \(T\); a distinguished
constant term yields the
[[langlands/arthur-selberg-trace-formula|trace-formula]] distribution.

For a cuspidal [[langlands/automorphic-form|automorphic form]] every
proper-parabolic constant term vanishes,
so truncation leaves it unchanged in the sufficiently regular region.

## From truncation to weights

Unfolding the truncated kernel creates the combinatorial weight functions in
[[langlands/weighted-orbital-integral|weighted orbital integrals]] on the
geometric side and weighted characters on the spectral side.

## References

1. James Arthur, “A truncation process for reductive groups,” *Bulletin of the
   American Mathematical Society* 83 (1977), 748–750.
   [Project Euclid](https://projecteuclid.org/journals/bulletin-of-the-american-mathematical-society/volume-83/issue-4/A-truncation-process-for-reductive-groups/bams/1183539458.full).
2. James Arthur, “An introduction to the trace formula,” in *Harmonic
   Analysis, the Trace Formula, and Shimura Varieties*, Clay Mathematics
   Proceedings 4, 2005, §§13–14.
   [Clay](https://www.claymath.org/library/cw/arthur/pdf/61.pdf).
