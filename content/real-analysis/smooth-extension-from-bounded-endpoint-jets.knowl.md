+++
id = "real-analysis/smooth-extension-from-bounded-endpoint-jets"
title = "Smooth extension from bounded endpoint jets"
kind = "theorem"
summary = "Compatible derivative limits can be continued through an endpoint by realizing their normal jet on the other side."
aliases = []
domains = ["real-analysis"]
section_mode = "progressive"
prerequisites = ["real-analysis/one-sided-jet-limits-from-derivative-bounds", "real-analysis/borel-jet-extension", "real-analysis/smooth-extension", "real-analysis/smooth-zero-extension", "real-analysis/compactly-supported-function"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 2
+++

Under the hypotheses of [[real-analysis/one-sided-jet-limits-from-derivative-bounds|one-sided endpoint jet limits]], a smooth \(f\) on \(U\times(0,T)\) admits a smooth extension through time \(T\), locally in \(U\). If all its slices have support in one fixed compact \(K\subset U\), the extension for \(t\ge T\) can retain that spatial support and vanish for \(t\ge T+1\).

## Match the normal jet

Let \(F_j(x)=\lim_{t\uparrow T}\partial_t^jf(x,t)\). Borel's theorem gives a smooth \(g(x,\sigma)\) with \(\partial_\sigma^jg(x,0)=F_j(x)\). Use \(g(x,t-T)\) for \(t\ge T\) and the original \(f\) for \(t<T\). Every mixed derivative has matching one-sided limits. The coordinate-segment fundamental theorem of calculus proves that the glued function is smooth.

For fixed compact support, all \(F_j\) retain that support, and the shrinking-cutoff Borel construction retains it while being supported in \(|\sigma|\le1\). This extends the given function, rather than asserting convergence of its formal endpoint Taylor series.
