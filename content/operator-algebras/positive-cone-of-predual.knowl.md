+++
id = "operator-algebras/positive-cone-of-predual"
title = "Positive cone of the predual"
kind = "definition"
summary = "The positive cone of a von Neumann algebra predual consists of its normal positive functionals."
aliases = ["normal positive functional cone"]
domains = ["operator-algebras", "functional-analysis"]
section_mode = "progressive"
+++

Let \(M\) be a [[operator-algebras/von-neumann-algebra|von Neumann algebra]]
with [[operator-algebras/predual|predual]] \(M_*\). The **positive cone of the
predual** is
\[
(M_*)_+=\{\varphi\in M_*:\varphi(x)\geq0\text{ for every }x\in M_+\},
\]
where \(M_+\) is the [[operator-algebras/positive-cone|positive cone]] of
\(M\). Its elements are precisely the positive
[[operator-algebras/normal-functional|normal functionals]] on \(M\). The cone
is norm closed, convex, proper, and generating in the self-adjoint part of
\(M_*\). It defines the order
\(\varphi\leq\psi\) exactly when \(\psi-\varphi\in(M_*)_+\).

## Norm and Jordan decomposition

For \(\varphi\in(M_*)_+\), positivity gives
\[
\lVert\varphi\rVert=\varphi(1).
\]
Every self-adjoint normal functional has a unique Jordan decomposition
\[
\omega=\omega_+-\omega_-,
\]
where \(\omega_\pm\in(M_*)_+\) have orthogonal support projections and
\(\lVert\omega\rVert=\lVert\omega_+\rVert+\lVert\omega_-\rVert\). Taking real
and imaginary parts then shows that every element of \(M_*\) is a linear
combination of four positive normal functionals
[Takesaki, vol. I, Chapter III, §2].

## Concrete realization

For \(M=B(H)\), the predual is the
[[functional-analysis/schatten-class-operator|trace-class operators]], with pairing
\[
\varphi_T(x)=\operatorname{Tr}(Tx).
\]
Under this identification, \((M_*)_+\) corresponds exactly to the positive
trace-class operators. [[operator-algebras/normal-state|Normal states]]
correspond to those positive operators whose trace is one. For a general
concrete von Neumann algebra \(M\subseteq B(H)\), the predual is a quotient of
the trace class, so a normal
[[operator-algebras/positive-linear-functional|positive functional]] can have
more than one positive trace-class representative.

## Order-theoretic role

The cone \((M_*)_+\) is not the positive cone of \(M\) itself: its elements
are functionals, not operators in \(M\). It records the order that is
compatible with the canonical duality \(M=(M_*)^*\). Normal states form the
base
\[
\{\varphi\in(M_*)_+:\varphi(1)=1\}
\]
of the nonzero cone, while unbounded
[[operator-algebras/normal-weight|normal weights]] lie outside \(M_*\).

## References

1. Masamichi Takesaki, *Theory of Operator Algebras I*, Springer, 1979. [DOI record](https://doi.org/10.1007/978-1-4612-6188-9). Relevant: Chapter III, §2 on the predual, positive normal functionals, and Jordan decomposition.
2. Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras, Volume I: Elementary Theory*, American Mathematical Society, 1997. [AMS record](https://bookstore.ams.org/GSM/15). Relevant: §5.2 on normal functionals and the predual order.
