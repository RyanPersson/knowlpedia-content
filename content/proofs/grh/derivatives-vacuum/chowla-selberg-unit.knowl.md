+++
id = "proofs/grh/derivatives-vacuum/chowla-selberg-unit"
title = "The Chowla-Selberg unit of the CM curve"
kind = "definition"
summary = "The complex number u, a unit at every p-adic place, that normalises the areas of all conjugates of the CM curve."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Parameters.chowlaSelbergUnit", "New.Parameters.norm_iota_chowlaSelbergUnit", "New.Parameters.area_mul_norm_chowlaSelbergUnit_sq"]
lean_files = ["src/New/Derivatives/Vacuum/TightFrames.lean"]
+++

Let \(\mathcal{E}\) be the [[proofs/grh/derivatives-vacuum/cm-curve-and-period|CM curve]] of the parameters \(P\). The **Chowla–Selberg unit** \(u\in\mathbb{C}\) is a complex number chosen by the [[?lean:New.CMLattice.chowla_selberg|Chowla–Selberg formula]] for \(\mathcal{E}\). It has the following two properties, and nothing else about it is used.

1. For every prime \(p\) and every [[?lean:New.PadicPlace|\(p\)-adic place]] \(\iota_p\colon\mathbb{C}\to\mathbb{C}_p\), \(\lvert\iota_p(u)\rvert_p=1\).
2. For every field automorphism \(\sigma\) of \(\mathbb{C}\) over \(K\), with \(\mathcal{E}^{\sigma}\) the [[?lean:New.CMLattice.galConjugate|conjugate CM lattice]] and \(A(\mathcal{E}^\sigma)\) the area of its period parallelogram,
\[ A(\mathcal{E}^{\sigma})\,\lvert\sigma(u)\rvert^{2}=\pi\,e^{c}\,\frac{2\pi}{\sqrt d},\qquad c=\gamma-\operatorname{Re}\frac{L'}{L}(1,\chi_K), \]
where \(\gamma\) is the [[?c:Euler–Mascheroni constant|Euler–Mascheroni constant]] and \(\chi_K\) is the [[?c:Quadratic Dirichlet character of a quadratic field|quadratic character]] of \(K\) (the constant \(c\) is [[?lean:New.chowlaSelbergConst|the Chowla–Selberg constant]] of \(d\)).

## References

1. Lean: `New.Parameters.chowlaSelbergUnit`, `New.Parameters.norm_iota_chowlaSelbergUnit`, `New.Parameters.area_mul_norm_chowlaSelbergUnit_sq` in `src/New/Derivatives/Vacuum/TightFrames.lean`.
