+++
id = "asymptotics/shrinking-cutoff-asymptotic-summation"
title = "Asymptotic summation by shrinking cutoffs"
kind = "theorem"
summary = "Increasing decay orders with stage-independent derivative losses admit a smooth locally finite realization and quantitative tails."
aliases = ["shrinking-cutoff summation", "smooth asymptotic realization"]
domains = ["asymptotics"]
section_mode = "progressive"
prerequisites = ["real-analysis/cutoff-of-a-controlled-scale", "asymptotics/diagonal-choice-of-shrinking-scales", "analysis/locally-finite-smooth-sum", "real-analysis/multi-index-leibniz-rule", "asymptotics/logarithmic-loss-absorption", "real-analysis/cartesian-jet", "real-analysis/natural-logarithm", "real-analysis/real-power"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 2
+++

Let \(0<q<q_0\le1\) on \(\Omega\), with \(q\) smooth, bounded below on compact subsets, and \(|\partial^\alpha q|\le C_\alpha q^{1-c|\alpha|}\). Suppose smooth functions \(f_j\), all on \(\Omega\), satisfy
\[
|f_j|_m\le C_{j,m}q^{g_j-\ell_m}(1+|\log q|)^{P_{j,m}},
\qquad 0<g_1\le g_2\le\cdots\to\infty,
\]
where \(\ell_m\ge0\) is nondecreasing and independent of \(j\). There are \(a_{j+1}\ge2a_j\), \(a_1^{-1}<q_0\), such that
\[
f=\sum_{j\ge1}\chi(a_jq)f_j
\]
is smooth and locally finite. With \(f^{[J]}=\sum_{j=1}^Jf_j\), for \(J\ge\max(1,m)\) and \(q<(2a_J)^{-1}\),
\[
|f-f^{[J]}|_m\le2^{-J}q^{g_{J+1}/2-L_m},\qquad L_m=\ell_m+cm.
\]
Here \(\chi=1\) on \([0,1/2]\) and \(\chi=0\) on \([1,\infty)\). This is **[[asymptotics/diagonal-choice-of-shrinking-scales|shrinking-cutoff]] asymptotic summation**.

## Choice and tail proof

The cutoff derivative bound and Leibniz rule bound the \(j\)-th cutoff term through order \(m\) by \(\widehat C_{j,m}q^{g_j-L_m}(1+|\log q|)^{\widehat P_{j,m}}\). Choose \(a_j\) so that the coefficient times \(q^{g_j/2}\) is at most \(2^{-j}\) for \(m\le j\) throughout \(q\le a_j^{-1}\). This is a finite list of vanishing requirements.

On a compact subset, \(q\ge\delta>0\), so only finitely many cutoff terms survive. For \(q<(2a_J)^{-1}\), the first \(J\) cutoffs equal one. The remaining derivative bounds sum to at most \(q^{g_{J+1}/2-L_m}\sum_{j>J}2^{-j}\), proving the tail estimate.

## Retaining the original orders

To compare after a fixed truncation \(N\), choose a larger fixed \(J\) with \(g_{J+1}/2\ge g_{N+1}\). The finite block \(N+1,\ldots,J\) retains its original orders near zero; the tail has the desired order by the estimate. Logs can be retained or absorbed by a small power loss. This realizes an asymptotic expansion without asserting convergence of the uncut series.

## References

- [Melrose, Lectures on Pseudodifferential Operators, Lecture 2 and its addenda](https://math.mit.edu/~rbm/18.157-F05.pdf).
