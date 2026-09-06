+++
id = "complex-analysis/residue-theorem"
title = "Residue theorem"
kind = "theorem"
summary = "A contour integral of a meromorphic function is the winding-number-weighted sum of its residues."
aliases = ["Cauchy residue theorem"]
domains = ["complex-analysis"]
prerequisites = ["complex-analysis/meromorphic-function", "complex-analysis/winding-number", "complex-analysis/residue", "complex-analysis/complex-contour-integral"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(D\subseteq\mathbb C\) be open, let \(f\) be meromorphic on \(D\), and let \(\gamma\) be a closed piecewise \(C^1\) contour avoiding the poles of \(f\). Suppose \(\operatorname{Ind}(\gamma,a)=0\) for every \(a\notin D\) and only finitely many poles have nonzero index. Then
\[
\int_\gamma f(z)\,dz
=2\pi i\sum_{a\in D}\operatorname{Ind}(\gamma,a)
\operatorname{Res}(f,a).
\]

## Usual simple-contour form

If \(\gamma\) is a positively oriented simple closed contour whose interior and boundary lie in \(D\), then every interior point has index \(1\) and every exterior point has index \(0\). The formula reduces to \(2\pi i\) times the sum of the [[complex-analysis/residue|residues]] at poles inside.

## Uses

The theorem computes real and complex integrals, extracts coefficients, and yields the [[complex-analysis/argument-principle|argument principle]] after applying it to the [[complex-analysis/logarithmic-derivative|logarithmic derivative]] \(f'/f\). Its winding-number formulation keeps orientation and multiply connected geometry explicit.

## References

1. John B. Conway, *Functions of One Complex Variable I*, 2nd ed., Springer, 1978. [Publisher record](https://doi.org/10.1007/978-1-4612-6313-5). Relevant: Chapter VI, §1.
