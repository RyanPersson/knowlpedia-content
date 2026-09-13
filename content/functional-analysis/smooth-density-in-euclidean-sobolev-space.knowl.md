+++
id = "functional-analysis/smooth-density-in-euclidean-sobolev-space"
title = "Smooth compact-support approximation in Euclidean Sobolev space"
kind = "theorem"
summary = "Every finite-exponent integer-order Sobolev function on the whole space can be approximated by test functions."
aliases = []
domains = ["functional-analysis"]
section_mode = "progressive"
prerequisites = ["functional-analysis/sobolev-space", "real-analysis/mollifier", "real-analysis/cutoff-function", "real-analysis/multi-index-leibniz-rule", "functional-analysis/test-function-space"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 2
+++

For an integer \(k\ge0\) and \(1\le p<\infty\), the [[functional-analysis/test-function-space|test functions]] \(C_c^\infty(\mathbb R^n)\) are dense in \(W^{k,p}(\mathbb R^n)\): for every \(u\) there are \(u_j\in C_c^\infty\) with \(\|u_j-u\|_{W^{k,p}}\to0\).

## Cut off, then smooth

Choose a smooth cutoff \(\chi=1\) near zero and set \(\chi_R(x)=\chi(x/R)\). The Leibniz formula gives \(\chi_Ru\to u\) in \(W^{k,p}\): the main terms converge by integrable tails, and terms with a derivative on \(\chi_R\) carry a factor \(R^{-1}\) or smaller. For fixed \(R\), mollification converges for every weak derivative through order \(k\) and preserves compact support up to an \(\varepsilon\)-neighborhood. A diagonal choice gives the sequence.

This assertion concerns the whole space. On a domain with boundary, test functions need not approximate arbitrary Sobolev boundary values. The restriction \(p<\infty\) is also essential to this statement.

## References

- [Hunter, Sobolev Spaces, §§3.5–3.7](https://www.math.ucdavis.edu/~hunter/pdes/ch3.pdf).
