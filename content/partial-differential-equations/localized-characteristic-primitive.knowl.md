+++
id = "partial-differential-equations/localized-characteristic-primitive"
title = "Localized characteristic primitive with an explicit defect"
kind = "definition"
summary = "Subtracting a transported total integral makes a primitive compactly supported and records the cutoff error exactly."
aliases = ["compact transport primitive", "modified radial integral"]
domains = ["partial-differential-equations"]
section_mode = "progressive"
prerequisites = ["partial-differential-equations/shifted-characteristic-primitive", "real-analysis/cutoff-function", "real-analysis/product-rule", "shared-foundations/support-of-a-function", "harmonic-analysis/normalized-torus-average"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 2
+++

For the [[partial-differential-equations/shifted-characteristic-primitive|characteristic integrals]] \(I^-,I^+,J=I^-+I^+\), choose a smooth \(\chi(U)\) equal to zero below a finite interval and one above it. Define
\[
I_\chi F=I^-F-\chi JF=(1-\chi)I^-F-\chi I^+F.
\]
This **localized primitive** obeys the exact identity
\[
D_M I_\chi F=F-\chi'(U)JF.
\]
It has compact support in \(U\), contained between the smallest and largest endpoints of the source support and the cutoff transition.

## Support and averaging

Below both intervals, \(I^-F=0\) and \(\chi=0\); above both, \(I^-F=JF\) and \(\chi=1\). The support can fill gaps between source pieces. Since torus translation preserves its normalized measure,
\[
\langle JF\rangle_y=\int_{\mathbb R}\langle F(s,\cdot)\rangle_y\,ds.
\]
Thus a zero integrated torus mean makes the defect's mean zero. It need not make the defect itself zero. If \(F\) is independent of \(y\), the same zero integral makes \(JF=0\) exactly.
