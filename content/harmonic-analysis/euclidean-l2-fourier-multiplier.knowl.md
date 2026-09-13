+++
id = "harmonic-analysis/euclidean-l2-fourier-multiplier"
title = "Euclidean L2 Fourier multiplier"
kind = "definition"
summary = "A bounded measurable frequency function defines a bounded operator on Euclidean L2."
aliases = ["bounded Fourier multiplier on L2"]
domains = ["harmonic-analysis"]
section_mode = "progressive"
prerequisites = ["harmonic-analysis/plancherel-theorem-lca", "functional-analysis/fourier-transform-schwartz-space", "functional-analysis/bounded-linear-operator", "measure-theory/essential-supremum"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For \(m\in L^\infty(\mathbb R^n)\), the **\(L^2\) Fourier multiplier with symbol \(m\)** is the operator \(T_m\) determined by
\[
\widehat{T_mf}=m\widehat f\qquad(f\in L^2(\mathbb R^n)).
\]
[[harmonic-analysis/plancherel-theorem-lca|Plancherel's theorem]] makes it a bounded operator, with \(\|T_m\|_{L^2\to L^2}=\|m\|_\infty\), where the latter is the essential supremum.

## Scope

The upper bound follows by multiplying inside the Fourier \(L^2\) norm. The reverse bound follows by taking a nonzero Fourier function supported on a finite-measure subset where \(|m|\) is close to its essential supremum. Boundedness of \(m\) alone does not imply \(L^p\) boundedness for other \(p\). Nor does it define multiplication of arbitrary tempered distributions by \(m\).
