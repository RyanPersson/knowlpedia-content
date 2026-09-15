+++
id = "ergodic-theory"
title = "Ergodic Theory"
kind = "section"
summary = "Probability-preserving dynamics, Koopman representations, ergodic theorems, and their arithmetic and noncommutative applications."
aliases = ["Ergodic Theory"]
domains = ["ergodic-theory"]
section_mode = "continuous"
prerequisites = []
+++

**Ergodic theory** studies measure-preserving dynamics through invariant events, time averages, recurrence, and mixing. These reading paths connect its probability foundations with Koopman representations, operator algebras, and arithmetic examples.

## Start here

1. [[ergodic-theory/measure-preserving-system|A probability-preserving system]] specifies the space, its measurable events, a probability measure, and a transformation.
2. [[ergodic-theory/finite-uniform-system|The finite uniform example]] computes the three-point and general permutation cases explicitly.
3. [[ergodic-theory/ergodic-transformation|Ergodicity]] says every invariant event has probability zero or one.
4. [[ergodic-theory/koopman-representation|The Koopman representation]] turns the dynamics into a unitary action on functions.
5. [[ergodic-theory/fixed-function-ergodicity-criterion|The fixed-function criterion]] connects these viewpoints; [[ergodic-theory/birkhoff-ergodic-theorem|Birkhoff's theorem]] identifies typical time averages.

## Branches

- [[ergodic-theory/foundations-index|Probability spaces and dynamical systems]] — Start with measurable events and probabilities, then add transformations, invariant events, factors, and flows.
- [[ergodic-theory/ergodic-theorems-index|Averaging, recurrence, and decomposition]] — The averaging theorems identify limits; recurrence forces returns; decomposition resolves a system into ergodic components.
- [[ergodic-theory/koopman-spectrum-index|Koopman operators, representations, and spectrum]] — Translate dynamics into linear operators. Follow fixed vectors to ergodicity, then eigenfunctions, spectral measures, mixing, and continuous-time generators.
- [[ergodic-theory/examples-index|Finite, toral, and Gaussian examples]] — Work from permutations to rotations and mixing maps, then transport cube dynamics into Gaussian coordinates.
- [[ergodic-theory/arithmetic-index|Number-field translations]] — Construct the Archimedean torus and its character lattice before comparing one translation with the joint additive action of the ring of integers.
- [[ergodic-theory/noncommutative-index|Noncommutative dynamics and orbit spaces]] — The function algebra and its state encode classical probability. Crossed products retain orbit motion; the rotation algebra links this construction to foliations and noncommutative differentiation.
- [[ergodic-theory/entropy-cocycles-index|Entropy and growth along orbits]] — Entropy measures information in orbit observations. Subadditive and linear cocycles describe growth, leading to Kingman and Oseledets.
- [[ergodic-theory/applications-index|Arithmetic, Hamiltonian, and data applications]] — Follow recurrence to arithmetic progressions, volume preservation to Hamiltonian Koopman dynamics, and finite observations to data-driven operator approximations.

## Three conventions to keep in view

- For forward time averages use \(U_Tf=f\circ T\). A left group representation uses \(\kappa(g)f=f\circ T_{g^{-1}}\). The inverse makes the order of group multiplication correct.
- A [[ergodic-theory/number-field-translation-ergodicity|single number-field translation]] has a trace-integrality criterion. The [[ergodic-theory/ring-of-integers-translation-action|joint ring-of-integers action]] has a different invariant-character test.
- The [[operator-algebras/ergodicity-factor-criterion|factor criterion for crossed products]] requires essential freeness. The regular crossed product uses an additional group-coordinate Hilbert space.
