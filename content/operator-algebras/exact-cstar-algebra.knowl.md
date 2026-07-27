+++
id = "operator-algebras/exact-cstar-algebra"
title = "Exact C*-algebra"
kind = "definition"
summary = "A C-star algebra whose minimal tensor product preserves every short exact sequence of C-star algebras."
aliases = ["exactness of a C*-algebra"]
domains = ["operator-algebras"]
section_mode = "progressive"
+++

A \(C^*\)-algebra \(A\) is **exact** if tensoring with \(A\) by the
[[operator-algebras/minimal-cstar-tensor-product|minimal \(C^*\)-tensor
product]] preserves every
[[operator-algebras/cstar-exact-sequence|short exact sequence]]: whenever
\[
0\longrightarrow I\longrightarrow B\longrightarrow B/I\longrightarrow 0
\]
is exact, so is
\[
0\longrightarrow I\otimes_{\min}A\longrightarrow
B\otimes_{\min}A\longrightarrow (B/I)\otimes_{\min}A
\longrightarrow 0.
\]
Thus the first map must remain injective and its image must be exactly the
kernel of the quotient map. The last map is always surjective; exactness is
the assertion that minimal tensoring introduces no additional kernel.

## Equivalent formulations

It is enough to test canonical ideal–quotient sequences. For every closed
[[algebra-rings/two-sided-ideal|two-sided ideal]] \(I\triangleleft B\), there is a canonical surjection
\[
(B\otimes_{\min}A)/(I\otimes_{\min}A)
\longrightarrow (B/I)\otimes_{\min}A.
\]
The algebra \(A\) is exact precisely when this map is injective, hence a
\(*\)-isomorphism, for every pair \((B,I)\). Exactness can equivalently be
placed in the first tensor factor because the minimal tensor product is
symmetric [Brown–Ozawa, §2.3](https://doi.org/10.1090/gsm/088).

## Permanence and examples

Exactness passes to \(C^*\)-subalgebras, quotients, and inductive limits,
although it is not a general three-space property for extensions. Every
[[operator-algebras/nuclear-cstar-algebra|nuclear \(C^*\)-algebra]] is exact,
but the converse fails. For example, the
[[operator-algebras/reduced-group-cstar-algebra|reduced group
\(C^*\)-algebra]] \(C_r^*(\mathbb F_2)\) of the
[[algebra-groups/free-group|free group]] on two generators is exact and
nonnuclear. This example separates exactness, which concerns the behavior of
the minimal tensor product on extensions, from nuclearity, which requires
agreement of the minimal and maximal tensor norms in every tensor product
[Brown–Ozawa, Chapter 2](https://doi.org/10.1090/gsm/088).

## Conventions and scope

**Warning.** Exactness is not the statement that the algebraic functor
\(-\otimes A\) is exact before completion; tensor products of complex vector
spaces already have that property. The issue is whether completion in the
minimal \(C^*\)-norm creates a larger kernel.

## References

1. Nathanial P. Brown and Narutaka Ozawa, *C*-Algebras and Finite-Dimensional Approximations*, American Mathematical Society, 2008. [AMS DOI record](https://doi.org/10.1090/gsm/088). Relevant: §2.3 on exact \(C^*\)-algebras and their permanence properties.
2. Eberhard Kirchberg, “The Fubini theorem for exact C*-algebras,” *Journal of Operator Theory* 10 (1983), 3–8. [Journal record](https://jot.theta.ro/jot/archive/1983-010-001/1983-010-001-001.html). Relevant: the tensor-product characterization of exactness.
