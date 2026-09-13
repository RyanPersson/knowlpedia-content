+++
id = "real-analysis/dyadic-scale-partition"
title = "Smooth dyadic partition of a positive scale"
kind = "construction"
summary = "A locally finite partition of unity with uniform derivative bounds after dilation."
aliases = ["dyadic scale decomposition"]
domains = ["real-analysis"]
section_mode = "progressive"
prerequisites = ["real-analysis/cutoff-function", "topology/locally-finite-family", "shared-foundations/telescoping-sum", "real-analysis/scaled-cutoff-estimate"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

Choose a smooth nonincreasing \(\rho:\mathbb R\to[0,1]\) with \(\rho=1\) on \(( -\infty,1]\) and \(\rho=0\) on \([2,\infty)\). Put
\[
\chi(s)=\rho(s)-\rho(2s),\qquad
Q_\ell=2^{-\ell},\qquad \chi_\ell(q)=\chi(q/Q_\ell).
\]
For \(q>0\), the functions \(\chi_\ell\), \(\ell\in\mathbb Z\), form a smooth **dyadic scale partition**:
\[
\chi_\ell\ge0,\qquad \sum_{\ell\in\mathbb Z}\chi_\ell(q)=1,
\qquad \operatorname{supp}\chi_\ell\subset[Q_\ell/2,2Q_\ell].
\]
The family is [[topology/locally-finite-family|locally finite]] on \((0,\infty)\); at most three closed support intervals contain a given point.

## Proof and derivative bounds

The finite sum from \(\ell=-M\) to \(N\) telescopes to \(\rho(2^{-M}q)-\rho(2^{N+1}q)\), which equals one for sufficiently large \(M,N\). Differentiating gives \(|\partial_q^k\chi_\ell|\le C_k Q_\ell^{-k}\); on its support this is at most \(C'_k q^{-k}\). The constants are independent of \(\ell\). Hence every fixed power of \(q\partial_q\) is uniformly bounded as well.
