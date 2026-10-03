+++
id = "ergodic-theory/ring-of-integers-translation-action"
title = "Ergodic translation action of the ring of integers"
kind = "theorem"
summary = "The joint action by all integral multiples of an increment is ergodic exactly when there is no integral linear relation modulo the ring of integers."
aliases = []
domains = ["ergodic-theory"]
section_mode = "progressive"
prerequisites = ["ergodic-theory/ergodic-action", "harmonic-analysis/number-field-torus-characters", "algebra-fields-galois/codifferent"]
+++

Fix \(\omega\in K_\infty^d\). The maps
\[
S_b([x])=[x+b\omega]\qquad(b\in\mathcal O_K)
\]
form a Haar-preserving action of the additive group \((\mathcal O_K,+)\) on \((K_\infty/\mathcal O_K)^d\). This action is [[ergodic-theory/ergodic-action|ergodic]] if and only if
\[
k\cdot\omega\notin\mathcal O_K\qquad(0\ne k\in\mathcal O_K^d).
\]
Equivalently, \(1,\omega_1,\ldots,\omega_d\) are linearly independent over the diagonally embedded field \(K\).

## Proof using characters

A [[harmonic-analysis/number-field-torus-characters|character]] indexed by \(a\in(\mathcal O_K^\vee)^d\) is fixed by every \(S_b\) exactly when
\[
\operatorname{Tr}_\infty(b(a\cdot\omega))\in\mathbb Z
\quad\text{for every }b\in\mathcal O_K,
\]
or \(a\cdot\omega\in\mathcal O_K^\vee\). The latter equivalence also holds for elements initially in \(K_\infty\): expansion in the trace-dual basis forces integral coefficients.

If a nonzero such \(a\) exists, choose \(N\) clearing the codifferent and put \(k=Na\). Then \(k\in\mathcal O_K^d\setminus\{0\}\) and \(k\cdot\omega\in\mathcal O_K\). Conversely any such \(k\) is already a codifferent frequency with codifferent pairing. Fourier completeness proves the criterion. Clearing rational denominators in a \(K\)-linear relation proves the final equivalence.

## Scope

These are translations indexed by the additive group, not multiplication maps \([x]\mapsto[bx]\). When \(K=\mathbb Q\), this action is iteration of one translation. For higher-degree fields it involves several commuting generators.
