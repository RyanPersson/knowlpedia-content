+++
id = "ergodic-theory/invariant-sigma-algebra"
title = "Invariant sigma-algebra"
kind = "definition"
summary = "The measurable events unchanged by a transformation modulo null sets."
aliases = []
domains = ["ergodic-theory"]
section_mode = "progressive"
prerequisites = ["ergodic-theory/measure-preserving-system", "shared-foundations/symmetric-difference", "measure-theory/sigma-algebra"]
+++

The **invariant sigma-algebra** of a [[ergodic-theory/measure-preserving-system|probability-preserving system]] is
\[
\mathcal I_T=\{E\in\Sigma:\mu(T^{-1}E\triangle E)=0\},
\]
where \(\triangle\) is [[shared-foundations/symmetric-difference|symmetric difference]]. Its events are invariant modulo null sets. For an action of \(G\), require this equality for every \(T_g\), and write \(\mathcal I_G\).

## Why it is a sigma-algebra

Preimages commute with complements and countable unions, and a countable union of null sets is null. These facts verify closure. Every measurable null set belongs to \(\mathcal I_T\).

## Statistical meaning

The limit of time averages is [[probability/conditional-expectation|conditional expectation]] onto this sigma-algebra. It keeps the information that does not change under the dynamics.
