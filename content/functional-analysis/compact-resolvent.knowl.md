+++
id = "functional-analysis/compact-resolvent"
title = "Operator with compact resolvent"
kind = "definition"
summary = "A closed operator whose resolvent is compact at one, equivalently every, resolvent point."
aliases = ["compact-resolvent operator", "compact resolvent"]
domains = ["functional-analysis", "operator-theory", "spectral-theory"]
prerequisites = ["functional-analysis/closed-linear-operator", "linear-algebra/banach-space", "functional-analysis/resolvent-set-closed-operator", "linear-algebra/compact-operator", "functional-analysis/resolvent-identity"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(T:\mathcal D(T)\subseteq X\to X\) be a densely defined
[[functional-analysis/closed-linear-operator|closed operator]] on a
[[linear-algebra/banach-space|Banach space]], and suppose its
[[functional-analysis/resolvent-set-closed-operator|resolvent set]]
\(\rho(T)\) is nonempty. The operator \(T\) has **compact resolvent** if
\[
(T-\lambda I)^{-1}:X\longrightarrow X
\]
is a [[linear-algebra/compact-operator|compact operator]] for some
\(\lambda\in\rho(T)\). The [[functional-analysis/resolvent-identity|resolvent identity]] then implies compactness for
every \(\lambda\in\rho(T)\), so the definition does not depend on the chosen
resolvent point. Compact resolvent is stronger than closedness: it says that
solving \((T-\lambda I)x=y\) sends bounded sets of data to relatively compact
sets in \(X\).

## Compact domain embedding

Give \(\mathcal D(T)\) the [[functional-analysis/graph-norm|graph norm]]
\(\|x\|_T=\|x\|+\|Tx\|\). When \(\rho(T)\neq\varnothing\), \(T\) has compact
resolvent exactly when the inclusion
\[
(\mathcal D(T),\|\cdot\|_T)\hookrightarrow X
\]
is compact. This reformulation often proves compactness through an embedding
theorem rather than by constructing the resolvent explicitly.

## Spectral consequences

Every point of the
[[functional-analysis/spectrum-closed-operator|spectrum]] of a
compact-resolvent operator is an isolated eigenvalue of finite algebraic
multiplicity, and the spectrum has no finite accumulation point. The spectrum
may be empty for a general non-self-adjoint unbounded operator. If it is
infinite, its eigenvalues can accumulate only at infinity.

## Self-adjoint case and examples

For a
[[functional-analysis/self-adjoint-unbounded-operator|self-adjoint operator]]
\(D\) on a [[linear-algebra/hilbert-space|Hilbert space]], compact resolvent is equivalent to compactness of
\((1+D^2)^{-1/2}\). The spectral theorem then provides an [[linear-algebra/orthonormal-basis|orthonormal basis]] of
eigenvectors, with eigenvalues of finite multiplicity whose [[real-analysis/absolute-value|absolute values]]
tend to infinity. [[differential-geometry/elliptic-differential-operator|Elliptic differential operators]] on compact manifolds,
subject to suitable elliptic boundary conditions when a boundary is present,
are standard examples.

## References

- [Konrad Schmüdgen, *Unbounded Self-adjoint Operators on Hilbert Space*, Chapter 6 (Springer, 2012)](https://doi.org/10.1007/978-94-007-4753-1)
- [E. Brian Davies, *Linear Operators and their Spectra*, Chapter 4 (Cambridge University Press, 2007)](https://doi.org/10.1017/CBO9780511618864)
