+++
id = "functional-analysis/resolvent-set-closed-operator"
title = "Resolvent set of a closed operator"
kind = "definition"
summary = "The scalars for which a closed operator has an everywhere-defined bounded inverse."
aliases = ["operator resolvent set", "regular set"]
domains = ["functional-analysis"]
section_mode = "progressive"
prerequisites = ["functional-analysis/closed-linear-operator", "linear-algebra/banach-space", "functional-analysis/bounded-linear-operator", "shared-foundations/bijective-function"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(T:\operatorname{Dom}(T)\subseteq X\to X\) be a
[[functional-analysis/closed-linear-operator|closed linear operator]] on a
complex [[linear-algebra/banach-space|Banach space]]. Its **resolvent set** is
\[
\rho(T)=\{\lambda\in\mathbb C:\lambda I-T\text{ is bijective and }
(\lambda I-T)^{-1}:X\to X\text{ is bounded}\}.
\]
For \(\lambda\in\rho(T)\), the
[[functional-analysis/bounded-linear-operator|bounded linear operator]]
\[
R(\lambda,T)=(\lambda I-T)^{-1}
\]
is the **resolvent operator**. Its range lies in \(\operatorname{Dom}(T)\),
although it is viewed as an operator on \(X\). Because \(T\) is closed,
bijectivity already forces this inverse to be bounded by the closed graph
theorem.

## Basic properties

The resolvent set is open in \(\mathbb C\), and
\(\lambda\mapsto R(\lambda,T)\) is operator-norm holomorphic there. If
\(\lambda,\mu\in\rho(T)\), then
\[
R(\lambda,T)-R(\mu,T)
  =(\mu-\lambda)R(\lambda,T)R(\mu,T).
\]
This [[functional-analysis/resolvent-identity|resolvent identity]] gives a local Neumann-series expansion and explains
both openness and holomorphy. The
[[functional-analysis/spectrum-closed-operator|spectrum of \(T\)]] is the complement
\(\mathbb C\setminus\rho(T)\); for an unbounded operator that complement need
not be bounded.

## Domain and sign conventions

Some authors define the resolvent as \((T-\lambda I)^{-1}\), which differs
from the convention above by a minus sign. Either convention gives the same
set \(\rho(T)\). Boundedness here is measured in the ambient norm of \(X\),
not only in the [[functional-analysis/graph-norm|graph norm]] on
\(\operatorname{Dom}(T)\). Closedness is what
turns an algebraic inverse defined on all of \(X\) into a bounded one.

## Example

For the multiplication operator \((Tf)(x)=x f(x)\) on \(L^2(\mathbb R)\),
with maximal domain \(\{f:xf\in L^2(\mathbb R)\}\), every
\(\lambda\notin\mathbb R\) lies in \(\rho(T)\). The resolvent multiplies by
\((\lambda-x)^{-1}\), whose [[measure-theory/essential-supremum|essential supremum]] is at most
\(|\operatorname{Im}\lambda|^{-1}\). No real \(\lambda\) is in the resolvent
set.

## References

1. Tosio Kato, *Perturbation Theory for Linear Operators*, 2nd ed., Springer, 1995. [Publisher record](https://doi.org/10.1007/978-3-642-66282-9). Relevant: Chapter III on closed operators, spectra, and resolvents.
2. Konrad Schmüdgen, *Unbounded Self-adjoint Operators on Hilbert Space*, Springer, 2012. [Publisher record](https://doi.org/10.1007/978-94-007-4753-1). Relevant: Chapter 1, §3 on the spectrum of a closed operator.
