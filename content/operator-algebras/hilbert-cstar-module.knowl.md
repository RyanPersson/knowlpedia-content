+++
id = "operator-algebras/hilbert-cstar-module"
title = "Hilbert C*-module"
kind = "definition"
summary = "A module over a C-star algebra that is complete for the norm induced by an algebra-valued inner product."
aliases = ["Hilbert module", "right Hilbert A-module"]
domains = ["operator-algebras"]
section_mode = "progressive"
+++

Let \(A\) be a [[operator-algebras/cstar-algebra|\(C^*\)-algebra]]. A **right
Hilbert \(A\)-module** is a right [[algebra-modules/module|\(A\)-module]] \(E\)
with a map \(\langle\cdot,\cdot\rangle_A:E\times E\to A\), complex-linear in
the second variable, such that, for \(x,y,z\in E\) and \(a\in A\),
\[
\langle x,y+z\rangle_A=\langle x,y\rangle_A+\langle x,z\rangle_A,\qquad
\langle x,ya\rangle_A=\langle x,y\rangle_Aa,\qquad
\langle x,y\rangle_A=\langle y,x\rangle_A^*,
\]
\(\langle x,x\rangle_A\) is positive, and \(\langle x,x\rangle_A=0\) only when
\(x=0\). Finally, \(E\) is complete for
\(\|x\|=\|\langle x,x\rangle_A\|^{1/2}\). Thus the inner product is linear in
the second variable under this convention.

## Standard examples

The algebra \(A\) is a Hilbert \(A\)-module over itself with
\(\langle a,b\rangle_A=a^*b\). The column module \(A^n\) has
\[
\langle(a_i),(b_i)\rangle_A=\sum_{i=1}^{n}a_i^*b_i.
\]
A [[linear-algebra/hilbert-space|Hilbert space]] is exactly a Hilbert module
over \(\mathbb C\). Unlike a Hilbert space, a Hilbert \(A\)-module need not have
an [[linear-algebra/orthonormal-basis|orthonormal basis]], and a closed submodule need not possess an orthogonal
complement.

## Adjointable and compact operators

An \(A\)-linear map \(T:E\to F\) is **adjointable** if there is an
\(A\)-linear map \(T^*:F\to E\) satisfying
\(\langle Tx,y\rangle_A=\langle x,T^*y\rangle_A\). Adjointable maps are
automatically bounded, but bounded \(A\)-linear maps need not be adjointable.
The [[linear-algebra/compact-operator|compact operators]] on \(E\) are the norm closure of the span of
\(\theta_{x,y}(z)=x\langle y,z\rangle_A\); “compact” here is a module-theoretic
notion and need not mean compact as a Banach-space operator
[Lance, Chapter 1](https://doi.org/10.1017/CBO9780511526206).

## Conventions and scope

Some authors use left modules and inner products linear in the first variable;
all displayed formulas must then be reversed consistently. Fullness, meaning
that the closed span of \(\langle E,E\rangle_A\) equals \(A\), is an additional
condition rather than part of the definition. Self-dual modules over a von
Neumann algebra form a more restrictive \(W^*\)-module theory and should not
be assumed for a general Hilbert \(C^*\)-module.

## References

1. E. C. Lance, Hilbert \(C^*\)-Modules: A Toolkit for Operator Algebraists, Cambridge University Press, 1995. [Publisher record](https://doi.org/10.1017/CBO9780511526206). Relevant: Chapter 1 on Hilbert modules, adjointable maps, and compact module operators.
