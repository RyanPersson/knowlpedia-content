+++
id = "proofs/grh/upper-objects/chain-of-glued-lifts-becomes-direct"
title = "A chain of glued double lifts is a chain of direct lifts after a power of Up"
kind = "theorem"
summary = "For a chain of lifts obeying the lift law, the composite of p glued double lifts of a ramified vector is an explicit scalar times the composite of 2p direct lifts of the p-th power of Up."
aliases = ["all lifts become direct"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.IsSplitLevel.compUpTo_gluedLift_eq_smul", "New.IsSplitLevel.gluedLift", "New.IsSplitLevel.upOperator_compUpTo_direct", "New.IsSplitLevel.compUpTo_direct_mem_ramified"]
lean_files = ["src/New/UpperBound/Objects/LiftLawsModuloN.lean"]
proof_status = "full"
+++

Let \(P\) be a [[proofs/grh/upper-objects/split-level|split level]] for \(N\). For \(j\ge0\) let \(X_j\) be a finite index set, \(\pi_j\) a complex representation of \(\mathrm{GL}_{X_j^+}(E_P)\), and \(L_j\colon\Psi\mapsto L_j(\Psi)\in\operatorname{Hom}(\pi_j,\pi_{j+1})\) a lift, linear in its datum, that obeys the [[proofs/grh/upper-objects/lift-law|lift law]] with factor \(\gamma_j\). Let \(d_0,d_1,\dots\) be complex numbers. The \(i\)-th **glued double lift** is
\[
G_i=d_i\cdot\pi_{2i+2}(D_N)\circ\sum_{y}L_{2i+1}(\operatorname{char}_y)\circ L_{2i}(\operatorname{lastcol}_y)\ \colon\ \pi_{2i}\to\pi_{2i+2},
\]
the sum over \(y\in((\mathbb Z/N)^P)^{X_{2i+1}^+}\) (see [[proofs/grh/upper-objects/data-modulo-n|data modulo \(N\)]]). Let \(c_i\) be the number of primitive vectors in \(((\mathbb Z/N)^P)^{X_{2i+1}^+}\) and write \(\mathcal D_j=L_{j-1}(\operatorname{direct})\circ\dots\circ L_0(\operatorname{direct})\colon\pi_0\to\pi_j\).

**Theorem (all lifts become direct).** For every [[proofs/grh/upper-objects/ramified-vector-at-split-level|ramified vector]] \(\varphi\in\pi_0\) and every \(p\ge0\),
\[
G_{p-1}\circ\dots\circ G_0\,(\varphi)=\Big(\prod_{i<p}d_i\,c_i\prod_{l<2i+2}\gamma_l\Big)\cdot\mathcal D_{2p}\big(\mathrm{Up}^p\varphi\big),
\]
where \(\mathrm{Up}\) is the [[proofs/grh/upper-objects/up-operator|operator Up]] on \(\pi_0\).

## Proof

*Step 1.* For ramified \(\varphi\) and all \(j\), \(\mathcal D_j\varphi\) is ramified, by induction from property 1 of the lift law.

*Step 2.* For ramified \(\varphi\) and all \(j\), \(\mathrm{Up}(\mathcal D_j\varphi)=\big(\prod_{l<j}\gamma_l\big)\mathcal D_j(\mathrm{Up}\,\varphi)\). This is induction on \(j\): by Step 1 and part 3 of the [[proofs/grh/upper-objects/mirror-lift-through-direct-lift|mirror lemma]] for \(L_j\), \(\mathrm{Up}\,L_j(\operatorname{direct})\mathcal D_j\varphi=\gamma_jL_j(\operatorname{direct})\mathrm{Up}\,\mathcal D_j\varphi\).

*Step 3.* Induction on \(p\); the case \(p=0\) is trivial. Assume the formula for \(q\) and put \(\varphi_q=\mathrm{Up}^q\varphi\), which is ramified because Up preserves ramified vectors. By Step 1, \(\mathcal D_{2q}\varphi_q\) is ramified, so the [[proofs/grh/upper-objects/glued-double-lift|glued double lift lemma]] for the pair \(L_{2q},L_{2q+1}\) gives
\[
G_q\big(\mathcal D_{2q}\varphi_q\big)=d_q\,c_q\,\gamma_{2q+1}\gamma_{2q}\cdot L_{2q+1}(\operatorname{direct})L_{2q}(\operatorname{direct})\,\mathrm{Up}\big(\mathcal D_{2q}\varphi_q\big).
\]
By Step 2, \(\mathrm{Up}(\mathcal D_{2q}\varphi_q)=\prod_{l<2q}\gamma_l\cdot\mathcal D_{2q}(\mathrm{Up}^{q+1}\varphi)\). Hence \(G_q(\mathcal D_{2q}\varphi_q)=d_qc_q\prod_{l<2q+2}\gamma_l\cdot\mathcal D_{2q+2}(\mathrm{Up}^{q+1}\varphi)\); multiplying by the scalar of the induction hypothesis gives the formula for \(q+1\). \(\square\)

## References

1. Lean: `New.IsSplitLevel.compUpTo_gluedLift_eq_smul` in `src/New/UpperBound/Objects/LiftLawsModuloN.lean`.
