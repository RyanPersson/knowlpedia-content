+++
id = "proofs/grh/determinant-exchange/descent-as-pairing-with-kernel-form"
title = "The normalized descent is the inner product with the kernel form"
kind = "lemma"
summary = "The value at g of the normalized descent of a form on V is the inner product of the kernel form at g with that form."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.DescentPair.normalizedDescent_eq_inner_vectorKernelForm", "New.DescentPair.normalizedDescent_apply"]
lean_files = ["src/New/Determinant/Norms/VectorKernel.lean"]
proof_status = "full"
+++

**Lemma.** Let \(O\) be a [[?lean:New.DescentPair|descent pair]] with spaces \(W\), \(V\), let \(\Xi\) be an [[?lean:New.DescentPair.FormV|algebraic form on \(V\)]] of the pair, and let \(\theta\Xi\) be its [[?lean:New.DescentPair.normalizedDescent|normalized descent]], a function on \(U(W)(\mathbb{A})\). For every \(g\in U(W)(\mathbb{A})\),
\[
(\theta\Xi)(g)=\bigl\langle\theta_W(g,\cdot),\Xi\bigr\rangle ,
\]
the inner product, in the space of forms on \(V\), of the [[proofs/grh/determinant-exchange/vector-kernel-equivariance|kernel form]] at \(g\) with \(\Xi\).

Here the inner product of two forms \(\Xi',\Xi\) on \(V\) is the [[?lean:New.stdClassSum|class sum]] of the Gram pairings of their values,
\[
\langle\Xi',\Xi\rangle=\sum_{h\in\Gamma\backslash U(V)(\mathbb{A}_f)/K}\frac{\langle\Xi'(h),\Xi(h)\rangle}{\#(\Gamma\cap hKh^{-1})},
\]
with \(\Gamma=U(V)(E)\) and \(K\) the level of the pair.

## Proof

By definition the normalized descent is the class sum
\[
(\theta\Xi)(g)=\sum_{h}\frac{\kappa_{g,h}(\Xi(h))}{\#(\Gamma\cap hKh^{-1})}
\]
of the conjugate kernel \(\kappa_{g,h}\) applied to the values of \(\Xi\). By the defining property of the [[proofs/grh/determinant-exchange/vector-valued-theta-kernel|vector-valued theta kernel]], \(\kappa_{g,h}(\xi)=\langle\theta_W(g,h),\xi\rangle\). So the summand is the Gram pairing of the values at \(h\) of the kernel form and of \(\Xi\), and the sum is the inner product of the two forms ([[?lean:New.LevelPlaces.LevelForm.innerAt_eq_stdClassSum|the inner product of level forms as a class sum]]).

## References

1. Lean: `New.DescentPair.normalizedDescent_eq_inner_vectorKernelForm` in `src/New/Determinant/Norms/VectorKernel.lean`.
