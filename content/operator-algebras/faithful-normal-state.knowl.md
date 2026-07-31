+++
id = "operator-algebras/faithful-normal-state"
title = "Faithful normal state"
kind = "definition"
summary = "A normal state that detects every nonzero positive element of a von Neumann algebra."
aliases = ["f.n. state"]
domains = ["operator-algebras"]
section_mode = "progressive"
+++

Let \(M\) be a [[operator-algebras/von-neumann-algebra|von Neumann algebra]]. A
**faithful normal state** is a [[operator-algebras/normal-state|normal state]]
\(\varphi:M\to\mathbb C\) that is faithful:
\[
x\in M_+,\quad \varphi(x)=0\quad\Longrightarrow\quad x=0.
\]
Equivalently, \(\varphi(x^*x)=0\) implies \(x=0\) for every \(x\in M\).
Thus the state is both ultraweakly continuous and nondegenerate on the
positive cone. Neither adjective implies the other: normality is a continuity
condition, whereas faithfulness says that no nonzero positive element is
invisible to the state. In particular, a faithful normal state distinguishes
zero from every positive element.

## Equivalent characterizations

A normal state \(\varphi\) is faithful exactly when its
[[operator-algebras/support-projection-of-functional|support projection]] is
\(1\). Equivalently, in the [[operator-algebras/gns-construction|GNS representation]]
of \(\varphi\), the [[operator-algebras/cyclic-vector|cyclic vector]] is
[[operator-algebras/separating-vector|separating]] for the represented von
Neumann algebra. These
characterizations connect positivity, support, and representation theory
[Takesaki, discussion of faithful normal states].

## Existence and examples

A von Neumann algebra admits a faithful normal state exactly when it is
sigma-finite, also called countably decomposable in this setting. If \(H\) is
separable, choose a positive trace-class operator \(\rho\) with trivial kernel
and \(\operatorname{Tr}(\rho)=1\); then
\(\varphi(x)=\operatorname{Tr}(\rho x)\) is a faithful normal state on
\(B(H)\). By contrast, \(B(H)\) for nonseparable \(H\) has no faithful normal
state.

## Distinctions

A [[operator-algebras/faithful-state-cstar-algebra|faithful state]] on the
underlying \(C^*\)-algebra need not be normal. Likewise, a normal state can
fail to be faithful when its support is a proper projection. Faithful normal
states are bounded normalized functionals, not the possibly unbounded
faithful normal [[operator-algebras/semifinite-weight|semifinite weights]] used in modular theory.

## References

1. Masamichi Takesaki, *Theory of Operator Algebras I*, Springer, 1979. [DOI record](https://doi.org/10.1007/978-1-4612-6188-9). Relevant: the chapters on normal positive functionals, sigma-finiteness, and standard representations.
