+++
id = "shared-foundations/descent-through-surjection"
title = "Descent of a function through a surjection"
kind = "definition"
summary = "A function factors uniquely through a surjection exactly when it is constant on its fibers."
aliases = ["descent of a function", "function descent"]
domains = ["shared-foundations"]
section_mode = "progressive"
prerequisites = ["shared-foundations/surjective-function", "shared-foundations/function", "shared-foundations/composition-of-functions"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

Given a [[shared-foundations/surjective-function|surjection]] \(p:X\to Y\), a function \(f:X\to Z\) **descends through \(p\)** if there is a function \(F:Y\to Z\) such that \(f=F\circ p\).

## Criterion and uniqueness

Descent holds exactly when \(p(x)=p(x')\) implies \(f(x)=f(x')\). In that case define \(F(y)=f(x)\) for any \(x\) over \(y\); constancy on fibers makes the value independent of the choice, and surjectivity gives uniqueness.

For a smooth covering, a smooth descending function has a smooth descended representative by the local inverse charts. In the torus covering \(p_A\), the criterion becomes invariance under all [[topology/deck-transformation|deck translations]] \(a\) with \(Aa\in\mathbb Z^n\). Invariance under an arbitrary smaller collection of translations need not suffice.
