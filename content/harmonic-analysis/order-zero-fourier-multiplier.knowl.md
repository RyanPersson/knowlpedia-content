+++
id = "harmonic-analysis/order-zero-fourier-multiplier"
title = "Order-zero Fourier multiplier"
kind = "definition"
summary = "A bounded smooth-away-from-zero symbol with scale-invariant derivative bounds of every order."
aliases = []
domains = ["harmonic-analysis"]
section_mode = "progressive"
prerequisites = ["harmonic-analysis/euclidean-l2-fourier-multiplier", "real-analysis/multi-index-notation", "real-analysis/class-ck-function"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

An **order-zero Fourier multiplier** here is \(m(D)\) with symbol \(m\in C^\infty(\mathbb R^n\setminus\{0\})\) such that
\[
M_k(m):=\max_{|\gamma|\leq k}\sup_{\xi\ne0}
 |\xi|^{|\gamma|}|\partial^\gamma m(\xi)|<\infty
\quad(k=0,1,2,\ldots).
\]
Here \(\gamma\) is a [[real-analysis/multi-index-notation|multi-index]]. In particular \(m\) is bounded, so it defines an [[harmonic-analysis/euclidean-l2-fourier-multiplier|L2 multiplier]].

The symbol has [[real-analysis/class-ck-function|smooth derivatives]] on the punctured frequency space.

## Real fields

The condition \(m(-\xi)=\overline{m(\xi)}\) ensures that \(m(D)\) preserves real functions. A scalar symbol acts componentwise on vector fields and preserves the divergence-free condition.
