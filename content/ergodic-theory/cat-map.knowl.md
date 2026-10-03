+++
id = "ergodic-theory/cat-map"
title = "Arnold cat map"
kind = "example"
summary = "A mixing toral automorphism whose Koopman operator moves Fourier characters through unbounded frequencies."
aliases = ["Arnold’s cat map", "hyperbolic toral automorphism example"]
domains = ["ergodic-theory"]
section_mode = "progressive"
prerequisites = ["topology/flat-torus", "ergodic-theory/koopman-operator", "harmonic-analysis/characters-compact-abelian-fourier-basis", "ergodic-theory/strong-mixing"]
+++

The **cat map** is the automorphism of [[topology/flat-torus|\(\mathbb T^2\)]] given by
\[
T_A(x)=Ax\bmod\mathbb Z^2,\qquad
A=\begin{pmatrix}2&1\\1&1\end{pmatrix}.
\]
Its determinant is one and its inverse has integer entries, so it is an invertible group automorphism preserving Haar probability. It is [[ergodic-theory/strong-mixing|strongly mixing]].

## Fourier mechanism

For \(e_k(x)=e^{2\pi ik\cdot x}\),
\[
U_{T_A}e_k=e_{A^{\mathsf T}k},\qquad
\langle U_{T_A}^ne_k,e_\ell\rangle=1_{\{(A^{\mathsf T})^nk=\ell\}}.
\]
The eigenvalues of \(A\) are \((3\pm\sqrt5)/2\). Neither eigenline contains a nonzero integer vector. Every nonzero integer \(k\) therefore has a nonzero expanding component and \(\|(A^{\mathsf T})^nk\|\to\infty\).

Each displayed correlation is eventually zero for fixed nonzero frequencies. Density of trigonometric polynomials proves mixing for all mean-zero \(L^2\) observables. These Fourier characters form a useful basis, but they are not Koopman eigenfunctions: the operator permutes their frequencies.
