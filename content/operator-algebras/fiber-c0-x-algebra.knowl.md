+++
id = "operator-algebras/fiber-c0-x-algebra"
title = "Fiber of a C_0(X)-algebra"
kind = "definition"
summary = "The quotient of a C_0(X)-algebra by the ideal of elements vanishing at a point."
aliases = ["fiber algebra A_x", "C*-fiber"]
domains = ["operator-algebras", "topology"]
prerequisites = ["operator-algebras/c0-x-algebra", "operator-algebras/quotient-cstar-algebra"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(A\) be a [[operator-algebras/c0-x-algebra|\(C_0(X)\)-algebra]] with structure map \(\Phi\), and let \(x\in X\). Put
\[
I_x=\overline{\Phi(\{f\in C_0(X):f(x)=0\})A}.
\]
The **fiber of \(A\) at \(x\)** is the [[operator-algebras/quotient-cstar-algebra|quotient \(C^*\)-algebra]]
\[
A_x=A/I_x.
\]
For \(a\in A\), its image in \(A_x\) is denoted \(a(x)\). This is an algebraic fiber attached to the \(C_0(X)\)-structure, not merely a set-theoretic preimage of a map.
Equivalently, one quotients out the part of \(A\) localized away from \(x\).

## Pointwise norm

The quotient norm gives
\[
\lVert a(x)\rVert=\inf_{b\in I_x}\lVert a+b\rVert.
\]
For fixed \(a\in A\), the function \(x\mapsto\lVert a(x)\rVert\) is upper semicontinuous and vanishes at infinity. It need not be continuous; continuity for every \(a\) is an additional condition on the \(C_0(X)\)-algebra.

## Exact sequence

Evaluation at \(x\) is the quotient map \(q_x\colon A\to A_x\), and it fits into the [[operator-algebras/cstar-exact-sequence|short exact sequence]]
\[
0\longrightarrow I_x\longrightarrow A
\xrightarrow{q_x}A_x\longrightarrow0.
\]
The fiber may be zero. Two distinct points may also produce isomorphic fibers, because the construction records position over \(X\) as well as the fiber’s abstract isomorphism class.

## Bundle interpretation

The disjoint union
\[
\mathcal A=\bigsqcup_{x\in X}A_x
\]
has a canonical topology making it an [[operator-algebras/upper-semicontinuous-cstar-bundle|upper-semicontinuous \(C^*\)-bundle]]. Each \(a\in A\) then gives the continuous section \(x\mapsto a(x)\), and these sections determine the topology. The resulting section algebra recovers \(A\).

## References

1. May Nilsen, “C*-Bundles and \(C_0(X)\)-Algebras,” *Indiana University Mathematics Journal* 45 (1996), 463–477. [DOI record](https://doi.org/10.1512/iumj.1996.45.1086). Relevant: fibers and the bundle associated to a \(C_0(X)\)-algebra.
2. Dana P. Williams, *Crossed Products of C*-Algebras*, Mathematical Surveys and Monographs 134, American Mathematical Society, 2007. [DOI record](https://doi.org/10.1090/surv/134). Relevant: Appendix C, especially fiber ideals and sectional representation.
