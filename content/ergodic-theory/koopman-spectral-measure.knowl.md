+++
id = "ergodic-theory/koopman-spectral-measure"
title = "Spectral measure of an observable"
kind = "definition"
summary = "The positive measure whose Fourier coefficients are the autocorrelations of an observable."
aliases = ["scalar Koopman spectral measure"]
domains = ["ergodic-theory"]
section_mode = "progressive"
prerequisites = ["ergodic-theory/koopman-operator", "functional-analysis/spectral-theorem-unitary-operator", "ergodic-theory/correlation-function"]
+++

Let \(T\) be invertible and probability preserving, and let \(E\) be the spectral resolution of the forward [[ergodic-theory/koopman-operator|Koopman operator]] \(U_T\). The **spectral measure of \(f\in L^2\)** is the finite positive Borel measure
\[
\sigma_f(B)=\langle E(B)f,f\rangle=\|E(B)f\|_2^2
\qquad(B\subseteq\mathbb S^1\text{ Borel}).
\]
Its total mass is \(\|f\|_2^2\), and its Fourier coefficients are
\[
\int_{\mathbb S^1}z^n\,d\sigma_f(z)=\langle U_T^nf,f\rangle.
\]

## Atoms and fixed vectors

An atom at \(\lambda\) records a nonzero component of \(f\) in the \(\lambda\)-eigenspace. In particular, mass at \(1\) is the squared norm of its invariant component. A unit-norm eigenfunction has spectral measure \(\delta_\lambda\).

## Mixing

Weak mixing makes \(\sigma_f\) atomless for every mean-zero \(f\). Strong mixing requires its nonzero-time Fourier coefficients to tend to zero, which is a stronger condition than atomlessness.
