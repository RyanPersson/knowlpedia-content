+++
id = "langlands/local-gamma-factor"
title = "Local gamma factor"
kind = "definition"
summary = "The local functional-equation factor combining epsilon and the ratio of dual L-factors."
aliases = ["gamma factor", "local gamma factor of a representation", "gamma(s,V,psi)"]
domains = ["langlands", "number-theory", "harmonic-analysis"]
prerequisites = ["langlands/weil-deligne-representation", "algebra-fields-galois/local-field", "algebra-representation-theory/character", "langlands-letter/knowls/contragredient-representation"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

For a [[langlands/weil-deligne-representation|Weil–Deligne representation]]
\(V\) of a
[[algebra-fields-galois/local-field|local field]]
\(F\) and a nontrivial additive
[[algebra-representation-theory/character|character]] \(\psi\), the **local
gamma factor** is

\[
\gamma(s,V,\psi)=
\varepsilon(s,V,\psi)
\frac{L(1-s,V^\vee)}{L(s,V)},
\]

where \(\varepsilon(s,V,\psi)\) is the
[[langlands/local-epsilon-factor|local epsilon factor]] and \(V^\vee\) is the
[[langlands-letter/knowls/contragredient-representation|dual
representation]]. This convention places the functional equation around
\(s=\tfrac12\); shifts occur when an L-function is normalized differently.

## Analytic characterization

In Tate's thesis the factor is characterized by the local functional equation
for [[harmonic-analysis/fourier-transform-lca|Fourier transforms]].
Higher-rank Rankin–Selberg integrals and the
Langlands–Shahidi method similarly compare a zeta integral with its dual and
produce a gamma factor.

Gamma factors are especially useful because local converse theorems can
recognize a representation from families of twisted gamma factors.  Under
[[langlands/local-langlands-correspondence-for-gln|local Langlands for
\(\operatorname{GL}_n\)]], the analytic factors agree with the corresponding
Artin factors on the Weil–Deligne side.

## Convention warning

Some authors write the quotient of L-factors in the reciprocal order or use
\(\psi^{-1}\) on the dual side.  A bare symbol \(\gamma(s,\cdots)\) is therefore
not portable without its functional equation.

## References

1. John Tate, “Fourier analysis in number fields and Hecke's zeta-functions,”
   in *Algebraic Number Theory*, Academic Press, 1967, 305–347.
2. Hervé Jacquet, Ilya Piatetski-Shapiro, and Joseph Shalika,
   “Rankin–Selberg convolutions,” *American Journal of Mathematics* 105
   (1983), 367–464. [JSTOR](https://doi.org/10.2307/2374264).
