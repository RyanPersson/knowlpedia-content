+++
id = "functional-analysis/core-of-closed-operator"
title = "Core of a closed operator"
kind = "definition"
summary = "A subdomain whose graph closure recovers the entire closed operator."
aliases = ["operator core", "essential domain"]
domains = ["functional-analysis"]
section_mode = "progressive"
+++

Let \(T:\operatorname{Dom}(T)\subseteq X\to X\) be a
[[functional-analysis/closed-linear-operator|closed linear operator]] on a
[[linear-algebra/banach-space|Banach space]]. A [[convex-analysis/linear-subspace|linear subspace]] \(D\subseteq\operatorname{Dom}(T)\) is a
**core for \(T\)** if the closure of the restricted operator \(T|_D\) is
\(T\). Equivalently, \(D\) is dense in \(\operatorname{Dom}(T)\) for the
[[functional-analysis/graph-norm|graph norm]]
\[
\|x\|_T=\|x\|+\|Tx\|.
\]
Thus every \(x\in\operatorname{Dom}(T)\) admits \(x_n\in D\) with both
\(x_n\to x\) and \(Tx_n\to Tx\) in \(X\). Density of \(D\) in \(X\) alone is
not enough.

## Graph interpretation

The graph of \(T|_D\) is
\[
\{(x,Tx):x\in D\}\subseteq X\times X.
\]
The core condition says that its closure is exactly the graph of \(T\).
Consequently, values of \(T\) on the smaller test domain determine the closed
operator uniquely. This is why differential operators are often first
computed on smooth compactly supported functions and then recovered by graph
closure.

## How cores are used

Suppose \(S\) is a [[functional-analysis/closable-operator|closable operator]] with
\(\operatorname{Dom}(S)=D\subseteq\operatorname{Dom}(T)\) and \(Sx=Tx\) on
\(D\). Then \(D\) is a core for \(T\) exactly when \(\overline S=T\). In
particular, proving that a proposed test domain is a core justifies checking
identities and approximation arguments there before passing to the full
domain.

## Warning: ambient density versus graph density

For an unbounded operator, convergence \(x_n\to x\) does not control
\(Tx_n\). A dense invariant subspace can therefore fail to be a core.
Likewise, “essential domain” is sometimes used as a synonym for a core, but
in discussions of [[functional-analysis/symmetric-operator|symmetric
operators]] the nearby phrase “essentially
self-adjoint” adds a separate assertion about the closure being
self-adjoint.

## References

1. Tosio Kato, *Perturbation Theory for Linear Operators*, 2nd ed., Springer, 1995. [Publisher record](https://doi.org/10.1007/978-3-642-66282-9). Relevant: Chapter III on closability, graph norms, and cores.
2. Konrad Schmüdgen, *Unbounded Self-adjoint Operators on Hilbert Space*, Springer, 2012. [Publisher record](https://doi.org/10.1007/978-94-007-4753-1). Relevant: Chapter 1 on closed operators and core domains.
