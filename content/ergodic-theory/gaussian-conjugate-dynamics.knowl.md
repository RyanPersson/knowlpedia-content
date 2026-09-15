+++
id = "ergodic-theory/gaussian-conjugate-dynamics"
title = "Gaussian dynamics by measurable conjugacy"
kind = "construction"
summary = "Transport of arbitrary uniform-cube dynamics to Gaussian coordinates using the normal CDF."
aliases = []
domains = ["ergodic-theory"]
section_mode = "progressive"
prerequisites = ["probability/probability-integral-transform", "ergodic-theory/measurable-conjugacy", "ergodic-theory/automorphism-group-probability-space"]
+++

Let \(F_d(x)=(\Phi(x_1),\ldots,\Phi(x_d))\) be the [[probability/probability-integral-transform|normal-CDF isomorphism]] from Gaussian \(\mathbb R^d\) to the uniform cube. For any measurable cube self-map \(S\), define
\[
T=F_d^{-1}\circ S\circ F_d.
\]
Then \(T\) preserves Gaussian probability exactly when \(S\) preserves cube probability. Invertibility modulo null sets, ergodicity, and mixing are preserved by this [[ergodic-theory/measurable-conjugacy|conjugacy]]. Every Gaussian-preserving measurable self-map arises in this way.

## Groups and monoids

This identifies \(\operatorname{Aut}(\mathbb R^d,\gamma_d)\) with the automorphism group of the uniform cube, and identifies the [[algebra-groups/monoid|monoids]] that include noninvertible maps. The [[measure-theory/atomless-standard-isomorphism-theorem|atomless isomorphism theorem]] further identifies the cube with an interval modulo null sets.

## What the description means

Allowing arbitrary measurable transformations imposes no extra classification restriction from Gaussian coordinates. Restricting to linear transformations gives the much smaller group \(O(d)\), with no ergodic members. The transported maps can be highly discontinuous.
