+++
id = "proofs/grh/upper-objects/glued-double-lift"
title = "A glued double lift is two direct lifts after Up"
kind = "lemma"
summary = "On ramified vectors the double lift with the glued datum, moved by diag(1,...,1,1/N), equals the number of primitive vectors times gamma' gamma times the two direct lifts of Up."
aliases = ["glued double lift"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.IsSplitLevel.LiftLaw.sum_charDatum_lastColDatum", "New.IsSplitLevel.LiftLaw.glued_eq_direct_direct_upOperator", "New.IsSplitLevel.exists_GL_smul_lastBasisVector"]
lean_files = ["src/New/UpperBound/Objects/LiftLawsModuloN.lean"]
proof_status = "full"
+++

**Lemma.** Let \(P\) be a [[proofs/grh/upper-objects/split-level|split level]] for \(N\). Let \(L\colon\Psi\mapsto L(\Psi)\in\operatorname{Hom}(\pi,\pi')\) and \(L'\colon\Psi\mapsto L'(\Psi)\in\operatorname{Hom}(\pi',\pi'')\) obey the [[proofs/grh/upper-objects/lift-law|lift law]] with factors \(\gamma\) and \(\gamma'\), for representations \(\pi,\pi',\pi''\) of \(\mathrm{GL}_{n^+}(E_P)\), \(\mathrm{GL}_{n'^+}(E_P)\), \(\mathrm{GL}_{n''^+}(E_P)\). Let \(\varphi\in\pi\) be [[proofs/grh/upper-objects/ramified-vector-at-split-level|ramified]] and let \(c\) be the number of primitive vectors in \(((\mathbb Z/N)^P)^{n'^+}\). With the [[proofs/grh/upper-objects/data-modulo-n|data modulo \(N\)]]:

1. \(\displaystyle\sum_{y}L'(\operatorname{char}_y)\big(L(\operatorname{lastcol}_y)\varphi\big)=c\cdot L'(\operatorname{mirror})\big(L(\operatorname{direct})\varphi\big)\), the sum over all \(y\in((\mathbb Z/N)^P)^{n'^+}\);
2. \(\displaystyle\pi''(D_N)\sum_{y}L'(\operatorname{char}_y)\big(L(\operatorname{lastcol}_y)\varphi\big)=c\,\gamma'\gamma\cdot L'(\operatorname{direct})\Big(L(\operatorname{direct})\big(\mathrm{Up}\,\varphi\big)\Big)\),

where \(\mathrm{Up}\) is the [[proofs/grh/upper-objects/up-operator|operator Up]] on \(\pi\).

The left-hand sum is the double lift whose datum is the glued datum \(\sum_y\operatorname{lastcol}_y\otimes\operatorname{char}_y\).

## Proof

*1.* If \(y\) is not primitive, all its entries vanish at some \(w\in P\), and \(L(\operatorname{lastcol}_y)\varphi=0\) by part 2 of the [[proofs/grh/upper-objects/lift-law-vanishing-on-ramified-vectors|vanishing lemma]] (with \(r(T)=Te_\ast\)). If \(y\) is primitive, there is \(\kappa\in\mathrm{GL}_{n'^+}((\mathbb Z/N)^P)\) with \(\kappa e_\ast=y\): at each place \(w\) a vector over the field \(\mathbb Z/N\) with a nonzero entry is the image of \(e_\ast\) under an invertible matrix, and these matrices assemble over the product ring. Lift \(\kappa\) to \(k\in\mathrm{GL}_{n'^+}(\mathcal O_P)\). By properties 2 and 3 of the lift law,
\[
L'(\operatorname{char}_{\bar ke_\ast})\big(L(\operatorname{lastcol}_{\bar ke_\ast})\varphi\big)=L'(\operatorname{char}_{\bar ke_\ast})\big(\pi'(k)L(\operatorname{direct})\varphi\big)=L'(\operatorname{char}_{e_\ast})\big(L(\operatorname{direct})\varphi\big),
\]
and \(\operatorname{char}_{e_\ast}\) is the mirror datum. Summing over the \(c\) primitive vectors gives 1.

*2.* The vector \(L(\operatorname{direct})\varphi\) is ramified (property 1 of the lift law). By the [[proofs/grh/upper-objects/mirror-lift-through-direct-lift|mirror lemma]], part 2, for \(L'\) and then part 3 for \(L\),
\[
\pi''(D_N)L'(\operatorname{mirror})\big(L(\operatorname{direct})\varphi\big)=\gamma'L'(\operatorname{direct})\big(\mathrm{Up}\,L(\operatorname{direct})\varphi\big)=\gamma'\gamma\,L'(\operatorname{direct})\big(L(\operatorname{direct})\mathrm{Up}\,\varphi\big).
\]
Multiply by \(c\) and use 1. \(\square\)

## References

1. Lean: `New.IsSplitLevel.LiftLaw.sum_charDatum_lastColDatum`, `glued_eq_direct_direct_upOperator` in `src/New/UpperBound/Objects/LiftLawsModuloN.lean`.
