+++
id = "langlands/ind-coherent-sheaf"
title = "Ind-coherent sheaf"
kind = "definition"
summary = "An object of the cocomplete category obtained by adjoining filtered colimits to coherent sheaves on a derived stack."
aliases = ["IndCoh object", "ind-coherent complex"]
domains = ["langlands", "algebraic-geometry-foundations"]
section_mode = "progressive"
prerequisites = ["algebraic-geometry-foundations/coherent-sheaf"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

For a suitable derived scheme or stack \(Y\), the category
\(\operatorname{IndCoh}(Y)\) is the ind-completion of the category
\(\operatorname{Coh}(Y)\) of coherent complexes. An **ind-coherent sheaf** on
\(Y\) is an object of \(\operatorname{IndCoh}(Y)\).

Unlike quasi-coherent sheaves, ind-coherent sheaves carry a functorial notion
of [[langlands/singular-support-of-coherent-sheaf|singular support]] when
\(Y\) is quasi-smooth. On a smooth \(Y\), the distinction is largely a
renormalization; on a singular derived stack it records additional
directions.

## References

1. Dima Arinkin and Dennis Gaitsgory, “Singular support of coherent sheaves,
   and the geometric Langlands conjecture,” *Selecta Mathematica* 21 (2015),
   1–199. [arXiv](https://arxiv.org/abs/1201.6343).
