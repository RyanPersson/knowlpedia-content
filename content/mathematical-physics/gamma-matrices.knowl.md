+++
id = "mathematical-physics/gamma-matrices"
title = "Gamma matrices"
kind = "definition"
summary = "Matrices representing Clifford multiplication in a chosen basis of a spinor module."
aliases = ["Dirac gamma matrices", "Clifford matrices"]
domains = ["mathematical-physics", "differential-geometry"]
section_mode = "progressive"
prerequisites = ["linear-algebra/quadratic-form", "differential-geometry/spinor-module", "differential-geometry/clifford-module", "linear-algebra/matrix"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \((V,g)\) be a finite-dimensional real or complex [[linear-algebra/quadratic-form|quadratic space]] with
basis \(e_a\), and let
\(c:\operatorname{Cl}(V,g)\to\operatorname{End}(\Delta)\) be a
[[differential-geometry/spinor-module|spinor module]] written in a basis of
\(\Delta\). The **gamma matrices** are
\[
\gamma_a=c(e_a).
\]
Using the geometric Clifford convention \(v^2=-g(v,v)1\), they satisfy
\[
\gamma_a\gamma_b+\gamma_b\gamma_a=-2g_{ab}I.
\]
Thus gamma matrices are the basis-dependent matrices of
[[differential-geometry/clifford-module|Clifford multiplication]], not
additional invariant geometric objects.

## Raised indices

Writing \(g^{ab}\) for the inverse matrix, set
\(\gamma^a=g^{ab}\gamma_b\). Contracting gamma matrices with the components of
a vector or covector is the
[[mathematical-physics/clifford-slash-notation|Clifford slash notation]].

## Minkowski-signature convention

For the Lorentzian knowls in this collection, take
\[
\eta=\operatorname{diag}(-1,+1,+1,+1).
\]
Under the geometric convention used here,
\[
\gamma_0^2=+I,
\qquad
\gamma_j^2=-I\quad(j=1,2,3).
\]
Many physics texts instead use the opposite metric signature
\(\eta_{\mathrm{phys}}=\operatorname{diag}(+1,-1,-1,-1)\) together with
\[
\{\gamma^\mu,\gamma^\nu\}=+2\eta^{\mu\nu}I.
\]
With \(\eta_{\mathrm{phys}}=-\eta\), this has the same numerical right-hand
side as the convention in the core. If one changes only the Clifford sign
while holding the metric fixed, multiplying all complex gamma matrices by
\(i\) passes between the two relations. Metric signature and Clifford sign
must therefore be recorded separately.

## Change of basis and spin covariance

Changing the basis of the spinor module conjugates every gamma matrix
simultaneously. A spin transformation \(s\) satisfies
\[
\rho(s)c(v)\rho(s)^{-1}=c(svs^{-1}),
\]
so the matrices transform compatibly with the orthogonal action on \(V\).
Different-looking gamma-matrix realizations can therefore describe equivalent
Clifford representations.

## Related constructions

In even dimension, the normalized product of all gamma matrices represents
the [[differential-geometry/chirality-operator|chirality operator]]. The
normalization is convention-dependent, whereas the resulting grading of the
complex spin representation is invariant.

## References

1. H. Blaine Lawson Jr. and Marie-Louise Michelsohn, *Spin Geometry*,
   Princeton University Press, 1989. [DOI
   record](https://doi.org/10.1515/9781400883912). Relevant: Chapter I.
2. Daniel S. Freed, *Five Lectures on Supersymmetry*, American Mathematical
   Society, 1999. Relevant: Lectures 1–2.
3. Michael E. Peskin and Daniel V. Schroeder, *An Introduction to Quantum
   Field Theory*, Addison–Wesley, 1995. Relevant: Sections 3.1–3.4 for the
   common physics sign convention.
