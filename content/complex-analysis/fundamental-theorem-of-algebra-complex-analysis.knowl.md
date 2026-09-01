+++
id = "complex-analysis/fundamental-theorem-of-algebra-complex-analysis"
title = "Fundamental theorem of algebra (complex analysis)"
kind = "theorem"
summary = "Every nonconstant complex polynomial has a complex root, with a proof via Liouville's theorem."
aliases = ["fundamental theorem of algebra"]
domains = ["complex-analysis", "algebra"]
prerequisites = []
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Every nonconstant polynomial \(p\in\mathbb C[z]\) has a zero in \(\mathbb C\). Consequently, a degree-\(n\) polynomial factors as
\[
p(z)=c\prod_{j=1}^{n}(z-\alpha_j)
\]
for complex numbers \(\alpha_j\), counted with multiplicity.

## Complex-analytic proof

If \(p\) had no zero, then \(1/p\) would be entire. Since \(|p(z)|\to\infty\) as \(|z|\to\infty\), the reciprocal is bounded outside a large disc; continuity bounds it on the disc. The [[complex-analysis/liouville-theorem|Liouville theorem]] would make \(1/p\), and hence \(p\), constant, a contradiction.

## Scope

The theorem says that \(\mathbb C\) is [[algebraic-geometry-foundations/algebraically-closed-field|algebraically closed]]. The proof recorded here is analytic; algebraic and topological proofs establish the same statement by different methods. The theorem does not say that polynomial roots can always be expressed by radicals.

## References

1. John B. Conway, *Functions of One Complex Variable I*, 2nd ed., Springer, 1978. [Publisher record](https://doi.org/10.1007/978-1-4612-6313-5). Relevant: Chapter III, §4.
