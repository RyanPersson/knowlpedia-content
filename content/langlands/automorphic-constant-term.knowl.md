+++
id = "langlands/automorphic-constant-term"
title = "Constant term of an automorphic form"
kind = "definition"
summary = "The integral of an automorphic form along the unipotent radical of a parabolic subgroup."
aliases = ["automorphic constant term", "constant term along a parabolic", "parabolic constant term"]
domains = ["langlands", "harmonic-analysis"]
section_mode = "progressive"
prerequisites = ["langlands-letter/knowls/global-local-fields-completions", "algebraic-geometry-foundations/reductive-algebraic-group", "algebraic-geometry-foundations/parabolic-subgroup", "algebraic-geometry-foundations/unipotent-radical", "langlands/automorphic-form", "langlands-letter/knowls/adeles-restricted-product", "harmonic-analysis/haar-measure", "algebraic-geometry-foundations/levi-subgroup", "harmonic-analysis/parabolic-modulus-character"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(F\) be a
[[langlands-letter/knowls/global-local-fields-completions|global field]], let
\(G\) be a connected
[[algebraic-geometry-foundations/reductive-algebraic-group|reductive
\(F\)-group]], and let \(P=MN\) be a
[[algebraic-geometry-foundations/parabolic-subgroup|parabolic subgroup]] with
[[algebraic-geometry-foundations/unipotent-radical|unipotent radical]] \(N\).
For an [[langlands/automorphic-form|automorphic form]] \(\phi\) on
\(G(F)\backslash G(\mathbb A_F)\), where \(\mathbb A_F\) is the
[[langlands-letter/knowls/adeles-restricted-product|adele ring]], its
**constant term along \(P\)** is

\[
\phi_P(g)=
\int_{N(F)\backslash N(\mathbb A_F)}\phi(ng)\,dn.
\]

The quotient is compact for unipotent \(N\), so the integral is well-defined
for the standard classes of automorphic forms after fixing
[[harmonic-analysis/haar-measure|Haar measure]]. The
result transforms as an automorphic function on the
[[algebraic-geometry-foundations/levi-subgroup|Levi subgroup]] \(M\), with a
normalization depending on whether the
[[harmonic-analysis/parabolic-modulus-character|factor
\(\delta_P^{-1/2}\)]] is included.

## Cuspidality

An automorphic form is
[[langlands/cuspidal-automorphic-representation|cuspidal]] exactly when
\(\phi_P=0\) for every proper
parabolic subgroup \(P\).  This vanishing removes all contributions arriving
from lower-rank Levi subgroups.

## Eisenstein series and truncation

Constant terms of [[langlands-letter/knowls/eisenstein-series|Eisenstein
series]] are finite sums involving standard intertwining operators.  Their
asymptotics control poles,
[[langlands/residual-automorphic-spectrum|residual representations]], and the
[[langlands/continuous-automorphic-spectrum|continuous spectrum]].
[[langlands/arthur-truncation|Arthur truncation]] subtracts selected
constant terms in the cuspidal directions to make
[[langlands/arthur-selberg-trace-formula|trace-formula]] kernels
integrable.

## References

1. Robert P. Langlands, *On the Functional Equations Satisfied by Eisenstein
   Series*, Lecture Notes in Mathematics 544, Springer, 1976, Chapter II.
2. James Arthur, “An introduction to the trace formula,” in *Harmonic
   Analysis, the Trace Formula, and Shimura Varieties*, Clay Mathematics
   Proceedings 4, 2005, §§7 and 13.
   [Clay](https://www.claymath.org/library/cw/arthur/pdf/61.pdf).
