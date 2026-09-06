+++
id = "noncommutative-geometry/compact-quantum-metric-space"
title = "Compact quantum metric space"
kind = "definition"
summary = "An order-unit space with a seminorm whose state-space metric induces the weak-star topology."
aliases = ["quantum compact metric space"]
domains = ["noncommutative-geometry", "operator-algebras"]
section_mode = "progressive"
prerequisites = ["operator-algebras/order-unit-space", "convex-analysis/seminorm", "functional-analysis/weak-star-topology", "operator-algebras/state-cstar-algebra"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(A\) be a real
[[operator-algebras/order-unit-space|order-unit space]] with order unit \(e\)
and state space \(S(A)\). A **compact quantum metric space** is a pair
\((A,L)\) in which \(L\) is a [[convex-analysis/seminorm|seminorm]] on a
dense order-unit subspace of \(A\), \(L(a)=0\) exactly for
\(a\in\mathbb Re\), and
\[
\rho_L(\varphi,\psi)=\sup\{|\varphi(a)-\psi(a)|:L(a)\leq1\}
\]
induces the [[functional-analysis/weak-star-topology|weak-star topology]] on \(S(A)\). The seminorm \(L\) is then called a Lip-norm. For a unital \(C^*\)-algebra \(B\), one takes \(A=B_{\mathrm{sa}}\); the elements of \(S(A)\) are the restrictions of [[operator-algebras/state-cstar-algebra|states on \(B\)]].

## Total-boundedness criterion

The weak-star metrizability condition is equivalent to total boundedness of the image of the \(L\)-unit ball in the quotient \(A/\mathbb Re\). Equivalently, after choosing a state \(\varphi_0\), the slice
\[
\{a\in A:L(a)\leq1,\ \varphi_0(a)=0\}
\]
is totally bounded in the order-unit norm. This criterion is often more practical than checking the topology directly.

## Spectral triples

A unital [[noncommutative-geometry/spectral-triple|spectral triple]] can supply \(L(a)=\lVert[D,a]\rVert\). Its associated [[noncommutative-geometry/connes-distance|Connes spectral distance]] has the same dual formula as \(\rho_L\). It defines a compact quantum metric space only when the zero-seminorm elements are precisely the scalars and the resulting metric induces the weak-star topology. [[functional-analysis/compact-resolvent|Compact resolvent]] of \(D\) alone does not imply either condition.

## Classical example and a near miss

For a compact [[topology/metric-space|metric space]] \(X\), take \(A=C(X,\mathbb R)\) and let \(L\) be the ordinary Lipschitz seminorm. The resulting metric on states is the Kantorovich metric on [[probability/probability-measure|probability measures]] and induces their weak-star topology. Thus compact metric spaces embed contravariantly into this framework.

If \(L\) vanishes on a nonconstant function, it is not a Lip-norm: states that distinguish that function are infinitely far apart after rescaling it. The failed axiom is the scalar-kernel condition.

## Conventions and scope

Rieffel's original definition is formulated for order-unit spaces, not only \(C^*\)-algebras. Later frameworks often impose lower semicontinuity, a Leibniz inequality, or matrix-level conditions; these are additional structures, not part of the definition in the core. The term “Lip-norm” names \(L\), whereas “compact quantum metric space” names the pair \((A,L)\).

## References

1. Marc A. Rieffel, “Metrics on State Spaces,” *Documenta Mathematica* 4 (1999), 559–600. [EMS DOI record](https://doi.org/10.4171/DM/68). Relevant: §§1–2 on metrics induced by Lipschitz seminorms.
2. Marc A. Rieffel, *Gromov–Hausdorff Distance for Quantum Metric Spaces*, Memoirs of the American Mathematical Society 168, no. 796 (2004), 1–65. [AMS DOI record](https://doi.org/10.1090/memo/0796). Relevant: §2 on compact quantum metric spaces and Lip-norm criteria.
