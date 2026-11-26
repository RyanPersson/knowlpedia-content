+++
id = "proofs/grh/determinant-exchange/single-lift"
title = "The single lift from W_j to V_j"
kind = "definition"
summary = "The theta lift, for a tame character and an index j, from the forms of principal level on W_j to the algebraic forms on the definite space V_j."
aliases = ["Theta_j", "single lift"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.singleLift", "New.Data.singleLift_apply", "New.Data.ofAlgForm_singleLift"]
lean_files = ["src/New/Determinant/Norms/AdjointThetaLift.lean"]
+++

Let \(D\) be the [[?lean:New.Data|data]] of the proof, with CM field \(E\), number of lifts \(m\) and ranks \(r\), \(t\). Let \(\vartheta\) be a [[?lean:New.Data.TameChar|tame character]] and \(j\) a natural number. For \(1\le j\le m\) let \(O_{j,\vartheta}\) be the [[?lean:New.Data.descentPair|descent pair]] \((W_j,V_j)\) with the character \(\chi_j\vartheta\): here \(W_j\) is the [[?lean:New.Data.spaceW|space \(W_j\)]] of rank \(r\) and \(V_j\) is the definite space of rank \(r+t\).

The **single lift** \(\Theta_{j,\vartheta}\) is the linear map from the [[?lean:New.Data.principalForms|forms of principal level]] on \(W_j\) (parameter \(\lambda^Y\), level \(J_M\): principal at the chosen places and maximal elsewhere) to the algebraic forms on \(V_j\) of the pair, defined for \(1\le j\le m\) as the restriction of the [[proofs/grh/determinant-exchange/theta-lift-of-descent-pair|theta lift]] \(\Theta_W\) of the pair \(O_{j,\vartheta}\) (the parameter of \(D\) on \(W_j\) [[?lean:New.Data.fitsParams_descentPair|fits this pair]]), and as \(0\) for \(j\) outside \(1,\dots,m\).

## Remarks

For \(1\le j\le m\) and a form \(y\) of principal level, the function on \(U(V_j)(\mathbb{A})\) attached to \(\Theta_{j,\vartheta}y\) is the theta lift of \(y\) by the datum of the highest weight vector.

## References

1. Lean: `New.Data.singleLift` in `src/New/Determinant/Norms/AdjointThetaLift.lean`.
