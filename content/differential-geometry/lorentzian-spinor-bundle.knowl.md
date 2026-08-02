+++
id = "differential-geometry/lorentzian-spinor-bundle"
title = "Lorentzian spinor bundle"
kind = "definition"
summary = "The Clifford module bundle associated to a Lorentzian spin structure and a spin representation."
aliases = ["spinor bundle of a Lorentzian manifold", "bundle of Lorentzian spinors"]
domains = ["differential-geometry", "fiber-bundles", "mathematical-physics"]
section_mode = "progressive"
+++

Let \((M,g)\) carry a [[differential-geometry/lorentzian-spin-structure|Lorentzian spin structure]] \(P_{\mathrm{Spin}}\), and let \(\Delta_{1,n-1}\) be a real or complex module for the relevant [[differential-geometry/clifford-algebra|Clifford algebra]], restricted to \(\mathrm{Spin}^+(1,n-1)\). The associated **Lorentzian spinor bundle** is
\[
S=P_{\mathrm{Spin}}\times_{\mathrm{Spin}^+(1,n-1)}\Delta_{1,n-1}.
\]
It is a [[differential-geometry/clifford-module|Clifford module bundle]] with multiplication
\[
c(v)c(w)+c(w)c(v)=-2g(v,w)\operatorname{id}_S.
\]

## Associated connection

The Lorentzian Levi–Civita connection lifts to \(P_{\mathrm{Spin}}\) and induces a covariant derivative \(\nabla^S\) on \(S\). Clifford contraction gives
the [[differential-geometry/lorentzian-dirac-operator|Lorentzian Dirac
operator]]. Unlike the [[noncommutative-geometry/dirac-operator|Dirac operator]] on a
[[differential-geometry/spinor-bundle|Riemannian spinor bundle]], this operator
is not elliptic.

## Representation choices

The rank and additional structures of \(S\) depend on dimension, signature,
scalar field, and the chosen spin representation.
[[differential-geometry/majorana-spinor|Majorana]],
[[differential-geometry/weyl-spinor|Weyl]], and
[[differential-geometry/majorana-weyl-spinor|Majorana–Weyl]] conditions exist
only in appropriate signatures and dimensions. The [[differential-geometry/dirac-spinor|complex spinor]] bundle
forgets some signature-dependent real structure even though its Clifford
action still remembers the Lorentzian metric.

## Spinor pairing

In indefinite signature the natural invariant spinor pairing is generally not a positive-definite [[fiber-bundles/hermitian-metric|Hermitian metric]] preserved in the same way as in Riemannian geometry. [[differential-geometry/formal-adjoint-differential-operator|Formal adjoints]] and conserved currents therefore require an explicitly chosen pairing and a time orientation; they should not be imported unchanged from the Riemannian \(L^2\) theory.

## References

1. Helga Baum, *Spin-Strukturen und Dirac-Operatoren über pseudoriemannschen Mannigfaltigkeiten*, Teubner, 1981. [Bibliographic record](https://zbmath.org/0476.53047). Relevant: Chapters 2–3.
2. Christian Bär, Nicolas Ginoux, and Frank Pfäffle, *Wave Equations on Lorentzian Manifolds and Quantization*, European Mathematical Society, 2007. [Publisher record](https://doi.org/10.4171/037). Relevant: §§1.3 and 3.4.
