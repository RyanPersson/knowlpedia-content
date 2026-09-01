+++
id = "langlands/stable-distribution"
title = "Stable distribution"
kind = "definition"
summary = "An invariant distribution that depends only on stable orbital-integral data."
aliases = ["stable invariant distribution", "stable character distribution", "stable virtual character"]
domains = ["langlands", "harmonic-analysis"]
prerequisites = ["algebraic-geometry-foundations/reductive-algebraic-group", "algebra-fields-galois/local-field", "harmonic-analysis/distribution-local-group", "langlands/strongly-regular-semisimple-element", "langlands/stable-orbital-integral", "algebra-groups/conjugacy-class", "langlands/stable-conjugacy"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(G\) be a connected
[[algebraic-geometry-foundations/reductive-algebraic-group|reductive group]]
over a [[algebra-fields-galois/local-field|local field]]
\(F\). An
[[harmonic-analysis/distribution-local-group|invariant distribution]]
\(D\) on \(C_c^\infty(G(F))\) is **stable** if

\[
D(f)=0
\]

whenever all [[langlands/strongly-regular-semisimple-element|strongly regular
semisimple]]
[[langlands/stable-orbital-integral|stable orbital integrals]] of \(f\) vanish.
Equivalently, \(D\) factors through the space of stable orbital-integral data
rather than depending on the individual
[[algebra-groups/conjugacy-class|\(G(F)\)-conjugacy classes]] inside a
[[langlands/stable-conjugacy|stable class]].

This functional definition remains meaningful when a distribution has no
pointwise character function.

## Packet characters

For a tempered [[langlands/l-packet|L-packet]] \(\Pi_\varphi\) on a
[[algebraic-geometry-foundations/quasi-split-reductive-group|quasi-split
group]], the appropriately normalized sum

\[
S\Theta_\varphi=\sum_{\pi\in\Pi_\varphi}\Theta_\pi
\]

is expected, and in many established cases known, to be stable.  Other
characters of the parameter's
[[langlands/component-group-of-l-parameter|component group]] give generally
unstable weighted sums whose transfers come from
[[langlands/endoscopic-datum|endoscopic groups]].

## Global role

The [[langlands/stable-trace-formula|stable trace formula]] rewrites invariant
trace-formula distributions as combinations of stable distributions on
endoscopic groups. Stability is therefore the distributional language in
which [[langlands/endoscopic-transfer|packet transfer]] and
[[langlands-letter/knowls/langlands-functoriality-l-homomorphism|functoriality]]
become visible.

## References

1. Robert P. Langlands and Diana Shelstad, “On the definition of transfer
   factors,” *Mathematische Annalen* 278 (1987), 219–271.
2. James Arthur, “A stable trace formula. I. General expansions,” *Journal of
   the Institute of Mathematics of Jussieu* 1 (2002), 175–277.
   [DOI](https://doi.org/10.1017/S147474800200005X).
