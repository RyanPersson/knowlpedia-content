+++
id = "operator-algebras/tomita-operator"
title = "Tomita operator"
kind = "definition"
summary = "The Tomita operator is the closed antilinear operator obtained from the adjoint operation relative to a cyclic separating vector."
aliases = ["involutive Tomita operator"]
domains = ["operator-algebras"]
section_mode = "progressive"
+++

Let \(M\subseteq B(H)\) be a
[[operator-algebras/von-neumann-algebra|von Neumann algebra]] and let
\(\Omega\in H\) be both a [[operator-algebras/cyclic-vector|cyclic vector]] and
a [[operator-algebras/separating-vector|separating vector]] for \(M\). On the
dense subspace \(M\Omega\), define the antilinear operator
\[
S_0(x\Omega)=x^*\Omega,\qquad x\in M.
\]
Separatingness makes this formula well-defined, and cyclicity makes its domain
dense. The operator \(S_0\) is closable; its closure \(S=\overline{S_0}\) is
the **Tomita operator** of \((M,\Omega)\). It is closed, densely defined, and
satisfies \(S^2\xi=\xi\) whenever both sides are defined.

## Closability and the commutant

The companion operator \(F_0(x'\Omega)=x'^*\Omega\) on \(M'\Omega\) is densely
defined because separatingness for \(M\) is equivalent to cyclicity for the
[[operator-algebras/commutant|commutant]] \(M'\). The inclusions
\(S_0^*\supseteq F_0\) and \(F_0^*\supseteq S_0\) prove that both operators
are closable. In fact, their closures satisfy \(S^*=F\)
[Takesaki, Chapter VI, §1].

## Polar decomposition and modular data

The [[shale-paper/polar-decomposition|polar decomposition]] of the closed
antilinear operator is
\[
S=J\Delta^{1/2}.
\]
Here \(J\) is the
[[operator-algebras/modular-conjugation|modular conjugation]] and
\(\Delta=S^*S\) is the
[[operator-algebras/modular-operator|modular operator]]. These objects depend
on the pair \((M,\Omega)\), not on \(M\) alone. Their decisive properties are
the content of the [[operator-algebras/tomita-takesaki-theorem|Tomita–Takesaki
theorem]].

## Examples and scope

For \(M=B(K)\) acting by left multiplication on the [[functional-analysis/hilbert-schmidt-operator|Hilbert–Schmidt operators]]
\(\operatorname{HS}(K)\), the identity Hilbert–Schmidt vector is available
only when \(K\) is finite-dimensional; then \(S(x)=x^*\). More generally a
faithful [[quantum-foundations/density-operator|density operator]] supplies a cyclic separating vector in the standard
Hilbert–Schmidt realization.

**Warning.** If \(\Omega\) is not separating, \(x\Omega=0\) need not imply
\(x^*\Omega=0\), so the displayed rule may not be well-defined. If it is not
cyclic, \(M\Omega\) is not dense and no densely defined Tomita operator on all
of \(H\) results.

## References

1. Masamichi Takesaki, *Theory of Operator Algebras I*, Springer, 1979. [DOI record](https://doi.org/10.1007/978-1-4612-6188-9). Relevant: Chapter VI, §1 on the closable operators \(S_0\) and \(F_0\).
