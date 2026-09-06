+++
id = "functional-analysis/resolvent-identity"
title = "Resolvent identity"
kind = "definition"
summary = "An algebraic identity relating resolvent operators at different parameters or for different operators."
aliases = ["first resolvent identity", "second resolvent identity"]
domains = ["functional-analysis"]
section_mode = "progressive"
prerequisites = ["functional-analysis/closed-linear-operator", "linear-algebra/banach-space", "functional-analysis/resolvent-set-closed-operator", "functional-analysis/bounded-linear-operator"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(T\) be a [[functional-analysis/closed-linear-operator|closed linear
operator]] on a complex [[linear-algebra/banach-space|Banach space]], and write
\(R_T(\lambda)=(\lambda I-T)^{-1}\) for \(\lambda\) in its
[[functional-analysis/resolvent-set-closed-operator|resolvent set]]. The
**resolvent identity** for two parameters \(\lambda,\mu\in\rho(T)\) is
\[
R_T(\lambda)-R_T(\mu)
=(\mu-\lambda)R_T(\lambda)R_T(\mu).
\]
It follows by inserting the factors \(\lambda I-T\) and \(\mu I-T\) and is
an identity of [[functional-analysis/bounded-linear-operator|bounded
operators]] on the ambient space. In particular, the two resolvents commute.
The name also covers the closely related identity comparing the resolvents of
two different operators.

## Analytic consequences

Taking \(\mu\) close to \(\lambda\) rewrites the identity as
\[
R_T(\mu)
=R_T(\lambda)\bigl(I-(\mu-\lambda)R_T(\lambda)\bigr)^{-1}.
\]
The Neumann series for the inverse proves locally that the resolvent set is
open and that \(\lambda\mapsto R_T(\lambda)\) is holomorphic in
[[linear-algebra/operator-norm|operator norm]].
Differentiating with this sign convention gives
\[
\frac{d}{d\lambda}R_T(\lambda)=-R_T(\lambda)^2.
\]
These conclusions and their higher-derivative versions are standard tools in
spectral perturbation theory.

## Comparison of two operators

Suppose \(A\) and \(B\) are [[functional-analysis/closed-linear-operator|closed operators]] and \(A-B\) acts on the range
needed below, as happens when they have a common domain and \(A-B\) extends to
a bounded operator. At a common resolvent point \(\lambda\),
\[
R_A(\lambda)-R_B(\lambda)
=R_A(\lambda)(A-B)R_B(\lambda).
\]
This second resolvent identity converts control of the perturbation \(A-B\)
into control of the resolvents. Domain compatibility is essential for
unbounded operators; the displayed product is not meaningful merely because
\(\lambda\) belongs to both resolvent sets.

## Sign conventions

Some authors define the resolvent by \((T-\lambda I)^{-1}\) rather than
\((\lambda I-T)^{-1}\). The corresponding formulas have different displayed
signs but identical mathematical content. “First” commonly refers to the
two-parameter identity for one operator, while “second” refers to the
comparison identity, although this terminology is not completely uniform.

## References

1. Tosio Kato, *Perturbation Theory for Linear Operators*, 2nd ed., Springer, 1995. [DOI record](https://doi.org/10.1007/978-3-642-66282-9). Relevant: Chapter III, especially §6 on resolvents and spectra.
2. Michael Reed and Barry Simon, *Methods of Modern Mathematical Physics I: Functional Analysis*, Academic Press, 1972. [Publisher record](https://doi.org/10.1016/B978-0-12-585001-8.X5001-6). Relevant: Chapter VII on operator spectra and resolvents.
