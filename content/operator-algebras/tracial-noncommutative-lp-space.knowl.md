+++
id = "operator-algebras/tracial-noncommutative-lp-space"
title = "Tracial noncommutative L^p space"
kind = "definition"
summary = "The space of trace-measurable operators whose p-th absolute powers have finite trace."
aliases = ["Lp(M,tau)", "semifinite noncommutative Lp space"]
domains = ["operator-algebras"]
section_mode = "progressive"
prerequisites = ["operator-algebras/faithful-normal-semifinite-trace", "operator-algebras/tau-measurable-operator", "linear-algebra/operator-norm"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(M\) have a
[[operator-algebras/faithful-normal-semifinite-trace|faithful normal semifinite trace]] \(\tau\), and let \(0<p<\infty\). The **tracial noncommutative
\(L^p\) space** is
\[
L^p(M,\tau)=
\left\{x\in S(M,\tau):\tau(|x|^p)<\infty\right\},
\]
where \(S(M,\tau)\) is the algebra of
[[operator-algebras/tau-measurable-operator|\(\tau\)-measurable operators]]
affiliated with \(M\). Its \(p\)-size is
\(\lVert x\rVert_p=\tau(|x|^p)^{1/p}\). For \(p\geq1\) this is a complete
norm; for \(0<p<1\) it is a complete quasinorm. By convention
\(L^\infty(M,\tau)=M\) with the [[linear-algebra/operator-norm|operator norm]].

## Products, duality, and interpolation

Noncommutative Hölder inequality gives
\[
\lVert xy\rVert_r\leq\lVert x\rVert_p\lVert y\rVert_q
\quad\text{when}\quad
\frac1r=\frac1p+\frac1q.
\]
For \(1\leq p<\infty\) and conjugate exponent \(q\), the pairing
\((x,y)\mapsto\tau(xy)\) identifies the Banach dual of \(L^p(M,\tau)\) with
\(L^q(M,\tau)\), with the usual endpoint interpretation. The spaces also form
the expected complex interpolation scale. These results extend classical
\(L^p\) inequalities to noncommuting products.

## Canonical examples

For \(M=L^\infty(X,\mu)\) and \(\tau(f)=\int_X f\,d\mu\), the construction is
the classical \(L^p(X,\mu)\). For \(M=B(H)\) with its usual trace, it is the
Schatten class: [[linear-algebra/compact-operator|compact operators]] whose singular values form an
\(\ell^p\)-sequence. In a
[[operator-algebras/finite-von-neumann-algebra|finite von Neumann algebra]]
with normalized trace, every bounded element belongs to every finite \(L^p\),
and completing the bounded finite-trace ideal in
\(\lVert\cdot\rVert_p\) gives the same space.

## Dependence and scope

**Warning.** The notation \(L^p(M,\tau)\) records the trace because the concrete
norm and realization depend on it. This semifinite construction should not be
identified by definition with the
[[operator-algebras/noncommutative-lp-space|Haagerup \(L^p(M)\) space]] of an
arbitrary [[operator-algebras/von-neumann-algebra|von Neumann algebra]]. When \(M\) is semifinite, however, the Haagerup
space is canonically isometric to the appropriate tracial construction. Also,
\(\lVert\cdot\rVert_p\) is not a norm when \(0<p<1\).

## References

1. Edward Nelson, “Notes on Non-Commutative Integration,” Journal of Functional Analysis 15 (1974), 103–116. [DOI record](https://doi.org/10.1016/0022-1236%2874%2990014-7). Relevant: pp. 107–116 on integration and \(L^p\)-type spaces for a semifinite trace.
2. Thierry Fack and Hideki Kosaki, “Generalized s-Numbers of \(\tau\)-Measurable Operators,” Pacific Journal of Mathematics 123 (1986), 269–300. [DOI record](https://doi.org/10.2140/pjm.1986.123.269). Relevant: §§3–4 on measure convergence, \(L^p\) norms, and Hölder-type inequalities.
