+++
id = "differential-geometry/lorentzian-spin-structure"
title = "Lorentzian spin structure"
kind = "definition"
summary = "A lift of the oriented, time-oriented Lorentz frame bundle through the spin double cover."
aliases = ["spin structure on a Lorentzian manifold", "Lorentzian spin lift"]
domains = ["differential-geometry", "fiber-bundles", "mathematical-physics"]
prerequisites = ["differential-geometry/time-orientation", "differential-geometry/lorentzian-manifold", "lie-groups/restricted-spin-group"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \((M,g)\) be an oriented and [[differential-geometry/time-orientation|time-oriented]] [[differential-geometry/lorentzian-manifold|Lorentzian \(n\)-manifold]] of signature \((1,n-1)\), with negative directions listed first, and let \(P_{\mathrm{SO}^+(1,n-1)}(M)\) be its bundle of oriented, time-oriented pseudo-orthonormal frames. Write \(\mathrm{Spin}^+(1,n-1)\) for the full preimage of \(\mathrm{SO}^+(1,n-1)\) under the spin covering, as in the [[lie-groups/restricted-spin-group|restricted spin group]]. A **Lorentzian spin structure** is a principal \(\mathrm{Spin}^+(1,n-1)\)-bundle \(P_{\mathrm{Spin}}\to M\) and an equivariant double covering
\[
\Phi:P_{\mathrm{Spin}}\longrightarrow P_{\mathrm{SO}^+(1,n-1)}(M)
\]
whose restriction to each fiber is induced by the spin double covering \(\mathrm{Spin}^+(1,n-1)\to\mathrm{SO}^+(1,n-1)\). Defining \(\mathrm{Spin}^+\) by this full preimage keeps the fiber map two-to-one also in the low-dimensional signature \((1,1)\).

## Relation to the Riemannian definition

This is the signature-\((1,n-1)\) analogue of a [[fiber-bundles/spin-structure|Riemannian spin structure]]. The reduction to \(\mathrm{SO}^+(1,n-1)\) records both space orientation and time orientation; without those choices the appropriate structure group is larger and the lifting problem changes.

For an oriented, time-oriented Lorentzian manifold, existence is again controlled by
\[
w_2(TM)=0.
\]
When structures exist, their isomorphism classes form a torsor for \(H^1(M;\mathbb Z/2)\), subject to the usual hypotheses on the manifold.

## Associated geometry

The Lorentzian Levi–Civita connection lifts uniquely to the spin principal bundle. Choosing a real or complex representation of the signature-dependent spin group produces a [[differential-geometry/lorentzian-spinor-bundle|Lorentzian spinor bundle]] and its [[fiber-bundles/spin-connection|spin connection]]. Clifford contraction of that connection gives a [[differential-geometry/lorentzian-dirac-operator|Lorentzian Dirac operator]]; on flat Minkowski spacetime this specializes to the [[mathematical-physics/minkowski-dirac-operator|Minkowski Dirac operator]].

## Convention warning

Labels such as \(\mathrm{Spin}(1,n-1)\) and \(\mathrm{Spin}(n-1,1)\) are not interchangeable until the sign convention for the [[differential-geometry/clifford-algebra|Clifford algebra]] has been stated. Here \(g\) has one negative direction and [[differential-geometry/clifford-module|Clifford multiplication]] satisfies \(c(v)^2=-g(v,v)\).

## References

1. Helga Baum, *Spin-Strukturen und Dirac-Operatoren über pseudoriemannschen Mannigfaltigkeiten*, Teubner, 1981. [Bibliographic record](https://zbmath.org/0476.53047). Relevant: Chapters 1–2.
2. Christian Bär, Nicolas Ginoux, and Frank Pfäffle, *Wave Equations on Lorentzian Manifolds and Quantization*, European Mathematical Society, 2007. [Publisher record](https://doi.org/10.4171/037). Relevant: §1.3.
