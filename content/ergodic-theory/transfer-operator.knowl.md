+++
id = "ergodic-theory/transfer-operator"
title = "Transfer operator of a probability-preserving map"
kind = "definition"
summary = "The adjoint of forward composition on L2, describing backward averaging and transport of densities."
aliases = ["Perron–Frobenius operator", "Perron-Frobenius operator"]
domains = ["ergodic-theory"]
section_mode = "progressive"
prerequisites = ["ergodic-theory/koopman-operator", "functional-analysis/adjoint-bounded-operator"]
+++

The **transfer operator** \(P_T\) of a probability-preserving transformation is the [[functional-analysis/adjoint-bounded-operator|Hilbert-space adjoint]] \(P_T=U_T^*\) on \(L^2\). With inner products linear in the first argument, it is characterized by
\[
\int (P_T f)\overline h\,d\mu
=\int f\,\overline{h\circ T}\,d\mu.
\]
It is a positive contraction and \(P_T1=1\). If \(T\) is invertible, \(P_Tf=f\circ T^{-1}\).

## Doubling-map example

For \(T(x)=2x\bmod1\),
\[
P_T f(x)=\tfrac12\bigl(f(x/2)+f((x+1)/2)\bigr).
\]
The operator averages over the two preimages. It is not composition with a nonexistent inverse map. The same duality extends to a positive \(L^1\) operator transporting densities relative to the invariant probability measure.
