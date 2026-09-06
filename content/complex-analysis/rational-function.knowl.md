+++
id = "complex-analysis/rational-function"
title = "Rational function"
kind = "definition"
summary = "A quotient of complex polynomials, equivalently a holomorphic self-map of the Riemann sphere."
aliases = ["complex rational function", "rational map of the Riemann sphere"]
domains = ["complex-analysis", "algebra"]
section_mode = "progressive"
prerequisites = ["complex-analysis/meromorphic-function", "differential-geometry/holomorphic-map", "complex-analysis/riemann-sphere"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

A **rational function** is a quotient
\[
R(z)=\frac{P(z)}{Q(z)}
\]
of complex polynomials \(P,Q\in\mathbb C[z]\) with \(Q\ne0\), where two quotients represent the same function when they agree after cancellation. It defines a [[complex-analysis/meromorphic-function|meromorphic function]] on \(\mathbb C\) and extends uniquely to a [[differential-geometry/holomorphic-map|holomorphic map]]
\[
R:\widehat{\mathbb C}\longrightarrow\widehat{\mathbb C}
\]
of the [[complex-analysis/riemann-sphere|Riemann sphere]].

## Value at infinity

The zero rational function has \(R(\infty)=0\). For nonzero \(R\), choose
coprime \(P\ne0\) and \(Q\). Then \(R(\infty)\) is \(0\) if
\(\deg P<\deg Q\), the ratio of leading coefficients if the degrees agree,
and \(\infty\) if \(\deg P>\deg Q\). This is exactly the value obtained in the
coordinate \(w=1/z\) near infinity.

## Degree

For nonconstant \(R=P/Q\) in lowest terms,
\[
\deg R=\max(\deg P,\deg Q).
\]
Every value of the sphere has \(\deg R\) preimages counted with multiplicity. Degree \(1\) rational functions are precisely [[complex-analysis/mobius-transformation|Möbius transformations]]; higher-degree maps are branched coverings rather than automorphisms.

## Characterization

Every nonconstant holomorphic map \(\widehat{\mathbb C}\to\widehat{\mathbb C}\) is rational. More generally, every such map that is not identically \(\infty\) is represented by a quotient \(P/Q\); the constant map with value \(\infty\) is represented projectively by \([1:0]\). Equivalently, the field of meromorphic functions on the [[algebraic-geometry-foundations/projective-line|projective line]] is \(\mathbb C(z)\).

## References

1. Otto Forster, *Lectures on Riemann Surfaces*, Springer, 1981. [Publisher record](https://doi.org/10.1007/978-1-4612-5961-9). Relevant: Chapter 1, §§8–9.
