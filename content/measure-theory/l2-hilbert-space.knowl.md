+++
id = "measure-theory/l2-hilbert-space"
title = "Hilbert space of square-integrable observables"
kind = "definition"
summary = "Square-integrable functions modulo almost-everywhere equality, with the integral inner product."
aliases = ["L2 Hilbert space", "square-integrable observable space"]
domains = ["measure-theory"]
section_mode = "progressive"
prerequisites = ["measure-theory/lp-space", "linear-algebra/hilbert-space"]
+++

For a measure space \((X,\Sigma,\mu)\), the **complex Hilbert space \(L^2(X,\mu)\)** consists of measurable \(f:X\to\mathbb C\) with \(\int |f|^2\,d\mu<\infty\), identified modulo almost-everywhere equality, with
\[
\langle f,h\rangle=\int_X f\overline h\,d\mu,
\qquad \|f\|_2=\left(\int_X|f|^2\,d\mu\right)^{1/2}.
\]
The inner product here is linear in its first argument. Completeness is the \(p=2\) case of completeness of [[measure-theory/lp-space|\(L^p\) spaces]].

## Probability spaces

If \(\mu(X)=1\), then \(1\in L^2\), \(\|1\|_2=1\), and \(L^\infty\subseteq L^2\subseteq L^1\). The orthogonal complement of constants is the space of mean-zero observables.

## Finite example

On a uniform \(n\)-point space this is \(\mathbb C^n\) with \(\langle z,w\rangle=n^{-1}\sum_j z_j\overline{w_j}\). As a Hilbert space it has dimension \(n\); the separate function algebra on the same set uses coordinatewise multiplication.
