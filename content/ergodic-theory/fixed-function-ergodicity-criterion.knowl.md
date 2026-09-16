+++
id = "ergodic-theory/fixed-function-ergodicity-criterion"
title = "Fixed-function criterion for ergodicity"
kind = "theorem"
summary = "Ergodicity is equivalent to constants being the only invariant L2 or bounded observables."
aliases = []
domains = ["ergodic-theory"]
section_mode = "progressive"
prerequisites = ["ergodic-theory/ergodic-action", "ergodic-theory/koopman-representation", "measure-theory/l-infinity-function", "measure-theory/indicator-function"]
+++

For a probability-preserving action \(G\curvearrowright(X,\mu)\), the following are equivalent:

1. The action is [[ergodic-theory/ergodic-action|ergodic]].
2. \(L^2(X,\mu)^G=\mathbb C1\), where the superscript means vectors fixed by every Koopman operator.
3. \(L^\infty(X,\mu)^G=\mathbb C1\).

For a single probability-preserving transformation, including a noninvertible one, the corresponding criterion is \(\ker(U_T-I)=\mathbb C1\).

## Proof

An invariant event \(E\) gives the fixed indicator \(1_E\); it is constant almost everywhere exactly when \(\mu(E)\in\{0,1\}\). Conversely, a nonconstant invariant complex measurable function has a nonconstant real or imaginary part. Some level set of that part has intermediate probability and is invariant modulo null sets. This contradicts ergodicity.

## Algebraic form

Under inverse pullback on the function algebra, this reads \(A^\alpha=\mathbb C1\). It is a fixed-point statement, not [[lie-groups/irreducible-unitary-representation|irreducibility]] of a Hilbert-space representation.

## References

1. Jesse Peterson, [*Lecture notes on ergodic theory*](https://www.math.vanderbilt.edu/~peters10/teaching/Spring2011/ErgodicTheoryNotes.pdf), 2011. Lemma 2.2.5.
