+++
id = "operator-algebras/strictly-positive-element"
title = "Strictly positive element of a C*-algebra"
kind = "definition"
summary = "A strictly positive element is a positive element whose generated hereditary subalgebra is the whole C*-algebra."
aliases = ["strictly positive C*-element"]
domains = ["operator-algebras"]
section_mode = "progressive"
prerequisites = ["operator-algebras/cstar-algebra", "operator-algebras/positive-element", "operator-algebras/hereditary-cstar-subalgebra", "operator-algebras/positive-linear-functional"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(A\) be a [[operator-algebras/cstar-algebra|\(C^*\)-algebra]]. A
[[operator-algebras/positive-element|positive element]] \(h\in A_+\) is
**strictly positive** if the
[[operator-algebras/hereditary-cstar-subalgebra|hereditary \(C^*\)-subalgebra]] it generates is all of \(A\):
\[
\overline{hAh}=A.
\]
Equivalently, every nonzero
[[operator-algebras/positive-linear-functional|positive linear functional]]
\(\omega\) on \(A\) satisfies \(\omega(h)>0\). Strict positivity therefore
means that \(h\) has full support throughout \(A\); it is stronger than
\(h\geq0\) and does not, in a nonunital algebra, mean that \(h\) is invertible
inside \(A\).

## Equivalent characterizations

After rescaling so that \(0\leq h\leq1\), the following are equivalent:
\(h\) is strictly positive; \(\overline{hA}=\overline{Ah}=A\); and the
sequence
\[
e_n=f_n(h),\qquad f_n(t)=\min\{nt,1\},
\]
is an [[operator-algebras/approximate-identity|approximate identity]] for
\(A\). Consequently, \(A\) contains a strictly positive element exactly when
it is [[operator-algebras/sigma-unital-cstar-algebra|\(\sigma\)-unital]].

## Examples and non-examples

In a unital \(C^*\)-algebra, a positive element is strictly positive exactly
when it is positive and invertible. In \(C_0(\mathbb R)\), the function
\[
h(x)=e^{-x^2}
\]
is strictly positive even though it is not invertible as an element of
\(C_0(\mathbb R)\). More generally, a positive function in \(C_0(X)\) is
strictly positive exactly when it is nonzero at every point of \(X\).
The function \(x^2e^{-x^2}\) is positive but not strictly positive because
evaluation at \(0\) annihilates it.

For [[operator-algebras/compact-operator-cstar-algebra|\(K(H)\)]], a positive
[[linear-algebra/compact-operator|compact operator]] is strictly positive
precisely when it has trivial kernel and dense range. Such an operator exists
only when \(H\) is separable.

## Conventions and scope

“Strictly positive” has a specialized meaning here. It does not mean that
there is an \(\varepsilon>0\) with \(h\geq\varepsilon1\) in the
[[operator-algebras/unitization|unitization]]; that stronger inequality would
make \(h\) invertible and cannot hold for typical nonunital examples.
Likewise, “full positive element” can refer to generation of the whole
[[operator-algebras/closed-two-sided-ideal|closed two-sided ideal]], a weaker
condition than generating the whole hereditary subalgebra.

## References

1. Gert K. Pedersen, *\(C^*\)-Algebras and Their Automorphism Groups*, 2nd ed., Academic Press, 2018. [DOI record](https://doi.org/10.1016/C2016-0-03431-9). Relevant: §1.4 on strictly positive elements, hereditary subalgebras, and countable approximate units.
