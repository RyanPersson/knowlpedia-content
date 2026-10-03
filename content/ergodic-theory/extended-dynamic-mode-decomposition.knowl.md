+++
id = "ergodic-theory/extended-dynamic-mode-decomposition"
title = "Extended dynamic mode decomposition"
kind = "construction"
summary = "A least-squares approximation of Koopman evolution in a chosen finite dictionary of observables."
aliases = ["EDMD", "finite-dictionary Koopman approximation"]
domains = ["ergodic-theory"]
section_mode = "progressive"
prerequisites = ["ergodic-theory/koopman-operator", "linear-algebra/orthogonal-projection", "ergodic-theory/birkhoff-ergodic-theorem"]
+++

Choose [[ergodic-theory/observable|observables]] \(\psi_1,\ldots,\psi_r\) and sample pairs \(y_m=T(x_m)\). **Extended dynamic mode decomposition (EDMD)** approximates each \(U_T\psi_j\) by \(\sum_iK_{ij}\psi_i\) through empirical least squares. Define
\[
(G_M)_{ij}=\frac1M\sum_m\overline{\psi_i(x_m)}\psi_j(x_m),\qquad
(C_M)_{ij}=\frac1M\sum_m\overline{\psi_i(x_m)}\psi_j(y_m).
\]
If \(G_M\) is invertible, the coefficient matrix is \(K_M=G_M^{-1}C_M\). A singular Gram matrix requires a specified least-squares solution or regularization.

## Population operator

For linearly independent \(L^2(\mu)\) observables, replace the empirical sums by integrals. The resulting matrix represents \(P_VU_T|_V\), with \(V=\operatorname{span}\{\psi_j\}\) and \(P_V\) the orthogonal projection. It is exact on \(V\) when \(U_TV\subseteq V\).

## Ergodic sampling

If \(T\) preserves an ergodic probability and \(x_m=T^mx_0\), Birkhoff's theorem makes these finitely many Gram and cross-moment entries converge for almost every \(x_0\). Their integrability follows from Cauchy–Schwarz. If the population Gram matrix is invertible, the empirical matrices are eventually invertible and \(K_M\) converges to the fixed-dictionary population matrix.

This is not a general theorem of convergence of all fitted eigenvalues to the spectrum of the infinite-dimensional [[ergodic-theory/koopman-operator|Koopman operator]] as the dictionary grows.

## References

1. M. O. Williams, I. G. Kevrekidis, and C. W. Rowley, [“A Data-Driven Approximation of the Koopman Operator: Extending Dynamic Mode Decomposition”](https://arxiv.org/pdf/1408.4408), §§2–3; the trajectory-sampling statement follows here by Birkhoff.
