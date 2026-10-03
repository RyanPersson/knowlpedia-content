+++
id = "operator-algebras/tracial-mean-ergodic-theorem"
title = "Mean ergodic theorem for a finite tracial system"
kind = "theorem"
summary = "Noncommutative time averages converge in trace L2 to the conditional expectation onto the fixed algebra."
aliases = []
domains = ["operator-algebras"]
section_mode = "progressive"
prerequisites = ["operator-algebras/finite-von-neumann-algebra", "operator-algebras/tracial-noncommutative-lp-space", "operator-algebras/fixed-point-algebra", "operator-algebras/normal-conditional-expectation", "ergodic-theory/von-neumann-mean-ergodic-theorem"]
+++

Let \(M\) be a [[operator-algebras/von-neumann-algebra|von Neumann algebra]] with faithful normal tracial state \(\tau\), and let \(\alpha\) be a normal \(\tau\)-preserving automorphism. Write \(E:M\to M^\alpha\) for the \(\tau\)-preserving [[operator-algebras/normal-conditional-expectation|normal conditional expectation]]. Then
\[
\left\|\frac1N\sum_{n=0}^{N-1}\alpha^n(a)-E(a)\right\|_{2,\tau}\longrightarrow0
\qquad(a\in M),
\quad\|a\|_{2,\tau}=\tau(a^*a)^{1/2}.
\]
If \(M^\alpha=\mathbb C1\), the limit is \(\tau(a)1\).

## Hilbert-space mechanism

The GNS implementation is unitary on \(L^2(M,\tau)\). Its fixed subspace is \(L^2(M^\alpha,\tau)\), and the extension of \(E\) is the orthogonal projection onto that subspace. The Hilbert-space mean ergodic theorem therefore gives the conclusion.

## Mode of convergence

This statement is convergence in the trace \(L^2\) norm. There is no underlying point \(x\) at which to evaluate a general noncommutative observable. Noncommutative pointwise theorems require separately defined replacements for almost-everywhere convergence.
