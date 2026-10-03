+++
id = "ergodic-theory/automorphism-group-probability-space"
title = "Automorphism group of a probability space"
kind = "definition"
summary = "The group of invertible measure-preserving transformations modulo almost-everywhere equality."
aliases = ["measure-preserving automorphism group"]
domains = ["ergodic-theory"]
section_mode = "progressive"
prerequisites = ["measure-theory/measure-space-isomorphism", "algebra-groups/group", "algebra-groups/monoid"]
+++

The **automorphism group** \(\operatorname{Aut}(X,\mu)\) consists of [[measure-theory/measure-space-isomorphism|measure-space isomorphisms]] from a probability space to itself, modulo almost-everywhere equality. Its operation is composition, its identity is the identity map, and inversion is the measurable inverse modulo null sets.

## Endomorphisms

All measure-preserving self-maps, including noninvertible ones, form a [[algebra-groups/monoid|monoid]] instead. Ergodic automorphisms generally do not form a subgroup: on a nontrivial space, the identity is not ergodic, while \(T^{-1}\) is ergodic whenever \(T\) is.

## Finite and Gaussian models

For a uniform \(n\)-point space this group is \(S_n\). For an atomless standard space it is isomorphic, by conjugation, to the automorphism group of Lebesgue probability on an interval; see the [[measure-theory/atomless-standard-isomorphism-theorem|isomorphism theorem]].
