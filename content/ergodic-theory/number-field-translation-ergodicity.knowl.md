+++
id = "ergodic-theory/number-field-translation-ergodicity"
title = "Ergodicity of a single number-field translation"
kind = "theorem"
summary = "A single translation is ergodic exactly when every nonzero dual frequency has nonintegral trace pairing with its increment."
aliases = []
domains = ["ergodic-theory"]
section_mode = "progressive"
prerequisites = ["harmonic-analysis/number-field-torus-characters", "ergodic-theory/compact-abelian-rotation", "algebra-fields-galois/archimedean-trace-pairing"]
+++

For \(\omega\in K_\infty^d\), [[ergodic-theory/compact-abelian-rotation|translation]] \(T_\omega([x])=[x+\omega]\) on \(X=(K_\infty/\mathcal O_K)^d\) with Haar probability is ergodic if and only if
\[
\operatorname{Tr}_\infty(a\cdot\omega)\notin\mathbb Z
\qquad\bigl(0\ne a\in(\mathcal O_K^\vee)^d\bigr).
\]

## Fourier proof

Inverse pullback satisfies
\[
\alpha_\omega(\chi_a)=e^{-2\pi i\operatorname{Tr}_\infty(a\cdot\omega)}\chi_a.
\]
The [[harmonic-analysis/number-field-torus-characters|character]] is fixed exactly when its trace pairing is integral. Character completeness gives the fixed-function criterion.

## Equivalent integral-coefficient test

The same ergodicity test can quantify over \(0\ne k\in\mathcal O_K^d\). Indeed, \(\mathcal O_K\subseteq\mathcal O_K^\vee\), and multiplying a violating codifferent frequency by an integer \(N\) with \(N\mathcal O_K^\vee\subseteq\mathcal O_K\) produces a violating integral frequency. This does not change which lattice indexes all Fourier characters.

## Distinction from a ring action

The condition \(k\cdot\omega\notin\mathcal O_K\) for nonzero integral \(k\) is instead the criterion for the [[ergodic-theory/ring-of-integers-translation-action|joint ring-of-integers translation action]]. It is insufficient for one translation in higher-degree fields.
