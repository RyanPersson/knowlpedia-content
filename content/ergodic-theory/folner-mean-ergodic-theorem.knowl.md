+++
id = "ergodic-theory/folner-mean-ergodic-theorem"
title = "Mean ergodic theorem along Følner sets"
kind = "theorem"
summary = "Averages of a unitary representation over inverse Følner sets converge to the fixed-vector projection."
aliases = []
domains = ["ergodic-theory"]
section_mode = "progressive"
prerequisites = ["harmonic-analysis/folner-condition", "lie-groups/strongly-continuous-unitary-representation", "harmonic-analysis/invariant-vector", "linear-algebra/orthogonal-projection"]
+++

Let \(G\) be a countable discrete group with finite nonempty [[harmonic-analysis/folner-condition|left Følner sets]] \(F_N\), so \(|hF_N\triangle F_N|/|F_N|\to0\) for each \(h\in G\). For a [[lie-groups/strongly-continuous-unitary-representation|unitary representation]] \(\pi\) and projection \(P\) onto its [[harmonic-analysis/invariant-vector|invariant vectors]],
\[
\frac1{|F_N|}\sum_{g\in F_N}\pi(g^{-1})v\longrightarrow Pv
\quad\text{in Hilbert-space norm}.
\]
The inverse is part of this convention: left Følner sets give the required right translation control for these operators.

## Reason and Koopman form

The averages fix invariant vectors. Applied to \(\pi(h)w-w\), their norm is at most \(|h^{-1}F_N\triangle F_N|\|w\|/|F_N|\), which tends to zero. The closed span of such differences is the orthogonal complement of the fixed vectors.

For inverse-pullback Koopman representations, the averages are \(|F_N|^{-1}\sum_{g\in F_N}f\circ T_g\). The result is mean convergence; it does not assert pointwise convergence along arbitrary Følner sequences.

## References

1. Jesse Peterson, [*Lecture notes on ergodic theory*](https://www.math.vanderbilt.edu/~peters10/teaching/Spring2011/ErgodicTheoryNotes.pdf), 2011. §1.6.1, mean ergodic theorem for amenable groups.
