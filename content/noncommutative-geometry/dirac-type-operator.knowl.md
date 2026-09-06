+++
id = "noncommutative-geometry/dirac-type-operator"
title = "Dirac-type operator"
kind = "definition"
summary = "A first-order differential operator whose principal symbol is Clifford multiplication."
aliases = ["generalized Dirac operator", "Clifford-symbol operator"]
domains = ["noncommutative-geometry", "differential-geometry"]
section_mode = "progressive"
prerequisites = ["differential-geometry/riemannian-manifold", "differential-geometry/clifford-module", "differential-geometry/principal-symbol", "differential-geometry/elliptic-differential-operator"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(M\) be a [[differential-geometry/riemannian-manifold|Riemannian manifold]] and \(E\to M\) a Hermitian [[differential-geometry/clifford-module|Clifford module]] with Clifford multiplication \(c:T^*M\to\operatorname{End}(E)\). A **Dirac-type operator** on \(E\) is a first-order differential operator
\[
D:\Gamma^\infty(E)\longrightarrow\Gamma^\infty(E)
\]
whose [[differential-geometry/principal-symbol|principal symbol]] satisfies
\[
\sigma_1(D)(x,\xi)=c_x(\xi).
\]
Here the symbol convention has no factor of \(i\), so \(c_x(\xi)^2=-|\xi|^2\operatorname{id}_{E_x}\). Therefore the symbol is invertible for \(\xi\neq0\), and every Dirac-type operator is an [[differential-geometry/elliptic-differential-operator|elliptic differential operator]]. Formal self-adjointness is included only when explicitly stated.

## Construction from a Clifford connection

If \(\nabla^E\) is a metric Clifford connection, then
\[
D_{\nabla^E}=c\circ\nabla^E=\sum_j c(e^j)\nabla^E_{e_j}
\]
is Dirac type. Adding any smooth bundle endomorphism preserves its principal symbol, so every \(D_{\nabla^E}+\Phi\) is also Dirac type. Conversely, a Dirac-type operator determines a compatible connection plus a zero-order endomorphism after the metric data are fixed.

## Examples and consequences

The [[noncommutative-geometry/dirac-operator|spin Dirac operator]], the Hodge–de Rham operator \(d+d^*\), and the signature operator are standard examples. Squaring a Dirac-type operator produces a second-order operator of Laplace type; for a Clifford connection, the Weitzenböck formula separates this square into a connection Laplacian and a curvature endomorphism.

## Conventions and scope

**Warning.** Authors vary between “Dirac type,” “generalized Dirac,” and “Dirac operator.” Some require formal self-adjointness, grading oddness, or construction from a Clifford connection. None of those extra conditions follows merely from the symbol identity used here. The spin Dirac operator is a distinguished example, not a synonym for the whole class.

## References

1. N. Berline, E. Getzler, and M. Vergne, *Heat Kernels and Dirac Operators*, Springer, 1992. [Publisher record](https://doi.org/10.1007/978-3-642-58088-8). Relevant: chapter 3, Clifford modules and generalized Dirac operators.
2. H. B. Lawson Jr. and M.-L. Michelsohn, *Spin Geometry*, Princeton University Press, 1989. [Publisher record](https://doi.org/10.1515/9781400883912). Relevant: chapters II–III, Dirac operators and their symbols.
