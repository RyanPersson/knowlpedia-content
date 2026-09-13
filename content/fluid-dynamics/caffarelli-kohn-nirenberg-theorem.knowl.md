+++
id = "fluid-dynamics/caffarelli-kohn-nirenberg-theorem"
title = "Caffarelli–Kohn–Nirenberg partial regularity theorem"
kind = "theorem"
summary = "The interior singular set of an unforced suitable three-dimensional solution has zero parabolic one-dimensional measure."
aliases = ["CKN theorem"]
domains = ["fluid-dynamics"]
section_mode = "progressive"
prerequisites = ["fluid-dynamics/suitable-weak-solution", "fluid-dynamics/singular-set-of-weak-solution", "measure-theory/parabolic-hausdorff-measure", "partial-differential-equations/partial-regularity"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

Let \((u,p)\) be an **unforced** [[fluid-dynamics/suitable-weak-solution|suitable weak solution]] of the three-dimensional Navier–Stokes equations on an open cylinder \(Q\), with \(\nu>0\). Its interior [[fluid-dynamics/singular-set-of-weak-solution|singular set]] satisfies
\[
\mathcal H^1_{\rm par}(S(u))=0,
\]
where \(\mathcal H^1_{\rm par}\) is [[measure-theory/parabolic-hausdorff-measure|parabolic one-dimensional Hausdorff measure]]. This is the unforced interior form of the **Caffarelli–Kohn–Nirenberg partial regularity theorem**.

It is a [[partial-differential-equations/partial-regularity|partial regularity]] statement.

## Scope

The conclusion is [[partial-differential-equations/partial-regularity|partial regularity]], not emptiness of the singular set. Boundary versions and forced versions require additional hypotheses and estimates. The theorem uses suitability, including its local energy inequality.

## References

- [Caffarelli, Kohn and Nirenberg, Partial regularity of suitable weak solutions (1982)](https://doi.org/10.1002/cpa.3160350604).
