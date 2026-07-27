+++
id = "operator-algebras/adjointable-operator-hilbert-module"
title = "Adjointable operator on a Hilbert C*-module"
kind = "definition"
summary = "A module map between Hilbert C*-modules that admits an adjoint with respect to their module-valued inner products."
aliases = ["adjointable module map", "L(E,F)"]
domains = ["operator-algebras", "functional-analysis"]
section_mode = "progressive"
+++

Let \(E\) and \(F\) be right
[[operator-algebras/hilbert-cstar-module|Hilbert \(C^*\)-modules]] over the
same \(C^*\)-algebra \(A\), with inner products linear in the second variable.
An \(A\)-linear map \(T:E\to F\) is **adjointable** if there is an \(A\)-linear
map \(T^*:F\to E\) such that
\[
\langle Tx,y\rangle_F=\langle x,T^*y\rangle_E
\]
for all \(x\in E\) and \(y\in F\). The adjoint, when it exists, is unique, and
\(T\) is automatically bounded. The space of such maps is denoted
\(\mathcal L_A(E,F)\); \(\mathcal L_A(E)=\mathcal L_A(E,E)\) is a unital
\(C^*\)-algebra.

## Comparison with Hilbert-space operators

For \(A=\mathbb C\), Hilbert \(A\)-modules are [[linear-algebra/hilbert-space|Hilbert spaces]] and every
[[functional-analysis/bounded-linear-operator|bounded operator on a Hilbert
space]] has an adjoint. For general coefficient algebras, a bounded
\(A\)-linear map need not be adjointable. Thus boundedness alone is not the
standard morphism condition for Hilbert \(C^*\)-modules. Adjointability is
equivalent to the graph of \(T\) being an orthogonally complemented submodule
of \(E\oplus F\) [Lance, Chapter 1](https://doi.org/10.1017/CBO9780511526206).

## Compact operators and composition

For \(y\in F\) and \(x\in E\), the rank-one operator
\(\theta_{y,x}:E\to F\) is defined by
\(\theta_{y,x}(z)=y\langle x,z\rangle_E\), and
\(\theta_{y,x}^*=\theta_{x,y}\). The closed linear span of these operators is
the algebra of compact module operators \(\mathcal K_A(E,F)\). These need not
be compact as Banach-space operators. Adjointable maps compose, satisfy
\((ST)^*=T^*S^*\), and act as multipliers of the compact operators.

## Conventions and scope

If module inner products are taken linear in the first variable, the displayed
adjoint identity is rewritten accordingly. The notation \(\mathcal L(E,F)\)
usually means adjointable maps in Hilbert-module theory but often means all
bounded maps in Banach-space theory, so the ambient category matters. Modules
over different coefficient algebras require additional correspondence data;
the definition above assumes the same right coefficient algebra.

## References

1. E. Christopher Lance, *Hilbert C*-Modules: A Toolkit for Operator Algebraists*, Cambridge University Press, 1995. [DOI record](https://doi.org/10.1017/CBO9780511526206). Relevant: Chapter 1 on adjointable and compact module operators.
