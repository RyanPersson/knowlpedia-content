+++
id = "lie-groups/thirty-dimensional-generation-module-in-e7"
title = "Thirty-dimensional generation module in e7"
kind = "theorem"
summary = "Each 30-root projection class in E7 is an sl6 module Λ²C⁶ plus Λ⁴C⁶ and restricts to one Standard Model generation without two neutrino singlets."
aliases = ["30-dimensional generation module", "generation module without right-handed neutrinos", "N k module in e7"]
domains = ["lie-groups", "representation-theory", "mathematical-physics"]
section_mode = "progressive"
+++

For a labeled defining weight \(w_k\) in the [[lie-groups/generation-plane|generation plane]], let
\[
\Phi_k=\{r\in\Phi(E_7):\pi(r)=\pm w_k\},
\qquad
N_k:=\bigoplus_{r\in\Phi_k}(\mathfrak e_7)_r.
\]
Then \(N_k\) is a \(30\)-dimensional \(\mathfrak{sl}_6^{\mathrm{SM}}\)-submodule of the adjoint \(\mathfrak e_7\)-module, and
\[
N_k\cong
\Lambda^2\mathbb C^6\oplus\Lambda^4\mathbb C^6
\]
as \(\mathfrak{sl}_6^{\mathrm{SM}}\)-modules, where the summands are [[lie-groups/exterior-power-representation|exterior-power representations]].

This is a [[lie-groups/representation-of-a-lie-algebra|module]] and vector-space decomposition. In general \(N_k\) is not a [[lie-groups/lie-subalgebra|Lie subalgebra]] of \(\mathfrak e_7\).

## Restriction to the standard sl5

Using the defining-module splitting \(\mathbb C^6\cong\mathbb C^5\oplus\mathbb C\), restriction to [[lie-groups/standard-sl5-in-e7|\(\mathfrak{sl}_5^{\mathrm{SM}}\)]] gives
\[
N_k\cong
\Lambda^1\mathbb C^5
\oplus\Lambda^2\mathbb C^5
\oplus\Lambda^3\mathbb C^5
\oplus\Lambda^4\mathbb C^5.
\]
The formula follows from the [[lie-groups/exterior-algebra-of-a-direct-sum|exterior algebra of a direct sum]] and its degree decomposition.

## Standard Model interpretation

On restriction to \(\mathfrak g_{\mathrm{SM}}\), this is the [[mathematical-physics/standard-model-exterior-algebra-representation|one-generation exterior-algebra representation]] with the degree-zero and degree-five singlets omitted. These two missing one-dimensional summands are the right-handed neutrino and its antiparticle, both [[mathematical-physics/right-handed-neutrino-gauge-singlet|gauge singlets]]. Adding the two generation-root spaces produces the [[lie-groups/generation-module-as-even-exterior-algebra|32-dimensional generation module]].

## Dependence on choices and conventions

The three spaces \(N_k\) require a compatible [[lie-groups/cartan-subalgebra|Cartan subalgebra]] and a labeling of the three defining weights. Reversing highest-weight conventions exchanges \(\Lambda^2\mathbb C^6\) with its dual \(\Lambda^4\mathbb C^6\); their direct sum is unaffected. The particle/antiparticle and chirality labels additionally depend on the chosen Standard Model representation conventions.

## References

1. John C. Baez, “Three Generations in E7,” 2026, Lemma 9 and Theorem 10. [arXiv:2608.06271](https://arxiv.org/abs/2608.06271).
2. John C. Baez and John Huerta, “The Algebra of Grand Unified Theories,” *Bulletin of the American Mathematical Society* 47 (2010), 483–552, especially the exterior-algebra description of fermions. [arXiv:0904.1556](https://arxiv.org/abs/0904.1556).
