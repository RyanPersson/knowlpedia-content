+++
id = "operator-algebras/group-measure-space-construction"
title = "Group–measure-space construction"
kind = "construction"
summary = "The regular von Neumann crossed product of a probability space by a countable group action."
aliases = ["group-measure-space algebra"]
domains = ["operator-algebras"]
section_mode = "progressive"
prerequisites = ["ergodic-theory/measure-preserving-action", "operator-algebras/von-neumann-crossed-product", "operator-algebras/commutative-von-neumann-algebra"]
+++

For a [[ergodic-theory/measure-preserving-action|measure-preserving action]] of a countable discrete group \(G\) on \((X,\mu)\), put \(A=L^\infty(X,\mu)\) and \(\alpha_g(f)=f\circ T_{g^{-1}}\). The **group–measure-space algebra** is the von Neumann crossed product \(A\rtimes_\alpha G\). Concretely, on \(H=\ell^2(G,L^2(X,\mu))\), set
\[
(\pi(f)\xi)_h=\alpha_{h^{-1}}(f)\xi_h,
\qquad (u_g\xi)_h=\xi_{g^{-1}h}.
\]
Then \(A\rtimes G=(\pi(A)\cup\{u_g:g\in G\})''\).

## Covariance and trace

The generators satisfy \(u_g\pi(f)u_g^*=\pi(\alpha_g(f))\). Finite sums \(\sum_g f_gu_g\) form an ultraweakly dense algebraic core. The formula
\[
\tau\left(\sum_g f_gu_g\right)=\int_X f_e\,d\mu
\]
extends to a faithful normal tracial state.

## Why the regular representation matters

The extra \(\ell^2(G)\) coordinate retains group coefficients. Using only multiplication and Koopman operators on \(L^2(X)\) need not recover this algebra. On a one-point space with trivial \(\mathbb Z\)-action, those operators generate \(\mathbb C\), while the crossed product is \(L(\mathbb Z)\cong L^\infty(\mathbb S^1)\).

## References

1. Sorin Popa, [*Ergodic theory of group actions*](https://www.math.ucla.edu/~popa/Books/OElectures.pdf). §4.1.
