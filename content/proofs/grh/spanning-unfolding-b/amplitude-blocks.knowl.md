+++
id = "proofs/grh/spanning-unfolding-b/amplitude-blocks"
title = "Maps with amplitude blocks"
kind = "definition"
summary = "A linear map from the source space to a representation of the residue group whose translated Gram blocks are the amplitude sums of all terms divided by the unipotent covolume."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.HasAmplitudeBlocks"]
lean_files = ["src/New/Spanning/Unfolding/Moments.lean"]
+++

Let \(S\) be a [[proofs/grh/spanning-unfolding-b/filling-data|filling datum]] with residue group \(\bar G\). Consider the *source* \(\mathcal{X}=\mathbb{C}^{\mathcal{C}\times I}\), the Euclidean space with orthonormal basis \(e_{(c,i)}\) indexed by a [[proofs/grh/spanning-unfolding-b/filling-classes-and-terms|class]] \(c\) and a Bessel coordinate \(i\); its dimension is the [[proofs/grh/spanning-unfolding-b/filling-constants|source dimension]] \(\dim_S\). Let \(\rho\) be a complex [[?c:Linear representation of a group|representation]] of \(\bar G\) on an inner product space \(V\) and \(P\colon\mathcal{X}\to V\) a linear map. The pair \((\rho,P)\) **has amplitude blocks** if for all \(s\in\bar G\) and all \(x=(c,i)\), \(y=(c',j)\)
\[
\bigl\langle\rho(s)Pe_y,\ Pe_x\bigr\rangle=\frac{A(c,s,c')_{(i,j)}}{\nu},
\]
where the inner product is conjugate-linear in its first argument, \(A(c,s,c')\) is the [[proofs/grh/spanning-unfolding-b/filling-amplitude|amplitude sum]] of all rational terms over the block \((c,s,c')\) for the full Bessel function, and \(\nu\) is the [[proofs/grh/spanning-unfolding-b/filling-constants|unipotent covolume]].

## Remarks

Equivalently, the matrix of \(P_s=P^*\rho(s)P\) has entries \(\langle P_se_y,e_x\rangle=A(c,s,c')_{(i,j)}/\nu\); in the convention of the source text the blocks of \(P_s\) are the complex conjugates of the normalised amplitude sums. The condition holds for the Poincaré map of the main argument after scaling ([[?lean:New.Data.hasAmplitudeBlocks_scaledPoincare|amplitude blocks of the Poincaré map]]).

## References

1. Lean: `New.Filling.HasAmplitudeBlocks` in `src/New/Spanning/Unfolding/Moments.lean`.
