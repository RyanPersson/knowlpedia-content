+++
id = "langlands/orbital-integral"
title = "Orbital integral"
kind = "knowl"
summary = "The invariant distribution obtained by integrating a test function over a conjugacy orbit."
aliases = ["orbital integrals", "semisimple orbital integral"]
domains = ["langlands", "harmonic-analysis", "representation-theory"]
section_mode = "progressive"
+++

Let \(F\) be a
[[langlands-letter/knowls/global-local-fields-completions|local field]], let
\(G\) be a connected
[[algebraic-geometry-foundations/reductive-algebraic-group|reductive
\(F\)-group]], and let \(\gamma\in G(F)\) be
[[langlands-letter/knowls/semisimple-element-and-class|semisimple]]. For a
[[harmonic-analysis/test-function-space-local-group|test function]]
\(f\in C_c^\infty(G(F))\), the **orbital integral** of \(f\) at \(\gamma\)
is

\[
O_\gamma(f)
=
\int_{G_\gamma(F)\backslash G(F)}
f(x^{-1}\gamma x)\,d\dot x,
\]

where \(G_\gamma\) is the
[[algebra-groups/centralizer|centralizer]] of \(\gamma\) and the quotient measure
comes from chosen [[harmonic-analysis/haar-measure|Haar measures]].

## Invariance

The [[harmonic-analysis/distribution-local-group|distribution]]
\(O_\gamma\) depends only on the \(G(F)\)-conjugacy class
of \(\gamma\). It is invariant under conjugating the test function.
Its numerical value depends on the Haar-measure normalization, so measure
choices are part of any exact transfer identity.

For \(F\) nonarchimedean, \(C_c^\infty\) means locally constant and compactly
supported. For an archimedean field it means smooth and compactly supported.

## Strongly regular case

When \(\gamma\) is
[[langlands/strongly-regular-semisimple-element|strongly regular
semisimple]], \(G_\gamma\) is a torus and the integral has its cleanest
form. Different rational [[algebra-groups/conjugacy-class|conjugacy classes]] can nevertheless lie in one
[[langlands/stable-conjugacy|stable conjugacy class]]. Their sum is a
[[langlands/stable-orbital-integral|stable orbital integral]], while
character-weighted sums are \(\kappa\)-orbital integrals.

## Global role

For a factorizable adelic test function \(f=\bigotimes_v f_v\), a regular
elliptic global orbital term factors, after compatible measure choices, as a
centralizer volume times a product of local orbital integrals. The geometric
side of the [[langlands/arthur-selberg-trace-formula|Arthur–Selberg trace
formula]] also contains
[[langlands/weighted-orbital-integral|weighted orbital integrals]] attached to
[[algebraic-geometry-foundations/levi-subgroup|Levi]]
subgroups and nonelliptic classes.

## Lie algebra version

For \(X\in\mathfrak g(F)\) semisimple and
\(f\in C_c^\infty(\mathfrak g(F))\), one uses the same formula with
\(x^{-1}Xx=\operatorname{Ad}(x^{-1})X\). The [[lie-groups/lie-algebra|Lie algebra]] version is central
to geometric proofs of the [[langlands/fundamental-lemma|fundamental lemma]].

## References

1. Harish-Chandra, “A submersion principle and its applications,” in
   *Geometry and Analysis*, 1981.
2. Ngô Bảo Châu, “Survey on the fundamental lemma,” §§1.3–1.4.
   [PDF](https://math.uchicago.edu/~ngo/survey.pdf).
