+++
id = "ergodic-theory/maximal-ergodic-theorem"
title = "Maximal ergodic theorem"
kind = "theorem"
summary = "A positive partial-sum event has nonnegative integral of the summand."
aliases = []
domains = ["ergodic-theory"]
section_mode = "progressive"
prerequisites = ["ergodic-theory/measure-preserving-system", "measure-theory/l1-function"]
+++

Let \(T\) [[ergodic-theory/measure-preserving-transformation|preserve a probability measure]] and let \(f\in L^1(X,\mu;\mathbb R)\). Set
\[
S_nf=\sum_{j=0}^{n-1}f\circ T^j,\qquad
E_N=\left\{x:\max_{1\leq n\leq N}S_nf(x)>0\right\}.
\]
The **maximal ergodic theorem** gives \(\int_{E_N} f\,d\mu\geq0\). The same conclusion holds for \(E=\{\sup_{n\geq1}S_nf>0\}\).

## Proof of the finite statement

Put \(M_N=\max(0,S_1f,\ldots,S_Nf)\). On \(E_N\), separating the first summand gives \(M_N\leq f+M_N\circ T\). Since \(M_N=0\) off \(E_N\) and \(M_N\geq0\), measure preservation gives
\[
\int_{E_N}f\,d\mu\geq\int M_N\,d\mu-\int_{E_N}M_N\circ T\,d\mu\geq0.
\]
The infinite statement follows from dominated convergence as \(E_N\) increases to \(E\).

## Maximal inequality

Apply the theorem to \(|h|-a\), for \(h\in L^1\) and \(a>0\). With the [[ergodic-theory/time-average|time averages]] \(A_n\), it gives
\[
\mu\{\sup_{n\geq1} A_n|h|>a\}\leq\frac{\|h\|_1}{a}.
\]
This controls the set of trajectories with a large averaging error. It is the key estimate for extending pointwise convergence from well-behaved observables to all of \(L^1\).

## References

1. Jesse Peterson, [*Lecture notes on ergodic theory*](https://www.math.vanderbilt.edu/~peters10/teaching/Spring2011/ErgodicTheoryNotes.pdf), 2011. §2.5, maximal ergodic inequality.
