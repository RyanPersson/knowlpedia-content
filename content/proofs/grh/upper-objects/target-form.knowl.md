+++
id = "proofs/grh/upper-objects/target-form"
title = "Forms of principal level, good forms and target forms"
kind = "definition"
summary = "On a hermitian space of rank r with the target parameter at infinity: the forms fixed by the principal level at the chosen places, the action of the chosen group on them, the good forms (image of e_0), and the target forms (good forms on Y_0)."
aliases = ["target forms", "good forms", "principal forms", "row", "target dimension"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.principalForms", "New.Data.principalRep", "New.Data.goodForms", "New.Data.targetForms", "New.Data.targetDim"]
lean_files = ["src/New/UpperBound/Objects/Rows.lean"]
+++

Let \(D\) be [[?lean:New.Data|admissible data]] and let \(V\) be a [[?lean:New.Space|space]] on the [[proofs/grh/upper-objects/index-sets-of-the-hermitian-spaces|row index set]] \(\mathcal R\) (rank \(r\)) with signs \(s\). Let \(\lambda=(\lambda_\tau)\) be the [[proofs/grh/upper-objects/signs-and-parameter-of-w|doubled target parameter]] and \(\Theta_{\lambda,s}\) the [[?lean:New.typeKernel|type kernel]] of \((\lambda,s)\): the product over the infinite places of the kernels reproducing the discrete series of Harish-Chandra parameter \(\lambda_\tau/2\) on \(U(\operatorname{diag}s)\).

**Definition.**

* The **forms of principal level** on \(V\) are the [[?lean:New.Space.Form|forms on \(U(V)(\mathbb A)\) of type \(\Theta_{\lambda,s}\)]] that are fixed by the principal level at the chosen places: the integral finite adelic points reducing to \(1\) at every chosen place above \(p_0,p_1\). (The level is contained in the standard maximal compact subgroup and imposes no congruence at \(N\) or at the places of a twist: the forms are invariant under the full local maximal compact subgroups at all finite places other than the chosen places and their conjugates.)
* The [[proofs/grh/upper-objects/good-idempotent|group \(\bar G\) of the chosen places]] acts on them: an element acts through an integral lift with the given reductions.
* The **good forms** on \(V\) are the image of the [[proofs/grh/upper-objects/good-idempotent|good idempotent]] \(e_0\in\mathbb C[\bar G]\) on the forms of principal level.
* The **target forms** are the good forms on [[proofs/grh/upper-objects/spaces-y-and-w|\(Y_0\)]]; their dimension is the **target dimension** \(d\).

## Remarks

The spaces of forms of principal level are finite-dimensional when the parameter has the gap \(\Delta\) for the signs \(s\); see [[proofs/grh/upper-objects/principal-forms-are-finite-dimensional|finiteness]]. Other files call target forms *rows*.

## References

1. Lean: `New.Data.principalForms`, `New.Data.principalRep`, `New.Data.goodForms`, `New.Data.targetForms` in `src/New/UpperBound/Objects/Rows.lean`.
