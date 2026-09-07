+++
id = "mathematical-physics/single-particle-structure-sigma-h"
title = "Single Particle Structure Σ(H)"
kind = "knowl"
summary = "Segal's package (K,B) extracted from a complex Hilbert space H for CCR quantization"
aliases = ["single-particle-structure-sigma-h", "Single Particle Structure Σ(H)"]
domains = ["mathematical-physics"]
legacy_source_path = "shale-paper/single-particle-structure-sigma-h.md"
prerequisites = ["linear-algebra/hilbert-space", "linear-algebra/symplectic-form", "functional-analysis/symplectic-hilbert-space"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Given a complex [[linear-algebra/hilbert-space|Hilbert space]] \(H\), its **single particle structure** is
\(\Sigma(H)=(K,B)\), where \(K\) is \(H\) viewed as a *real* [[linear-algebra/hilbert-space|Hilbert space]] with [[linear-algebra/inner-product|inner product]] \(\Re(\cdot,\cdot)_c\),
and \(B(z_1,z_2)=\Im(z_1,z_2)_c\).

## Remarks

**Key properties:**
- \(B\) is a [[linear-algebra/symplectic-form|symplectic form]] on \(K\) (skew + nondegenerate).
- Symmetries of the free boson field act as \(B\)-preserving maps on \(K\).

## Examples

- \(H=L^2(\mathbb R^d)\) gives a real [[differential-geometry/classical-phase-space|phase space]] \(K\) with \(B=\Im(\cdot,\cdot)\).
