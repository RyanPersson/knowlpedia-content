+++
id = "langlands/weighted-orbital-integral"
title = "Weighted orbital integral"
kind = "definition"
summary = "An orbital integral multiplied by Arthur's parabolic weight, forming the fine geometric terms of the trace formula."
aliases = ["Arthur weighted orbital integral", "weighted orbital integral J_M", "J_M(gamma,f)"]
domains = ["langlands", "harmonic-analysis"]
prerequisites = ["algebraic-geometry-foundations/reductive-algebraic-group", "algebra-fields-galois/local-field", "algebraic-geometry-foundations/levi-subgroup", "convex-analysis/convex-hull", "algebraic-geometry-foundations/parabolic-subgroup", "langlands/orbital-integral"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(G\) be a connected
[[algebraic-geometry-foundations/reductive-algebraic-group|reductive group]]
over a [[algebra-fields-galois/local-field|local field]],
let \(M\) be a
[[algebraic-geometry-foundations/levi-subgroup|Levi subgroup]], and let
\(\gamma\in M(F)\) be regular enough for the integral below.  An **Arthur
weighted orbital integral** has the form

\[
J_M(\gamma,f)=
\int_{G_\gamma(F)\backslash G(F)}
f(x^{-1}\gamma x)\,v_M(x)\,dx.
\]

Here \(v_M(x)\) is a nonnegative weight built from the
[[convex-analysis/convex-hull|convex hull]] of the Iwasawa height vectors of
\(x\) for the
[[algebraic-geometry-foundations/parabolic-subgroup|parabolic subgroups]] with
Levi \(M\).
When \(M=G\), the weight is \(1\) and \(J_G(\gamma,f)\) is the ordinary
[[langlands/orbital-integral|orbital integral]].

## Why the weight appears

[[langlands/arthur-truncation|Arthur truncation]] cuts a noncompact
automorphic kernel in several parabolic directions.  After unfolding, the
volume of the resulting truncation polytope produces \(v_M(x)\).  Weighted
orbital integrals therefore encode contributions induced from proper Levi
subgroups on the fine geometric side of the
[[langlands/arthur-selberg-trace-formula|trace formula]].

## Invariance and transfer

The initial distributions \(J_M(\gamma,\cdot)\) are generally noninvariant.
Arthur combines them with correction terms to form invariant distributions
\(I_M(\gamma,\cdot)\). Stabilizing these terms requires weighted
[[langlands/endoscopic-transfer|endoscopic transfer]], which is subtler than
the unweighted [[langlands/fundamental-lemma|fundamental lemma]].

## References

1. James Arthur, “An introduction to the trace formula,” in *Harmonic
   Analysis, the Trace Formula, and Shimura Varieties*, Clay Mathematics
   Proceedings 4, 2005, §§11 and 18–19.
   [Clay](https://www.claymath.org/library/cw/arthur/pdf/61.pdf).
2. James Arthur, “The local behaviour of weighted orbital integrals,” *Duke
   Mathematical Journal* 56 (1988), 223–293.
