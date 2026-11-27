+++
id = "proofs/grh/upper-seesaw/seesaw-datum"
title = "The seesaw datum"
kind = "construction"
summary = "The tensor of finite data for the upper chain obtained as the weighted sum over the cuts of the evaluated data; it is invariant under the levels and an admissible combination of glued vacua."
aliases = ["evaluated tensor", "phi_xi"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.evaluatedTensor", "New.Data.evaluatedTensor_mk", "New.Data.seesawDatum", "New.Data.isInvariant_seesawDatum", "New.Data.exists_isAdmissibleCombination_seesawDatum"]
lean_files = ["src/New/UpperBound/Seesaw/SeesawIdentity.lean"]
proof_status = "full"
+++

Let \(\vartheta\) be a tame character. For a tuple \(c=(c_i)\) of classes
\(c_i\in G_{i,f}/J_i\) with representatives \(\tilde c_i\), the **evaluated tensor** is the pure
tensor of the [[proofs/grh/upper-seesaw/tower-gradings-and-evaluated-data|evaluated data]] of all
\(\varrho+1\) pairs of edges,
\[
E(\vartheta,c)=E_\varrho(\vartheta,\tilde c)\otimes\dots\otimes E_0(\vartheta,\tilde c),
\]
an element of the space of [[?lean:New.Data.ChainTensor|chain tensors]] (finite data for the chain
of lifts \(X_0\to\dots\to X_m\)). It does not depend on the representatives
([[proofs/grh/upper-seesaw/unfolding-stage-as-coefficient-of-chain|invariance of the evaluated
data]]). The **seesaw datum** is the [[proofs/grh/upper-seesaw/cut-sum|cut sum]]
\[
\varphi_{\vartheta}=\Sigma_{m}\bigl(E(\vartheta,\cdot)\bigr).
\]

## Properties

1. (**Invariance.**) \(\varphi_\vartheta\) is
   [[?lean:New.Data.ChainTensor.IsInvariant|jointly invariant]] for \(\vartheta\): it is fixed by
   every tuple \(b=(b_j)\) with \(b_j\) in the level of \(U(X_j)\) for \(j<m\) and \(b_m=1\).
2. (**Admissibility.**) There is a constant \(C\) such that for every tame \(\vartheta\), with
   \(q=\mathrm{N}Q\) and \(\mathcal{C}=M^{fn_m^{2}}\): \(\varphi_\vartheta\) is an
   [[proofs/grh/upper-seesaw/admissible-combination|admissible combination]] of the
   \(C\,\mathrm{gv}(x)\), \(x\) admissible for \(q\), with denominator \(\mathcal{C}^{2m}\) away
   from \(q\) and, if \(Q=\emptyset\), size \(\mathcal{C}^{m}\).

## Proof

(1) Let \(b\) be given and let \(h_i\) be the image of \(b_i\) in \(G_{i,f}\) for \(i<m\) and
\(h_i=1\) for \(i\ge m\). By linearity of the joint action and part 2 of the cut sum lemma,
\[
b\cdot\varphi_\vartheta=\Sigma_m\bigl(b\cdot E(\vartheta,\cdot)\bigr),\qquad\Sigma_m\bigl(E(\vartheta,\cdot)\bigr)=\Sigma_m\bigl(E(\vartheta,h\cdot{-})\bigr),
\]
so it suffices that \(E(\vartheta,[hy])=b\cdot E(\vartheta,[y])\) for every tuple \(y\); the joint
action on a pure tensor acts on the factor \(i\) by
\(\omega(b_{2i},b_{2i+1})\otimes\omega(b_{2i+1},b_{2i+2})\). The translated point data satisfy
\(\Phi_k^{hy}=\omega(h_k,h_{k+1})\Phi_k^{y}\), since the finite Weil action is a homomorphism.
For \(i<\varrho\) the evaluation is that of the middle double lift, and
[[proofs/grh/upper-seesaw/double-lift-evaluation-equivariant|equivariance of the finite
evaluation]] (with \(\epsilon=\mathrm{id}\)) gives the claim for the factor \(i\). For
\(i=\varrho\) it is that of the last double lift; here \(h_m=1\) is the image of \(1\) under the
last grading, \(\epsilon(1)=1\), and \(b_m=1\).

(2) By [[proofs/grh/upper-seesaw/evaluated-data-admissible|admissibility of the evaluated data]],
each value \(E(\vartheta,[y])\) at a tuple \(y\) integral away from \(q\) is an admissible
combination of the \(C\,\mathrm{gv}(x)\) with denominator \(\mathcal{C}^{2m}\) (for every \(Q\)) and, when \(Q=\emptyset\), size \(1\). By
part 3 of the cut sum lemma, \(\varphi_\vartheta\) is an admissible combination of these values with
denominator \(1\) (for every \(Q\)) and, when \(Q=\emptyset\), size \(\mathcal{C}^{m}\).
[[proofs/grh/upper-seesaw/admissible-combination-substitution|Substitution]] gives the claim.
\(\blacksquare\)

## References

1. Lean: `New.Data.seesawDatum`, `New.Data.evaluatedTensor`, `New.Data.isInvariant_seesawDatum`, `New.Data.exists_isAdmissibleCombination_seesawDatum` in `src/New/UpperBound/Seesaw/SeesawIdentity.lean`.
