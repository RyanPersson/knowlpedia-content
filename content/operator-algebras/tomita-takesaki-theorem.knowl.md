+++
id = "operator-algebras/tomita-takesaki-theorem"
title = "Tomita–Takesaki theorem"
kind = "theorem"
summary = "The Tomita–Takesaki theorem identifies the commutant through modular conjugation and proves invariance under modular evolution."
aliases = ["fundamental theorem of modular theory"]
domains = ["operator-algebras"]
section_mode = "progressive"
+++

Let \(M\subseteq B(H)\) be a
[[operator-algebras/von-neumann-algebra|von Neumann algebra]] with
[[operator-algebras/cyclic-vector|cyclic]]
[[operator-algebras/separating-vector|separating vector]] \(\Omega\). Write
\(S=J\Delta^{1/2}\) for the polar decomposition of its
[[operator-algebras/tomita-operator|Tomita operator]]. The
**Tomita–Takesaki theorem** asserts
\[
JMJ=M'
\qquad\text{and}\qquad
\Delta^{it}M\Delta^{-it}=M\quad(t\in\mathbb R).
\]
Here \(J\) is the
[[operator-algebras/modular-conjugation|modular conjugation]], \(\Delta\) the
[[operator-algebras/modular-operator|modular operator]], and \(M'\) the
[[operator-algebras/commutant|commutant]]. Consequently
\(\sigma_t^\Omega(x)=\Delta^{it}x\Delta^{-it}\) is a strongly continuous
one-parameter group of \(*\)-automorphisms of \(M\).
These conclusions are intrinsic to the standard pair \((M,\Omega)\):
\(J\) exchanges the algebra with its commutant, while the modular unitaries
normalize \(M\). In particular, the displayed automorphisms are defined for
every real \(t\), not merely on an analytic subalgebra.

## Hypotheses and setting

Cyclicity makes \(M\Omega\) dense, while separatingness makes
\(S_0(x\Omega)=x^*\Omega\) well-defined and ensures that \(M'\Omega\) is
dense. These are exactly the vector hypotheses used to construct the two
closed antilinear operators whose polar factors appear in the theorem.
General von Neumann algebras are treated by faithful normal semifinite weights,
standard forms, or reduction to supports rather than by assuming that a cyclic
separating vector exists in an arbitrary representation.

## Proof architecture

The proof first compares the closures of
\(S_0(x\Omega)=x^*\Omega\) and
\(F_0(x'\Omega)=x'^*\Omega\). Analytic continuation of matrix coefficients,
together with the polar decomposition, gives the inclusions
\(JMJ\subseteq M'\) and
\(\Delta^{it}M\Delta^{-it}\subseteq M\). Applying the same argument to the
commutant and to \(-t\) upgrades both inclusions to equalities. The full
argument is given in
[Takesaki, Chapter VI, §1](https://doi.org/10.1007/978-1-4612-6188-9).

## Consequences

The unitary group \(\Delta^{it}\) supplies canonical modular dynamics for the
faithful normal [[operator-algebras/vector-state|vector state]]. The
conjugation \(J\) gives an intrinsic
anti-isomorphism between \(M\) and its commutant in standard position. The
weight form of the theorem yields the
[[operator-algebras/modular-automorphism-group|modular automorphism group]] of
every [[operator-algebras/normal-semifinite-faithful-weight|normal semifinite
faithful weight]], a central tool in the structure theory of type III
algebras.

## Conventions and scope

**Warning.** Replacing \(\Delta^{it}x\Delta^{-it}\) by
\(\Delta^{-it}x\Delta^{it}\) reverses the time parameter. Both conventions
occur when modular operators or inner products are normalized differently;
formulas involving KMS boundary values must use one convention consistently.

## References

1. Masamichi Takesaki, *Theory of Operator Algebras I*, Springer, 1979. [DOI record](https://doi.org/10.1007/978-1-4612-6188-9). Relevant: Chapter VI, §1, the fundamental theorem of modular theory.
