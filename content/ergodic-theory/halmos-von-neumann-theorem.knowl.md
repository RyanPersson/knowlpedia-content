+++
id = "ergodic-theory/halmos-von-neumann-theorem"
title = "Halmos–von Neumann theorem"
kind = "theorem"
summary = "Ergodic systems with discrete spectrum are exactly compact metrizable abelian group rotations, up to measurable conjugacy."
aliases = []
domains = ["ergodic-theory"]
section_mode = "progressive"
prerequisites = ["ergodic-theory/discrete-spectrum", "ergodic-theory/ergodic-transformation", "ergodic-theory/measurable-conjugacy", "measure-theory/standard-probability-space", "harmonic-analysis/haar-measure"]
+++

An invertible [[ergodic-theory/ergodic-transformation|ergodic]] probability-preserving system on a [[measure-theory/standard-probability-space|standard probability space]] has [[ergodic-theory/discrete-spectrum|discrete spectrum]] if and only if it is measurably conjugate modulo null sets to
\[
R_a:K\to K,\qquad R_a(x)=x+a,
\]
where \(K\) is a compact metrizable abelian group with normalized [[harmonic-analysis/haar-measure|Haar measure]] and \(\overline{\{na:n\in\mathbb Z\}}=K\).

## Spectral classification

Two such ergodic systems are measurably conjugate exactly when their groups of Koopman eigenvalues agree as subgroups of \(\mathbb S^1\). Standardness makes this group countable. Its [[harmonic-analysis/pontryagin-dual|Pontryagin dual]] supplies the compact rotation model.

With the forward convention \(Uf=f\circ T\), the rotation point is evaluation \(a(\lambda)=\lambda\). Inverse pullback conjugates these eigenvalues; the two conventions must not be mixed when writing the model.

## Scope

The compact group can be finite, a torus, or an infinite totally disconnected group. The theorem does not classify systems with continuous spectral components from their Koopman representation alone.

## References

1. Asgar Jamneshan and Henrik Kreidler, [*Ergodic Structure Theory and Applications*](https://ajamnesh.github.io/pdf/ISem28_notes.pdf), ISEM 28 lecture notes. Theorems 6.2.6–6.2.8.
