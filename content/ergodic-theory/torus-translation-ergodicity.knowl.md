+++
id = "ergodic-theory/torus-translation-ergodicity"
title = "Ergodicity criterion for torus translations"
kind = "theorem"
summary = "A torus translation is ergodic exactly when one and its coordinate increments are rationally independent."
aliases = ["irrational rotation ergodicity", "Kronecker rotation criterion"]
domains = ["ergodic-theory"]
section_mode = "progressive"
prerequisites = ["ergodic-theory/compact-abelian-rotation", "topology/flat-torus", "harmonic-analysis/characters-compact-abelian-fourier-basis"]
+++

On \(\mathbb T^d=\mathbb R^d/\mathbb Z^d\), \(d\geq1\), with Haar probability, [[ergodic-theory/compact-abelian-rotation|translation]] \(T_\omega(x)=x+\omega\) is ergodic if and only if
\[
k\cdot\omega\notin\mathbb Z\qquad(0\ne k\in\mathbb Z^d).
\]
Equivalently, \(1,\omega_1,\ldots,\omega_d\) are linearly independent over \(\mathbb Q\).

## Fourier proof

For \(e_k(x)=e^{2\pi ik\cdot x}\),
\[
U_{T_\omega}e_k=e^{2\pi ik\cdot\omega}e_k,
\qquad \alpha_\omega(e_k)=e^{-2\pi ik\cdot\omega}e_k.
\]
The first is forward Koopman composition; the second is inverse pullback on \(L^\infty\). Their fixed Fourier modes agree. Completeness of the characters and the fixed-function criterion prove the result.

## Examples

For a circle, the increment must be irrational. In two dimensions, \((\sqrt2,\sqrt3)\) works, while \((\theta,\theta)\) fails even for irrational \(\theta\), because \(k=(1,-1)\) gives zero. Rational independence is a joint condition, not separate irrationality of coordinates.

Every torus translation has discrete spectrum and, for \(d\geq1\), nonconstant eigenfunctions. Thus none is weakly mixing.
