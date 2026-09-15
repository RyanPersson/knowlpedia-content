+++
id = "ergodic-theory/irrational-rotation-orbit-space"
title = "Orbit space of an irrational rotation"
kind = "example"
summary = "An orbit quotient with many points but only constant continuous invariant functions and trivial measurable invariants."
aliases = []
domains = ["ergodic-theory"]
section_mode = "progressive"
prerequisites = ["ergodic-theory/torus-translation-ergodicity", "algebra-groups/orbit", "lie-groups/orbit-space", "topology/quotient-topology"]
+++

For irrational \(\theta\), let \(T_\theta(x)=x+\theta\) on \(\mathbb T\). Its [[lie-groups/orbit-space|orbit space]] is \(Q=\mathbb T/{\sim}\), where \(x\sim y\) means \(y=x+n\theta\) for some \(n\in\mathbb Z\). Every orbit is countable and dense, while \(Q\) has many distinct points. The quotient topology on \(Q\) is indiscrete: its only open sets are \(\varnothing\) and \(Q\).

## Why functions collapse

A continuous function constant on each orbit is constant on the dense orbit of any one point and hence on the whole circle. A nonempty proper saturated open subset would have a nonempty invariant closed complement containing a dense orbit, a contradiction. This proves the quotient-topology assertion.

Haar ergodicity also gives \(L^\infty(\mathbb T)^\alpha=\mathbb C1\), even though invariant null sets such as individual orbits exist. The [[operator-algebras/group-measure-space-construction|crossed product]] retains functions and implementing motion and provides a richer algebraic object associated with this quotient.

## References

1. Alain Connes, [*Noncommutative Geometry*](https://alainconnes.org/wp-content/uploads/book94bigpdf.pdf), 1994, Introduction, examples of quotient spaces.
