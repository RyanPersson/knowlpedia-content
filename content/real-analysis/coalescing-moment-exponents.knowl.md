+++
id = "real-analysis/coalescing-moment-exponents"
title = "Inverse loss when two moment exponents coalesce"
kind = "theorem"
summary = "A two-row moment matrix from translated positive bumps has inverse size of reciprocal order in the exponent separation."
aliases = ["coalescing moment weights"]
domains = ["real-analysis"]
section_mode = "progressive"
prerequisites = ["linear-algebra/moment-pairing-matrix", "linear-algebra/matrix-inverse", "real-analysis/exponential-function", "real-analysis/mean-value-theorem", "asymptotics/big-o", "differential-geometry/bump-function", "linear-algebra/operator-norm"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 2
+++

Fix a nonnegative nonzero compactly supported smooth bump \(\beta\) on \(\mathbb R\), and centers \(c_1<c_2\). Pair the translated bumps \(\beta(y-c_j)\) with weights \(e^{s_i y}\), \(i=1,2\), where the distinct slopes lie in a fixed compact interval. The resulting matrix \(B\) obeys
\[
\|B^{-1}\|=O(|s_2-s_1|^{-1})
\quad\text{as }s_2-s_1\longrightarrow0.
\]
This quantifies loss of invertibility of the [[linear-algebra/moment-pairing-matrix|moment system]] near equal weights.

## Determinant computation

Set \(b(s)=\int e^{st}\beta(t)\,dt>0\) and \(\Delta=c_2-c_1\). Dividing row \(i\) by the bounded positive factor \(e^{s_i c_1}\) gives entries \((b(s_i),e^{s_i\Delta}b(s_i))\). The determinant is
\[
b(s_1)b(s_2)(e^{s_2\Delta}-e^{s_1\Delta}).
\]
The mean value theorem makes its absolute value comparable to \(|s_2-s_1|\); the numerator entries in the inverse formula remain bounded. The logarithmic substitution \(r=e^y\) converts power-weight moment problems into this exponential-weight setting, with the Jacobian included in the profile.
