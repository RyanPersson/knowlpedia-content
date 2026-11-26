+++
id = "proofs/grh/upper-seesaw/cut-sum"
title = "Weighted sums over the cuts"
kind = "lemma"
summary = "The sum over the cut points of all stages, weighted by inverse multiplicities, is invariant under the levels of the definite groups and is an admissible combination of the values of the summand."
aliases = ["cutSum"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.cutSumAt", "New.Data.cutSum", "New.Data.map_cutSum", "New.Data.cutSumAt_smul", "New.Data.cutSum_comp_smul", "New.Data.isAdmissibleCombination_cutSumAt", "New.Data.isAdmissibleCombination_cutSum"]
lean_files = ["src/New/UpperBound/Seesaw/Cut.lean"]
proof_status = "full"
+++

Notation as in [[proofs/grh/upper-seesaw/stage-cuts|the stage cuts]]: cut points \(\Omega_j\) and
multiplicities \(\mu_j\). Let \(M\) be a complex vector space and \(S\) a function from tuples
\(c=(c_i)_{i\ge0}\), \(c_i\in G_{i,f}/J_i\), to \(M\).

**Definition.** For \(k\le m\), the **cut sum** is
\[
\Sigma_k(S)=\sum_{x_0\in\Omega_0}\cdots\sum_{x_{k-1}\in\Omega_{k-1}}\ \prod_{j<k}\mu_j(x_j)^{-1}\;S(x_0,\dots,x_{k-1},1,1,\dots),
\]
defined recursively by summing the coordinate \(k-1\) first (innermost) and then applying
\(\Sigma_{k-1}\).

**Lemma.**

1. \(L(\Sigma_k(S))=\Sigma_k(L\circ S)\) for a linear map \(L\).
2. Let \(h=(h_i)\) be finite points with \(h_i\) the image of an element of the level of \(U(X_i)\)
   for \(i<k\) and \(h_i=1\) for \(i\ge k\). Then \(\Sigma_k(S(h\cdot{-}))=\Sigma_k(S)\).
3. \(\Sigma_k(S)\) is an [[proofs/grh/upper-seesaw/admissible-combination|admissible combination]]
   of the values \(S(y)\), over all tuples \(y\) of points integral away from \(q\), with
   denominator \(1\) away from \(q\) and, if \(Q=\emptyset\), size \(\mathcal{C}^{k}\).

## Proof

(1) Linearity, by induction on \(k\).

(2) Induction on \(k\). In the innermost sum over \(x\in\Omega_{k-1}\), the substitution
\(x\mapsto h_{k-1}x\) permutes \(\Omega_{k-1}\) and preserves \(\mu_{k-1}\); so \(h_{k-1}\) drops
out, and the induction hypothesis applies to \(h\) with its entry \(k-1\) replaced by \(1\).

(3) One sum over the coordinate \(j\) is a sum of the terms \(\mu_j(x)^{-1}S(\dots,x,\dots)\),
\(x\in\Omega_j\). Each \(x\) is integral away from \(q\), and \(\mu_j(x)\) divides a power of
\(q\), so \(\mu_j(x)^{-1}\) is [[proofs/grh/upper-seesaw/integral-away|integral away from \(q\)]].
Each coefficient has absolute value \(\mu_j(x)^{-1}\le1\) at every conjugate (it is rational, and \(\mu_j(x)\ge1\) on \(\Omega_j\) since it divides a power of \(q\)). If \(Q=\emptyset\), the points over \(\Omega_j\) are integral everywhere, so \(\Omega_j\) has at most \(\mathcal{C}\) elements ([[proofs/grh/upper-seesaw/stage-cuts|stage cuts]]); hence size \(\mathcal{C}\). Iterating with
[[proofs/grh/upper-seesaw/admissible-combination-substitution|substitution]] multiplies the sizes:
\(\mathcal{C}^{k}\). \(\blacksquare\)

## References

1. Lean: `New.Data.cutSum`, `New.Data.cutSum_comp_smul`, `New.Data.isAdmissibleCombination_cutSum` in `src/New/UpperBound/Seesaw/Cut.lean`.
