+++
id = "mathematical-physics/gamma-matrices"
title = "Gamma matrices"
kind = "definition"
summary = "Matrices representing Clifford multiplication in a chosen basis of a spinor module."
aliases = ["Dirac gamma matrices", "Clifford matrices"]
domains = ["mathematical-physics", "differential-geometry"]
section_mode = "progressive"
+++

Let \((V,g)\) be a finite-dimensional real or complex quadratic space with
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

## Raised indices and slash notation

Writing \(g^{ab}\) for the inverse matrix, set
\(\gamma^a=g^{ab}\gamma_b\). For a covector
\(\xi=\xi_a e^a\), slash notation abbreviates its Clifford action:
\[
\slashed{\xi}=\gamma^a\xi_a.
\]
The Clifford relation implies
\[
\slashed{\xi}^{\,2}=-g^{-1}(\xi,\xi)I
\]
under the convention of the core. This identity is what makes the square of a
Dirac operator have the metric quadratic form as its principal symbol.

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

## Chirality matrix

In even dimension, an appropriately normalized product of all gamma matrices
defines the complex volume or chirality operator. Its normalization depends
on dimension, signature, and the Clifford sign. Its \(+1\) and \(-1\)
eigenspaces are the two Weyl modules; a vector gamma matrix exchanges them.

## References

1. H. Blaine Lawson Jr. and Marie-Louise Michelsohn, *Spin Geometry*,
   Princeton University Press, 1989. [DOI
   record](https://doi.org/10.1515/9781400883912). Relevant: Chapter I.
2. Daniel S. Freed, *Five Lectures on Supersymmetry*, American Mathematical
   Society, 1999. Relevant: Lectures 1–2.
3. Michael E. Peskin and Daniel V. Schroeder, *An Introduction to Quantum
   Field Theory*, Addison–Wesley, 1995. Relevant: Sections 3.1–3.4 for the
   common physics sign convention.
