+++
id = "proofs/grh/derivatives-vacuum/unit-linear-form"
title = "Vectors with a unit linear form at p"
kind = "definition"
summary = "A vector y of E such that the period factor times the conjugate of each CM embedding of y is a unit at a given p-adic place."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Parameters.HasUnitLinearForm"]
lean_files = ["src/New/Derivatives/Vacuum/ShortVectors.lean"]
+++

Let \(P\) be [[?lean:New.Parameters|parameters]], \(s\in\mathbb{N}\), \(p\) a prime and \(\iota_p\colon\mathbb{C}\to\mathbb{C}_p\) a [[?lean:New.PadicPlace|\(p\)-adic place]]. A vector \(y\in E\) **has a unit linear form at \(\iota_p\)** if
\[ \bigl\lvert\iota_p\bigl(\varpi\,\overline{\Phi_\tau(y)}\bigr)\bigr\rvert_p=1\qquad\text{for every infinite place }\tau\text{ of }E, \]
where \(\varpi\) is the [[proofs/grh/derivatives-vacuum/jet-scale|period factor]]. These numbers are the coefficients of the linear form \(z\mapsto\varpi\sum_\tau\overline{\Phi_\tau(y)}z_\tau\).

## References

1. Lean: `New.Parameters.HasUnitLinearForm` in `src/New/Derivatives/Vacuum/ShortVectors.lean`.
