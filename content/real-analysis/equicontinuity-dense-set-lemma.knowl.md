+++
id = "real-analysis/equicontinuity-dense-set-lemma"
title = "Equicontinuity and dense sets lemma"
kind = "knowl"
summary = "On a compact metric space, equicontinuity allows pointwise Cauchy behavior on a dense set to upgrade to uniform Cauchy behavior."
aliases = ["equicontinuity-dense-set-lemma", "Equicontinuity and dense sets lemma"]
domains = ["real-analysis"]
prerequisites = ["topology/metric-space", "topology/dense-set", "real-analysis/equicontinuity", "real-analysis/uniform-cauchy"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
legacy_source_path = "real-analysis/equicontinuity-dense-set-lemma.md"
+++

**Equicontinuity and dense sets lemma.** Let \(K\) be a compact [[topology/metric-space|metric space]], let \(D\subseteq K\) be [[topology/dense-set|dense]], and let \((f_n)\) be an [[real-analysis/equicontinuity|equicontinuous]] sequence of functions \(f_n:K\to\mathbb R\). If \((f_n(x))\) is Cauchy for every \(x\in D\), then \((f_n)\) is [[real-analysis/uniform-cauchy|uniformly Cauchy]] on \(K\).

## Remarks

Because \(\mathbb R\) is complete, the [[real-analysis/uniform-cauchy-iff-uniform-convergence|uniform Cauchy criterion]] implies that \((f_n)\) converges [[real-analysis/uniform-convergence|uniformly]] on \(K\).
