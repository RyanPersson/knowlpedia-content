+++
id = "differential-geometry/spinor-bundle"
title = "Spinor bundle"
kind = "definition"
summary = "The vector bundle associated to a spin structure through a spin representation."
aliases = ["bundle of spinors", "spinor module bundle"]
domains = ["differential-geometry", "fiber-bundles"]
section_mode = "progressive"
+++

Let \((M,g)\) be an oriented Riemannian \(n\)-manifold equipped with a [[fiber-bundles/spin-structure|spin structure]] \(P_{\mathrm{Spin}}(M)\to M\), and let \(\Delta_n\) be a real or complex [[differential-geometry/spinor-module|spinor module]], restricted to its spin representation of \(\mathrm{Spin}(n)\). The corresponding **spinor bundle** is the [[fiber-bundles/associated-vector-bundle|associated vector bundle]]
\[
S=P_{\mathrm{Spin}}(M)\times_{\mathrm{Spin}(n)}\Delta_n.
\]
The compatible Clifford action on \(\Delta_n\) makes \(S\) a [[differential-geometry/clifford-module|Clifford module bundle]]: each tangent vector or covector acts fiberwise by Clifford multiplication. A choice of spinor module and scalar field is part of the construction, so “the spinor bundle” is convention-dependent unless these choices are understood.

## Construction from frames

The spin structure is a principal \(\mathrm{Spin}(n)\)-bundle together with a two-to-one [[fiber-bundles/equivariant-map|equivariant map]] to the oriented orthonormal frame bundle. Passing from a spin frame \(p\) and a spinor \(\psi\in\Delta_n\) to the [[shared-foundations/equivalence-class|equivalence class]]
\[
[p,\psi]=[pg,\rho(g)^{-1}\psi]
\]
produces the fiber of \(S\) over the base point of \(p\). Using the alternative associated-bundle convention changes the location of the inverse but gives an isomorphic construction when used consistently.

## Chirality in even dimension

For even \(n\), the complex spin representation has a natural chirality decomposition
\[
\Delta_n=\Delta_n^+\oplus\Delta_n^-,
\]
and hence
\[
S=S^+\oplus S^-.
\]
Clifford multiplication by a tangent vector exchanges \(S^+\) and \(S^-\). In odd dimension the standard irreducible complex spinor bundle has no analogous intrinsic chiral splitting; imposing an artificial doubling is additional data.

## Connection and Dirac operator

The Levi-Civita connection lifts through the spin structure to a covariant derivative
\[
\nabla^S:\Gamma^\infty(S)\to\Gamma^\infty(T^*M\otimes S).
\]
Composing it with Clifford multiplication gives the spin [[noncommutative-geometry/dirac-operator|Dirac operator]]
\[
D=c\circ\nabla^S.
\]
On a [[topology/closed-manifold|closed manifold]], \(D\) with initial domain
\(C^\infty(S)\subset L^2(S)\) is symmetric and essentially self-adjoint. Its
closure is self-adjoint, with domain the first [[functional-analysis/sobolev-space|Sobolev space]] \(H^1(S)\), and
is the operator in the canonical commutative [[noncommutative-geometry/spectral-triple|spectral triple]].

## Variants

A \(\mathrm{Spin}^c\) structure produces a complex spinor bundle using a representation of \(\mathrm{Spin}^c(n)\); it does not require an ordinary spin structure. Depending on dimension and signature, spin representations may also admit real or quaternionic structures. These variants should not be identified with the complex Riemannian spinor bundle without stating the relevant structure group and representation.

## Pseudo-Riemannian signatures

For a [[differential-geometry/pseudo-riemannian-manifold|pseudo-Riemannian
manifold]] of constant signature \((p,q)\), the analogous construction starts
from a \(\operatorname{Spin}(p,q)\)-structure and a specified real or complex
\(\operatorname{Cl}(p,q)\)-module:
\[
S=P_{\operatorname{Spin}(p,q)}(M)
\times_{\operatorname{Spin}(p,q)}\Delta_{p,q}.
\]
The ordering of \((p,q)\) and the convention \(v^2=\pm g(v,v)\) must be stated,
because both affect the real Clifford algebra and hence the possible Majorana
or quaternionic structures. Over \(\mathbb C\), signature does not affect the
complexified Clifford algebra, but it still affects the real geometric group
acting on the bundle.

The analytic behavior also changes with signature. On a Riemannian manifold
the spin Dirac operator is elliptic. For the dedicated Lorentzian construction,
see the [[differential-geometry/lorentzian-spinor-bundle|Lorentzian spinor
bundle]]. Its relativistic Dirac operator is of hyperbolic type, so the
closed-Riemannian self-adjointness statement above must not be transferred
without specifying a spacetime, a Cauchy problem, and an analytic realization.

## References

1. H. Blaine Lawson Jr. and Marie-Louise Michelsohn, *Spin Geometry*, Princeton University Press, 1989. [DOI record](https://doi.org/10.1515/9781400883912). Relevant: Chapter II, spinor bundles and Dirac operators.
2. Nicole Berline, Ezra Getzler, and Michèle Vergne, *Heat Kernels and Dirac Operators*, Springer, 1992. [DOI record](https://doi.org/10.1007/978-3-642-58088-8). Relevant: Chapter 3, Clifford modules and Dirac operators.
