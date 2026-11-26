+++
id = "proofs/grh/onelift-comparison/denominator-bound"
title = "Denominator bound for the projection to a space of forms"
kind = "definition"
summary = "An l-adic bound, per dimension and row, for the denominators of the orthogonal projections to a subspace Z of integral forms orthogonal to the false lifts."
aliases = ["denominator at most beta"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Selmer.DenominatorLe"]
lean_files = ["src/New/OneLift/TestedForms.lean"]
+++

Let \(O\) be a [[?lean:New.DescentPair|descent pair]] with Weil data, \(\ell\) a prime, \(\iota\colon\mathbb{C}\simeq\overline{\mathbb{Q}}_\ell\) an isomorphism, \(e_0\in\mathbb{C}[\bar G_M]\), \(Z\) a subspace of the forms on \(V\), and \(\beta\in\mathbb{R}\). Write \(\operatorname{pr}_Z\) for the [[linear-algebra/orthogonal-projection|orthogonal projection]] to \(Z\) and \(\lvert\cdot\rvert_\iota\) for the \(\ell\)-adic absolute value pulled back by \(\iota\).

The projection to \(Z\) has **denominator at most \(\beta\)** at \(\iota\) (for \(O,e_0\)) if there is a linear operator \(\Lambda\) on \(Z\) with
\[
\lvert\det\Lambda\rvert_\iota\ \ge\ \exp\bigl(-\dim Z\cdot\lvert r\rvert\cdot\beta\bigr)
\]
such that for every form \(y\) that is integral at \(\iota\) and [[proofs/grh/onelift-comparison/false-lifts|orthogonal to the false lifts]] for \((e_0,Z^\perp)\):

1. \(\Lambda(\operatorname{pr}_Z y)\) is integral at \(\iota\); and
2. \(\lvert\langle y',\Lambda(\operatorname{pr}_Z y)\rangle\rvert_\iota\le 1\) for every form \(y'\) integral at every embedding \(\mathbb{C}\to\mathbb{C}_\ell\).

Here a form is integral at an embedding if all its values have [[?lean:New.weylGauge|gauge]] at most \(1\) there.

## Remarks

This is a congruence-number condition: \(\Lambda\) clears the \(\ell\)-adic denominators of the projection to \(Z\) (in use, a space of lifts), at a determinant cost of \(\ell^{-\beta'}\) per dimension and per row of \(W\).

## References

1. Lean: `New.Selmer.DenominatorLe` in `src/New/OneLift/TestedForms.lean`.
