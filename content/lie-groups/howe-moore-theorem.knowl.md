+++
id = "lie-groups/howe-moore-theorem"
title = "Howe–Moore theorem"
kind = "theorem"
summary = "Matrix coefficients vanish at infinity for representations of a noncompact simple Lie group without invariant vectors."
aliases = ["Howe-Moore vanishing theorem"]
domains = ["lie-groups"]
section_mode = "progressive"
prerequisites = ["fiber-bundles/lie-group", "lie-groups/simple-lie-algebra", "lie-groups/strongly-continuous-unitary-representation", "harmonic-analysis/invariant-vector", "harmonic-analysis/coefficient-function"]
+++

Let \(G\) be a connected noncompact real Lie group with simple Lie algebra and finite center. If a strongly continuous [[lie-groups/strongly-continuous-unitary-representation|unitary representation]] \(\pi\) has no nonzero [[harmonic-analysis/invariant-vector|invariant vectors]], then
\[
\langle\pi(g)v,w\rangle\longrightarrow0\qquad(g\to\infty)
\]
for every \(v,w\), where \(g\to\infty\) means leaving every compact subset of \(G\). This is the **Howe–Moore theorem**.

## Dynamical application

Apply the theorem to the reduced Koopman representation of an ergodic probability-preserving action, assuming strong continuity. Ergodicity removes invariant vectors, so the action is [[ergodic-theory/strong-mixing|mixing]]. The conclusion concerns the whole group tending to infinity, not just a specified sequence of times.

For \(G=SL_2(\mathbb R)\), these hypotheses hold. This is a special rigidity phenomenon of the group; an ergodic action of \(\mathbb Z\), such as an irrational rotation, need not be mixing.

## References

1. Corina Ciobotaru, [“A unified proof of the Howe–Moore property”](https://arxiv.org/pdf/1403.0223), Theorem 1.1 and the definition of the Howe–Moore property.
