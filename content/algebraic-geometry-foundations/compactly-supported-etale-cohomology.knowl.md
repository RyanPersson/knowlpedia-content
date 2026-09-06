+++
id = "algebraic-geometry-foundations/compactly-supported-etale-cohomology"
title = "Compactly supported étale cohomology"
kind = "definition"
summary = "Étale cohomology formed with the exceptional direct image, retaining only classes with proper support."
aliases = ["étale cohomology with compact support", "compact support etale cohomology", "H_c etale"]
domains = ["algebraic-geometry-foundations", "langlands", "algebra-homological"]
section_mode = "progressive"
prerequisites = ["algebraic-geometry-foundations/scheme", "algebraic-geometry-foundations/small-etale-site", "algebra-homological/cochain-complex"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(X\) be a separated [[algebraic-geometry-foundations/scheme|scheme]] of
finite type over a field \(k\), let
\(f:X\to\operatorname{Spec}k\), and let \(\mathcal F\) be a sheaf on the
[[algebraic-geometry-foundations/small-etale-site|étale site]] or a
[[algebra-homological/cochain-complex|complex]] with suitable torsion or
\(\ell\)-adic coefficients. Its
**compactly supported étale cohomology** is

\[
H_c^i(X_{\bar k},\mathcal F)
=H^i\!\left(\operatorname{Spec}\bar k,
Rf_!\mathcal F\right).
\]

The exceptional direct image \(Rf_!\) retains sections whose support is proper
over the base.

## Compactification description

If \(j:X\hookrightarrow\overline X\) is an open immersion into a proper
scheme, then

\[
R\Gamma_c(X_{\bar k},\mathcal F)
\simeq R\Gamma(\overline X_{\bar k},j_!\mathcal F).
\]

The result is independent of the chosen compactification.  If \(X\) itself is
proper, compactly supported and ordinary étale cohomology agree.

## Arithmetic role

For a variety over a [[algebra-fields-galois/finite-field|finite field]],
[[algebra-fields-galois/frobenius-endomorphism|Frobenius]] acts on \(H_c^i\).
The
Grothendieck–Lefschetz trace formula expresses point counts as an alternating
sum of traces on these groups.  In the Langlands program, compactly supported
cohomology of [[langlands/shtuka|shtuka]] and
[[langlands/local-shtuka|local-shtuka]] spaces carries commuting Hecke and
[[langlands-letter/knowls/galois-extension-and-group|Galois]] actions.

## References

1. Alexander Grothendieck, *SGA 4*, Exposé XVII, Lecture Notes in Mathematics
   305, Springer, 1973.
2. The Stacks Project Authors, “More Étale Cohomology,” §63.12,
   “Compactly supported cohomology.”
   [Stacks Project](https://stacks.math.columbia.edu/tag/0GJY).
