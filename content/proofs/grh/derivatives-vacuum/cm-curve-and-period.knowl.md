+++
id = "proofs/grh/derivatives-vacuum/cm-curve-and-period"
title = "The CM curve and the period of K"
kind = "definition"
summary = "A fixed CM lattice that is a complex multiple of the ring of integers of K, and the multiplier, called the period."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Parameters.cmCurve", "New.Parameters.cmPeriod", "New.Parameters.latticeModule_cmCurve", "New.Parameters.cmPeriod_mem_cmCurve_lattice"]
lean_files = ["src/New/Derivatives/Vacuum/TightFrames.lean"]
+++

Let \(P\) be [[?lean:New.Parameters|parameters]], with prime \(d\), and let \(K=\mathbb{Q}(\sqrt{-d})\subset\mathbb{C}\) with [[?c:Ring of integers of a number field|ring of integers]] \(\mathcal{O}_K\). The **CM curve** of \(P\) is a [[?lean:New.CMLattice|CM lattice]] \(\mathcal{E}\) for \(d\), and the **period** of \(K\) is a nonzero complex number \(\Omega_0\), both chosen once and for all so that the lattice of \(\mathcal{E}\) is
\[ \Lambda_{\mathcal{E}}=\Omega_0\,\mathcal{O}_K\subset\mathbb{C}. \]

## Remarks

The pair \((\mathcal{E},\Omega_0)\) is obtained by choice from the existence statement [[?lean:New.QuadField.exists_cmLattice_latticeModule_eq_scaledIdeal|every nonzero fractional ideal \(\mathfrak{a}\) of \(K\) has a complex multiple \(u\mathfrak{a}\), \(u\in\mathbb{C}^\times\), that is the lattice of a CM lattice]], applied to the unit ideal; the scale \(u=\Omega_0\) is produced by that statement (a CM lattice is normalised at its marked point, so the scale cannot be prescribed). A CM lattice carries more data than its lattice (a marked point of order two); only the displayed equality is used about the choice. In particular \(\Omega_0\in\Lambda_{\mathcal{E}}\), since \(1\in\mathcal{O}_K\).

## References

1. Lean: `New.Parameters.cmCurve`, `New.Parameters.cmPeriod`, `New.Parameters.latticeModule_cmCurve`, `New.Parameters.cmPeriod_mem_cmCurve_lattice` in `src/New/Derivatives/Vacuum/TightFrames.lean`.
