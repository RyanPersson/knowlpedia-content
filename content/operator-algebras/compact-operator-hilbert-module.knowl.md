+++
id = "operator-algebras/compact-operator-hilbert-module"
title = "Compact operator on a Hilbert C*-module"
kind = "definition"
summary = "An operator in the norm-closed span of rank-one operators between Hilbert C*-modules."
aliases = ["generalized compact operator", "K(E,F)", "rank-one Hilbert-module operator"]
domains = ["operator-algebras", "functional-analysis"]
section_mode = "progressive"
+++

Let \(E\) and \(F\) be right Hilbert \(A\)-modules. For \(x\in E\) and
\(y\in F\), the rank-one operator \(\theta_{y,x}:E\to F\) is
\[
\theta_{y,x}(z)=y\langle x,z\rangle_A.
\]
The space of **compact operators from \(E\) to \(F\)** is
\[
\mathcal K_A(E,F)=
\overline{\operatorname{span}}\{\theta_{y,x}:x\in E,\ y\in F\},
\]
where the closure is in the
[[linear-algebra/operator-norm|operator norm]] inside
[[operator-algebras/adjointable-operator-hilbert-module|the adjointable operators]]
\(\mathcal L_A(E,F)\). The word “compact” names this norm-closed
rank-one span; it does not assert that the operator maps bounded sets to
[[topology/relatively-compact-set|relatively compact sets]].
This construction depends only on the Hilbert-module structures and the given
coefficient algebra.

## Adjoint and composition

Each rank-one operator is adjointable, with
\(\theta_{y,x}^*=\theta_{x,y}\). If \(S\in\mathcal L_A(F,G)\),
\(T\in\mathcal L_A(D,E)\), and \(k\in\mathcal K_A(E,F)\), then
\(Sk\in\mathcal K_A(E,G)\) and \(kT\in\mathcal K_A(D,F)\). These formulas
explain why generalized compact operators are stable under composition with
adjointable maps.

## The algebra \(\mathcal K_A(E)\)

When \(E=F\), one writes \(\mathcal K_A(E)\). It is a \(C^*\)-algebra and a
closed two-sided ideal of \(\mathcal L_A(E)\). For distinct modules,
\(\mathcal K_A(E,F)\) is generally only a closed linear space of operators,
not an algebra. It appears as an off-diagonal corner in the compact operators
on \(E\oplus F\).

## Relation to Hilbert-space compactness

For \(A=\mathbb C\), Hilbert \(A\)-modules are
[[linear-algebra/hilbert-space|Hilbert spaces]] and this definition recovers
the usual compact operators. Over a general
\(C^*\)-algebra, a rank-one operator may have infinite-dimensional range as a
complex vector space. Finite-rank approximation therefore refers to module
rank-one operators, not to finite-dimensional linear ranges.

## References

1. E. Christopher Lance, *Hilbert C*-Modules: A Toolkit for Operator Algebraists*, Cambridge University Press, 1995. [Publisher record](https://doi.org/10.1017/CBO9780511526206). Relevant: Chapter 1 on adjointable and compact module operators.
2. Iain Raeburn and Dana P. Williams, *Morita Equivalence and Continuous-Trace C*-Algebras*, American Mathematical Society, 1998. [Publisher record](https://doi.org/10.1090/surv/060). Relevant: Chapter 2 on Hilbert modules and compact operators.
