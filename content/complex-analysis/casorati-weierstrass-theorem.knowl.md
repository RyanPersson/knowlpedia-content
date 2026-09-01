+++
id = "complex-analysis/casorati-weierstrass-theorem"
title = "Casorati–Weierstrass theorem"
kind = "theorem"
summary = "Near an essential singularity, the image of every punctured neighborhood is dense in the complex plane."
aliases = ["Casorati-Weierstrass theorem", "Weierstrass–Casorati theorem"]
domains = ["complex-analysis"]
prerequisites = []
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(a\) be an essential isolated singularity of a holomorphic function \(f\). For every \(\delta>0\), the set
\[
f\bigl(\{z:0<|z-a|<\delta\}\bigr)
\]
is dense in \(\mathbb C\).

## Equivalent sequential form

For every \(w\in\mathbb C\), there is a sequence \(z_n\to a\), with \(z_n\ne a\), such that \(f(z_n)\to w\). Thus no finite value can be separated by a neighborhood from all values of \(f\) sufficiently close to the singularity.

## Proof idea

If some disc around \(w\) were omitted near \(a\), then \(1/(f-w)\) would be bounded there. Riemann's removable singularity theorem would extend that reciprocal across \(a\). Its value at \(a\) would either be nonzero, making \(f\) removable, or zero of finite order, making \(f\) have a pole—both contradict essentiality.

## Strengthening

The [[complex-analysis/great-picard-theorem|great Picard theorem]] strengthens density to actual infinite attainment of every complex value with at most one exception.

## References

1. John B. Conway, *Functions of One Complex Variable I*, 2nd ed., Springer, 1978. [Publisher record](https://doi.org/10.1007/978-1-4612-6313-5). Relevant: Chapter V, §2.
