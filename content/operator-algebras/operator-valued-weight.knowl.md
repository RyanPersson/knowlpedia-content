+++
id = "operator-algebras/operator-valued-weight"
title = "Operator-valued weight"
kind = "definition"
summary = "An extended-positive-valued bimodular weight from a von Neumann algebra to a von Neumann subalgebra."
aliases = ["operator valued weight"]
domains = ["operator-algebras"]
section_mode = "progressive"
+++

Let \(N\subseteq M\) be unital
[[operator-algebras/von-neumann-algebra|von Neumann algebras]]. An
**operator-valued weight from \(M\) to \(N\)** is a map
\[
T:M_+\longrightarrow\widehat N_+
\]
into the [[operator-algebras/extended-positive-cone|extended positive cone]]
that is additive, positively homogeneous, and \(N\)-bimodular in the positive
sense:
\[
T(a^*xa)=a^*T(x)a
\qquad(x\in M_+,\ a\in N).
\]
The operations on the right are those of \(\widehat N_+\). Unlike a
conditional expectation, \(T(x)\) may be unbounded or infinite. No normality,
faithfulness, or semifiniteness is implicit unless it is stated separately.

## Regularity conditions

The weight \(T\) is normal when it preserves suprema of increasing nets in
\(M_+\), and faithful when \(T(x)=0\) implies \(x=0\). It is semifinite when
\[
\mathfrak n_T=\{x\in M:T(x^*x)\in N_+\}
\]
is ultraweakly dense in \(M\). If \(T\) is normal, faithful, and semifinite
and \(\varphi\) is a normal semifinite faithful scalar weight on \(N\), then
\(\varphi\circ T\) is such a weight on \(M\)
[Haagerup, §2](https://doi.org/10.1016/0022-1236%2879%2990053-3).

## Conditional expectations

A [[operator-algebras/conditional-expectation|conditional expectation]]
\(E:M\to N\) restricts to an operator-valued weight whose values lie in the
bounded cone \(N_+\) and satisfy \(E(1)=1\). Thus operator-valued weights
generalize conditional expectations by allowing extended positive values.
A merely [[operator-algebras/positive-linear-map|positive map]] \(M\to N\)
need not be an operator-valued weight: it can fail the displayed
\(N\)-bimodularity identity.

## Composition

The composition \(\varphi\circ T\) is defined intrinsically because each
scalar weight \(\varphi\) extends from \(N_+\) to \(\widehat N_+\) by monotone
limits. This construction allows information about scalar weights on \(M\)
to be transferred through an inclusion \(N\subseteq M\), and is one of the
main uses of operator-valued weights in modular theory.

## References

1. Uffe Haagerup, “Operator-Valued Weights in von Neumann Algebras I,” *Journal of Functional Analysis* 32 (1979), 175–206. [DOI record](https://doi.org/10.1016/0022-1236%2879%2990053-3). Relevant: §§1–2 on the definition, regularity properties, and composition with scalar weights.
2. Masamichi Takesaki, *Theory of Operator Algebras II*, Springer, 2003. [DOI record](https://doi.org/10.1007/978-3-662-10451-4). Relevant: Chapter IX, §4 on conditional expectations and operator-valued weights.
