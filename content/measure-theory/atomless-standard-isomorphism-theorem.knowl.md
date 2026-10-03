+++
id = "measure-theory/atomless-standard-isomorphism-theorem"
title = "Isomorphism theorem for atomless standard probability spaces"
kind = "theorem"
summary = "Every atomless standard probability space is isomorphic modulo null sets to the unit interval with Lebesgue probability."
aliases = []
domains = ["measure-theory"]
section_mode = "progressive"
prerequisites = ["measure-theory/standard-probability-space", "measure-theory/atomless-probability-space", "measure-theory/measure-space-isomorphism", "measure-theory/lebesgue-measure"]
+++

Every [[measure-theory/atomless-probability-space|atomless]] [[measure-theory/standard-probability-space|standard probability space]] is [[measure-theory/measure-space-isomorphism|isomorphic modulo null sets]] to \(([0,1],\mathcal L,\lambda)\), where \(\lambda\) is Lebesgue probability and \(\mathcal L\) its completed sigma-algebra.

## Consequence for dynamics

Consequently, an invertible probability-preserving system on any such space can be transported to any other by \(T\mapsto bTb^{-1}\). This preserves ergodicity and mixing. In particular, changing the finite dimension of a Gaussian probability space imposes no restriction on its measurable dynamics up to conjugacy.

## Scope

The isomorphism is measure theoretic. A square and an interval satisfy the theorem even though they are not homeomorphic.

## References

1. Jesse Peterson, [*Lecture notes on ergodic theory*](https://www.math.vanderbilt.edu/~peters10/teaching/Spring2011/ErgodicTheoryNotes.pdf), 2011. §2.3, “A remark about measure spaces.”
