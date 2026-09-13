+++
id = "functional-analysis/three-dimensional-sobolev-inequality"
title = "Three-dimensional Sobolev inequality"
kind = "theorem"
summary = "The L6 norm of a whole-space H1 function is bounded by its L2 gradient norm."
aliases = ["H1 to L6 embedding"]
domains = ["functional-analysis"]
section_mode = "progressive"
prerequisites = ["functional-analysis/sobolev-space", "functional-analysis/smooth-density-in-euclidean-sobolev-space", "convex-analysis/holder-inequality-integrals", "measure-theory/tonellis-theorem", "real-analysis/fundamental-theorem-of-calculus-i", "measure-theory/lp-space", "real-analysis/gradient"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 2
+++

For \(u\in H^1(\mathbb R^3)=W^{1,2}(\mathbb R^3)\),
\[
\|u\|_6\le C\|\nabla u\|_2.
\]
The norms are whole-space [[measure-theory/lp-space|Lebesgue norms]]. The same estimate holds for a vector field, with a dimensional constant.

## An elementary route

For real \(f\in C_c^1(\mathbb R^3)\), the fundamental theorem of calculus gives \(|f(x,y,z)|\le A_1(y,z)=\int|\partial_1f(s,y,z)|\,ds\), and analogously \(A_2(x,z),A_3(x,y)\). Hence \(|f|^{3/2}\le(A_1A_2A_3)^{1/2}\). Integrating first in \(x\) and using Cauchy–Schwarz, then in \((y,z)\) and using it again, yields
\[
\|f\|_{3/2}\le\prod_{j=1}^3\|\partial_jf\|_1^{1/3}\le C\|\nabla f\|_1.
\]
Apply this to \(f=|u|^4\). Hölder gives \(\|u\|_6^4\le C\|u\|_6^3\|\nabla u\|_2\); divide if \(u\ne0\). Smooth compact-support approximation extends the inequality to \(H^1\).

## References

- [Hunter, Sobolev Spaces, §§3.5–3.7](https://www.math.ucdavis.edu/~hunter/pdes/ch3.pdf).
