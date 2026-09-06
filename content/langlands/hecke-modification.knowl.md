+++
id = "langlands/hecke-modification"
title = "Hecke modification"
kind = "definition"
summary = "A change of a G-bundle at one point, given by an isomorphism away from that point."
aliases = ["modification of a G-bundle"]
domains = ["langlands", "algebraic-geometry-foundations"]
section_mode = "progressive"
prerequisites = ["algebraic-geometry-foundations/principal-g-bundle-on-scheme"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(X\) be a smooth curve, \(x\in X\), and \(E,E'\)
[[algebraic-geometry-foundations/principal-g-bundle-on-scheme|principal
\(G\)-bundles]].
A **Hecke modification of \(E\) to \(E'\) at \(x\)** is an isomorphism
\[
\beta:E|_{X\setminus\{x\}}\xrightarrow{\sim}
E'|_{X\setminus\{x\}}.
\]
Thus the bundles may differ at \(x\) but agree on its complement.

## Relative position

After choosing a local coordinate and trivializations near \(x\), the
modification gives a point of the
[[langlands/affine-grassmannian|affine Grassmannian]]. Its
\(G\lbrack\!\lbrack t\rbrack\!\rbrack\)-orbit, indexed by a
[[langlands/dominant-coweight|dominant coweight]] \(\lambda\), is the
relative position of the modification. The bound “relative position at most
\(\lambda\)” uses the associated
[[langlands/affine-schubert-variety|affine Schubert variety]].

## Example for GL_n

For \(G=GL_n\), a modification is a pair of [[fiber-bundles/vector-bundle|vector bundles]] identified away
from \(x\). An elementary modification can replace \(E\) by the kernel of a
surjection \(E\to i_{x*}Q\), changing the degree by \(-\dim Q\).

## References

1. Vladimir Drinfeld, “Two-dimensional \(\ell\)-adic representations of the
   fundamental group of a curve over a finite field and automorphic forms on
   \(GL(2)\),” *American Journal of Mathematics* 105 (1983), 85–114.
   [DOI](https://doi.org/10.2307/2374382).
