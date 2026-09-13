+++
id = "measure-theory/hausdorff-measure"
title = "Hausdorff measure in a metric space"
kind = "definition"
summary = "An outer measure obtained from covers by sets of small diameter and a power cost."
aliases = ["Hausdorff outer measure"]
domains = ["measure-theory"]
section_mode = "progressive"
prerequisites = ["topology/metric-space", "topology/diameter", "measure-theory/outer-measure", "real-analysis/infimum", "real-analysis/real-power"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For \(s>0\) and \(E\) in a metric space, define
\[
\mathcal H^s_\delta(E)=\inf\left\{\sum_j(\operatorname{diam}U_j)^s:
E\subseteq\bigcup_jU_j,\ \operatorname{diam}U_j\le\delta\right\}.
\]
The **Hausdorff outer measure** is \(\mathcal H^s(E)=\lim_{\delta\downarrow0}\mathcal H^s_\delta(E)\). The limit exists because the covering infimum increases as the allowed diameters shrink. Its restriction to Borel sets is a measure. This convention omits a normalization constant; null sets are unaffected by multiplying by a fixed positive constant.

## Dimension and metric

The associated [[measure-theory/hausdorff-dimension|Hausdorff dimension]] records the threshold where these measures vanish. The metric is part of the definition: a different scaling of time and space can change both the measure and the dimension. For \(s=0\), the conventional Hausdorff measure is counting measure.
