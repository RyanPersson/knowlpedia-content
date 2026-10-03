+++
id = "algebra-rings/associative-algebra-derivation"
title = "Derivation of an associative algebra"
kind = "definition"
summary = "A linear map satisfying the Leibniz product rule."
aliases = []
domains = ["algebra-rings"]
section_mode = "progressive"
prerequisites = ["algebra-modules/algebra-over-ring", "linear-algebra/linear-map"]
+++

A **derivation** of an [[algebra-modules/algebra-over-ring|associative algebra]] \(A\) over a field \(k\) is a \(k\)-linear map \(\delta:A\to A\) satisfying the Leibniz rule
\[
\delta(ab)=\delta(a)b+a\delta(b)\qquad(a,b\in A).
\]
For a unital algebra, this implies \(\delta(1)=0\).

## Examples

Ordinary differentiation on polynomial functions is a derivation. For fixed \(c\in A\), the commutator \(a\mapsto ca-ac\) is a derivation, since its two middle terms cancel in the Leibniz identity. Derivations of dense subalgebras of operator algebras need not be bounded or extend to the whole completion.
