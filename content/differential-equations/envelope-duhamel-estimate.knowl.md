+++
id = "differential-equations/envelope-duhamel-estimate"
title = "Duhamel estimate with a common envelope"
kind = "lemma"
summary = "A propagator ratio bound preserves a source envelope at the cost of the interval length."
aliases = []
domains = ["differential-equations"]
section_mode = "progressive"
prerequisites = ["differential-equations/duhamel-formula", "harmonic-analysis/pulse-envelope", "linear-algebra/operator-norm"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

Let \(U(t,s)\) be a [[differential-equations/fundamental-matrix|propagator]] on \([0,L]\), and suppose a positive function \(P\) satisfies
\[
\|U(t,s)\|\le C\frac{P(t)}{P(s)}\qquad(0\le s\le t\le L).
\]
If \(z'=A(t)z+g(t)\), \(z(0)=0\), and \(\|g(t)\|\le G P(t)\), then
\[
\|z(t)\|\le C G t P(t)\le C G L P(t).
\]

## Proof and hypotheses

The [[differential-equations/duhamel-formula|Duhamel formula]] gives \(z(t)=\int_0^t U(t,s)g(s)\,ds\), and the two envelope factors at \(s\) cancel in the norm estimate. Nonzero initial data add at most \(C P(t)\|z(0)\|/P(0)\). A bound on values is proved here; parameter derivatives require differentiating the equation and controlling the resulting coefficient derivatives and source terms.
