+++
id = "ergodic-theory/gaussian-rotation-example"
title = "Ergodic Gaussian maps transported from rotations"
kind = "example"
summary = "Explicit nonlinear Gaussian-preserving maps obtained by adding an increment in normal-CDF coordinates."
aliases = []
domains = ["ergodic-theory"]
section_mode = "progressive"
prerequisites = ["ergodic-theory/gaussian-conjugate-dynamics", "ergodic-theory/torus-translation-ergodicity"]
+++

For \(\omega\in\mathbb R^d\), the almost-everywhere formula
\[
T_\omega(x)_j=\Phi^{-1}\bigl((\Phi(x_j)+\omega_j)\bmod1\bigr)
\]
defines an invertible Gaussian-preserving transformation modulo null sets. It is [[ergodic-theory/ergodic-transformation|ergodic]] exactly when \(k\cdot\omega\notin\mathbb Z\) for every nonzero \(k\in\mathbb Z^d\).

## Boundary convention

The inverse CDF is defined on \((0,1)\), so points whose rotated coordinates equal zero require care. Delete all torus points whose integer-time orbit meets a coordinate boundary. This is a countable union of null sets with invariant conull complement. Transport the rotation on that complement; the discarded Gaussian-null set may be fixed to obtain an everywhere-defined measurable bijection on the completed space.

## Fixed functions and phases

The transported Fourier functions
\[
h_k(x)=\exp\left(2\pi i\sum_j k_j\Phi(x_j)\right)
\]
form an orthonormal basis. Inverse pullback satisfies \(\alpha_\omega(h_k)=e^{-2\pi ik\cdot\omega}h_k\). Nonlinear \(T_\omega\) therefore still produces a complex-linear operator \(\alpha_\omega\) on functions.

For \(d=1\), an irrational increment gives an ergodic example. For increment \(1/2\), \(h_2\) is nonconstant and fixed. In dimension two, equal irrational increments fix \(h_{(1,-1)}\), while \((\sqrt2,\sqrt3)\) gives an ergodic system.

## Noninvertible Gaussian example

Replacing rotation by doubling gives \(x\mapsto\Phi^{-1}(2\Phi(x)\bmod1)\) almost everywhere. It is mixing and noninvertible, inherited from the doubling map. Forward composition supplies a state-preserving endomorphism rather than inverse pullback.
