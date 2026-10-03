+++
id = "ergodic-theory/shannon-mcmillan-breiman-theorem"
title = "Shannon–McMillan–Breiman theorem"
kind = "theorem"
summary = "Typical orbit-name probabilities decay exponentially at the partition entropy rate."
aliases = ["Shannon-McMillan-Breiman theorem", "asymptotic equipartition theorem for dynamics"]
domains = ["ergodic-theory"]
section_mode = "progressive"
prerequisites = ["ergodic-theory/kolmogorov-sinai-entropy", "ergodic-theory/ergodic-transformation", "ergodic-theory/measurable-partition"]
+++

Let \(T\) be [[ergodic-theory/ergodic-transformation|ergodic]] and probability preserving, and let \(\mathcal P\) be a [[ergodic-theory/measurable-partition|finite measurable partition]]. With \(\mathcal P^{(n)}=\bigvee_{j=0}^{n-1}T^{-j}\mathcal P\),
\[
-\frac1n\log\mu(\mathcal P^{(n)}(x))\longrightarrow h_\mu(T,\mathcal P)
\quad\text{for almost every }x.
\]
This is the finite-partition **Shannon–McMillan–Breiman theorem**. The union of zero-probability cells over all \(n\) is a null set and can be omitted.

## Interpretation

For a typical trajectory, the probability of observing its length-\(n\) name is \(\exp(-n h_\mu(T,\mathcal P)+o(n))\). If the partition is generating, its [[ergodic-theory/kolmogorov-sinai-entropy|entropy rate]] is the entropy of the entire system. The result extends the independent-symbol information law to dependent observations in any ergodic system.

## References

1. Karma Dajani, [*Introduction to Ergodic Theory and its Applications to Number Theory*](https://www.staff.science.uu.nl/~kraai101/LectureNotesMM-2.pdf), 2014, Theorem 5.4.2.
