+++
id = "differential-geometry/majorana-weyl-spinor"
title = "Majorana–Weyl spinor"
kind = "definition"
summary = "A chiral spinor fixed by a compatible real structure that preserves chirality."
aliases = ["Majorana-Weyl spinor", "real chiral spinor"]
domains = ["differential-geometry", "mathematical-physics"]
prerequisites = ["differential-geometry/majorana-spinor", "differential-geometry/weyl-spinor"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let
\[
\Delta=\Delta^+\oplus\Delta^-
\]
be an even-dimensional complex spinor module, and let \(J\) be a
[[differential-geometry/majorana-spinor|Majorana real structure]] that
preserves each half-spin module:
\[
J(\Delta^\pm)\subseteq\Delta^\pm.
\]
A **Majorana–Weyl spinor** of positive or negative chirality is a spinor
\(\psi\in\Delta^\pm\) such that
\[
J\psi=\psi.
\]
It is therefore simultaneously a [[differential-geometry/weyl-spinor|Weyl
spinor]] and a Majorana spinor.

The definition is available only when the dimension and signature admit a
real structure compatible with the chiral decomposition. The existence of a
Majorana condition and the existence of Weyl spinors separately do not imply
that the two conditions are compatible.

## References

1. Pierre Deligne, “Notes on spinors,” in *Quantum Fields and Strings: A
   Course for Mathematicians*, Volume 1, American Mathematical Society, 1999,
   pp. 99–135.
2. Daniel S. Freed, *Five Lectures on Supersymmetry*, American Mathematical
   Society, 1999. Relevant: Lectures 1–2.
