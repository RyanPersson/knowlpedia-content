+++
id = "differential-geometry/chirality-operator"
title = "Chirality operator"
kind = "definition"
summary = "The normalized complex Clifford volume element acting on an even-dimensional spinor module."
aliases = ["chirality matrix", "complex volume operator"]
domains = ["differential-geometry", "mathematical-physics"]
prerequisites = ["linear-algebra/quadratic-form", "differential-geometry/spinor-module", "differential-geometry/clifford-algebra", "differential-geometry/clifford-module", "mathematical-physics/gamma-matrices"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(V\) be an oriented complex [[linear-algebra/quadratic-form|quadratic space]] of even dimension, and let
\(\Delta\) be a complex
[[differential-geometry/spinor-module|spinor module]]. The oriented Clifford
volume element has a scalar normalization \(\omega_{\mathbb C}\) satisfying
\[
\omega_{\mathbb C}^{\,2}=1.
\]
The **chirality operator** on \(\Delta\) is
\[
\Gamma=c(\omega_{\mathbb C}).
\]
The normalizing scalar depends on the dimension, signature, and convention
\(c(v)^2=\pm g(v,v)\); the defining requirements are
\(\Gamma^2=1\) and the chosen orientation.

The chirality operator commutes with the even [[differential-geometry/clifford-algebra|Clifford algebra]] and
anticommutes with [[differential-geometry/clifford-module|Clifford multiplication]] by every vector:
\[
\Gamma c(v)=-c(v)\Gamma.
\]
Its eigenspaces give the half-spin decomposition
\[
\Delta=\Delta^+\oplus\Delta^-,
\qquad
\Delta^\pm=\ker(\Gamma\mp1).
\]
Elements of these eigenspaces are
[[differential-geometry/weyl-spinor|Weyl spinors]].

In a matrix realization, \(\Gamma\) is an appropriately normalized product of
all [[mathematical-physics/gamma-matrices|gamma matrices]]. It is often denoted
\(\gamma_5\) in four-dimensional physics, but the invariant construction is
not tied to that dimension or notation.

## References

1. H. Blaine Lawson Jr. and Marie-Louise Michelsohn, *Spin Geometry*,
   Princeton University Press, 1989. [DOI
   record](https://doi.org/10.1515/9781400883912). Relevant: Chapter I, §5.
2. Daniel S. Freed, *Five Lectures on Supersymmetry*, American Mathematical
   Society, 1999. Relevant: Lecture 1.
