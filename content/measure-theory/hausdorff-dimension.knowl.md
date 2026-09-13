+++
id = "measure-theory/hausdorff-dimension"
title = "Hausdorff dimension"
kind = "definition"
summary = "The critical power at which Hausdorff measures become zero."
aliases = []
domains = ["measure-theory"]
section_mode = "progressive"
prerequisites = ["measure-theory/hausdorff-measure", "real-analysis/infimum", "convex-analysis/extended-real-number-system-and-conventions"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For a set \(E\) in a metric space, its **Hausdorff dimension** is
\[
\dim_H E=\inf\{s>0:\mathcal H^s(E)=0\},
\]
with infimum infinity if this set is empty. Here \(\mathcal H^s\) is [[measure-theory/hausdorff-measure|Hausdorff measure]] for the specified metric. The definition assigns dimension zero to the empty set; some authors use a different empty-set convention.

## Critical exponent

If \(s<t\), a cover by sets of diameter at most \(\delta\) has its \(t\)-cost bounded by \(\delta^{t-s}\) times its \(s\)-cost. Hence finiteness at exponent \(s\) forces vanishing at each larger exponent. At the critical exponent, the measure can be zero, finite positive, or infinite.
