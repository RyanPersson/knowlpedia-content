+++
id = "ergodic-theory/poincare-recurrence-theorem"
title = "Poincare recurrence theorem"
kind = "theorem"
summary = "Almost every point of a measurable event returns to it infinitely often in a finite measure-preserving system."
aliases = ["Poincaré recurrence theorem"]
domains = ["ergodic-theory"]
section_mode = "progressive"
prerequisites = ["ergodic-theory/measure-preserving-system", "measure-theory/almost-everywhere"]
+++

If \(T\) [[ergodic-theory/measure-preserving-transformation|preserves a probability measure]] and \(E\) is measurable, then almost every \(x\in E\) has \(T^nx\in E\) for infinitely many positive integers \(n\). This is the **Poincaré recurrence theorem**; ergodicity and invertibility are not required.

## Proof

Let \(B\subseteq E\) be the points that never return to \(E\) at positive times. The sets \(T^{-n}B\), \(n\geq0\), are pairwise disjoint and have equal measure. Finiteness of the total measure forces \(\mu(B)=0\). A point of \(E\) with only finitely many returns eventually reaches \(B\), so all such points lie in the null set \(\bigcup_{n\geq0}T^{-n}B\).

## Scope

Recurrence does not assert a period or a uniform return-time bound. Translation on the real line with infinite Lebesgue measure shows why finiteness of the measure matters.

## References

1. Jesse Peterson, [*Lecture notes on ergodic theory*](https://www.math.vanderbilt.edu/~peters10/teaching/Spring2011/ErgodicTheoryNotes.pdf), 2011. §2.6.
