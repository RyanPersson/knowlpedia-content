+++
id = "asymptotics/little-o"
title = "Little-o notation"
kind = "definition"
summary = "A quantity negligible relative to a comparison function in a specified limit."
aliases = []
domains = ["asymptotics"]
section_mode = "progressive"
prerequisites = ["shared-foundations/function", "real-analysis/limit-of-a-function-at-a-point", "real-analysis/modulus-on-c", "linear-algebra/normed-vector-space"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 2
+++

For functions \(f\) and \(g>0\) on a punctured right neighborhood of zero, **\(f(\varepsilon)=o(g(\varepsilon))\) as \(\varepsilon\downarrow0\)** means the following [[real-analysis/limit-of-a-function-at-a-point|limit]] vanishes:
\[
\lim_{\varepsilon\downarrow0}\frac{f(\varepsilon)}{g(\varepsilon)}=0.
\]
Equivalently, for every \(\eta>0\) there is \(\delta>0\) such that \(|f(\varepsilon)|\le\eta g(\varepsilon)\) for \(0<\varepsilon<\delta\). A norm replaces absolute value for vector-valued quantities.

## Comparison with a bounded ratio

Little-o implies [[asymptotics/big-o|Big-O]], but not conversely: \(\varepsilon^2=o(\varepsilon)\), while \(\varepsilon\) is not \(o(\varepsilon)\). A uniform little-o statement requires one \(\delta\) for all values of every parameter declared uniform.

## References

- [NIST Digital Library of Mathematical Functions, §2.1: Definitions and elementary properties](https://dlmf.nist.gov/2.1).
